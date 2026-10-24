"""Build the sprint progress report straight from the GitHub Project.

Reads every Project item (Status, Iteration, SWP, Hours, Role, labels) with
`gh project item-list`, keeps the leaf items of the sprint, and writes
reports/progress-report-sprint-<x>.md: status summary, hours done / remaining,
burndown (ideal vs actual from the simulation scenario), late items with the
reason posted on the issue, and schedule risks with concrete actions.

Usage: python3 -I scripts/build-sprint-progress-report.py <repo-root> --scenario backlog/sprint-s1-simulation.json
"""
import argparse
import json
import subprocess
from collections import defaultdict
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--scenario", required=True)
    a = ap.parse_args()
    root = Path(a.root)
    sc = json.loads((root / a.scenario).read_text(encoding="utf-8"))
    sp = sc["sprint"]
    data = json.loads((root / "backlog" / "backlog.json").read_text(encoding="utf-8"))
    gmap = json.loads((root / "backlog" / "github-map.json").read_text(encoding="utf-8"))
    num_to_id = {v["number"]: k for k, v in gmap["issues"].items()}
    leaf_ids = set()
    title = {}
    for e in data["epics"]:
        for i in e["issues"]:
            title[i["id"]] = i["title"]
            for x in (i.get("sub_issues") or [i]):
                leaf_ids.add(x["id"])

    raw = subprocess.run(["gh", "project", "item-list", str(gmap["project"]["number"]), "--owner", "linhvtm-2475",
                          "--limit", "1000", "--format", "json"], capture_output=True, text=True, check=True).stdout
    items = json.loads(raw)["items"]
    rows = []
    for it in items:
        num = (it.get("content") or {}).get("number")
        bid = num_to_id.get(num)
        itv = it.get("iteration") or {}
        if bid in leaf_ids and isinstance(itv, dict) and itv.get("title") == sp:
            rows.append({"id": bid, "status": it.get("status") or "Todo", "hours": float(it.get("hours") or 0),
                         "swp": float(it.get("sWP") or it.get("swp") or 0), "role": it.get("role") or "?"})

    plan_h = sum(r["hours"] for r in rows)
    by_status = defaultdict(lambda: [0, 0.0])
    by_role = defaultdict(lambda: [0.0, 0.0])
    for r in rows:
        by_status[r["status"]][0] += 1
        by_status[r["status"]][1] += r["hours"]
        by_role[r["role"]][0] += r["hours"]
        if r["status"] == "Done":
            by_role[r["role"]][1] += r["hours"]
    done_h = by_status["Done"][1]
    pct = sc["burndown_actual_remaining_pct"]
    days = len(pct) - 1
    ideal = [round(plan_h * (1 - d / days)) for d in range(days + 1)]
    # Shape from the scenario, end point anchored to what the Project actually shows as not Done.
    rem_end = plan_h - done_h
    actual = [round(plan_h - (plan_h - rem_end) * (100 - p) / (100 - pct[-1])) for p in pct]

    md = [f"# Báo cáo tiến độ — Sprint {sp} ({sc['start']} → {sc['end']}) — GIẢ LẬP", "",
          "> Bài thực hành LAB-5. Sprint chưa diễn ra thật; trạng thái trên board được cập nhật theo kịch bản "
          f"`{a.scenario}` để mô phỏng kết thúc sprint. Mọi con số dưới đây đọc trực tiếp từ GitHub Project "
          "(trường Status, Iteration, Hours), không nhập tay.", "",
          "## 1. Tóm tắt", "",
          f"- **Kế hoạch:** {len(rows)} việc · {plan_h:.0f} giờ (SWP × 1,85).",
          f"- **Hoàn thành:** {by_status['Done'][0]} việc · {done_h:.0f} giờ (**{done_h / plan_h:.0%}** giờ kế hoạch).",
          f"- **Đang làm:** {by_status['In Progress'][0]} việc · {by_status['In Progress'][1]:.0f} giờ · "
          f"**Chưa bắt đầu:** {by_status['Todo'][0]} việc · {by_status['Todo'][1]:.0f} giờ → chuyển sang S2.",
          "- **Đánh giá:** nền tảng (thứ tự khóa, idempotency, bảng quy tắc có version, audit, catalog mã) đã xong — đúng mục tiêu S1. "
          "Trễ tập trung ở đăng nhập Entra ID (chờ thông tin tenant của khách), phân vùng DB (lỗi thiết kế GAP-00-05) và khung batch.", "",
          "## 2. Trạng thái theo vai", "", "| Vai | Giờ kế hoạch | Giờ xong | % |", "|---|---:|---:|---:|"]
    md += [f"| {k} | {v[0]:.0f} | {v[1]:.0f} | {v[1] / v[0]:.0%} |" for k, v in sorted(by_role.items()) if v[0]]
    md += ["", "## 3. Burndown (giờ còn lại)", "", "```mermaid", "xychart-beta",
           f'  title "Burndown {sp} (giờ còn lại)"', '  x-axis "Ngày làm việc" [' + ", ".join(f'"D{d}"' for d in range(days + 1)) + "]",
           f'  y-axis "Giờ" 0 --> {int(plan_h) + 20}', f"  line [{', '.join(map(str, ideal))}]", f"  line [{', '.join(map(str, actual))}]", "```", "",
           "Đường thứ nhất: lý tưởng. Đường thứ hai: thực tế (giả lập): 2 ngày đầu chậm do onboard +1 QA và môi trường Azure dev chưa ổn định; "
           f"điểm cuối = giờ của các việc chưa Done trên Project ({rem_end:.0f} giờ, {rem_end / plan_h:.0%}).", "",
           "| Ngày | " + " | ".join(f"D{d}" for d in range(days + 1)) + " |", "|---|" + "---:|" * (days + 1),
           "| Lý tưởng | " + " | ".join(map(str, ideal)) + " |", "| Thực tế | " + " | ".join(map(str, actual)) + " |", "",
           "## 4. Việc trễ (lý do đã ghi trên issue)", "", "| Issue | Trạng thái | Lý do |", "|---|---|---|"]
    for iid, why in sc["in_progress"].items():
        md.append(f"| #{gmap['issues'][iid]['number']} {iid} {title.get(iid, '')[:50]} | Đang làm | {why} |")
    for iid, why in sc["todo"].items():
        md.append(f"| #{gmap['issues'][iid]['number']} {iid} {title.get(iid, '')[:50]} | Chưa bắt đầu | {why} |")
    md += ["", "## 5. Rủi ro trễ và hành động", "",
           "| # | Rủi ro | Ảnh hưởng | Hành động | Người / hạn |", "|---|---|---|---|---|",
           "| R1 | Khách chưa cung cấp thông tin tenant Entra ID và thời hạn token (Q-COM-07) | Đăng nhập là nền của mọi màn; S2 không demo được luồng đăng nhập thật | Gửi khách danh sách thông tin cần (app registration, redirect URI, nhóm vai trò) kèm hạn 12-23; trong lúc chờ dùng tenant dev của Sun* để test | BrSE · 12-23 |",
           "| R2 | GAP-00-05: bảng phân vùng có PK / UNIQUE thiếu cột phân vùng | Chặn migration các bảng lớn → trễ EP-05, EP-06 và PoC truy vết ≤ 60 giây | Lập CR sửa DB design (thêm cột phân vùng vào khóa), duyệt trong tuần đầu S2; PoC hiệu năng dời sang S3 | SA + Linh · 12-25 |",
           "| R3 | ISS-35 (khóa tài xế, H-6) chưa quyết, lỡ hạn 11-16 | EP04-I01 chưa bắt đầu; engine giờ lái 2024 (S5) có nguy cơ trễ, đây là ràng buộc pháp lý | Đưa vào steering tháng 12; nếu chưa quyết trước S2 thì áp phương án khuyến nghị PA A và ghi rủi ro | PM + Linh · S2 ngày 1 |",
           "| R4 | Infra quá tải (IaC Azure viết tay, không có skill) | Khung batch Functions dời S2; IF.1 ERP (S2) phụ thuộc | Tạm chuyển 0,5 BE sang hỗ trợ IaC trong S2; dùng template Bicep có sẵn của Microsoft | PM · S2 |",
           "| R5 | S6 vẫn quá tải 135% sau khi cân (docs/sprint-capacity.md) | Có thể trễ G4 (03-19) | Theo dõi velocity S1–S2; nếu thực tế < 85% kế hoạch thì kéo 1 BE từ S4 hoặc dùng buffer 05-17 → 05-28 | PM · cuối S2 |", "",
           "## 6. Kế hoạch S2", "",
           f"- Mang sang: {by_status['In Progress'][0] + by_status['Todo'][0]} việc S1 chưa xong ({by_status['In Progress'][1] + by_status['Todo'][1]:.0f} giờ).",
           "- Ưu tiên: hoàn tất đăng nhập Entra ID khi có thông tin tenant, CR phân vùng, khung batch, rồi E1 入荷 và ルール版 giờ lái.",
           "- Velocity S1 (giả lập): dùng làm hệ số giờ thực tế / SWP cho lần chấm lại (thay hệ số 1,85 từ 5 mẫu)."]
    out = root / "reports" / f"progress-report-sprint-{sp}.md"
    out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(out, len(rows), round(plan_h), round(done_h))


if __name__ == "__main__":
    main()

"""Merge backlog/group-*.json into backlog/backlog.json, validate against the
break conventions, and render docs/spec-gaps.md + docs/differences-vs-lab4.md.

Usage: python3 -I scripts/merge-and-validate-backlog.py <repo-root>
Exit code 1 when a blocking rule is violated (public-repo content rules,
duplicate IDs, missing Definition of Done).
"""
import json
import re
import sys
from pathlib import Path

ROLES = {"BE", "FE", "QA", "Infra", "BrSE", "PM", "SA"}
SPRINTS = ["P10", "S0", "S1", "S2", "S3", "S4", "S5", "S6", "HARD", "ST", "UAT", "CUT", "HYP"]
JA_RUN = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uff00-\uffef]{41,}")
SECRET = re.compile(r"(gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20,})")
DOD = re.compile(r"Định nghĩa xong", re.I)


def walk(epics):
    for e in epics:
        yield "epic", e, None
        for i in e.get("issues", []):
            yield "issue", i, e
            for s in i.get("sub_issues", []):
                yield "sub", s, i


def check_text(item_id, text, errors):
    if "@" in text:
        errors.append(f"{item_id}: chứa '@' (email / mention)")
    if JA_RUN.search(text):
        errors.append(f"{item_id}: chuỗi tiếng Nhật liên tục > 40 ký tự (nghi chép nguyên văn)")
    if SECRET.search(text):
        errors.append(f"{item_id}: mẫu giống khóa bí mật")


def main(root):
    root = Path(root)
    groups = sorted((root / "backlog").glob("group-*.json"))
    epics, gaps, diffs = [], [], []
    for g in groups:
        data = json.loads(g.read_text(encoding="utf-8"))
        epics += data.get("epics", [])
        gaps += data.get("spec_gaps", [])
        diffs += data.get("differences", [])

    apply_overrides(root, epics)
    errors, warns, seen = [], [], set()
    counts = {"epic": 0, "issue": 0, "sub": 0}
    for kind, it, parent in walk(epics):
        counts[kind] += 1
        iid = it.get("id", "?")
        if iid in seen:
            errors.append(f"{iid}: ID trùng")
        seen.add(iid)
        body = it.get("body", "")
        check_text(iid, it.get("title", "") + "\n" + body, errors)
        if kind == "issue" and not DOD.search(body):
            errors.append(f"{iid}: thiếu mục Định nghĩa xong")
        if kind != "epic":
            if it.get("role") not in ROLES:
                errors.append(f"{iid}: role không hợp lệ {it.get('role')!r}")
            if it.get("sprint") not in SPRINTS:
                errors.append(f"{iid}: sprint không hợp lệ {it.get('sprint')!r}")
        if kind == "sub" and parent and parent.get("sprint") in SPRINTS and it.get("sprint") in SPRINTS:
            if SPRINTS.index(it["sprint"]) > SPRINTS.index(parent["sprint"]):
                warns.append(f"{iid}: sprint sub-issue sau sprint issue cha")
    by_id = {it["id"]: it for _, it, _ in walk(epics)}
    for kind, it, _ in walk(epics):
        for dep in it.get("depends_on", []) or []:
            if dep not in seen:
                errors.append(f"{it['id']}: phụ thuộc {dep} không tồn tại")
            elif by_id[dep].get("sprint") in SPRINTS and it.get("sprint") in SPRINTS and \
                    SPRINTS.index(by_id[dep]["sprint"]) > SPRINTS.index(it["sprint"]):
                warns.append(f"{it['id']} ({it['sprint']}) phụ thuộc {dep} ({by_id[dep]['sprint']}) ở sprint sau")
    for gp in gaps:
        check_text(gp.get("id", "GAP?"), json.dumps(gp, ensure_ascii=False), errors)

    out = {"epics": epics, "spec_gaps": gaps, "differences": diffs}
    (root / "backlog" / "backlog.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    render_gaps(root, gaps)
    render_diffs(root, diffs)

    print(f"groups={len(groups)} epics={counts['epic']} issues={counts['issue']} sub_issues={counts['sub']} "
          f"gaps={len(gaps)} differences={len(diffs)} errors={len(errors)} warnings={len(warns)}")
    for e in errors[:60]:
        print("ERROR", e)
    for w in warns[:30]:
        print("WARN ", w)
    return 1 if errors else 0


def apply_overrides(root, epics):
    """Apply backlog/merge-overrides.json: cross-group boundaries, dependencies, sprint moves."""
    p = root / "backlog" / "merge-overrides.json"
    if not p.exists():
        return
    o = json.loads(p.read_text(encoding="utf-8"))
    by_id = {it["id"]: it for _, it, _ in walk(epics)}
    for iid, sp in o.get("sprint", {}).items():
        by_id[iid]["sprint"] = sp
    for iid in o.get("iteration_p10", []):
        by_id[iid]["sprint"] = "P10"
    for iid, deps in o.get("depends_add", {}).items():
        cur = by_id[iid].setdefault("depends_on", [])
        cur += [d for d in deps if d not in cur]
    for iid, note in o.get("note_append", {}).items():
        if note not in by_id[iid].get("body", ""):
            by_id[iid]["body"] = by_id[iid].get("body", "") + note


def cell(v):
    return str(v or "").replace("|", "\\|").replace("\n", " ")


def render_gaps(root, gaps):
    rows = ["# Spec gap phát hiện khi break (LAB-5)", "",
            "Chỗ hở / mâu thuẫn của detail design LAB-4 và basic design, ghi lại lúc break backlog. "
            "Không lặp finding đã có ở review DR cuối Step 3 (chỉ trỏ ID).", "",
            "| ID | Mức | Ở đâu | Mô tả | Đề xuất | Issue ảnh hưởng |", "|---|---|---|---|---|---|"]
    for g in gaps:
        rows.append(f"| {cell(g.get('id'))} | {cell(g.get('severity'))} | {cell(g.get('where'))} | "
                    f"{cell(g.get('desc'))} | {cell(g.get('proposal'))} | {cell(', '.join(g.get('issues', [])))} |")
    (root / "docs" / "spec-gaps.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def render_diffs(root, diffs):
    rows = ["# Khác biệt so với LAB-4 đã nộp", "",
            "Mỗi dòng là một chỗ backlog LAB-5 break khác LAB-4, kèm lý do. Không có khác biệt nào ngoài bảng này.", "",
            "| Tham chiếu LAB-4 | Thay đổi | Lý do | Ảnh hưởng backlog |", "|---|---|---|---|"]
    for d in diffs:
        rows.append(f"| {cell(d.get('lab4_ref'))} | {cell(d.get('change'))} | {cell(d.get('reason'))} | {cell(d.get('impact'))} |")
    (root / "docs" / "differences-vs-lab4.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))

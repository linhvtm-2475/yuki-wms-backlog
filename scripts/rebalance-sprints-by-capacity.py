"""Level-load sprints S1–S6 against team capacity by moving whole issues later.

Decision (Linh, 2026-10-24): combine +1 QA from S1 and +1 BE from S3 with moving
low-risk work into HARD/ST. Never moves domain-constrained issues, the D-A pair,
or an issue that an earlier-sprint issue depends on. Writes sprint moves into
backlog/merge-overrides.json ("sprint" + "sub_sprint") and docs/sprint-capacity.md.

Usage: python3 -I scripts/rebalance-sprints-by-capacity.py <repo-root>
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

ORDER = ["P10", "S0", "S1", "S2", "S3", "S4", "S5", "S6", "HARD", "ST", "UAT", "CUT", "HYP"]
DAYS = {"P10": 23, "S0": 5, "S1": 10, "S2": 11, "S3": 10, "S4": 10, "S5": 10, "S6": 10,
        "HARD": 5, "ST": 10, "UAT": 30, "CUT": 11, "HYP": 20}  # S2 / S5: holidays removed
FTE = {"P10": 3.5, "S0": 7.9, "S1": 7.9, "S2": 7.9, "S3": 8.4, "S4": 9.4, "S5": 9.4, "S6": 8.4,
       "HARD": 8.8, "ST": 8.8, "UAT": 4.75, "CUT": 4.5, "HYP": 2.45}
EXTRA = {sp: (1 if sp in ("S1", "S2", "S3", "S4", "S5", "S6") else 0) + (1 if sp in ("S3", "S4", "S5", "S6") else 0)
         for sp in ORDER}
FOCUS = 0.75
CONT = {"estimate:firm": .10, "estimate:provisional": .25, "estimate:placeholder": .50}
MOVABLE_FIRST = ("EP-14", "EP-07", "EP-13", "EP-15", "EP-10", "EP-08", "EP-06", "EP-02")
PINNED = {"EP03-I23", "EP03-I30"}  # D-A: shipment confirmation + POD per line ship together


def capacity(sp):
    return (FTE[sp] + EXTRA[sp]) * DAYS[sp] * 8 * FOCUS


def main(root):
    root = Path(root)
    data = json.loads((root / "backlog" / "backlog.json").read_text(encoding="utf-8"))
    hrs = json.loads((root / "backlog" / "swp-hours.json").read_text(encoding="utf-8"))
    ov_path = root / "backlog" / "merge-overrides.json"
    ov = json.loads(ov_path.read_text(encoding="utf-8"))

    issues = {}
    epic_of = {}
    for e in data["epics"]:
        for i in e["issues"]:
            issues[i["id"]] = i
            epic_of[i["id"]] = e["id"]

    def cost(i):
        leaves = i.get("sub_issues") or [i]
        return sum(hrs[x["id"]]["hours"] * (1 + CONT.get(hrs[x["id"]]["tier"], .25)) for x in leaves)

    dependents = defaultdict(set)
    for i in issues.values():
        for d in i.get("depends_on") or []:
            dependents[d].add(i["id"])

    sprint = {k: v["sprint"] for k, v in issues.items()}
    load = defaultdict(float)
    for k, i in issues.items():
        load[sprint[k]] += cost(i)

    def movable(k):
        i = issues[k]
        if k in PINNED or any(l.startswith("domain:") for l in i.get("labels", [])):
            return False
        return True

    moves = []
    for idx, sp in enumerate(ORDER[2:8], start=2):  # S1..S6
        cands = [k for k in issues if sprint[k] == sp and movable(k)]
        cands.sort(key=lambda k: (MOVABLE_FIRST.index(epic_of[k]) if epic_of[k] in MOVABLE_FIRST else 99, -cost(issues[k])))
        for k in cands:
            if load[sp] <= capacity(sp):
                break
            for target in ORDER[idx + 1:10]:  # later sprints up to ST
                deps_ok = all(ORDER.index(sprint[d]) >= ORDER.index(target) for d in dependents[k])
                if deps_ok and load[target] + cost(issues[k]) <= capacity(target):
                    load[sp] -= cost(issues[k])
                    load[target] += cost(issues[k])
                    moves.append((k, sp, target, round(cost(issues[k]))))
                    sprint[k] = target
                    break

    ov.setdefault("sprint", {})
    for k, _, target, _ in moves:
        ov["sprint"][k] = target
        for s in issues[k].get("sub_issues", []):
            ov["sprint"][s["id"]] = target
    ov_path.write_text(json.dumps(ov, ensure_ascii=False, indent=1), encoding="utf-8")

    rows = ["# Năng lực và tải sprint (sau khi cân, 2026-10-24)", "",
            "Năng lực = (FTE plan §9.2 + bổ sung) × ngày làm việc × 8 h × 75%. Bổ sung theo quyết định Linh: +1 QA từ S1, +1 BE từ S3. "
            "Tải = giờ SWP của mục lá + contingency theo độ tin (firm 10% · provisional 25% · placeholder 50%).", "",
            "| Sprint | Năng lực (h) | Tải sau cân (h) | Mức dùng |", "|---|---:|---:|---:|"]
    for sp in ORDER:
        rows.append(f"| {sp} | {round(capacity(sp))} | {round(load[sp])} | {load[sp] / capacity(sp):.0%} |")
    rows += ["", f"Đã dời {len(moves)} issue (kèm sub-issue):", "", "| Issue | Từ | Sang | Giờ + contingency |", "|---|---|---|---:|"]
    rows += [f"| {k} {issues[k]['title'][:70]} | {a} | {b} | {c} |" for k, a, b, c in moves]
    (root / "docs" / "sprint-capacity.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    for sp in ORDER:
        print(sp, round(capacity(sp)), round(load[sp]), f"{load[sp] / capacity(sp):.0%}")
    print("moves", len(moves))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")

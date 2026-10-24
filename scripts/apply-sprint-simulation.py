"""Apply a simulated sprint outcome (backlog/sprint-<x>-simulation.json) to the GitHub Project.

Leaf items of the sprint get Status Done (and the issue is closed as completed),
In Progress, or Todo per the scenario. An issue listed as in_progress gets its
first half of sprint leaves Done and the rest In Progress. Late issues get one
comment stating the reason, so the board explains itself. Parents are rolled up:
Done when all leaves are Done, else In Progress when any leaf started.

Usage: python3 -I scripts/apply-sprint-simulation.py <repo-root> --scenario backlog/sprint-s1-simulation.json [--dry-run]
"""
import argparse
import json
import subprocess
import time
from pathlib import Path


def gh(args):
    for attempt in range(4):
        p = subprocess.run(["gh"] + args, capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout
        time.sleep(20 * (attempt + 1))
    raise SystemExit(f"gh {' '.join(args)[:100]} failed: {p.stderr.strip()[:200]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--scenario", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    sc = json.loads((root / a.scenario).read_text(encoding="utf-8"))
    data = json.loads((root / "backlog" / "backlog.json").read_text(encoding="utf-8"))
    g = json.loads((root / "backlog" / "github-map.json").read_text(encoding="utf-8"))
    proj, status = g["project"], g["project"]["fields"]["Status"]
    repo = "linhvtm-2475/yuki-wms-backlog"
    sp = sc["sprint"]

    plan = {}  # backlog id -> status
    for e in data["epics"]:
        for i in e["issues"]:
            leaves = [x for x in (i.get("sub_issues") or [i]) if x["sprint"] == sp]
            if not leaves:
                continue
            if i["id"] in sc["todo"]:
                states = ["Todo"] * len(leaves)
            elif i["id"] in sc["in_progress"]:
                half = len(leaves) // 2
                states = ["Done"] * half + ["In Progress"] * (len(leaves) - half)
            else:
                states = ["Done"] * len(leaves)
            for x, st in zip(leaves, states):
                plan[x["id"]] = st
            if i.get("sub_issues"):
                all_leaves = i["sub_issues"]
                done_all = all(plan.get(x["id"]) == "Done" for x in all_leaves)
                started = any(plan.get(x["id"]) in ("Done", "In Progress") for x in all_leaves)
                plan[i["id"]] = "Done" if done_all else ("In Progress" if started else "Todo")

    counts = {}
    for st in plan.values():
        counts[st] = counts.get(st, 0) + 1
    print("plan", counts)
    (root / "backlog" / f"sprint-{sp.lower()}-applied.json").write_text(json.dumps(plan, indent=1), encoding="utf-8")
    if a.dry_run:
        return
    for iid, st in plan.items():
        rec = g["issues"][iid]
        gh(["project", "item-edit", "--id", rec["item_id"], "--project-id", proj["id"],
            "--field-id", status["id"], "--single-select-option-id", status["options"][st]])
        if st == "Done":
            gh(["issue", "close", str(rec["number"]), "--repo", repo, "--reason", "completed"])
        time.sleep(0.5)
    for iid, why in {**sc["in_progress"], **sc["todo"]}.items():
        rec = g["issues"][iid]
        gh(["issue", "comment", str(rec["number"]), "--repo", repo, "--body",
            f"**[Giả lập {sp}, {sc['end']}] Trễ so với kế hoạch:** {why}"])
        time.sleep(2)
    print("applied", len(plan))


if __name__ == "__main__":
    main()

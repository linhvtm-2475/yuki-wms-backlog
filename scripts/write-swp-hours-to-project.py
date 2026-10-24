"""Write the reviewed SWP and derived hours into the GitHub Project fields.

Input: the calibrated /tkm:sun-estimate payload (final SWP of leaf work items).
Containers (issues with sub-issues, epics) get the plain sum of their children.
Hours = SWP × HOURS_PER_SWP (docs/hours-convention.md), rounded to 0.5 h.

Usage:
  python3 -I scripts/write-swp-hours-to-project.py <repo-root> --payload <calibrated.json> [--dry-run]
Writes backlog/swp-hours.json (backlog id → swp, hours, tier) and is safe to re-run.
"""
import argparse
import json
import subprocess
import time
from pathlib import Path

HOURS_PER_SWP = 76 / 41  # 5 representatives reviewed by Linh on 2026-10-24: 76 h / 41 SWP


def hours(swp):
    return round(swp * HOURS_PER_SWP * 2) / 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--payload", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    gmap = json.loads((root / "backlog" / "github-map.json").read_text(encoding="utf-8"))
    tiers = json.loads((root / "backlog" / "estimate-tiers.json").read_text(encoding="utf-8"))["tiers"]
    data = json.loads((root / "backlog" / "backlog.json").read_text(encoding="utf-8"))
    payload = json.loads(Path(a.payload).read_text(encoding="utf-8"))
    by_number = {v["number"]: k for k, v in gmap["issues"].items()}
    leaf = {by_number[int(i["issueRef"].split("#")[1])]: i["finalSWP"] for i in payload["issues"]}

    out = {}
    for e in data["epics"]:
        etotal = 0
        for i in e["issues"]:
            subs = i.get("sub_issues", [])
            swp = sum(leaf[s["id"]] for s in subs) if subs else leaf[i["id"]]
            for s in subs:
                out[s["id"]] = {"swp": leaf[s["id"]], "hours": hours(leaf[s["id"]]), "tier": tiers.get(s["id"])}
            out[i["id"]] = {"swp": swp, "hours": hours(swp), "tier": tiers.get(i["id"])}
            etotal += swp
        out[e["id"]] = {"swp": etotal, "hours": hours(etotal), "tier": None}
    total_leaf = sum(leaf.values())
    print(f"leaf SWP={total_leaf} hours={hours(total_leaf)} items={len(out)}")
    (root / "backlog" / "swp-hours.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    if a.dry_run:
        return

    proj = gmap["project"]
    f = proj["fields"]
    done_path = root / "backlog" / "swp-hours-pushed.json"
    done = set(json.loads(done_path.read_text(encoding="utf-8"))) if done_path.exists() else set()
    for iid, v in out.items():
        if iid in done:
            continue
        item = gmap["issues"][iid]["item_id"]
        for field, val in (("SWP", v["swp"]), ("Hours", v["hours"])):
            for attempt in range(5):
                p = subprocess.run(["gh", "project", "item-edit", "--id", item, "--project-id", proj["id"],
                                    "--field-id", f[field]["id"], "--number", str(val)], capture_output=True, text=True)
                if p.returncode == 0:
                    break
                time.sleep(30 * (attempt + 1))
            else:
                raise SystemExit(f"failed {iid} {field}: {p.stderr.strip()[:200]}")
        done.add(iid)
        done_path.write_text(json.dumps(sorted(done)), encoding="utf-8")
        time.sleep(0.3)
    print("pushed", len(done))


if __name__ == "__main__":
    main()

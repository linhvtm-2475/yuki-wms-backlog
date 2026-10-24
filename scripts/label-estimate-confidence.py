"""Assign an estimate-confidence tier to every issue / sub-issue and push it as a label.

Tiers (brainstorm-261024-estimate-breakdown-risks §4.1):
  estimate:placeholder  blocked by ISS-35, or waiting on customer answer / data
  estimate:firm         backed by a LAB-4 detail design (dd:yes)
  estimate:provisional  everything else (basic design only, or a "write DD" task)
Sub-issues inherit the parent's tier unless their own text makes them placeholder.

Usage: python3 -I scripts/label-estimate-confidence.py <repo-root> --repo OWNER/REPO [--dry-run]
Writes backlog/estimate-tiers.json (id → tier) and is safe to re-run.
"""
import argparse
import json
import re
import subprocess
import time
from pathlib import Path

WAITING = re.compile(r"ISS-10|ISS-11|ISS-14|GAP-12-03|Q-NEW-|Q-DTL-TMP-09|Q-DEV-13|Q-TRC-04|Q-COMDB-10")
COLORS = {"estimate:firm": "0e8a16", "estimate:provisional": "fbca04", "estimate:placeholder": "b60205"}


def own_tier(it):
    text = it.get("title", "") + it.get("body", "")
    labels = set(it.get("labels", []))
    if "blocked:ISS-35" in labels or WAITING.search(text):
        return "estimate:placeholder"
    if "dd:yes" in labels:
        return "estimate:firm"
    return "estimate:provisional"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--repo", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    data = json.loads((root / "backlog" / "backlog.json").read_text(encoding="utf-8"))
    gmap = json.loads((root / "backlog" / "github-map.json").read_text(encoding="utf-8"))["issues"]

    tiers = {}
    for e in data["epics"]:
        for i in e["issues"]:
            t = own_tier(i)
            tiers[i["id"]] = t
            for s in i.get("sub_issues", []):
                st = own_tier(s)
                tiers[s["id"]] = "estimate:placeholder" if "placeholder" in (t + st) else t

    out = root / "backlog" / "estimate-tiers.json"
    done = json.loads(out.read_text(encoding="utf-8")).get("_pushed", []) if out.exists() else []
    counts = {k: sum(1 for v in tiers.values() if v == k) for k in COLORS}
    print("tiers", counts)
    if a.dry_run:
        return
    for name, color in COLORS.items():
        subprocess.run(["gh", "label", "create", name, "--repo", a.repo, "--color", color, "--force"], capture_output=True)
    for iid, tier in tiers.items():
        if iid in done:
            continue
        num = gmap[iid]["number"]
        p = subprocess.run(["gh", "api", f"repos/{a.repo}/issues/{num}/labels", "-f", f"labels[]={tier}"],
                           capture_output=True, text=True)
        if p.returncode != 0:
            print("fail", iid, p.stderr.strip()[:200])
            time.sleep(60)
            continue
        done.append(iid)
        out.write_text(json.dumps({"tiers": tiers, "_pushed": done}, ensure_ascii=False, indent=1), encoding="utf-8")
        time.sleep(1.0)
    print("pushed", len(done))


if __name__ == "__main__":
    main()

"""Publish backlog/backlog.json to a GitHub repo + Project (v2).

Idempotent: every created object is recorded in backlog/github-map.json, and a
re-run skips what already exists. Needs `gh` logged in with scopes repo + project.

Usage:
  python3 -I scripts/publish-backlog-to-github.py <repo-root> --owner OWNER --repo REPO \
      --project-title TITLE [--step labels|issues|links|project|fields|items|bodies|all] [--dry-run]
"""
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

# Sprint calendar from plan-261024-dev-phase-wbs.md §7 (start date, duration in days).
ITERATIONS = [
    ("P10", "2026-10-26", 33), ("S0", "2026-11-30", 7), ("S1", "2026-12-07", 14), ("S2", "2026-12-21", 21),
    ("S3", "2027-01-11", 14), ("S4", "2027-01-25", 14), ("S5", "2027-02-08", 21),
    ("S6", "2027-03-01", 14), ("HARD", "2027-03-15", 7), ("ST", "2027-03-22", 14),
    ("UAT", "2027-04-05", 42), ("CUT", "2027-05-17", 15), ("HYP", "2027-06-01", 28),
]
ROLES = ["BE", "FE", "QA", "Infra", "BrSE", "PM", "SA"]
THROTTLE = 8.0  # seconds between content-creating calls: GitHub secondary limit ~500/hour


class GH:
    def __init__(self, dry):
        self.dry = dry

    def run(self, args, input_json=None, parse=True):
        if self.dry:
            print("DRY gh", " ".join(args)[:160])
            return {}
        for attempt in range(6):
            p = subprocess.run(["gh"] + args, input=json.dumps(input_json) if input_json else None,
                               capture_output=True, text=True)
            err = p.stderr.lower()
            if p.returncode != 0 and any(k in err for k in ("rate limit", "abuse", "submitted too quickly", "connection reset", "timeout", "eof", "502", "503", "504")):
                wait = 120 * (attempt + 1)
                print(f"rate-limited, sleep {wait}s", flush=True)
                time.sleep(wait)
                continue
            break
        if p.returncode != 0:
            raise RuntimeError(f"gh {' '.join(args)[:120]} → {p.stderr.strip()[:400]}")
        return json.loads(p.stdout) if parse and p.stdout.strip() else p.stdout

    def graphql(self, query, **vars_):
        args = ["api", "graphql", "-f", f"query={query}"]
        for k, v in vars_.items():
            args += ["-F" if isinstance(v, (int, bool)) else "-f", f"{k}={json.dumps(v) if isinstance(v, bool) else v}"]
        return self.run(args)


def items(epics):
    for e in epics:
        yield e, None, "epic"
        for i in e.get("issues", []):
            yield i, e, "issue"
            for s in i.get("sub_issues", []):
                yield s, i, "sub-issue"


def labels_of(it, kind):
    ls = set(it.get("labels", [])) | {f"type:{kind}"}
    if it.get("role"):
        ls.add(f"role:{it['role']}")
    if it.get("sprint"):
        ls.add(f"sprint:{it['sprint']}")
    return sorted(ls)


def footer(it, parent):
    lines = ["", "---", f"`{it['id']}`"]
    if parent:
        lines[-1] += f" · cha: `{parent['id']}`"
    if it.get("bidding_ref"):
        lines.append("Bidding LAB-1: " + ", ".join(it["bidding_ref"]))
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--owner", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--project-title", required=True)
    ap.add_argument("--step", default="all")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    data = json.loads((root / "backlog" / "backlog.json").read_text(encoding="utf-8"))
    mpath = root / "backlog" / "github-map.json"
    m = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {"issues": {}, "links": [], "project": {}}
    gh = GH(a.dry_run)
    repo = f"{a.owner}/{a.repo}"
    steps = ["labels", "issues", "links", "project", "fields", "items", "bodies"] if a.step == "all" else [a.step]

    def save():
        if not a.dry_run:
            mpath.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    all_items = list(items(data["epics"]))

    if "labels" in steps:
        wanted = sorted({l for it, _, k in all_items for l in labels_of(it, k)})
        for l in wanted:
            color = {"type": "1d76db", "role": "0e8a16", "sprint": "c5def5", "domain": "d93f0b",
                     "blocked": "b60205", "dd": "fbca04"}.get(l.split(":")[0], "ededed")
            gh.run(["label", "create", l, "--repo", repo, "--color", color, "--force"], parse=False)
        print(f"labels={len(wanted)}")

    if "issues" in steps:
        for it, parent, kind in all_items:
            if it["id"] in m["issues"]:
                continue
            body = it.get("body", "") + footer(it, parent)
            args = ["api", f"repos/{repo}/issues", "-f", f"title={it['title']}", "-f", f"body={body}"]
            for l in labels_of(it, kind):
                args += ["-f", f"labels[]={l}"]
            r = gh.run(args)
            m["issues"][it["id"]] = {"number": r.get("number"), "id": r.get("id"), "node_id": r.get("node_id"), "kind": kind}
            save()
            if len(m["issues"]) % 50 == 0:
                print(f"issues created: {len(m['issues'])}", flush=True)
            time.sleep(THROTTLE)
        print(f"issues={len(m['issues'])}")

    if "links" in steps:
        done = {tuple(x) for x in m["links"]}
        for it, parent, kind in all_items:
            if not parent or (parent["id"], it["id"]) in done:
                continue
            p, c = m["issues"][parent["id"]], m["issues"][it["id"]]
            gh.run(["api", f"repos/{repo}/issues/{p['number']}/sub_issues", "-F", f"sub_issue_id={c['id']}"])
            m["links"].append([parent["id"], it["id"]])
            save()
            time.sleep(THROTTLE / 4)
        print(f"links={len(m['links'])}")

    if "project" in steps and not m["project"].get("id"):
        r = gh.run(["project", "create", "--owner", a.owner, "--title", a.project_title, "--format", "json"])
        m["project"] = {"id": r.get("id"), "number": r.get("number"), "url": r.get("url")}
        gh.graphql("mutation($p:ID!){updateProjectV2(input:{projectId:$p,public:true}){projectV2{public}}}",
                   p=m["project"]["id"])
        gh.run(["project", "link", str(m["project"]["number"]), "--owner", a.owner, "--repo", repo], parse=False)
        save()
        print("project", m["project"].get("url"))

    if "fields" in steps:
        pid = m["project"]["id"]
        f = m["project"].setdefault("fields", {})
        if "Iteration" not in f:
            its = ",".join(f'{{title:"{t}",startDate:"{d}",duration:{n}}}' for t, d, n in ITERATIONS)
            q = ("mutation($p:ID!){createProjectV2Field(input:{projectId:$p,dataType:ITERATION,name:\"Iteration\","
                 f"iterationConfiguration:{{startDate:\"{ITERATIONS[0][1]}\",duration:14,iterations:[{its}]}}}})"
                 "{projectV2Field{... on ProjectV2IterationField{id configuration{iterations{id title}}}}}}")
            r = gh.graphql(q, p=pid)
            fld = (r.get("data") or {}).get("createProjectV2Field", {}).get("projectV2Field", {})
            f["Iteration"] = {"id": fld.get("id"),
                              "options": {x["title"]: x["id"] for x in fld.get("configuration", {}).get("iterations", [])}}
        for name, dtype in (("SWP", "NUMBER"), ("Hours", "NUMBER")):
            if name not in f:
                r = gh.run(["project", "field-create", str(m["project"]["number"]), "--owner", a.owner,
                            "--name", name, "--data-type", dtype, "--format", "json"])
                f[name] = {"id": r.get("id")}
        if "Role" not in f:
            r = gh.run(["project", "field-create", str(m["project"]["number"]), "--owner", a.owner, "--name", "Role",
                        "--data-type", "SINGLE_SELECT", "--single-select-options", ",".join(ROLES), "--format", "json"])
            f["Role"] = {"id": r.get("id"), "options": {o["name"]: o["id"] for o in r.get("options", [])}}
        lst = gh.run(["project", "field-list", str(m["project"]["number"]), "--owner", a.owner, "--format", "json"])
        for fl in lst.get("fields", []):
            if fl.get("name") == "Status":
                f["Status"] = {"id": fl["id"], "options": {o["name"]: o["id"] for o in fl.get("options", [])}}
        save()
        print("fields", sorted(f))

    if "items" in steps:
        pid, f = m["project"]["id"], m["project"]["fields"]
        for it, parent, kind in all_items:
            rec = m["issues"][it["id"]]
            if rec.get("item_id"):
                continue
            url = f"https://github.com/{repo}/issues/{rec['number']}"
            try:
                r = gh.run(["project", "item-add", str(m["project"]["number"]), "--owner", a.owner, "--url", url, "--format", "json"])
                rec["item_id"] = r.get("id")
            except RuntimeError as exc:
                if "already exists" not in str(exc):
                    raise
                # Item was auto-added (e.g. via sub-issue linking): look up its existing item id.
                q = ("query($o:String!,$r:String!,$n:Int!){repository(owner:$o,name:$r){issue(number:$n)"
                     "{projectItems(first:10){nodes{id project{id}}}}}}")
                res = gh.graphql(q, o=a.owner, r=a.repo, n=rec["number"])
                nodes = res["data"]["repository"]["issue"]["projectItems"]["nodes"]
                rec["item_id"] = next(n["id"] for n in nodes if n["project"]["id"] == pid)
            base = ["project", "item-edit", "--id", rec["item_id"], "--project-id", pid]
            if it.get("role") in f["Role"]["options"]:
                gh.run(base + ["--field-id", f["Role"]["id"], "--single-select-option-id", f["Role"]["options"][it["role"]]], parse=False)
            if it.get("sprint") in f["Iteration"]["options"]:
                gh.run(base + ["--field-id", f["Iteration"]["id"], "--iteration-id", f["Iteration"]["options"][it["sprint"]]], parse=False)
            if "Todo" in f.get("Status", {}).get("options", {}):
                gh.run(base + ["--field-id", f["Status"]["id"], "--single-select-option-id", f["Status"]["options"]["Todo"]], parse=False)
            save()
            time.sleep(0.5)
        print("items added")

    if "bodies" in steps:
        # Replace backlog IDs in "Phụ thuộc" with real issue references.
        ids = {k: v["number"] for k, v in m["issues"].items()}
        pat = re.compile(r"\b(EP\d{2}-I\d{2,3}(?:-S\d{2})?)\b")
        for it, parent, kind in all_items:
            deps = it.get("depends_on") or []
            if not deps or m["issues"][it["id"]].get("deps_linked"):
                continue
            body = it.get("body", "") + footer(it, parent)
            body = pat.sub(lambda x: f"#{ids[x.group(1)]} ({x.group(1)})" if x.group(1) in ids and x.group(1) != it["id"] else x.group(1), body)
            dep_line = "\n**Phụ thuộc (link):** " + ", ".join(f"#{ids[d]}" for d in deps if d in ids)
            gh.run(["api", "-X", "PATCH", f"repos/{repo}/issues/{m['issues'][it['id']]['number']}", "-f", f"body={body}{dep_line}"])
            m["issues"][it["id"]]["deps_linked"] = True
            save()
            time.sleep(THROTTLE / 4)
        print("bodies linked")
    return 0


if __name__ == "__main__":
    sys.exit(main())

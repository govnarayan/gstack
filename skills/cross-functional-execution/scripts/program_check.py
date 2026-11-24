"""Program control check: schedule, capacity, logs, decision rights, change control and benefits. Python 3.10+, stdlib.

Reads a program file (see ../examples/usage-pricing-program.json) and reports:
  1. Forecast schedule from the status week, critical path(s) and slack against the committed finish.
  2. Weekly load per person, including commitments outside the program.
  3. Risk/assumption/issue/dependency log hygiene: owner, due date, staleness, high-severity issues without a decision.
  4. Decision log against the decision-rights map: recorded decider holds the D, Agree parties signed, proposals not
     presented as decisions.
  5. Change requests above the threshold approved by the named approver.
  6. Benefits with a baseline, source and owner; milestones with acceptance evidence and an acceptor.
  7. The finish week each option for an open decision would produce, recomputed rather than asserted.

Usage: python program_check.py <program.json> [--markdown <status.md>] [--strict]
--strict exits 1 when any blocking finding exists. Findings are prompts for owners, not verdicts on people.
"""
from __future__ import annotations

import argparse
import copy
import json
import pathlib
import sys


def schedule(tasks, status_week, remove=(), extra=None):
    """Forecast start/finish per task. Done tasks keep their planned dates; open work cannot start before the status week."""
    extra = extra or {}
    by_id = {t["id"]: t for t in tasks}
    removed = {tuple(pair) for pair in remove}
    order, seen, visiting = [], set(), set()

    def visit(tid):
        if tid in seen:
            return
        if tid in visiting:
            raise ValueError(f"Dependency cycle at {tid}")
        visiting.add(tid)
        for pre in by_id[tid]["after"]:
            if pre not in by_id:
                raise ValueError(f"{tid} depends on unknown task {pre}")
            visit(pre)
        visiting.discard(tid)
        seen.add(tid)
        order.append(tid)

    for t in tasks:
        visit(t["id"])
    plan, forecast = {}, {}
    for tid in order:
        t = by_id[tid]
        preds = [p for p in t["after"] if (tid, p) not in removed]
        base_start = max([plan[p][1] for p in preds], default=0)
        plan[tid] = (base_start, base_start + t["duration"])
        start = max([forecast[p][1] for p in preds], default=0)
        length = t["duration"] + t.get("forecast_extra_weeks", 0) + extra.get(tid, 0)
        if t["status"] == "done":
            forecast[tid] = plan[tid]
        elif t["status"] == "in_progress":
            if "remaining_weeks" not in t:
                raise ValueError(f"In-progress task {tid} needs remaining_weeks")
            forecast[tid] = (min(start, status_week), max(status_week, start) + t["remaining_weeks"] + extra.get(tid, 0))
        else:
            start = max(start, status_week)
            forecast[tid] = (start, start + length)
    return order, plan, forecast, removed


def critical_paths(tasks, order, forecast, removed):
    by_id = {t["id"]: t for t in tasks}
    finish = max(f for _, f in forecast.values())
    ends = [tid for tid in order if forecast[tid][1] == finish]
    paths = []

    def walk(tid, tail):
        preds = [p for p in by_id[tid]["after"] if (tid, p) not in removed and forecast[p][1] == forecast[tid][0]
                 and by_id[tid]["status"] != "done"]
        if not preds:
            paths.append([tid] + tail)
        for p in preds:
            walk(p, [tid] + tail)

    for e in ends:
        walk(e, [])
    return finish, paths


def latest(tasks, order, forecast, removed, commit):
    """Latest finish per task that still meets the commitment; slack = latest finish - forecast finish."""
    succ = {t["id"]: [] for t in tasks}
    for t in tasks:
        for p in t["after"]:
            if (t["id"], p) not in removed:
                succ[p].append(t["id"])
    late = {}
    for tid in reversed(order):
        late[tid] = min([late[s] - (forecast[s][1] - forecast[s][0]) for s in succ[tid]], default=commit)
    return {tid: late[tid] - forecast[tid][1] for tid in order}


def loads(program, forecast):
    weeks = range(program["status_week"], max(f for _, f in forecast.values()))
    result = {}
    for person, info in program["people"].items():
        row = {}
        for w in weeks:
            used = sum(t["load"] for t in program["tasks"] if t["owner"] == person and t["status"] != "done"
                       and forecast[t["id"]][0] <= w < forecast[t["id"]][1])
            used += sum(c["load"] for c in info["other_commitments"] if c["from_week"] <= w <= c["to_week"])
            row[w] = round(used, 2)
        result[person] = row
    return result


def finding(severity, area, item, message):
    return {"severity": severity, "area": area, "item": item, "message": message}


def check(program):
    findings = []
    week, commit = program["status_week"], program["committed_finish_week"]
    tasks = program["tasks"]
    order, plan, forecast, removed = schedule(tasks, week)
    finish, paths = critical_paths(tasks, order, forecast, removed)
    slack = latest(tasks, order, forecast, removed, commit)
    baseline_finish = max(f for _, f in plan.values())
    if finish > commit:
        findings.append(finding("blocking", "schedule", "finish",
                                f"Forecast finish week {finish} is {finish - commit} week(s) after the committed week {commit}"))
    if len(paths) > 1:
        findings.append(finding("warning", "schedule", "critical paths",
                                f"{len(paths)} paths share the finish date; shortening one alone will not move it: "
                                + "; ".join(" > ".join(p) for p in paths)))
    for t in tasks:
        if t["status"] != "done" and plan[t["id"]][1] <= week and t["status"] == "in_progress":
            findings.append(finding("warning", "schedule", t["id"],
                                    f"{t['name']} was planned to finish week {plan[t['id']][1]} and is still in progress"))
    load = loads(program, forecast)
    for person, row in load.items():
        over = {w: v for w, v in row.items() if v > program["people"][person]["capacity"] + 1e-9}
        if over:
            span = f"weeks {min(over)}-{max(over)}" if len(over) > 1 else f"week {min(over)}"
            findings.append(finding("blocking" if any(slack.get(t["id"], 1) <= 0 for t in tasks if t["owner"] == person
                                                      and t["status"] != "done") else "warning",
                                    "capacity", person, f"Loaded to {max(over.values()):.0%} in {span}, including outside commitments"))
    for r in program["raid"]:
        if r["status"] in ("closed", "realized"):
            continue
        if not r["owner"]:
            findings.append(finding("blocking", "log", r["id"], f"{r['type']} has no owner: {r['title']}"))
        if r["due_week"] < week:
            findings.append(finding("warning", "log", r["id"], f"Response due week {r['due_week']} has passed"))
        if week - r["updated_week"] >= 3:
            findings.append(finding("warning", "log", r["id"], f"Not updated for {week - r['updated_week']} weeks"))
        if r["type"] == "issue" and r["severity"] == "high" and not r.get("decision"):
            findings.append(finding("blocking", "log", r["id"], "High-severity issue has no decision or escalation route"))
    authority = program["authority"]
    for d in program["decisions"]:
        rights = authority.get(d["id"])
        if not rights:
            findings.append(finding("blocking", "decisions", d["id"], "Decision has no decision-rights entry"))
            continue
        if d["status"] == "decided":
            if d["decided_by"] != rights["decide"]:
                findings.append(finding("blocking", "decisions", d["id"],
                                        f"Recorded as decided by {d['decided_by'] or 'nobody'}; the decision right belongs to "
                                        f"{rights['decide']}. Treat as a recommendation until {rights['decide']} decides"))
            missing = [a for a in rights["agree"] if a not in d["agreed_by"]]
            if missing:
                findings.append(finding("blocking", "decisions", d["id"], f"Required agreement missing from {', '.join(missing)}"))
    for c in program["changes"]:
        limit = program["change_threshold"]
        above = c["schedule_weeks"] >= limit["schedule_weeks"] or c["cost_usd"] >= limit["cost_usd"]
        if c["status"] == "approved" and above and c["approved_by"] != limit["approver"]:
            findings.append(finding("blocking", "change control", c["id"],
                                    f"Above threshold but approved by {c['approved_by']}; approver is {limit['approver']}"))
        if c["status"] == "pending" and above:
            findings.append(finding("warning", "change control", c["id"], f"Pending above-threshold change: {c['title']}"))
    for b in program["benefits"]:
        if b["baseline"] is None or not b["baseline_source"]:
            findings.append(finding("blocking", "benefits", b["id"], f"No baseline for '{b['measure']}'; the target cannot be evaluated"))
        if not b["owner"]:
            findings.append(finding("warning", "benefits", b["id"], f"No owner for '{b['measure']}'"))
    for m in program["milestones"]:
        if not m["acceptor"]:
            findings.append(finding("blocking", "acceptance", m["id"], f"Milestone '{m['name']}' has no accepting owner"))
    options = []
    for decision, choices in program.get("options_for_open_decisions", {}).items():
        for choice in choices:
            o, _, f, rem = schedule(tasks, week, choice.get("remove_dependency", []), choice.get("extra_weeks", {}))
            end, ps = critical_paths(tasks, o, f, rem)
            options.append({"decision": decision, "option": choice["option"], "finish_week": end,
                            "meets_commit": end <= commit, "cost_usd": choice.get("cost_usd", 0),
                            "binding_paths": [" > ".join(p) for p in ps], "gives_up": choice["gives_up"]})
    return {"program": program["program"], "synthetic": program.get("synthetic", False), "status_week": week,
            "committed_finish_week": commit, "baseline_finish_week": baseline_finish, "forecast_finish_week": finish,
            "critical_paths": [" > ".join(p) for p in paths], "forecast": {k: list(v) for k, v in forecast.items()},
            "slack": slack, "load": load, "findings": findings, "options": options}


def markdown(result, program):
    names = {t["id"]: t["name"] for t in program["tasks"]}
    blocking = [f for f in result["findings"] if f["severity"] == "blocking"]
    state = "Off track" if result["forecast_finish_week"] > result["committed_finish_week"] else (
        "At risk" if blocking else "On track")
    lines = [f"# {result['program']}: status week {result['status_week']}" + (" (synthetic)" if result["synthetic"] else ""), "",
             f"**{state}.** Forecast finish week {result['forecast_finish_week']} against a commitment of week "
             f"{result['committed_finish_week']} (baseline plan: week {result['baseline_finish_week']}). "
             f"{len(blocking)} blocking finding(s).", "",
             "## Critical path", ""]
    lines += [f"- {p}" for p in result["critical_paths"]]
    lines += ["", "## Schedule", "", "| Task | Forecast weeks | Slack to commitment |", "|---|---|---:|"]
    status = {t["id"]: t["status"] for t in program["tasks"]}
    lines += [f"| {tid} {names[tid]} | {s}-{f} | {'done' if status[tid] == 'done' else result['slack'][tid]} |"
              for tid, (s, f) in result["forecast"].items()]
    lines += ["", "## Decision needed", ""]
    if result["options"]:
        lines += ["| Option | Finish week | Meets commitment | Cost | Binding path(s) | Gives up |", "|---|---:|---|---:|---|---|"]
        lines += [f"| {o['option']} | {o['finish_week']} | {'yes' if o['meets_commit'] else 'no'} | ${o['cost_usd']:,} | "
                  f"{'; '.join(o['binding_paths'])} | {o['gives_up']} |" for o in result["options"]]
    lines += ["", "## Findings", "", "| Severity | Area | Item | Finding |", "|---|---|---|---|"]
    lines += [f"| {f['severity']} | {f['area']} | {f['item']} | {f['message']} |" for f in result["findings"]]
    over = {p: {w: v for w, v in row.items() if v > 1} for p, row in result["load"].items()}
    lines += ["", "## Capacity above 100%", ""]
    lines += [f"- {p}: " + ", ".join(f"week {w} {v:.0%}" for w, v in row.items()) for p, row in over.items() if row] or ["- None"]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("program")
    parser.add_argument("--markdown", help="Write a status pack to this path")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    program = json.loads(pathlib.Path(args.program).read_text(encoding="utf-8"))
    result = check(copy.deepcopy(program))
    if args.markdown:
        pathlib.Path(args.markdown).write_text(markdown(result, program), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["forecast_finish_week", "committed_finish_week", "critical_paths", "options"]}
                     | {"blocking": sum(f["severity"] == "blocking" for f in result["findings"]),
                        "warnings": sum(f["severity"] == "warning" for f in result["findings"])}, indent=2))
    return 1 if args.strict and any(f["severity"] == "blocking" for f in result["findings"]) else 0


if __name__ == "__main__":
    sys.exit(main())

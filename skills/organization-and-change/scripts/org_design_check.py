"""Org design check: spans and layers before and after, capacity with hiring ramp, costed transition, and a
pooled-versus-dedicated staffing test. Python 3.10+, stdlib.

Usage:
  python org_design_check.py --roster ../examples/org-roster.csv --plan ../examples/org-design-plan.json [--markdown out.md]

Spans and layers are prompts to inspect work, not targets. A narrow span can be right for a player-coach in
specialist work; a wide one can be right for routine work. The script flags where the observed span sits outside
the range for the manager's declared role type, and where a manager has one or two reports, so owners can ask why.
The queueing test uses the Erlang C formula, which assumes random arrivals and exponential review times; real
reviews are burstier, so treat waits as a lower bound.
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import math
import pathlib
import sys


def load_roster(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return {r["id"]: r for r in csv.DictReader(handle)}


def apply_changes(roster, changes):
    people = copy.deepcopy(roster)
    for change in changes:
        fields = {k: v for k, v in change.items() if k not in ("id", "new", "match_manager", "match_title", "first")}
        if change.get("new"):
            people[change["id"]] = {"id": change["id"], "title": "", "manager_id": "", "team": "", "role_type": "ic",
                                    "declared_archetype": ""} | fields
        elif "match_manager" in change:
            for p in people.values():
                if p["manager_id"] == change["match_manager"] and p["id"] != change.get("id"):
                    p.update(fields)
        elif "match_title" in change:
            matches = [p for p in people.values() if p["title"] == change["match_title"]]
            for p in matches[: change.get("first", len(matches))]:
                p.update(fields)
        else:
            if change["id"] not in people:
                raise ValueError(f"Change refers to unknown person {change['id']}")
            people[change["id"]].update(fields)
    return people


def structure(people, archetypes):
    reports = {pid: [] for pid in people}
    roots = []
    for p in people.values():
        if p["manager_id"]:
            if p["manager_id"] not in people:
                raise ValueError(f"{p['id']} reports to unknown manager {p['manager_id']}")
            reports[p["manager_id"]].append(p["id"])
        else:
            roots.append(p["id"])
    if len(roots) != 1:
        raise ValueError(f"Expected one top of the scope, found {roots}")
    depth, stack = {roots[0]: 1}, [roots[0]]
    while stack:
        current = stack.pop()
        for r in reports[current]:
            if r in depth:
                raise ValueError(f"Reporting cycle at {r}")
            depth[r] = depth[current] + 1
            stack.append(r)
    if len(depth) != len(people):
        raise ValueError("Some people are not connected to the top of the scope (cycle or orphan)")
    managers = [p for p in people.values() if reports[p["id"]]]
    flags = []
    for m in managers:
        span = len(reports[m["id"]])
        low_high = archetypes.get(m["declared_archetype"])
        if span <= 2:
            flags.append({"id": m["id"], "title": m["title"], "span": span,
                          "flag": "one or two reports: check whether the role is a lead, a layer that adds a handoff, or a deliberate specialist manager"})
        elif low_high and not low_high[0] <= span <= low_high[1]:
            flags.append({"id": m["id"], "title": m["title"], "span": span,
                          "flag": f"span outside the {m['declared_archetype']} range {low_high[0]}-{low_high[1]}"})
        if m["role_type"] == "ic":
            flags.append({"id": m["id"], "title": m["title"], "span": span, "flag": "has reports but is recorded as an individual contributor"})
    for p in people.values():
        if p["role_type"] == "manager" and not reports[p["id"]]:
            flags.append({"id": p["id"], "title": p["title"], "span": 0, "flag": "manager role with no reports"})
    spans = sorted(len(reports[m["id"]]) for m in managers)
    return {"people": len(people), "managers": len(managers), "layers": max(depth.values()),
            "median_span": spans[len(spans) // 2] if spans else 0, "mean_span": round(sum(spans) / len(spans), 2) if spans else 0,
            "spans": {m["id"]: len(reports[m["id"]]) for m in managers}, "flags": flags,
            "deepest": sorted([pid for pid, d in depth.items() if d == max(depth.values())])}


def capacity(plan):
    cp = plan["capacity_plan"]
    out = {}
    for team, info in cp["teams"].items():
        staffed, productive, rows = info["current_fte"], info["current_fte"], []
        for i, q in enumerate(cp["quarters"]):
            new = info["hires"].get(q, 0)
            previous = info["hires"].get(cp["quarters"][i - 1], 0) if i else 0
            staffed_now = staffed + new
            productive = staffed_now - new * (1 - cp["ramp_first_quarter"])
            rows.append({"quarter": q, "staffed": staffed_now, "productive": round(productive, 2), "demand": info["demand_fte"][i],
                         "gap": round(productive - info["demand_fte"][i], 2)})
            staffed = staffed_now
            del previous
        out[team] = rows
    return out


def costs(plan):
    c, cp = plan["costs"], plan["capacity_plan"]
    quarters = cp["quarters"]
    run, one = {q: 0.0 for q in quarters}, {q: 0.0 for q in quarters}
    for team, info in cp["teams"].items():
        annual = c["loaded_annual_cost"][team]
        cumulative = 0
        for q in quarters:
            hires = info["hires"].get(q, 0)
            cumulative += hires
            run[q] += cumulative * annual / 4
            one[q] += hires * annual * c["recruiting_fee_share_of_annual"]
    for role, start in c["new_roles_start"].items():
        for q in quarters[quarters.index(start):]:
            run[q] += c["loaded_annual_cost"][role] / 4
    for item in c["one_time"]:
        one[item["quarter"]] += item["usd"]
    rows = [{"quarter": q, "added_run_rate": round(run[q]), "one_time": round(one[q]), "total": round(run[q] + one[q])} for q in quarters]
    return {"by_quarter": rows, "first_year_total": sum(r["total"] for r in rows),
            "exit_annual_run_rate": round(run[quarters[-1]] * 4)}


def erlang_c(servers, offered):
    """Probability an arrival waits, for `servers` parallel reviewers and `offered` load in erlangs."""
    if offered >= servers:
        return 1.0
    total = sum(offered ** k / math.factorial(k) for k in range(servers))
    top = offered ** servers / math.factorial(servers) * servers / (servers - offered)
    return top / (total + top)


def pool_test(plan):
    test, week_hours = plan["review_pool_test"], plan["productive_hours_per_fte_week"]
    results = []
    for option in test["options"]:
        pools = []
        for pool in option["pools"]:
            streams = [test["streams"][s] for s in pool["streams"]]
            arrivals = sum(s["arrivals_per_week"] for s in streams)
            work = sum(s["arrivals_per_week"] * s["hours_each"] for s in streams)
            mean_service = work / arrivals
            offered = work / week_hours                    # erlangs: busy reviewers needed on average
            n = pool["reviewers"]
            wait_probability = erlang_c(n, offered)
            if offered >= n:
                wait_days = math.inf
            else:
                wait_hours = wait_probability * mean_service / (n - offered)
                wait_days = wait_hours / (week_hours / 5)  # productive hours per working day
            pools.append({"streams": pool["streams"], "reviewers": n, "utilization": round(offered / n, 3),
                          "probability_of_waiting": round(wait_probability, 3),
                          "mean_wait_working_days": round(wait_days, 2) if math.isfinite(wait_days) else None})
        results.append({"option": option["name"], "reviewers": sum(p["reviewers"] for p in option["pools"]), "pools": pools})
    return results


def check(roster, plan):
    before = structure(roster, plan["span_archetypes"])
    after = structure(apply_changes(roster, plan["changes"]), plan["span_archetypes"])
    return {"synthetic": plan.get("synthetic", False), "scope": plan["scope"], "before": before, "after": after,
            "capacity": capacity(plan), "costs": costs(plan), "review_pool_test": pool_test(plan)}


def markdown(result):
    b, a = result["before"], result["after"]
    lines = [f"# Org design check{' (synthetic)' if result['synthetic'] else ''}", "", result["scope"], "",
             "## Spans and layers", "", "| Measure | Before | After |", "|---|---:|---:|",
             f"| People | {b['people']} | {a['people']} |", f"| Managers | {b['managers']} | {a['managers']} |",
             f"| Layers | {b['layers']} | {a['layers']} |", f"| Median span | {b['median_span']} | {a['median_span']} |",
             f"| Mean span | {b['mean_span']} | {a['mean_span']} |", "", "### Flags before", ""]
    lines += [f"- {f['id']} {f['title']} (span {f['span']}): {f['flag']}" for f in b["flags"]] or ["- None"]
    lines += ["", "### Flags after", ""]
    lines += [f"- {f['id']} {f['title']} (span {f['span']}): {f['flag']}" for f in a["flags"]] or ["- None"]
    lines += ["", "## Capacity against demand (FTE)", "", "| Team | Quarter | Staffed | Productive after ramp | Demand | Gap |", "|---|---|---:|---:|---:|---:|"]
    for team, rows in result["capacity"].items():
        lines += [f"| {team} | {r['quarter']} | {r['staffed']} | {r['productive']} | {r['demand']} | {r['gap']} |" for r in rows]
    lines += ["", "## Transition cost", "", "| Quarter | Added run-rate | One-time | Total |", "|---|---:|---:|---:|"]
    lines += [f"| {r['quarter']} | ${r['added_run_rate']:,} | ${r['one_time']:,} | ${r['total']:,} |" for r in result["costs"]["by_quarter"]]
    lines += [f"", f"First-year total ${result['costs']['first_year_total']:,}; exit annual run-rate ${result['costs']['exit_annual_run_rate']:,}.",
              "", "## Pooled versus dedicated review capacity", "", "| Option | Pool | Reviewers | Utilization | Chance of waiting | Mean wait (working days) |", "|---|---|---:|---:|---:|---:|"]
    for o in result["review_pool_test"]:
        for p in o["pools"]:
            wait = "unbounded" if p["mean_wait_working_days"] is None else p["mean_wait_working_days"]
            lines.append(f"| {o['option']} | {' + '.join(p['streams'])} | {p['reviewers']} | {p['utilization']:.0%} | {p['probability_of_waiting']:.0%} | {wait} |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--roster", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--markdown")
    args = parser.parse_args()
    result = check(load_roster(args.roster), json.loads(pathlib.Path(args.plan).read_text(encoding="utf-8")))
    if args.markdown:
        pathlib.Path(args.markdown).write_text(markdown(result), encoding="utf-8")
    print(json.dumps({"layers": [result["before"]["layers"], result["after"]["layers"]],
                      "flags": [len(result["before"]["flags"]), len(result["after"]["flags"])],
                      "first_year_cost": result["costs"]["first_year_total"],
                      "pool_test": [(o["option"], [p["mean_wait_working_days"] for p in o["pools"]]) for o in result["review_pool_test"]]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

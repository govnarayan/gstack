"""End-to-end self-serve analytics case: synthetic warehouse -> SQL -> checks -> dashboard. Python 3.10+, stdlib.

Runs two versions of five business queries against the same synthetic SQLite warehouse:
  sql/ai-draft/  first drafts of the kind an AI assistant commonly returns from a one-line request
  sql/reviewed/  the reviewed queries, with grain, definitions, exclusions and date handling stated
Each result is checked against an independent Python recomputation from raw rows (the "oracle"), plus
structural checks for join fan-out, denominators, NULL handling, rate arithmetic, cohort maturity and
partial periods. The reviewed set must pass every check; the draft set must fail the checks its defects break.

Usage:
  python analytics_demo.py --out <folder>            # builds the database, writes report and dashboard
  python analytics_demo.py --out <folder> --strict   # exit 1 if any reviewed check fails
Nothing is written inside the library. All data is invented.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import pathlib
import re
import sqlite3
import sys

HERE = pathlib.Path(__file__).resolve().parent
SQL = HERE.parent / "sql"
sys.path.insert(0, str(HERE))
import build_demo_db  # noqa: E402

QUERIES = ["monthly_revenue", "revenue_by_segment_q3", "activation_by_cohort", "active_at_quarter_end",
           "retention_90d_by_cohort"]
QUARTER_END = dt.date(2026, 9, 30)
TOLERANCE = 0.005


def rows(con, sql):
    cur = con.execute(sql)
    names = [d[0] for d in cur.description]
    return [dict(zip(names, r)) for r in cur.fetchall()]


def parse_ts(text):
    return dt.datetime.fromisoformat(text.replace(" ", "T"))


# ---------------------------------------------------------------- oracle: plain Python over raw rows
def oracle(con):
    accounts = {r["account_id"]: r for r in rows(con, "SELECT * FROM accounts")}
    real = {k for k, v in accounts.items() if not v["is_test"]}
    loaded = parse_ts(rows(con, "SELECT loaded_through FROM load_log WHERE table_name='events'")[0]["loaded_through"])
    invoices = rows(con, "SELECT * FROM invoices")
    subs = rows(con, "SELECT * FROM subscriptions")
    users = {r["user_id"]: r["account_id"] for r in rows(con, "SELECT user_id, account_id FROM users")}
    events = rows(con, "SELECT user_id, event_type, occurred_at FROM events")

    monthly = {}
    segment = {}
    for inv in invoices:
        if inv["status"] != "paid" or inv["account_id"] not in real:
            continue
        month = inv["invoice_date"][:7]
        monthly[month] = monthly.get(month, 0) + inv["amount_cents"] / 100
        if "2026-07-01" <= inv["invoice_date"] < "2026-10-01":
            seg = accounts[inv["account_id"]]["segment"]
            segment[seg] = segment.get(seg, 0) + inv["amount_cents"] / 100

    created = {k: parse_ts(accounts[k]["created_at"]) for k in real}
    def month_end(day):
        nxt = dt.date(day.year + (day.month == 12), day.month % 12 + 1, 1)
        return dt.datetime.combine(nxt, dt.time())  # first instant after the month
    eligible = {k for k in real if month_end(created[k]) + dt.timedelta(days=14) <= loaded}
    flags = {k: set() for k in eligible}
    for ev in events:
        account = users[ev["user_id"]]
        if account in flags and created[account] <= parse_ts(ev["occurred_at"]) < created[account] + dt.timedelta(days=14):
            flags[account].add(ev["event_type"])
    activation = {}
    for k in eligible:
        month = accounts[k]["created_at"][:7]
        bucket = activation.setdefault(month, {"accounts": 0, "activated": 0})
        bucket["accounts"] += 1
        bucket["activated"] += int({"create_project", "invite_teammate"} <= flags[k])

    def active_on(account, day):
        iso = day.isoformat()
        return [s for s in subs if s["account_id"] == account and s["started_at"] <= iso
                and (s["ended_at"] is None or s["ended_at"] > iso)]
    active = [s for k in real for s in active_on(k, QUARTER_END)]
    first = {}
    for s in subs:
        if s["account_id"] in real:
            first[s["account_id"]] = min(first.get(s["account_id"], s["started_at"]), s["started_at"])
    retention = {}
    for k, start in first.items():
        check_day = dt.date.fromisoformat(start) + dt.timedelta(days=90)
        if (month_end(dt.date.fromisoformat(start)).date() - dt.timedelta(days=1)) + dt.timedelta(days=90) > loaded.date():
            continue
        bucket = retention.setdefault(start[:7], {"accounts": 0, "retained": 0})
        bucket["accounts"] += 1
        bucket["retained"] += int(bool(active_on(k, check_day)))
    return {"loaded_through": loaded, "monthly": monthly, "segment": segment, "activation": activation,
            "active_accounts": len({s["account_id"] for s in active}), "mrr": sum(s["mrr_cents"] for s in active) / 100,
            "retention": retention, "eligible_accounts": len(eligible),
            "open_subscriptions": sum(1 for s in subs if s["ended_at"] is None and s["account_id"] in real
                                      and s["started_at"] <= QUARTER_END.isoformat())}


# ---------------------------------------------------------------- checks
def close(a, b):
    return a is not None and b is not None and abs(float(a) - float(b)) <= TOLERANCE * max(1.0, abs(float(b)))


def check(name, passed, detail, kind="error"):
    return {"check": name, "status": "pass" if passed else ("warn" if kind == "warn" else "fail"), "detail": detail}


def fanout_probe(con, sql, key):
    """Re-run the query's own FROM/JOIN/WHERE clause and compare row count with distinct base keys."""
    clause = re.search(r"\bFROM\b(.*?)(\bGROUP BY\b|\bORDER BY\b|;|$)", sql, re.S | re.I).group(1)
    total, distinct = con.execute(f"SELECT COUNT(*), COUNT(DISTINCT {key}) FROM {clause}").fetchone()
    return total, distinct


def run_checks(con, name, sql, result, truth, reviewed_monthly):
    out = []
    loaded_month = truth["loaded_through"].strftime("%Y-%m")
    if name == "monthly_revenue":
        bad = [r["month"] for r in result if not close(r["revenue_usd"], truth["monthly"].get(r["month"]))]
        out.append(check("matches independent recomputation (paid invoices, test accounts excluded)", not bad,
                         f"months that disagree: {bad}" if bad else "all months agree"))
        partial = [r["month"] for r in result if r["month"] >= loaded_month]
        out.append(check("partial final period is labeled, not compared with full months", not partial,
                         f"{partial} is loaded only through {truth['loaded_through']:%Y-%m-%d}; the dashboard must label it partial",
                         kind="warn"))
    elif name == "revenue_by_segment_q3":
        total = sum(r["revenue_usd"] for r in result)
        q3 = sum(v for k, v in reviewed_monthly.items() if "2026-07" <= k <= "2026-09")
        out.append(check("segment total reconciles to the monthly revenue total for Jul-Sep", close(total, q3),
                         f"segments sum to {total:,.2f}; monthly query says {q3:,.2f}"))
        joined, invoices = fanout_probe(con, sql, "i.invoice_id")
        out.append(check("joins keep one row per invoice (no fan-out)", joined == invoices,
                         f"{joined} joined rows for {invoices} invoices"
                         + ("" if joined == invoices else f": each invoice repeated about {joined / invoices:.1f} times")))
    elif name == "activation_by_cohort":
        accounts = sum(r["accounts"] for r in result)
        out.append(check("denominator is every eligible account, including those with no events",
                         accounts == truth["eligible_accounts"],
                         f"query counts {accounts} accounts; eligible non-test accounts in cohorts whose 14-day window closed = {truth['eligible_accounts']}"))
        arithmetic = [r["cohort_month"] for r in result
                      if not (0 <= (r["activation_rate"] or 0) <= 1 and r["accounts"]
                              and close(r["activation_rate"], r["activated"] / r["accounts"]))]
        out.append(check("rate equals activated / accounts (no integer division)", not arithmetic,
                         f"cohorts with wrong arithmetic: {arithmetic}" if arithmetic else "rates match their counts"))
        wrong = [r["cohort_month"] for r in result
                 if truth["activation"].get(r["cohort_month"], {}).get("activated") != r["activated"]]
        out.append(check("activated counts match the definition (project AND invite within 14 days)", not wrong,
                         f"cohorts that disagree: {wrong}" if wrong else "all cohorts agree"))
    elif name == "active_at_quarter_end":
        r = result[0]
        out.append(check("open-ended subscriptions (ended_at IS NULL) are counted as active",
                         (r["active_accounts"] or 0) >= truth["open_subscriptions"],
                         f"{truth['open_subscriptions']} open subscriptions started by {QUARTER_END}; query counts {r['active_accounts']} active accounts"))
        out.append(check("matches independent recomputation", close(r["active_accounts"], truth["active_accounts"])
                         and close(r["mrr_usd"], truth["mrr"]),
                         f"query {r['active_accounts']} accounts / {r['mrr_usd']}; recomputed {truth['active_accounts']} / {truth['mrr']:,.2f}"))
    elif name == "retention_90d_by_cohort":
        def closed(month):
            first = dt.date.fromisoformat(month + "-01")
            last = dt.date(first.year + (first.month == 12), first.month % 12 + 1, 1) - dt.timedelta(days=1)
            return last + dt.timedelta(days=90) <= truth["loaded_through"].date()
        immature = [r["cohort_month"] for r in result if not closed(r["cohort_month"])]
        out.append(check("only cohorts whose 90-day window has closed for every member are shown", not immature,
                         f"immature cohorts included: {immature}" if immature else "all cohorts mature"))
        wrong = [r["cohort_month"] for r in result
                 if truth["retention"].get(r["cohort_month"], {}).get("retained") != r["retained_90d"]
                 or truth["retention"].get(r["cohort_month"], {}).get("accounts") != r["accounts"]]
        out.append(check("retained counts measure status at start + 90 days, not today", not wrong,
                         f"cohorts that disagree: {wrong}" if wrong else "all cohorts agree"))
    return out


# ---------------------------------------------------------------- dashboard
def bar_chart(points, value_key, label_key, fmt, note_key=None, title=""):
    width, height, pad = 640, 220, 36
    peak = max([p[value_key] or 0 for p in points] + [1e-9])
    step = (width - pad * 2) / max(len(points), 1)
    bars = []
    for i, p in enumerate(points):
        value = p[value_key] or 0
        h = (height - pad * 2) * value / peak
        x, y = pad + i * step + step * 0.15, height - pad - h
        partial = note_key and p.get(note_key)
        cls = "bar partial" if partial else "bar"
        bars.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{step * 0.7:.1f}" height="{h:.1f}">'
                    f'<title>{html.escape(str(p[label_key]))}: {html.escape(fmt(value))}{" (partial)" if partial else ""}</title></rect>'
                    f'<text class="val" x="{x + step * 0.35:.1f}" y="{y - 4:.1f}">{html.escape(fmt(value))}</text>'
                    f'<text class="lab" x="{x + step * 0.35:.1f}" y="{height - pad + 14:.1f}">{html.escape(str(p[label_key])[2:])}'
                    f'{"*" if partial else ""}</text>')
    return (f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">'
            f'<line class="axis" x1="{pad}" y1="{height - pad}" x2="{width - pad}" y2="{height - pad}"/>{"".join(bars)}</svg>')


def dashboard(reviewed, draft, checks, truth, built_at):
    money = lambda v: f"${v:,.0f}"
    pct = lambda v: f"{v * 100:.0f}%"
    revenue = [dict(r, partial=r["month"] >= truth["loaded_through"].strftime("%Y-%m")) for r in reviewed["monthly_revenue"]]
    q3 = sum(r["revenue_usd"] for r in reviewed["revenue_by_segment_q3"])
    active = reviewed["active_at_quarter_end"][0]
    act = reviewed["activation_by_cohort"]
    ret = reviewed["retention_90d_by_cohort"]
    age_hours = (built_at - truth["loaded_through"]).total_seconds() / 3600
    fresh = "fresh" if age_hours <= 36 else "stale"
    reviewed_pass = all(c["status"] != "fail" for q in checks["reviewed"].values() for c in q)
    seg_rows = "".join(f"<tr><td>{html.escape(r['segment'])}</td><td>{money(r['revenue_usd'])}</td>"
                       f"<td>{r['revenue_usd'] / q3:.0%}</td><td>{r['paying_accounts']}</td></tr>"
                       for r in reviewed["revenue_by_segment_q3"])
    draft_q3 = sum(r["revenue_usd"] for r in draft["revenue_by_segment_q3"])
    d_act = draft["activation_by_cohort"]
    compare = [
        ("Q3 revenue by segment, total", money(draft_q3), money(q3), "join to users repeated each invoice once per active user"),
        ("Active accounts on Sep 30", f"{draft['active_at_quarter_end'][0]['active_accounts']}", f"{active['active_accounts']}",
         "ended_at > date silently drops open subscriptions (NULL)"),
        ("Activation rate, latest cohort", f"{d_act[-1]['activation_rate']}", pct(act[-1]['activation_rate']),
         "integer division, OR instead of AND, inner join drops accounts with no events, test accounts kept"),
        ("90-day retention, latest cohort shown", f"{draft['retention_90d_by_cohort'][-1]['cohort_month']}: {pct(draft['retention_90d_by_cohort'][-1]['retention_90d'])}",
         f"{ret[-1]['cohort_month']}: {pct(ret[-1]['retention_90d'])}", "status today instead of at day 90, and immature cohorts kept"),
    ]
    compare_rows = "".join(f"<tr><td>{a}</td><td class='bad'>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in compare)
    check_rows = "".join(
        f"<tr><td>{html.escape(q)}</td><td>{html.escape(c['check'])}</td><td class='{c['status']}'>{c['status'].upper()}</td>"
        f"<td class='{d['status']}'>{d['status'].upper()}</td></tr>"
        for q in QUERIES for c, d in zip(checks["reviewed"][q], checks["ai-draft"][q]))
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Synthetic Revenue Dashboard</title><style>
:root{{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a64;--line:#dedbd2;--card:#ffffff;--bar:#3d6b8c;--partial:#b7c7d4;--bad:#a23b2a;--ok:#2f6b3a;--warn:#8a6a12}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#161614;--fg:#ecebe6;--muted:#a3a29b;--line:#34332f;--card:#1f1f1c;--bar:#79a7c8;--partial:#3c5568;--bad:#e2806f;--ok:#7fc28b;--warn:#d9b45a}}}}
:root[data-theme="dark"]{{--bg:#161614;--fg:#ecebe6;--muted:#a3a29b;--line:#34332f;--card:#1f1f1c;--bar:#79a7c8;--partial:#3c5568;--bad:#e2806f;--ok:#7fc28b;--warn:#d9b45a}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif;margin:0;padding:24px 16px;}}
main{{max-width:980px;margin:0 auto}} h1{{font-size:22px;margin:0 0 4px}} h2{{font-size:16px;margin:28px 0 8px}}
.muted{{color:var(--muted)}} .tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:16px}}
.tile{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px}} .tile b{{display:block;font-size:24px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;overflow-x:auto}}
svg{{width:100%;height:auto}} .bar{{fill:var(--bar)}} .bar.partial{{fill:var(--partial)}} .axis{{stroke:var(--line)}}
.val,.lab{{font-size:10px;text-anchor:middle;fill:var(--muted)}} table{{border-collapse:collapse;width:100%;font-size:13px}}
td,th{{border-bottom:1px solid var(--line);padding:6px;text-align:left;vertical-align:top}} .bad,.fail{{color:var(--bad)}} .pass{{color:var(--ok)}} .warn{{color:var(--warn)}}
</style></head><body><main>
<h1>Synthetic revenue and activation dashboard</h1>
<p class="muted">Invented data for a teaching case. Data loaded through {truth['loaded_through']:%Y-%m-%d %H:%M} UTC; built {built_at:%Y-%m-%d %H:%M} UTC ({fresh}, {age_hours:.0f} hours old).
Reviewed queries: {"all checks pass" if reviewed_pass else "CHECK FAILURES, do not use"}. Owner: synthetic BizOps analyst. Next scheduled review: monthly.</p>
<div class="tiles">
<div class="tile"><span class="muted">Q3 2026 collected revenue</span><b>{money(q3)}</b><span class="muted">paid invoices, test accounts excluded</span></div>
<div class="tile"><span class="muted">Paying accounts on Sep 30</span><b>{active['active_accounts']}</b><span class="muted">MRR {money(active['mrr_usd'])}</span></div>
<div class="tile"><span class="muted">14-day activation, {act[-1]['cohort_month']} cohort</span><b>{pct(act[-1]['activation_rate'])}</b><span class="muted">{act[-1]['activated']} of {act[-1]['accounts']} accounts</span></div>
<div class="tile"><span class="muted">90-day retention, {ret[-1]['cohort_month']} cohort</span><b>{pct(ret[-1]['retention_90d'])}</b><span class="muted">{ret[-1]['retained_90d']} of {ret[-1]['accounts']} accounts</span></div>
</div>
<h2>Collected revenue by month</h2><div class="card">{bar_chart(revenue, "revenue_usd", "month", money, "partial", "Collected revenue by month")}
<p class="muted">* Partial month: loaded through {truth['loaded_through']:%b %d}. Do not compare it with full months.</p></div>
<h2>14-day activation by signup month</h2><div class="card">{bar_chart(act, "activation_rate", "cohort_month", pct, title="Activation by cohort")}
<p class="muted">Denominator includes accounts with no activity. Small cohorts move a lot: n ranges from {min(r['accounts'] for r in act)} to {max(r['accounts'] for r in act)}.</p></div>
<h2>90-day retention by first-payment month</h2><div class="card">{bar_chart(ret, "retention_90d", "cohort_month", pct, title="Retention by cohort")}
<p class="muted">Only cohorts whose 90-day window closed before the data load are shown.</p></div>
<h2>Q3 revenue by segment</h2><div class="card"><table><tr><th>Segment</th><th>Revenue</th><th>Share</th><th>Paying accounts</th></tr>{seg_rows}</table></div>
<h2>What the unreviewed AI drafts would have reported</h2><div class="card"><table><tr><th>Measure</th><th>AI draft</th><th>Reviewed</th><th>Why the draft is wrong</th></tr>{compare_rows}</table></div>
<h2>Checks</h2><div class="card"><table><tr><th>Query</th><th>Check</th><th>Reviewed</th><th>AI draft</th></tr>{check_rows}</table></div>
<h2>Definitions</h2><div class="card"><table>
<tr><td>Collected revenue</td><td>Sum of invoices with status paid, in the invoice month. Void and refunded invoices excluded. Not recognized revenue under accounting rules.</td></tr>
<tr><td>Paying account on a date</td><td>A subscription started on or before the date and not ended by it (open subscriptions have no end date).</td></tr>
<tr><td>14-day activation</td><td>Within 14 days of account creation, any user created a project and any user invited a teammate.</td></tr>
<tr><td>90-day retention</td><td>The account has an active subscription 90 days after its first subscription began.</td></tr>
<tr><td>Exclusions</td><td>Internal test accounts (is_test = 1).</td></tr></table></div>
</main></body></html>"""


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", required=True, help="Folder for demo.sqlite, report.json, report.md and dashboard.html")
    parser.add_argument("--built-at", default="2026-10-20T15:00:00", help="Simulated build time (UTC) for the freshness label")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if any reviewed check fails")
    args = parser.parse_args()
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(build_demo_db.build(out / "demo.sqlite"))
    truth = oracle(con)
    results, checks = {}, {}
    for variant in ["reviewed", "ai-draft"]:
        results[variant] = {q: rows(con, (SQL / variant / f"{q}.sql").read_text(encoding="utf-8")) for q in QUERIES}
    reviewed_monthly = {r["month"]: r["revenue_usd"] for r in results["reviewed"]["monthly_revenue"]}
    for variant in ["reviewed", "ai-draft"]:
        checks[variant] = {q: run_checks(con, q, (SQL / variant / f"{q}.sql").read_text(encoding="utf-8"),
                                         results[variant][q], truth, reviewed_monthly) for q in QUERIES}
    built_at = dt.datetime.fromisoformat(args.built_at)
    (out / "dashboard.html").write_text(dashboard(results["reviewed"], results["ai-draft"], checks, truth, built_at), encoding="utf-8")
    summary = {v: {q: [c["status"] for c in checks[v][q]] for q in QUERIES} for v in checks}
    report = {"synthetic": True, "loaded_through": truth["loaded_through"].isoformat(), "results": results,
              "checks": checks, "summary": summary}
    (out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    lines = ["# Self-serve analytics check report (synthetic)", ""]
    for v in ["reviewed", "ai-draft"]:
        lines.append(f"## {v}")
        for q in QUERIES:
            for c in checks[v][q]:
                lines.append(f"- {c['status'].upper()} {q}: {c['check']}. {c['detail']}")
        lines.append("")
    (out / "report.md").write_text("\n".join(lines), encoding="utf-8")
    con.close()
    failures = sum(c["status"] == "fail" for q in checks["reviewed"].values() for c in q)
    caught = sum(c["status"] == "fail" for q in checks["ai-draft"].values() for c in q)
    print(json.dumps({"reviewed_failures": failures, "draft_failures_caught": caught, "dashboard": str(out / "dashboard.html")}))
    return 1 if args.strict and failures else 0


if __name__ == "__main__":
    sys.exit(main())

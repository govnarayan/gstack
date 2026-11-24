# Worked case: from warehouse to dashboard

All data is invented. The numbers below come from running the case. They show how the method behaves, not results for any company.

## The setting

A growth-stage SaaS company has a small warehouse with six tables: `accounts`, `users`, `subscriptions`, `invoices`, `events` and `load_log`. The BizOps lead must prepare the Q3 business review. The CEO wants four answers: Q3 revenue and where it came from, paying accounts at quarter end, whether new accounts are activating, and whether early customers stay. The data team is busy with a migration, so the BizOps lead self-serves with an AI assistant.

The data contains the conditions that break real queries. Accounts have 1 to 80 users. Plan upgrades close one subscription row and open another. Open subscriptions have no end date. About 4 percent of invoices are void and 1 percent refunded. Six internal QA accounts carry large invoices. The last load ran on October 20, so October is partial.

Run it yourself:

```sh
python skills/self-serve-analytics/scripts/analytics_demo.py --out <scratch folder>
```

It writes `demo.sqlite`, `report.md`, `report.json` and `dashboard.html` to that folder.

## What the first drafts said

The lead gave the assistant one-line requests, as many people do. Every query ran without an error. The [drafts](../sql/ai-draft/) are kept unedited.

| Question | AI draft answer | Reviewed answer | Defect |
|---|---|---|---|
| Q3 revenue by segment | $2,312,640, Enterprise largest | $112,320, Mid-Market largest, Enterprise smallest | Joining invoices to users repeated each invoice about 10.5 times. Enterprise accounts have the most users, so the error also reversed the segment ranking |
| Paying accounts on Sep 30 | 8 accounts, $1,830 MRR | 207 accounts, $44,220 MRR | `ended_at > '2026-09-30'` is never true for open subscriptions, whose end date is NULL |
| 14-day activation by cohort | 0 for every month | 23 to 53 percent | Integer division returned zero. Underneath it, the inner join dropped accounts with no events, OR replaced AND, and test accounts stayed in |
| 90-day retention by cohort | Rising from 70 percent in January to 100 percent in September and October | 89 to 100 percent for January to June, and no later cohorts shown | Retention was measured as "subscribed today", which penalizes old cohorts and flatters young ones. Cohorts whose 90 days had not elapsed were included |
| Monthly revenue | January $15,720 | January $6,720 | Void and refunded invoices and QA accounts counted |

The retention draft is the most dangerous. It does not look broken. It tells a pleasing story of improving retention that the data does not support.

## How the review caught each defect

The script checks every result two ways. First, an independent recomputation in plain Python from raw rows, sharing no SQL logic. Second, structural checks aimed at specific failure types.

| Check | What it compares | Catches |
|---|---|---|
| Reconciliation | Segment total against the monthly revenue total for July to September | Fan-out, filter differences |
| Grain probe | Rows after the query's own joins against distinct invoices | Fan-out, quantified (5,639 rows for 539 invoices) |
| Denominator | Activation denominator against eligible accounts counted separately | Inner-join shrinkage, test accounts |
| Rate arithmetic | Each rate against its own numerator divided by denominator | Integer division |
| Open subscriptions | Active count against subscriptions with no end date | NULL comparisons |
| Maturity | Cohorts shown against cohorts whose window closed for every member | Immature cohorts |
| Partial period | Months after the last load | Partial months shown as full |

The reviewed queries pass every check. The drafts fail ten. October is flagged as a partial period in both, and the dashboard marks it.

## Reviewing a query step by step

Take the reviewed [activation query](../sql/reviewed/activation_by_cohort.sql).

1. `cohort` defines the denominator once: non-test accounts in signup months whose 14-day window closed before the data load, including the month's last day.
2. `early` reduces many events to one row per account with two flags. Doing this before joining back is what prevents fan-out.
3. The final step uses `LEFT JOIN`, so accounts that never acted count as not activated rather than disappearing.
4. `1.0 *` forces decimal division.
5. Both timestamps go through `datetime()` because stored values use a `T` separator and SQLite's function returns a space. Compared as raw text, a `T` timestamp is always later than a space timestamp on the same date.

Each line answers a question a reviewer should ask. When an assistant cannot explain a line this way, treat the line as suspect.

## A rival interpretation the case does not settle

January's 53 percent activation against 23 to 48 percent later could mean onboarding got worse. With cohorts of 18 to 32 accounts, a few accounts move the rate by ten points. The dashboard shows the counts beside the rates for this reason. A real review would check whether the January cohort differed in segment mix or acquisition channel before calling a decline.

## The dashboard

`dashboard.html` shows headline tiles with denominators and monthly revenue with October marked partial. It also shows activation and retention by mature cohort and Q3 revenue by segment. Further sections give a table of what the drafts would have reported, every check's status and definitions. Its header gives the load time, build time, freshness, owner and review cadence. If the build runs more than 36 hours after the last load, the dashboard labels itself stale.

## What this case does and does not show

It shows that a short checklist and two independent routes to each number catch the common defects in AI-drafted SQL, including ones that produce believable output. It does not show that the checks are complete. A warehouse with slowly changing dimensions, currency conversion, revenue recognition rules or late-arriving events needs more. Nor does it establish anyone's proficiency at a real company. That comes from correct, reviewed answers on that company's data.

The reviewed activation query checks both endpoints. An event at signup qualifies. An event before signup or at signup plus 14 days falls outside the window. The test plants two qualifying actions before signup and checks that only the denominator grows.

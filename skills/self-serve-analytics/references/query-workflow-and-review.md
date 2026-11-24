# Query workflow and review

This is the procedure for turning a business question into a number you can defend. It applies whether you type the SQL, an AI assistant drafts it, or a colleague hands it over. The examples use the tables in the [worked case](worked-analytics-case.md).

## 1. Pin the question

Write four things before touching data:

| Item | Example |
|---|---|
| Decision and audience | Product lead decides whether to delay a pricing change if new-account activation fell |
| Metric and definition | 14-day activation: within 14 days of account creation, some user created a project and some user invited a teammate |
| Population and period | Non-test accounts created January to September 2026, grouped by signup month |
| Precision needed | A drop of five points or more matters. Smaller moves are noise at these cohort sizes |

If you cannot write the definition, the question is not ready. Find the existing definition first (a metrics catalog, a governed metric in the BI tool, the data team, a finance policy). Write a new one only when none exists, and label it provisional.

## 2. Inspect the schema and the grain

Grain is what one row in a table represents. Most wrong numbers come from misreading it.

1. List tables and columns. In SQLite `PRAGMA table_info(invoices);`, in Postgres or most warehouses `SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'invoices';`.
2. State the grain of each table in one sentence and test it: `SELECT COUNT(*), COUNT(DISTINCT invoice_id) FROM invoices;` should match if `invoice_id` is the key.
3. Find the relationships. One account has many users, many subscriptions over time and many invoices. A subscription row closes and a new one opens on a plan change. Draw this before joining.
4. Profile the fields you will filter or group on: `SELECT status, COUNT(*) FROM invoices GROUP BY 1;` reveals `void` and `refunded`. `SELECT is_test, COUNT(*) FROM accounts GROUP BY 1;` reveals internal accounts.
5. Check NULLs in every date and status field: `SELECT COUNT(*) - COUNT(ended_at) FROM subscriptions;` counts open subscriptions. NULL usually means "not yet" or "unknown", and the two need different handling.
6. Check time: format, time zone and the latest loaded timestamp. A load log or `MAX(occurred_at)` tells you whether the last period is partial.

## 3. Write the logic in layers

Build the query as named steps (common table expressions, the `WITH` blocks) so each can be checked on its own.

1. **Population:** the rows that belong in the denominator, with exclusions applied once.
2. **Facts per unit:** aggregate the many side to one row per unit before joining it back. In the case, events become one row per account with `made_project` and `invited` flags.
3. **Join to the population with the right join type.** `LEFT JOIN` keeps population members with no activity. `INNER JOIN` silently drops them and shrinks the denominator.
4. **Aggregate to the result grain** and compute rates from counts in the same row, multiplying by `1.0` so integer division does not truncate.

## 4. Review defects that recur

Check each item explicitly. These are the ones the worked case's AI drafts actually made.

| Defect | How it appears | How to catch it |
|---|---|---|
| Join fan-out | Joining invoices to users repeats each invoice once per user | Compare `COUNT(*)` with `COUNT(DISTINCT invoice_id)` over the same FROM and WHERE. Reconcile the total to a query without the join |
| Shrunken denominator | Inner join to events drops accounts that never acted | Denominator must equal the population count computed separately |
| NULL comparisons | `ended_at > '2026-09-30'` is not true for NULL, so open subscriptions vanish | Count NULLs first. Write `(ended_at IS NULL OR ended_at > d)` |
| `NOT IN` with a NULL | `x NOT IN (1, NULL)` returns no rows ([PostgreSQL docs](https://www.postgresql.org/docs/current/functions-subquery.html)) | Prefer `NOT EXISTS` |
| `COUNT(column)` | Ignores NULLs, unlike `COUNT(*)` (see the aggregate functions page in the PostgreSQL docs) | Decide which you mean and say so |
| Integer division | `3 / 4` is `0` in SQLite and Postgres ([SQLite](https://www.sqlite.org/lang_expr.html), and PostgreSQL's page on mathematical functions and operators) | Multiply by `1.0`. Check that rate equals numerator divided by denominator |
| OR for AND | "Created a project and invited" written as `event_type IN (...)` | Re-read the definition against the predicate word by word |
| Status filters | Void and refunded invoices counted as revenue | Profile status values and filter explicitly |
| Test or internal rows | QA accounts with large invoices | Profile exclusion flags, apply them in the population step |
| Mixed timestamp formats | Stored `2026-01-05T10:00:00` compared as text with `2026-01-05 10:00:00` | Normalize both sides with the date function before comparing |
| Immature cohorts | A September cohort's 90-day retention reported in October | Show a cohort only after its last member's window closes |
| Status today used as status then | "Still subscribed now" used as "retained at day 90" | Evaluate state at the cohort's check date |
| Partial periods | October through the 20th plotted next to full months | Label or exclude the period after the last load |
| `BETWEEN` on timestamps | `BETWEEN '2026-07-01' AND '2026-09-30'` drops times on September 30 | Use half-open ranges: `>= start AND < next_start` |

## 5. Validate the result

A plausible number is not evidence. Use at least two of these, and all of them for a number that will drive a material decision.

1. **Reconcile to a trusted total.** Segment revenue must sum to the monthly revenue total for the same period and definition.
2. **Recompute by a second route.** The worked case recomputes every metric in plain Python from raw rows. In practice, a spreadsheet pivot on an export, a different table, or a finance report can serve.
3. **Check row counts after every join.** Any increase you cannot explain is a fan-out.
4. **Spot-check units.** Pick three accounts and trace them from raw rows to the result by hand.
Plant a qualifying event before signup and another exactly at the end of the window. Neither may enter the activation numerator. Keep the account in its eligible denominator.

5. **Test sensitivity.** Change one boundary (13 versus 14 days, include or exclude a segment) and see whether the conclusion holds.
6. **Compare with what people believe.** A large gap from the number leaders already use is either a finding or a bug. Find out which before presenting it.

## 6. Write it up so another person can check it

Ship the query with its question, definition, population, exclusions, grain, data freshness and the checks you ran. Keep the query in version control or a shared, named location, not in a chat history. A colleague should be able to rerun it next month and get a comparable number.

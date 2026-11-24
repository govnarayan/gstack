# AI-assisted SQL and code

A query can run successfully and select nobody. At Uber, a plausible status value differed from the value in the data. Inspect distinct values before accepting an empty result. [Uber Engineering](https://www.uber.com/us/en/blog/query-gpt/)

OpenAI compared executed answers with independently written queries. Give the reviewer a known result and vary a date, segment or experiment filter. Keep the original and corrected outputs. [OpenAI](https://openai.com/index/inside-our-in-house-data-agent/)

Anthropic found an additional review pass improved accuracy on its evaluation at the cost of more tokens and latency. Test it on decisions where an error changes action. [Anthropic](https://claude.com/resources/articles/how-anthropic-enables-self-service-data-analytics-with-claude)

For recurring reports, rerun the same questions after schema or business changes. Mark which failures are stale definitions, wrong tables, invalid filters or aggregation errors. Each needs a different fix.

AI assistants write runnable SQL and analysis code from a plain request. That changes which skill matters. Typing syntax from memory matters less. Stating the question, knowing the data's grain and reading a query critically matter more. Many strategy and operations job descriptions now ask for exactly this: enough SQL or Python to answer your own questions and to check analytical output or AI-generated code.

## How good is AI at this?

Public benchmarks give a rough calibration, with an important caveat: they test clean, well-documented schemas.

1. On the [BIRD benchmark](https://bird-bench.github.io/), the best published systems reached about 83 percent execution accuracy on the test set by October 2026. The human baseline was 92.96 percent.
   Roughly one answer in six was still wrong on curated databases.
2. The [Spider 2.0 paper](https://arxiv.org/abs/2411.07763) (2024, revised 2025) used enterprise-style warehouses and workflows.
   The best model at publication solved 21.3 percent of tasks, against 91.2 percent on the older Spider 1.0. Agent systems on its [leaderboard](https://spider2-sql.github.io/) have since scored far higher on some variants. Leaderboard entries use different systems and dates, so they do not compare directly with the paper.

The practical reading: AI drafts are a fast start, and a material share of them will be wrong in ways that still run. Most errors in company work come from context the model was never given: which table is trusted, what "active" means here, which accounts are internal. The [worked case](worked-analytics-case.md) shows five such errors in queries that all ran without complaint.

## What companies running this in production report

Company write-ups tell a consistent story. Accuracy depends far more on the business context the model gets than on the model.

| Source | Finding |
|---|---|
| [Anthropic, 2026](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) | Accuracy on internal analytics questions was at most 21 percent without curated context and skills, and consistently above 95 percent with them. Without maintenance it drifted from about 95 to about 65 percent in a month. Model-written metric definitions were net-negative, so a person owns each definition, and anything going to leadership gets human sign-off |
| [dbt Labs, 2026](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026) | On its own benchmark, querying through a governed semantic layer scored 98 to 100 percent against 84 to 90 percent for raw text-to-SQL. Raw SQL fails as a plausible wrong number, while the semantic layer fails as an error message. Vendor-run, 11 questions |
| [Independent study, 2026](https://arxiv.org/abs/2604.25149) | A 4 KB hand-written description of the data lifted accuracy by 17 to 23 points, from about 46 to 50 percent to about 68 percent. One dataset |
| [OpenAI, 2026](https://openai.com/index/inside-our-in-house-data-agent/) | Many-to-many joins, filter errors and unhandled NULLs can silently invalidate results. Users can query only tables they already have permission for. Evaluations compare result data, not only SQL text |
| [Pinterest, 2024](https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff) | First-attempt acceptance rose from 20 to over 40 percent. Finding the right table depended heavily on table documentation |
| [Snowflake docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst-evaluations) | Repeated runs of the same question can produce different SQL and scores, so evaluate several times |

Three practices follow for an operator.

1. **Use governed definitions first.** Check whether a semantic layer, certified table or metrics catalog already answers the question before asking for raw SQL.
2. **Keep a short context document.** One page on your company's key tables, grain, exclusions and definitions, pasted into every request, is the cheapest accuracy gain available.
3. **Keep golden questions.** Five to ten questions whose correct answers you have verified. Rerun them when the data, tool or model changes, and compare the result numbers, not just the SQL. This catches drift before leadership does.

## Give the assistant what it cannot guess

A one-line request produces a one-line understanding. Include:

1. **The question and the decision** it serves.
2. **Schema**: table names, columns, types and keys. Paste `information_schema` output or the table definitions, never sample customer rows unless the tool is approved for that data.
3. **The grain of each table** and the relationships ("one account has many users and many invoices. A plan change closes one subscription row and opens another").
4. **The metric definition**, word for word, including the time window.
5. **Population and exclusions**: test accounts, internal users, void statuses, regions.
6. **Dialect and conventions**: Snowflake, BigQuery, Postgres or SQLite, plus time zone and date format.
7. **What you want back**: the query in named steps, a sentence explaining each step, the checks it recommends and the expected grain of the result.

Then ask for the checks too: "Also write a query that confirms the join does not multiply invoice rows, and one that counts the denominator separately."

## Review the draft in this order

1. **Does it answer the question asked?** Restate the result in words: "one row per signup month. Accounts is every non-test account created that month. Activated is ..."
   If you cannot, ask the assistant to explain, then compare its explanation with your definition.
2. **Population and denominator.** Where are exclusions applied? Can an inner join drop members?
3. **Every join.** What is the grain on each side? Can it multiply rows? Run the row-count check.
4. **Filters.** NULL handling, status values, date boundaries, AND versus OR.
5. **Every calculation.** Integer division, rounding, units (cents versus dollars), rates computed from the same row's counts.
6. **Time.** Time zones, mixed formats, partial periods, cohort maturity.
7. **Validation.** Reconcile and recompute as in [query workflow and review](query-workflow-and-review.md#5-validate-the-result).

When the assistant corrects a defect, rerun every check. A fix to one clause can break another.

## What you must understand to review and explain the work

You do not need to write complex SQL from memory. You do need to read it and explain it to an executive or a data lead. The minimum:

| Concept | You can explain | Practice with |
|---|---|---|
| Table grain and keys | What one row is, and how to test it with `COUNT(*)` versus `COUNT(DISTINCT key)` | Profiling queries in the worked case |
| `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` | Which rows are kept, how they are grouped, and what the result's grain is | `monthly_revenue.sql` |
| Joins: inner, left, and fan-out | Why an inner join can shrink a denominator and a one-to-many join can multiply a sum | `revenue_by_segment_q3.sql`, both versions |
| NULL | Why `x > d` drops NULL rows, why `NOT IN` with NULL returns nothing, `COUNT(*)` versus `COUNT(col)` | `active_at_quarter_end.sql`, both versions |
| Aggregates and rates | Sum, count, distinct count, average of ratios versus ratio of sums, integer division | `activation_by_cohort.sql` |
| `WITH` steps (CTEs) | How to check each step on its own | `activation_by_cohort.sql` |
| Dates and windows | Half-open ranges, time zones, partial periods, cohort maturity | `retention_90d_by_cohort.sql` |
| Window functions | Running totals, previous-period comparisons and first or last rows per group (`ROW_NUMBER()`, `LAG()`) | Ask the assistant for a month-over-month change, then check it by hand |
| Reconciliation | Why two routes to the same number must agree, and what a gap means | `analytics_demo.py` checks |
| Python or a notebook | Loading a query result, a pivot, a chart, and a recomputation that does not reuse the SQL logic | `analytics_demo.py` oracle function |

## A short learning route

About ten to fifteen focused hours, using the worked case rather than generic exercises.

1. **Read and run (hours 1–3).** Run the demo. Open each reviewed query and write one sentence per clause on what it does.
   Run the profiling queries from step 2 of the workflow against `demo.sqlite` (any SQLite browser or `python -c` works).
2. **Break things on purpose (hours 4–6).** Change one reviewed query at a time to reintroduce a defect.
   Examples are inner instead of left join, dropping the NULL condition and dividing integers. Predict which check will fail, then run it. Tests in `tests/test_analytics_demo.py` show the pattern.
3. **Ask an assistant for new questions (hours 7–9).** For example: Q3 revenue by region, net revenue retention by segment, users per account distribution.
   Give it the schema and definitions. Review the draft with the checklist above. Add a check for each.
4. **Window functions and a notebook (hours 10–12).** Ask for month-over-month revenue change and first-invoice date per account. Recompute one result in Python or a spreadsheet.
5. **Your own company's data, read-only (hours 13–15).** One real question, with the data team's trusted tables and definitions, reviewed by someone who knows the data. That review is the evidence of competence, not the query count.

Interviewers asking whether you can self-serve usually probe whether you can get a correct number without an analyst, and whether you know when not to trust one. Be specific about what you can do: state the question precisely, direct an AI assistant, review joins, NULLs and denominators, and reconcile results. Do not claim fluent independent SQL authorship if you have not built it.

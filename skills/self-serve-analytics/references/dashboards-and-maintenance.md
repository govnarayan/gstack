# Dashboards and maintenance

A dashboard is useful when a named person makes a recurring decision faster or better because of it. Most dashboards fail by answering no particular question, by drifting from the definitions people use, or by going stale without anyone noticing.

## Before building

1. **Name the decision and the user.** "The VP Sales reviews pipeline coverage every Monday to decide where to move SDR capacity." If no recurring decision exists, write a one-time analysis instead.
2. **Choose three to six measures** that inform that decision: an outcome, its controllable drivers, and a guardrail. Link to the existing [company metrics](../../operating-cadence/references/company-metrics.md) method when choosing them.
3. **Fix the definition, grain, population and refresh need** for each measure. Daily refresh for a weekly decision wastes compute and attention.
4. **Agree the owner** who will answer questions and maintain it.

## Layout that supports the decision

| Element | Why |
|---|---|
| Headline tiles with the period and denominator under each number | A rate without its base hides small samples |
| Trend charts with the partial period visibly marked | The current month is otherwise read as a collapse |
| Cohort charts showing only mature cohorts | Young cohorts look better or worse purely from elapsed time |
| A breakdown that explains movement (segment, region, channel) | The decision usually depends on where the change came from |
| Definitions on the page | People stop arguing about what the number means |
| Freshness: data loaded through, built at, owner, next review | Users can tell whether to trust today's view |
| Check status | A failed reconciliation should be visible, not silent |

The [worked case dashboard](worked-analytics-case.md) includes each element, including a table showing what the unreviewed AI drafts would have reported. Keep charts plain: bars for comparing periods or groups, lines for long trends, tables when exact values matter. Avoid gauges, 3D and dual axes.

Eugene Wei was Amazon's first strategic planning analyst. He produced its monthly Analytics Package ([Wei, 2017](https://www.eugenewei.com/blog/2017/11/13/remove-the-legend)). It was 30 to 40 pages of charts on every part of the business, growing to about 100. A one-page written summary opened it. The CEO and every senior manager got the same package on the same day, so owners read their own pages closely. He contrasts this with wall screens running charts all day, which people learn to ignore. His chart rules are practical. Label lines directly instead of using a legend. Show data values when the reader wants detail, and drop gridlines once values are shown. Draw the target on the chart as a labeled line. Keep to a rolling four or eight quarters. He also notes that making the charts is how the analyst comes to understand the business.

## Small numbers and fair comparisons

Show counts beside rates. A cohort of 12 accounts moving from 50 to 58 percent is one account. Compare like with like: same day-of-month cut-off, same maturity window, same definition. When comparing periods, say whether a change exceeds normal month-to-month variation. If you cannot say, say that instead of implying a trend.

## Maintenance

| Cadence | Task |
|---|---|
| Every refresh | Freshness and reconciliation checks run automatically. A failure shows on the dashboard and alerts the owner |
| Monthly | Owner spot-checks one number against a second route and reviews whether the decision still uses it |
| When a source changes | New status values, new plan types, a migrated table or a changed definition trigger a re-review before the next use |
| Quarterly | Retire dashboards with no views or no decision and consolidate duplicates |

A dashboard with no owner should be archived. A number that has been wrong once, silently, loses trust for months.

## Failure signals

1. Two dashboards show different values for the same metric name.
2. Leaders export to spreadsheets to "fix" the numbers.
3. The dashboard's definition text no longer matches its query.
4. Nobody can say when it last refreshed.
5. Reviews spend time on what a number means rather than what to do.

Each signal points to a definition, ownership or maintenance gap rather than a charting problem.

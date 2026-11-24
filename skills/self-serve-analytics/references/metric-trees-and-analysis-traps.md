# Metric trees and analysis traps

[Query workflow and review](query-workflow-and-review.md) covers mechanical correctness: grain, joins, NULLs and dates. This reference covers the next layer. These are numbers computed correctly that still mislead. The small examples are invented and checked by hand.

## Build a metric tree before a dashboard

A metric tree breaks a top-level goal into the drivers that produce it. Revenue splits into accounts times revenue per account. Accounts split into new, retained and returning. Each split is an edge, and edges come in two kinds ([Count, 2024](https://count.co/blog/intro-to-metric-trees)).

| Edge type | Example | What it means |
|---|---|---|
| Formula | Signups = visitors × conversion rate | Arithmetic. If the inputs are right, the output is right |
| Influence | Lead score affects lead acceptance rate | A belief about cause. It needs evidence, and it can be wrong |

Label every edge. Most dashboard arguments come from treating an influence edge as if it were a formula. Start with one goal and two or three drivers. Agree the definitions with the owners, and use the tree in the operating review ([Mixpanel, 2025](https://mixpanel.com/blog/metric-trees-benefits-guide/)). A tree that nobody reviews goes stale.

Tie pay or targets to a node and the node starts to bend. In [a 1979 paper](https://jmde.journals.publicknowledgeproject.org/index.php/jmde_1/article/download/297/292), Donald Campbell put it as a law. The more an indicator drives decisions, the more it invites corruption and distorts the work it monitors. His example was police clearance rates, where pressure led to complaints going unrecorded. Muller's *The Tyranny of Metrics* (2018) sorts the damage into distorted information, gaming and cheating. He argues for metrics that inform judgment rather than replace it. Pair each targeted node with a check it cannot game, such as a quality or downstream measure.

Lenny Rachitsky surveyed growth-stage companies. He argues the North Star metric is strategy expressed as a number ([Lenny's Newsletter, 2021](https://www.lennysnewsletter.com/p/choosing-your-north-star-metric)). The tree is how that number connects to the work teams can change. The library's [company metrics](../../operating-cadence/references/company-metrics.md) method chooses measures by business mechanism and pairs with this.

## Metrics as a model of how the business works

Cedric Chin's [Commoncog series](https://commoncog.com/becoming-data-driven-first-principles/) derives a metrics practice from statistical process control, the method Deming and Wheeler taught. Most numbers wiggle. A process behavior chart, usually an XmR chart, draws limits from the data's own past variation. Movement inside the limits is routine noise, and a point outside them means something changed. Without that test, teams chase noise or stop trusting data altogether. With it, a team learns which actions move a number. Those actions become controllable input metrics, and the business becomes a causal model people share.

His [account of Amazon's Weekly Business Review](https://commoncog.com/the-amazon-weekly-business-review/), learned from former Amazon executive Colin Bryar, shows the practice at scale. Leaders review 400 to 500 metrics in 60 minutes each week. Each chart shows this year, last year and the target. Discussion is about controllable inputs, while outputs such as revenue are only reported. Owners check their numbers daily and must explain exceptional variation. Commoncog's own review covers 47 metrics in under 15 minutes, which suggests the form scales down. A metric tree's formula edges and influence edges map onto this split: inputs are the levers, outputs the results.

Keith Rabois adds a guard against single-number targets. In his ["How to Operate" talk](https://manassaloi.com/2020/02/17/rabois-os.html) (read via a reader's summary), he tells operators to pair opposing measures. An insurer that targets only fraud will treat every customer as a suspect, so measure service too. This is the same check against Campbell's law described above.

## Why self-serve efforts fail

Practitioners agree the bottleneck is rarely the tool. Benn Stancil, co-founder of Mode, [argues](https://www.kdnuggets.com/2021/11/missing-self-serve-bi.html) that business users do not want to analyze like analysts. They want to pick a known metric, filter it and break it down by a dimension. Build self-serve around that, and hire analysts for the rest. Crystal Widjaja built Gojek's analytics team. In [a Reforge essay](https://www.reforge.com/blog/why-most-analytics-efforts-fail) she traces "our data is a mess" to five root causes. Teams track metrics instead of analyzing them, think like developers instead of business users, and pick the wrong level of abstraction. They also write instead of showing, and treat data as a project rather than an ongoing job. Her fix starts from business and team goals, then tracks user journeys rather than just the metrics a goal needs.

Emily Thompson's lessons, [summarized by dbt Labs](https://roundup.getdbt.com/p/5-principles-of-self-service), give a test for whether a metric set works. Ask whether anyone can name the top three to five measures and say how each is defined. Then ask whether people know what drives them and believe they can move them. A "no" to any of these is a design problem, not a training problem.

## Mix effects and Simpson's paradox

An overall rate can fall while every segment improves, because the mix changed.

| Segment | Period A accounts | A activated | A rate | Period B accounts | B activated | B rate |
|---|---:|---:|---:|---:|---:|---:|
| SMB | 80 | 16 | 20% | 200 | 42 | 21% |
| Enterprise | 20 | 12 | 60% | 20 | 13 | 65% |
| Total | 100 | 28 | 28% | 220 | 55 | 25% |

Both segments improved, yet the total fell from 28 to 25 percent, because SMB grew from 80 to 91 percent of accounts. Reporting "activation fell three points" would be wrong about the product and right only about the mix. Always break a moving rate into segment rates and segment mix before explaining it. Kohavi's team showed the same reversal in online experiments whose traffic split changed during a ramp-up ([Kohavi et al., 2009](https://exp-platform.com/seven-pitfalls/)).

## Ratio of averages versus average of ratios

In period B above, the average of the two segment rates is 43 percent, while the pooled rate is 25 percent. Both are arithmetic, but they answer different questions. Pooling weights by volume and answers "what share of accounts activated". The simple average weights each segment equally and answers "how does a typical segment do". State which one a number is. When in doubt, pool the numerator and denominator.

## History-correct segments

Accounts change segment, owner, plan and region. If a query joins invoices to the account's current segment, every past invoice moves with it. An account that grew from SMB to Mid-Market in July makes Mid-Market look larger in January than it was. Warehouses handle this with history tables, called type-2 slowly changing dimensions. Each row carries a valid-from and valid-to date ([dbt snapshots](https://docs.getdbt.com/docs/build/snapshots)). Join each event to the row valid at the time:

```sql
JOIN account_segment_history AS h
  ON h.account_id = i.account_id
 AND i.invoice_date >= h.valid_from
 AND (h.valid_to IS NULL OR i.invoice_date < h.valid_to)
```

Ask the data team whether a history table exists. dbt snapshots record changes only from the first run onward and cannot be rebuilt, so history before that point may be gone. Then say so on the dashboard.

## Time zones: convert, then truncate

An event at 03:00 UTC on March 1 happened at 19:00 on February 28 in California. Truncating to the day in UTC first and converting afterward puts it in the wrong day and sometimes the wrong month. Convert to the business's reporting time zone first, then truncate to day or month. Check one example near a month boundary by hand.

## Experiments: check the split before the result

If a test was designed as 50/50 and the arms hold 4,000 and 3,700 accounts, the split itself is a finding. A chi-square test on that split gives a statistic of about 11.7 and a p-value near 0.0006, far too unlikely to be chance. This is a sample ratio mismatch. It is a symptom of a broken assignment, a bot filter, a logging delay or a bad join. Do not trust the outcome comparison until the cause is found ([Vermeer, SRM causes](https://www.lukasvermeer.nl/srm/docs/causes/)).

Two more rules. Decide the sample size and duration in advance. Checking significance repeatedly and stopping when it looks good inflates false positives. Ten looks turn a nominal 1 percent error rate into about 5 percent ([Evan Miller, 2010](https://www.evanmiller.org/how-not-to-run-an-ab-test.html)). Sequential testing designs allow early stopping legitimately. And watch guardrail metrics, such as refunds or support contacts, alongside the target metric.

The synthetic company-operations case in this library already applies these ideas. Its randomization fixes assignment before exposure, its denominator includes every assigned account, and it compares treatment with holdout rather than with history.

## Regression to the mean and immature cohorts

Pick the worst-performing teams or regions and re-measure them next month, and they will usually look better with no intervention, because extreme results partly reflect noise. Before crediting a fix, compare with similar units that received no fix. Recent cohorts have the same trap from the other side. Missing outcomes are not zero, and a young cohort's curve can look better or worse purely because its later months have not happened. Compare cohorts only at ages every one of them has reached. The worked case's retention query enforces this.

## A short checklist before presenting a change

1. Is the change real, or within normal month-to-month movement?
2. Did the mix shift? Show segment rates and segment shares.
3. Are segments assigned as of the event date, or as of today?
4. Are the periods complete and the cohorts mature?
5. Is the time zone the business's reporting zone?
6. For an experiment, does the observed split match the design?
7. Which edges in the metric tree are formulas, and which are beliefs?

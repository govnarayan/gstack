# Performance information

Use this method for company and business-unit decisions. Read [company metrics](company-metrics.md) to construct the business driver relationships across subscriptions, consumer, hardware, marketplaces, developer platforms, AI and hybrids. Read [cohort deep dives](cohort-deep-dives.md) when a movement requires matched populations, tenure, payment, contribution or mix analysis. These are company-performance methods, not a request to create functional scorecards.

## Start from the decision

Identify the audience, decision, time horizon, unit being measured, and action the owner can take. A metric is useful when it answers that question reliably. A single customer-value measure can align a team, but it cannot represent every product, business unit, operating obligation, and risk. Revenue, usage, and customer value are related hypotheses, not interchangeable facts.

Choose outcome measures, controllable drivers, and guardrails for material harms. Label a proposed driver as a hypothesis until its relationship to the outcome is supported. Activity can provide early evidence without being a valid proxy for value. More activity is not necessarily better.

## Metric definition and reproducibility

For each decision-relevant measure record:

| Field | Meaning |
|---|---|
| Plain definition and purpose | What the number represents and the decision it informs |
| Formula and unit | Calculation, units, numerator, denominator, aggregation, and treatment of zero or missing inputs |
| Population and period | Customer/account/unit identity and mapping, stock/flow/exposure, cohort eligibility, event, interval boundaries, time zone, maturity, pending observations and exclusions |
| Source and version | System, query or transformation, refresh time, known gaps, and definition change date |
| Accountability | Data owner, business owner, reviewer, and recipient of exceptions |
| Decision rule | Target or band, investigation trigger, expected action, and known gaming or blind spots |

Add revenue/cost/cash basis, gross/net treatment, discount/refund policy, consolidation and currency convention when the measure has an economic meaning. A metric contract includes a few raw-record examples and a reproducible query or calculation. It is incomplete if the chart title supplies the only definition.

Distinguish missing from zero and provisional from final. Show late-arriving data and restatements. Preserve definition history and disclose a break in comparability. Different purposes can legitimately require different definitions, so reconcile or label the difference rather than forcing one number everywhere.

If dashboards disagree, inspect definitions, populations, joins, periods, freshness, deduplication, currency, and treatment of events before changing charts. Reconcile to known records or a trusted functional source. For a sample of records, trace inclusion from raw event to reported total. Check that joins do not multiply rows and that repeated events do not become new customers.

Distinguish the event time, ingestion time, reliable coverage watermark and query execution time. A refreshed dashboard can still omit late events. Set a close/restatement rule with the data owner. Preserve a bridge from the old number to the corrected number so measurement changes are not credited as business improvement.

A shared table can support several packs with audience-appropriate subsets and access controls. Do not assume every executive, board, and external metric is a strict subset of a weekly pack. An internally useful number is not automatically approved for disclosure.

## Diagnose movement

Show current versus plan and comparable history, then identify the material contributors. Separate price, volume, mix, timing, and definition effects where useful. Inspect segments and distributions rather than assuming the aggregate applies to every case. State which changes are observed, which explanations are inferred, and what would falsify the preferred explanation.

For cohorts, define the anchor event and retained or successful behavior, compare equal ages, and mark incomplete observation periods. A newer cohort with a shorter observation window is not evidence of worse long-term retention. Separate changing acquisition mix from changes within segments. A coincident release or feature use does not alone establish causation.

Apply maturity before counting numerator and denominator. Do not include early successes from pending members against only a mature denominator. Keep mature failures, canceled customers and returned units when they are outcomes of the question. Use the full [cohort specification](cohort-deep-dives.md) for identities, origins, renewal opportunities, state transitions, censoring, revenue and fixed-mix comparisons.

For funnels, define eligible entry, unit, stage order, conversion window, and exclusions. Counts from unrelated populations are not a coherent funnel. Compare both absolute losses and rates, then assess value and feasible interventions. The biggest percentage drop is not automatically the best investment.

For commercial attribution, treat allocation of credit as a reporting convention rather than proof a channel caused a sale. Keep lookback windows, identity gaps, sales-cycle length, and full costs visible. Changing the model can alter credited returns without changing actual business performance.

## Forecasts and capacity

Separate historical actuals, approved targets, and forecasts. A forecast states expected outcomes under assumptions. A target states desired performance. Do not inflate drivers so the two coincide.

Identify a small number of meaningful drivers, their evidence, timing, dependencies, and ranges. For hiring-dependent growth, account for recruiting delay, productive ramp, sales-cycle lag, delivery capacity, and service capacity. Reconcile the forecast with the resources that can deliver it, using the relevant business model rather than assuming subscription sales.

Use scenarios around real uncertainty and correlated constraints. A hiring delay can change revenue, spend, service coverage, and delivery dates together. Compare past forecasts with actuals using the same horizon and definitions, diagnose systematic error, and revise assumptions with a dated rationale. Do not claim confidence from a model's precision alone.

Evaluate forecast error at the horizon the decision used: a one-week-ahead forecast is not comparable with a quarter-ahead forecast. State the sign convention, for example `forecast - actual`, and show signed error and absolute error by material driver. Percentage error is undefined when actual is zero, and a weighted total can hide large offsetting product errors. Inspect bias, interval coverage where ranges are supplied, and the cost of misses. Do not import a universal accuracy target.

For subscription metrics, use the staffed Finance or commercial owner's definitions and reconcile changes explicitly. Distinguish bookings, recurring revenue measures, recognized revenue, and cash. Unverified formulas and benchmark ranges are not validated accounting or financial guidance.

## Experiment evidence

For an experiment, record hypothesis, intervention, population, randomization unit, primary metric, guardrails, and minimum worthwhile effect. Establish sample, duration, analysis, and stopping plans before interpreting results. Inspect implementation, sample allocation, missing data, and changes during the test.

Report effect size, uncertainty, guardrail outcomes, and the business cost of the decision. Report what the selected statistical method establishes and what it does not. Do not translate a test threshold into a probability that the business conclusion is true, or treat an inconclusive test as proof of no effect. Do not extend a test opportunistically because a favorable trend narrowly missed a threshold. Use the prespecified method or label a new test and its changed assumptions.

At low volume, a suitably powered experiment may take longer than the decision can wait. Calculate the required sample for the actual baseline, effect, design, and method rather than importing a traffic table. Alternatives include qualitative investigation, a bounded pilot with explicit limits, or a reversible decision with monitoring. The threshold where the method changes is whether the required valid observations can arrive within the useful decision window, not a fixed company size.

Complete reproducible company metric calculations within the assigned brief. Use [financial resource decisions](../../financial-resource-decisions/SKILL.md) when the question becomes affordability, lifetime economics, cash forecasting or an allocation model. Coordinate specialist methods for experiments, survival estimates, complex forecasting and causal claims when their evidence requirements exceed the brief. Technical implementation and legal interpretations of analytics collection remain with the assigned owners.

## Artifact and quality check

Provide a reproducible metric record, comparable trend or cohort view, variance explanation with alternative hypotheses, forecast assumptions and uncertainty when relevant, and decision implications. An alert needs an owner, response path, and context. Frequent ignored alerts call for examining the signal and response capacity, not automatically raising the threshold and hiding the problem.

For a company review, include the driver tree and consolidation bridge as well as the metric table. Reconcile opening populations to closing populations, component revenue to the company total, contribution to its included costs, and any cash statement to actual receipts/payments. Counts of seats, devices, people, orders and API calls cannot be consolidated into one customer count. See the [worked company review](../examples/company-metrics-review.md) for a synthetic execution and explicitly rejected conclusions.

Before presenting a pack, check source timestamps, denominators, comparable windows, missing data, joins, and definition changes. Test a representative calculation against underlying records. Retain evidence links and give a plain account of what the numbers cannot establish.


## Worked calculation and interpretation tests

These numbers are synthetic. Recalculate with the organization's definitions and underlying records.

### Pool counts, then inspect mix

Suppose activation in an earlier period is 80/100 for self-service accounts and 20/100 for assisted accounts. Total activation is 100/200 = 50%. In a later period, self-service is 36/40 = 90% and assisted is 96/160 = 60%. Both segments improve, and the pooled rate is 132/200 = 66%. The unweighted mean of the two later rates is 75%, which is incorrect for the overall population because group sizes differ.

Now change only the later composition: self-service is 9/10 = 90%, assisted is 114/190 = 60%. Total is 123/200 = 61.5%. The two segment rates are unchanged from the preceding later-period example, yet the aggregate changes from 66% to 61.5% because the mix changes. Separate within-segment movement from composition before judging the intervention. Neither comparison by itself proves causality.

### Reject a mismatched observation window

A 14-day activation cohort has 200 eligible accounts. At the reporting cutoff, only 120 have had 14 days to activate, and 60 of those activated. Report 60/120 = 50% among mature accounts, with 80 pending. Do not use 60/200 = 30% as the completed 14-day activation rate. Also state that the mature subset may have a different mix, so its 50% is provisional evidence about the final cohort.

If the final deadline occurs before all cohort members mature, either stop cohort entry earlier, move the evaluation date explicitly, or use an appropriately labeled interim measure. Do not count pending observations as failures to obtain a convenient quarter-end number.

### Build a variance bridge that adds up

A simple service plan assumes 100 jobs at $200 each: $20,000. Actual is 90 jobs at $220: $19,800. Total variance is -$200.

Using plan price for the volume term and actual volume for the price term:

~~~text
Volume effect = (90 - 100) × $200 = -$2,000
Price effect = 90 × ($220 - $200) = +$1,800
Total = -$200
~~~

This is one explicit decomposition convention. It is an arithmetic bridge, not proof that price caused the volume change. For multiple products or customer types, account for mix and timing under an agreed method. Do not assert a causal explanation because the bridge balances.

### Treat a forecast as a driver model

For the same service, 120 expected requests × 75% completion = 90 completed jobs. At $220 realized price, forecast is $19,800. The target can still be $22,000. Closing the $2,200 gap requires a justified change: 10 additional completed jobs at that price, higher realized price, or a different mix. It cannot be closed by rewriting the forecast without evidence.

If available delivery capacity is 85 jobs, the forecast of 90 completed jobs is infeasible unless capacity, timing, or scope changes. A model that multiplies demand correctly can still fail the operating constraint.

### Test a warning against time to act

If validated data arrives 1 day late, the review can add up to 7 days of waiting, and corrective action needs 2 days, worst-case response is 10 days. If the harm becomes material in 5 days, add a faster exception route. More charts in the weekly pack cannot close that timing gap.

## Minimum evidence tests before distributing a performance pack

1. Trace one count and one rate from source records to the pack, including eligibility, duplicates, joins, and pending observations. Expand the check if it reveals a systematic problem.
2. Reconcile headline totals and variance components. Preserve negative movement and restatements instead of clipping them out of the display.
3. Compare actual, target and forecast under the same definitions and horizon. Label any deliberate difference and its reason.
4. Inspect the important segments, tails and service guardrails. A good average can coexist with harm to a small but important population.
5. Check that each material exception has an owner, useful response time, actual authority and a completion/effect check. A technically correct number without an actionable route is an incomplete operating mechanism.

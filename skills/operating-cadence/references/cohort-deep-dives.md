# Cohort and company deep dives

A cohort fixes a population at a meaningful origin and follows it through comparable elapsed time. It can show where a company result comes from without showing what caused it. Start with the decision and the rival explanations, then choose the cohort contract. More segmentation is useful only when it can separate explanations or change an action.

## 1. Write the investigation brief

State the observed company movement with actual, plan, prior period, population, source and cutoff. Estimate its company consequence before expanding the analysis. Name the leading explanation, strongest alternative, the evidence that distinguishes them, the owner and the decision deadline. State what a sufficiently strong result would change.

Example: recognized subscription revenue is growing while 90-day repeat value appears lower. Alternatives are a genuine decline within comparable customers, more low-repeat acquisition, younger observations, identity changes, or a paid-price/mix change. A revenue chart and a retention chart alone cannot settle the choice. The investigation needs matched tenure, identity, segment composition, payment and delivery economics.

## 2. Lock the cohort specification

Complete this table before producing the curve. Mark missing inputs; do not let a chart's defaults silently supply them.

| Contract field | Required decision and reproducible record |
|---|---|
| Question and scope | Company/unit, products/entities, decision, alternatives and relevant economic/customer consequence |
| Identity | Person/account/household/device/installation/transaction/developer organization; stable key; identity merge/split policy; mapping to payer and beneficiary |
| Grain | One record per cohort member, per member-period, per task or per installation; permitted many-to-one relationships |
| Origin | First signup, first accepted value, first paid service, first completed transaction, shipment, acceptance/installation or renewal opportunity, with exact event definition |
| Entry rule | Earliest-ever qualifying event versus earliest observable event; entry dates; lookback needed to establish newness; whether one identity can enter more than once |
| Eligibility | Pre-origin conditions, available market/product, test/internal exclusions, refunds/fraud handling, source coverage and left-truncation limits |
| Cohort assignment | Origin period/time zone and fixed pre-origin segmentation. Record later segment transitions separately |
| Outcome | Exact successful/retained behavior or state, accepted quality and deduplication; what does not qualify |
| Clock | Calendar days/weeks/months versus elapsed hours or anniversary periods; Day 0; interval boundaries and inclusive/exclusive endpoints |
| Horizon | Period-specific, any within a fixed window, or on/after a tenure point with a fixed observation ceiling; repeat opportunities when applicable |
| Maturity | Required full window, data cutoff, ingestion watermark and expected reporting lag; mature/pending counts by cell |
| Denominator | Original eligible cohort or explicitly qualified at-risk population; where exits, refunds and unknown outcomes remain; zero-denominator handling |
| Missingness/censoring | Who has not yet had the chance to be observed, lost telemetry, deletion policy, unavailable markets, and how each affects numerator/denominator |
| Revenue and cost | Recognition, billing, recurring snapshot or cash basis; currency; discounts/refunds; cohort acquisition cost; delivery cost; fixed/shared allocations |
| Transitions | New, continuing, lapsed/churned, paused, reactivated, migrated, retired, and mutually exclusive rules at each boundary |
| Comparison | Same-tenure cohorts, comparable calendar periods, segment/mix weights, seasonality, exposure and release changes |
| Provenance | Source tables/events, join keys, query version, definition version, refresh time, observed gaps and metric/business owners |
| Decision rule | Material effect or operational obligation, uncertainty requirement, action, decider, deadline and evidence that would reverse it |

An account cohort and a person cohort answer different questions. Mapping many users to an account can create activity without new paying accounts. A device replacement should not create a first-time customer. Anonymous-to-known identity merges need a versioned rule; otherwise apparent acquisition and retention can change when identity resolution changes. Retain a reconciliation from raw IDs to the chosen entity count.

If complete prior history is unavailable, label entrants as first observed since the coverage date, not necessarily newly acquired. Returning customers can otherwise be mistaken for high-retention new customers. If reactivation is the decision, use a reactivation cohort linked to the original identity; do not reset lifetime tenure in the original acquisition cohort.

## 3. Choose the right retained behavior and window

| Measure | Explicit meaning | Misinterpretation to reject |
|---|---|---|
| Fixed-window activation | At least one accepted value event within H time units after origin, among entrants with a full H window | Excluding entrants who never activate; counting early successes from immature entrants against only mature denominators |
| Period-specific retention | At least one return event in the exact tenure interval, among entrants with that interval complete | Treating a missing week as permanent churn or expecting this curve always to decline |
| Bounded on/after retention | At least one return event from tenure k through a fixed horizon H, with H fully observed | Comparing old cohorts with more future opportunity against newer ones with less |
| Continuous survival | No defined terminal lapse/churn through tenure k, under an explicit event rule | Calling any later return continuous retention after an earlier terminal event |
| Renewal success | Successful renewal among contracts that actually reached the defined renewal opportunity and full grace window | Using all subscriptions as denominator when many are not due |
| Revenue retention | Same-cohort revenue in matched snapshot or period windows relative to the locked baseline | Mixing annualized recurring charges with recognized revenue or adding new customers |

The retained behavior should follow the value cycle. A person can receive continuing subscription access without using the product in a particular week. A hardware user can be active while their household payer pauses service. Payment retention, use retention and customer outcome remain separate measures.

[Amplitude's retention documentation](https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation) distinguishes return in the exact interval from return on that interval or later, and explains its exclusion of incomplete intervals. Those defaults are source-specific. This method requires a declared ceiling for on/after comparisons so unequal future exposure does not decide the result. Exact-interval retention can rise across intervals because behavior is intermittent. A complete fixed-population on/after curve with a common ceiling cannot rise as the start of its qualifying window moves later.

Use half-open elapsed windows where practical. For origin `t0`, a 14-day activation window is `[t0, t0 + 14 days)`, and tenure week 2 is `[t0 + 14 days, t0 + 21 days)`. A return exactly on the upper boundary belongs to the next interval. Calendar-week cohorts are a different convention and need day-of-week exposure disclosed. Month 1 cannot silently mean 30 elapsed days in one query and the next calendar month in another.

## 4. Maturity, at-risk populations and censoring

At cutoff C, an entrant's window is mature only when its upper boundary is no later than the data's reliable observation watermark. Use event time plus validated coverage, not the warehouse refresh timestamp alone. A query run today can still lack yesterday's late events. State the backfill policy and publish changed historical results with a dated restatement.

For a simple completed-window rate, apply maturity to the member population before counting successes. Report `successful mature / eligible mature`, plus immature entrants and missing-data counts. Do not add known early successes from immature members to a mature numerator. Do not remove mature failures because they canceled, stopped using, returned a unit or deleted an account when those outcomes are part of the question. A churned customer is an outcome, not automatically censored.

Distinguish:

1. Administrative censoring: observation ends before the horizon. Keep the cell pending or use a separately specified survival analysis.
2. Missing observation: the event feed or identity history is incomplete. Report unknown coverage and sensitivity; absence of an event is not proven absence of behavior.
3. Terminal business event: churn, retirement or another contracted failure. Count according to the outcome rule rather than deleting the member from the cohort.

Dropping people who leave early biases results toward survivors. A survival estimator can use unequal follow-up under specified assumptions, but it is not a license to treat selective telemetry loss as harmless. If an investment decision requires estimated survival, recurring-event or competing-risk models, have the specialist state the estimand, assumptions, uncertainty and tests. Keep the raw exposure and event counts visible.

For device failures, report events per eligible device-time or first-failure survival under the chosen question. Devices with multiple repairs require event rules that distinguish first failure from repeat burden. For renewal cohorts, report eligible contracts, successes, explicit failures, pending grace periods and missing outcomes. For trial conversion, preserve unpaid and failed-payment entrants instead of conditioning on eventual billing success.

## 5. Separate tenure, calendar time and mix

Create a matrix with entry cohorts as rows and equal tenure intervals as columns. Every cell carries numerator, denominator, pending/unknown count, rate, source cutoff and definition version. Do not fill an unobserved triangle with zero. Use a second view of calendar-period performance to expose outages, seasonality or policy changes shared across cohorts.

An acquisition cohort can worsen because its members differ, because their experience differs, or because observation differs. Decompose in this order:

1. Verify identity, source coverage, definitions and equal window maturity.
2. Compare rates within pre-origin segments at the same tenure.
3. Recompute the aggregate under fixed comparison weights.
4. Inspect exposure changes, calendar effects and concentration; then investigate causal explanations.

For exhaustive mutually exclusive segments s, with rates r and cohort weights w, an exact two-period bridge is:

~~~text
Aggregate change = Σ w_old,s × (r_new,s - r_old,s)
                 + Σ (w_new,s - w_old,s) × r_new,s
                   within-segment effect + mix effect
~~~

This ordering allocates the interaction to mix. Other orders are legitimate but produce different component values; state the convention and reconcile the total. Fixed-mix comparison `Σ w_old,s × r_new,s` answers how the new segment rates would look at old mix. It is descriptive, not the observed new aggregate or an experimentally adjusted treatment effect. If a segment has no new observations, its new rate is missing. Do not silently borrow an old rate or reweight it away. State the overlap population or a justified model.

Avoid slicing on post-origin outcomes such as eventual high spend or later feature adoption when estimating whether an intervention helped. Those labels select on later behavior. Keep acquisition source and starting plan fixed at origin, then analyze plan/segment migrations as transitions. Show customer/revenue-weighted results separately when large accounts dominate. Report ranges or distributions where averages hide uneven outcomes.

## 6. Revenue, state transitions and contribution by cohort

Choose one revenue basis per view. An acquisition cohort can show monthly recognized revenue and observed cumulative contribution. An opening-revenue cohort can show snapshot net retention. An annual-prepay cohort can show collections, earned revenue and renewal opportunity. Each needs its own label and reconciliation.

For an opening account i with baseline recurring revenue b_i and closing recurring revenue e_i:

~~~text
Expansion = Σ max(e_i - b_i, 0)
Contraction = Σ (b_i - e_i) where 0 < e_i < b_i
Full loss = Σ b_i where e_i = 0
NRR = Σ e_i / Σ b_i
GRR = Σ min(b_i, e_i) / Σ b_i
~~~

These are proposed snapshot conventions with nonnegative revenue. Refund-driven negative recognized revenue belongs in a different period revenue contract, not a silently clipped version of these formulas. Explain reactivation, mergers, product migrations, currency and pricing separately. A source-defined consumption NRR may use two full periods of recognized revenue instead of these snapshots, as [Snowflake's filing](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm) demonstrates.

Create a state table so every original member has exactly one state at each boundary and transitions reconcile to next-period stocks. For a subscription, a declared example is trial, paid, paused, churned and retired. Define how a grace period is assigned and whether cancellation requested or cancellation effective controls the state. Reactivation is a transition from a prior nonpaying state, not a new customer. Products can be distinct subscriptions under the same household. Do not add trial members and payers into one paid stock.

Report gross exits and reactivations before any net rate. Net churn can hide heavy departure and expensive reacquisition. If contract length changes, a period with fewer renewal opportunities can show lower churn without improved renewal behavior. Segment by plan and tenure, then compare equivalent renewal opportunities.

For observed cohort contribution, show acquired identities, acquisition cash/cost boundary, revenue by tenure, delivery costs including failed work/free usage where relevant, returns/losses, and cumulative contribution before/after acquisition. A cohort with fewer paying customers can contribute more if price/mix or service cost differs, so retention alone cannot rank acquisition sources. Separate observed payback from projected lifetime. Use [financial resource decisions](../../financial-resource-decisions/SKILL.md) for extrapolation or allocation choices.

## 7. Reproducible query shape

The following is illustrative warehouse-neutral SQL. Adapt interval/date syntax. `origins` must contain each identity's true first qualifying origin, derived from sufficient history, and fixed eligible segment. `value_events` contains deduplicated accepted behavior with reliable event times. `reliable_cutoff` is the coverage watermark, not merely the query execution time.

~~~sql
WITH eligible AS (
  SELECT entity_id, origin_at, segment_at_origin
  FROM origins
  WHERE origin_at >= :entry_start AND origin_at < :entry_end
    AND eligible_at_origin = TRUE
), mature AS (
  SELECT * FROM eligible
  WHERE origin_at + INTERVAL '14 days' <= :reliable_cutoff
), member_outcome AS (
  SELECT m.entity_id, m.segment_at_origin,
         CASE WHEN EXISTS (
           SELECT 1 FROM value_events v
           WHERE v.entity_id = m.entity_id
             AND v.event_at >= m.origin_at
             AND v.event_at < m.origin_at + INTERVAL '14 days'
         ) THEN 1 ELSE 0 END AS activated
  FROM mature m
)
SELECT segment_at_origin, COUNT(*) AS eligible_mature,
       SUM(activated) AS successful_mature,
       1.0 * SUM(activated) / NULLIF(COUNT(*), 0) AS activation_rate
FROM member_outcome
GROUP BY segment_at_origin;
~~~

The `EXISTS` prevents repeated events from multiplying the member denominator. Produce a separate eligible/mature/pending/unknown coverage table, including segments with zero mature members. Check identity uniqueness before this query. For retention, replace the event bounds with the declared tenure interval and require that interval's upper bound to be complete. For revenue, aggregate revenue lines at identity-period grain before joining to one-row-per-member origins; joining raw events to raw invoice lines can multiply both.

Acceptance checks before presenting:

| Check | Expected evidence |
|---|---|
| Conservation | Eligible = mature + pending under complete coverage; unknowns separately reconciled under the declared policy |
| Population | Unique members match source identity counts after documented exclusions; no unexplained join growth |
| Boundaries | Trace events just before origin, exactly at lower/upper bound, duplicate, late arrival and missing identity |
| Known outcomes | Never activated, churned, paused, returned, replaced and reactivated members remain under their declared rules |
| Aggregation | Segment numerators/denominators sum to total for exclusive segments; deduplicate overlapping segments separately |
| Revenue | Cohort movement and new/transfer revenue reconcile to company totals without double counting |
| Comparability | Same tenure, clock, source version, mature windows and revenue basis, with intentional differences labeled |
| Interpretation | Describe observation, alternative cause, uncertainty and decision separately |

## 8. Translate the investigation into a company choice

Deliver the original company variance, cohort contract, raw cells, within/mix bridge, economics and evidence for competing explanations. Include the affected population and company consequence, not only a statistically interesting rate. Name what remains unknown and the next evidence that resolves it.

For a short decision brief, emit a compact contract alongside the finding: identity, origin and eligibility, fixed segment, qualifying outcome, exact tenure/window, mature denominator, missing/pending treatment, source cutoff and version. Unknown rules stay visibly unresolved. Keep the full query in supporting material if space is limited. Saying that the analyst will inspect definitions does not make the reported rate reproducible.

The strongest objection to a cohort-based resource change is selection: different acquisition, pricing, market or product exposure can explain the pattern. If the action is cheap and reversible, a bounded pilot with a stop condition may be sufficient. If the action makes a material commitment and depends on a causal claim, use a suitable experiment or specialist-designed comparison. The volume threshold where an experiment becomes useful is whether valid observations for the needed effect and design can arrive before the decision deadline; no universal user count is supplied.

Conclude with a specific decision, owner, latest safe date, displaced work and effect check. Preserve the original query/snapshot and the later result. A corrected metric can change the interpretation without changing an approved target. A business result can justify revisiting strategy without proving a specific intervention caused it.

The [worked company review](../examples/company-metrics-review.md) and its [arithmetic check](../scripts/check_company_metrics.py) exercise maturity, mix, account and revenue retention, stock movements, cost boundaries and misleading conclusions.

# Consumer subscription growth

Use this method when a membership combines several benefits, plans, distribution surfaces, or household users. It applies to an established subscription business as well as a new offer. The output is a choice about the next growth investment, with a model and a test that could overturn it.

## Define the growth decision

Resolve three questions first: which business outcome, over what horizon, and within which resource constraints? Paid membership count, retained paid members, revenue, contribution, and adoption of a particular benefit can favor different investments. A tier upgrade grows revenue without necessarily adding a subscription.

If the assignment supplies only a broad growth question, state a provisional objective and proceed. For example: maximize incremental paid memberships retained at month twelve, subject to positive contribution and the available product capacity. Identify which missing input could change the recommendation. Do not spend the interview asking an exhaustive questionnaire.

Define the counted unit: paying account, billing contract, household, seat, or individual user. Keep trials, promotional entitlements, family beneficiaries, active users, and paying memberships distinct. Count each membership once across benefits and distribution surfaces. Record how bundles, carrier billing, annual plans, cancellations, refunds, and payment grace periods affect status.

## Reconcile the business before selecting tactics

Build a paid-membership bridge over a consistent period:

`closing paid = opening paid + first-time paid + paid reactivations - voluntary departures - involuntary departures`

Reconcile the bridge to billing records. Changes between paid tiers belong in a separate plan-transition table. Family invitations and additional devices do not create paid memberships by themselves. Measure revenue and contribution separately, including plan mix, net price, discounts, partner shares, and variable service costs.

Use the following data at membership/cohort level where available:

| Record | Minimum fields | What it resolves |
|---|---|---|
| Billing status | membership ID, household ID where applicable, plan, payer, channel, start/end dates, trial/promo status, net receipts | Paid count and double-counting |
| Journey | eligibility, exposure/assignment, offer, trial, first payment, first/repeat value, cancellation | Funnel denominators and timing |
| Cohort | start period, tenure, acquisition source, geography/eligibility, prior plan, payment type | Composition versus genuine improvement |
| Benefit use | successful customer task, frequency, unused benefits, service failures | Why people buy, stay, or leave |
| Economics | receipts, refunds, platform/partner share, support, storage/service/AI cost, campaign and build cost | Incremental contribution |

Write the analysis query or table specification, not just a request for a dashboard. For a conversion cohort, freeze eligibility and exposure at assignment, then follow first payment and retained status over the stated window. Include non-converters and failed payments. Record exclusions and missing joins. Keep annual and monthly renewal populations separate before comparing retention.

## Segment by customer job and buying state

Segment hypotheses should explain a different offer, intervention, or economic result. Age bands or broad personas alone rarely establish that difference.

| Hypothesized job/state | Evidence to seek | Candidate decision |
|---|---|---|
| Approaching a storage constraint | Capacity trend, service interruption risk, payment intent, alternatives | Relevant capacity offer and purchase friction |
| Protecting household data | Backup/restore success, shared payer, actual household use | Household activation, resilience, benefit explanation |
| Paying for AI task value | Repeated successful tasks, alternatives, usage cost, willingness to pay | AI offer, discovery, limits, plan value |
| Already paying for several benefits | Existing spend, overlap, channel and contract restrictions | Bundle design, migration, cannibalization |
| Trial or discounted entrant | Original promise, post-discount price, first value, payment readiness | Activation, trial-to-paid, promotion quality |
| Established member at risk | Tenure, benefit use, service problems, price changes, payment failures | Fix the cause of loss, distinguish voluntary/involuntary |

These are hypotheses, not known segments or proven interventions. Compare independent customer accounts, behavior, support, and transaction evidence. A benefit can influence purchase even when used infrequently, so low usage does not alone justify removing it.

For each job compare the customer's current free/default option, doing nothing, specialist substitute, competing paid offer and other bundle. Record its adequacy, switching friction and the concrete improvement worth paying for. In a storage/AI membership, expanded capacity, backup confidence, sharing and successful AI tasks can face different alternatives. Verify any named competitor's current terms before using them. Do not assume ecosystem reach or an AI label establishes willingness to pay.

## Build a competing-hypothesis tree

Partition the growth gap into eligible reach, relevant exposure, first payment, sustained value, retention, reactivation, and tier movement. Then ask what limits the next increment.

Compare insufficient buyer access, an unclear offer, checkout friction, an unproven AI benefit, poor acquisition cohorts, repeated service failures, and payment problems. Each explanation implies a different next test. More promotion can worsen the business if it scales a cohort that does not retain or has negative contribution.

For each candidate, specify the affected population, evidence, mechanism, expected incremental effect, competing explanation, cost, owner, dependencies, and result that would reject it. Include improving existing retention and doing nothing as credible alternatives to a new acquisition campaign.

Distribution through an existing ecosystem can provide reach, but impressions are not incremental buyers. Examine eligibility, overlap among surfaces, already-intending buyers, channel conflict, offer consistency, payment ownership, and cannibalization. A bundle upgrade may transfer revenue across products rather than create company-level growth.

## Compare retained growth and economics

Use a common horizon. Separate one-off cohorts from a repeated monthly acquisition program. Retention uplift affects surviving members over time, not every original customer indefinitely. Evaluate price and cost changes by plan and usage distribution, especially where heavy AI or storage use changes margin.

The [cohort calculator](../scripts/subscription_cohorts.py) makes a narrow constant-rate comparison reproducible. Its [synthetic input](../examples/subscription-growth.json) is a teaching case. It does not estimate causal effects, forecast an entire company, or model annual billing, changing prices, different treatment margins, taxes, and refund timing. Use a paired full cohort model when those differences matter.

### Worked investment choice

All figures below are illustrative. Each initiative is evaluated alone, with no assumed interaction. The common horizon is twelve months. Expected counts are end-of-month memberships. Contribution uses those counts at a constant unit margin, without discounting or intra-month cash timing.

| Initiative | Population and supplied effect | Monthly survival | Contribution per retained member-month | One-time cost |
|---|---|---|---|---|
| Acquire new paid members | One million eligible non-paying accounts. Paid conversion improves by 0.5 percentage points. | 97% | $5 | $120,000 |
| Improve existing retention | 100,000 existing members. | 97% to 97.5% | $5, unchanged | $100,000 |
| Upgrade an AI offer | 10,000 existing members upgrade. | 97%, unchanged | Additional $2 after AI/service costs | $250,000 |

Run the example from the repository root:

```sh
python skills/commercial-strategy/scripts/subscription_cohorts.py skills/commercial-strategy/examples/subscription-growth.json
```

| Standalone result | New paid conversion | Existing retention | AI upgrade |
|---|---:|---:|---:|
| Incremental paid memberships at month twelve | 3,469.21 | 4,415.60 | 0 |
| Twelve-month incremental contribution after one-time cost | $127,477.42 | $59,483.76 | -$52,018.06 |

If the stated objective is ending paid memberships with positive contribution and only one delivery slot, retention wins under these hypotheses. If the objective is contribution, acquisition wins. The upgrade does not win a subscriber-count objective under unchanged survival, and its supplied margin does not cover its cost. It could become attractive if evidence supports acquisition, retention, or higher incremental margin effects that this case does not assume.

The retention-versus-acquisition count choice flips when treatment monthly survival is about 97.3952%, holding every other input fixed. The upgrade's contribution break-even requires about $2.5255 incremental margin per retained member-month under its stated survival and cost. These are case calculations, not benchmarks. Test sensitivity to effects, margin, delivery cost, and lag before selecting a project.

Do not add standalone estimates when people can receive multiple interventions. Model the combined treatment or allocate disjoint eligible populations. The current paid base cannot be claimed again as new acquisitions or as every plan's independent audience.

## Turn the recommendation into evidence

Specify the eligible population and assignment unit before exposure. Household or payer-level assignment can be necessary when members share benefits or see several surfaces. Identify spillovers and cross-surface contamination. Analyze by original assignment, including those who ignore the offer.

Measure first payment and retained paid contribution over the required horizon, not only trial starts or clicks. Distinguish statistical evidence from business significance and from the decision's cost of being wrong. Use actual baseline rates, variance, effect size, and renewal lag to design sample and duration with the responsible analyst. Do not invent a universal number of days or respondents.

Guardrails can include refunds, complaints, payment failures, service quality, task success, contribution, cancellation friction, and losses in adjacent products. Name the release/rollback owner and capacity dependency. If twelve-month outcomes cannot yet be observed, report the decision as a bounded staged investment using explicitly provisional indicators. Do not present early activation as proven long-term lift.

## Deliver a senior decision brief

Produce a paid-membership bridge, useful segmentation, competing diagnoses, an economic comparison, and the next experiment. Lead with the chosen investment, the strongest alternative, the evidence that would reverse the choice, and what stops competing for resources. State which inputs are observed, supplied assumptions, or unknown.

For an interview, explain the objective and count definition, show the limiting mechanism, compare plausible investments, and make a conditional recommendation. For an operating assignment, include the query specification, model, accountable owners, dependency decisions, and experiment record needed to execute it.

## Reconcile a cancellation twice

[Buffer's cancellation review](https://buffer.com/resources/lower-mrr-arr/) found that a canceled annual account could stay in reported recurring revenue until its paid service ended. Carry the cancellation notice date, service end and collection date separately.

At month end, reconcile opening recurring revenue to closing recurring revenue under the written policy. Then show expected losses already under notice. Route that second amount to the forecast owner. A definition change requires a restated comparison period before anyone diagnoses customer behavior.

[Buffer's earlier correction](https://buffer.com/resources/mistake-made-measuring-revenue-confusing-bookings-revenue-mrr/) distinguished cash collected from recurring revenue. Reconcile prepaid invoices to the cash plan separately. An annual prepayment changes the timing of receipts even if the customer buys exactly the same service.

# Company and business-unit metrics

Select measures from the business mechanism: who receives value, who pays, what repeats, what limits delivery, and when cash moves. Use the existing `company.archetype`, `company.go_to_market_motion`, `company.product_maturity` and `org.scope` fields. The business mechanisms below are analytical descriptions, not additional context identifiers.

The strongest objection to a company metric tree is false completeness: a balanced equation can hide weak demand, concentration, harm or an unsupported causal link. Keep the equations as reconciliations, state which links are hypotheses, and preserve customer outcomes and binding constraints alongside the financial totals. Use only branches that could change the current decision.

## 1. Establish the company boundary

Record the served company or unit, included products/entities/geographies, customer and payer identities, revenue streams, operating period, currency and consolidation rules. For each stream write one sentence describing how value is delivered and charged. A company selling equipment, subscriptions and consumables needs three mechanisms even if it has one brand and one reporting segment.

Ask these questions before choosing a headline:

| Question | Evidence needed | Consequence for the pack |
|---|---|---|
| Is value repeated, episodic, contracted or capacity constrained? | Customer behavior, contract terms, delivery records | Use the natural repeat or renewal window. Daily use may be irrelevant |
| Are user, account, payer, household, device and beneficiary different? | Identity map and purchase rules | Count each explicitly and map their relationships |
| Does payment precede or follow delivery? | Orders, invoices, recognition policy, collections | Show bookings/obligations, recognized revenue and cash separately |
| Does growth consume cash or scarce capacity before it earns? | Inventory, installation, compute, staffing and supplier commitments | Show the constraint and its lead time next to growth |
| Can a local win reduce company value? | Cross-product overlap, transfers, subsidies and shared costs | Reconcile unit and company effects, including displacement |

Propose a compact company view containing customer value/demand, repeat behavior, monetization, contribution, cash/commitments and a binding quality or risk condition. This is a completeness check, not six compulsory charts or a composite score. At finding-fit stage, observed repeat value and affordable learning can be more decision useful than a precise lifetime forecast. In a mature portfolio, consolidation, mix and cross-product transfers require more detail.

## 2. Build the driver relationships before choosing charts

For each headline, draw one path to the records that generate it. Label an identity `=` only when units, timing and boundaries match. Label a proposed behavioral relationship as a hypothesis. Usage causing renewal is a hypothesis. The sum of billed usage quantities times their net rates is an arithmetic identity under the stated billing policy.

~~~text
Population stock at close = opening + first additions + reactivations - exits
Period activity = sum of qualifying events, not closing stock × an unrelated average
Revenue = sum of recognized revenue lines in period
Gross profit = revenue - cost of revenue under Finance's policy
Defined contribution = revenue - the explicitly listed included costs
Company operating result = stream contributions - remaining costs, with no overlap
Closing available cash = opening available cash + receipts - payments
                        + net financing + defined transfers
~~~

Monthly closing users are a stock. Orders/month are a flow. Orders/active-user-month is a rate. Multiplying a closing stock by a period-average rate can miss entry/exit timing. Use the sum of daily eligible exposure or a clearly labeled approximation when timing matters. Do not sum monthly unique users into quarterly unique users. Do not average segment ratios unless weighting by their actual denominators.

The tree must also expose capacity: feasible delivered activity cannot exceed demand that can convert, available accepted supply, and bottleneck capacity for the relevant period. Capacity can be a stock of installed systems with utilization, a workload limit, or an installation queue. A volume forecast above the bottleneck needs a concrete capacity or scope change.

## 3. Contracted software and recurring subscriptions

Use this mechanism when payment buys recurring access, seats or contracted service. Enterprise sales and self-service can share the revenue mechanism while having different timing and concentration.

| Measure | Proposed internal contract | What changes the decision |
|---|---|---|
| Recurring run rate | Annualized recurring charges effective at a dated snapshot, under Finance's inclusion policy | Separate signed/not-live, live/paid, ramped contracts, discounts, one-off work, consumption and currency. This is not annual recognized revenue |
| Opening-cohort revenue bridge | Opening recurring revenue + expansion - contraction - full loss = same-cohort closing recurring revenue | Freeze accounts and baseline product scope. State treatment of reactivation, acquisitions, contract consolidation and price changes |
| Net revenue retention | Same-cohort closing recurring revenue / opening recurring revenue | New customers excluded. Expansion can mask losing many small customers |
| Gross revenue retention | Sum of min(opening, closing revenue) for each opening account / sum of opening revenue, under this snapshot convention | Excludes expansion account by account. State whether a price increase offsets contraction under the chosen policy |
| Account retention | Opening accounts still meeting active/paying condition at close / opening eligible accounts | Pair with revenue retention and concentration. Retained account counts do not establish retained economics |
| New and expansion monetization | Live recurring charge or recognized revenue added, separately from signed bookings | Expose implementation/acceptance lag, price versus seats/workload, and the few contracts that dominate |
| Contribution and cash | Stream revenue less listed service/acquisition costs. Actual collections and obligations separately | Annual prepayment can improve cash while usage costs or renewal risk worsen |

Opening-cohort retention plus new-customer revenue reconciles closing recurring revenue only if reactivation and transfers are assigned once. Use a separate movement row when policy excludes them from the opening cohort. Aggregate retention by summing numerators and denominators, not averaging customer or business-unit percentages. A zero opening denominator is undefined.

Consumption software needs a second branch: metered workload × realized rate, with credits, minimum commitments, overages and unused commitments visible. A capacity contract is not evidence that all contracted value was consumed. As a source-specific example, [Snowflake's FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm) defines NRR using product revenue in two successive one-year windows for customers active in the first month of the earlier year. Nonconsuming cohort members remain with zero later revenue. That measure cannot be compared mechanically with a month-end recurring-charge retention ratio.

Investigate rising revenue with falling account retention by opening-revenue band, tenure, product, acquisition source and concentration. Investigate falling consumption with stable contracts by active workload, usage intensity, optimization, price, credits and implementation timing. Contracted backlog alone cannot decide which explanation is right.

## 4. Consumer: use, payment and repeat value

Start with the natural value cycle. A daily communication product, monthly subscription and occasional purchase should not inherit the same retained-use event or window. Define a meaningful behavior, then report eligible people/households, first value, repeat value at equal tenure, frequency among repeaters, paid conversion, realized monetization and cost to serve. Include free users when they create material service cost or economic value.

| Revenue mechanism | Driver equation under a declared period | Required companion evidence |
|---|---|---|
| Subscription | Sum of recognized subscription revenue for paid exposure during the period | Paid stock roll-forward, trial-to-paid conversion after complete windows, renewal by plan/tenure, refunds, collection failure and app/payment fees |
| Advertising | Eligible impressions × fill rate × net realized revenue per filled impression | Meaningful retained use, advertising load, net versus gross ad revenue, advertiser concentration, service cost and customer-value guardrails |
| Direct purchase | Completed net orders × realized revenue per net order | Repeat purchase by equal age, returns/refunds, discounts, fulfillment and contribution |
| Mixed free and paid | Separate revenue branches, common identity map and total service cost | Free-to-paid movement, overlapping users, household plans and cross-product substitution |

Paid conversion needs a starting eligible population, start event and conversion deadline. Paid subscribers divided by this month's active users is a penetration snapshot, not the probability that a new user converts. A period-end paid stock divided into period revenue is not period revenue per average paying subscriber without an exposure adjustment. Daily active/monthly active is a usage-frequency indicator under stated definitions. It does not establish individual retention, customer value or causality.

For example, [Duolingo's Q1FY2026 definitions](https://investors.duolingo.com/static-files/aab30d54-eb91-422e-b365-c03859fea85c) count unique active paying accounts and exclude trials and nonpaying family members. That is a different unit from daily engaged users. Use the company's actual identity and billing rules before comparing payment and use.

When growth accelerates, inspect retained users and contribution by acquisition source at equal tenure. Gross additions can cover weaker repeat value. A cheaper acquisition source can look attractive on signup cost while producing fewer retained paying users or higher service costs. Show observed cumulative contribution per acquired user and acquisition payback to date. Extrapolated lifetime value belongs in a sourced financial scenario.

## 5. Hardware, physical systems and service installed base

Track the full path through demand, physical flow, accepted operation and later economics. Shipped units, channel sell-through, accepted installations, active devices, paying subscriptions and people served answer separate questions. Multiple devices can serve one account. A replacement can create a shipment without a new customer. The contract can put sale recognition before or after installation.

| Relationship | Contract and company decision |
|---|---|
| Physical flow | Opening channel inventory + shipments into channel - sell-through - returns to manufacturer ± transfers = closing channel inventory, all in consistent units. A shipment increase without sell-through can build inventory rather than prove demand |
| Installed base | Opening accepted installations + first installations + qualifying reactivations - retirements = closing accepted installed base. Show replacements separately so they do not count twice |
| Usage and capacity | Accepted available system-days × utilization × successful output per system-day in use = successful output under matched definitions. Separate unavailable, idle and productive exposure |
| Monetization | System sales/leases + recurring service + consumables/usage. Service attach = eligible installations taking a defined paid service within a fixed window / installations with a complete window |
| Delivery economics | Recognized stream revenue minus product cost, freight/installation, field service, returns and warranty according to the declared contribution boundary. Reconcile to accounting gross profit rather than renaming it |
| Cash and commitment | Inventory receipts/payments, deposits, supplier minimums, work in process, installation backlog and receivable collections by due date. Show cash committed before accepted delivery |

A shipment cohort can answer return and field-failure questions. An installation cohort answers utilization, service attach and customer benefit. Do not substitute one origin for the other. Warranty claims need eligible devices/exposure and age since shipment or installation under the actual warranty contract. Recent cohorts with little exposure are not evidence of improved reliability. Pair observed claims with unresolved cases, reporting lag and Finance's estimated obligations. A low return rate among sales that have not passed the return window is unfinished evidence.

Inventory turns = matched annual cost of sales / average inventory carrying value under the stated policy. Days of inventory requires a declared period/day convention. Neither ratio describes the cash needed for a specific supplier order. For allocation decisions, show units/value by age, committed purchase dates, cancellation rights, expected demand and cash dates. Good gross margin can coexist with cash pressure from inventory and installation delays.

The distinction is visible in [Intuitive Surgical's FY2025 filing](https://www.sec.gov/Archives/edgar/data/1035267/000103526726000010/isrg-20251231.htm): installed base, procedures, instruments/accessories, service and operating leases support different parts of the business. Its [2023 report](https://www.sec.gov/Archives/edgar/data/1035267/000103526724000118/a2023formarsv3.pdf) also describes recognition that varies between direct acceptance and distributor shipment. These examples establish why the contract matters, not a policy to impose elsewhere.

A connected subscription can require another identity. [Peloton's FY2026 definition](https://investor.onepeloton.com/news-releases/news-release-details/peloton-announces-q4-fy2026-financial-results) excludes paused subscriptions from paid subscriptions and nets reactivations/unpauses in its reported churn count. A company using gross cancellations will obtain a different measure. State both gross loss and recovery when the decision concerns underlying customer departure.

## 6. Marketplace and platform economics

For a marketplace, connect both sides to completed value in the relevant local market, category and time window. Registered supply and registered demand cannot establish that an eligible request finds acceptable supply.

~~~text
Completed transactions = eligible requests × completion probability
Defined transaction volume = sum of qualifying completed transaction values
Transaction fee revenue = sum of fee-bearing volume × realized fee rate
Total revenue = transaction fee revenue + distinct other revenue streams
Defined contribution = revenue - included incentives, payment, fulfillment,
                       loss, service and other transaction-dependent costs
~~~

Specify whether volume is booked or completed and how taxes, tips, cancellations, discounts and refunds enter each term. Revenue/volume is an effective monetization ratio only over matched boundaries. Advertising or subscription revenue can change it without changing transaction fees. Gross versus net revenue accounting can change the ratio without a comparable operating change. For example, [Uber's Q3FY2025 definition](https://investor.uber.com/news-events/news/press-release-details/2025/Uber-Announces-Results-for-Third-Quarter-2025/default.aspx) includes taxes/tolls/fees in Gross Bookings and does not adjust it for consumer discounts/refunds, while excluding driver tips. [Shopify's Q1FY2025 definition](https://www.shopify.com/investors/press-releases/merchant-success-drives-shopifys-excellent-q1---delivering-strong-revenue-growth-and-profitability) instead describes GMV net of refunds and inclusive of shipping, duty and value-added taxes. Compare source contracts before comparing ratios.

Company-level leading evidence includes eligible-request fulfillment, time to match/complete, demand repeat and supply continuation at equal tenure, concentration, and contribution per completed transaction. Inspect distributions by geography/category/time rather than only a global average. Subsidy-driven transaction growth can raise volume while lowering contribution. Adding supply can reduce utilization and supplier economics before it improves completion. A balanced aggregate can hide markets where one side cannot earn or receive value.

A developer/API platform needs a different branch: eligible developers/organizations → activated production integrations → retained end-customer workloads → billable usage and partner economics. Raw API calls can include retries, tests and abusive traffic. Separate production from test, organizations from keys, and successful end-user outcomes from calls. Measure partner dependence/concentration and the company's revenue share under actual agreements.

Test whether more relevant accepted supply improves demand-side success or repeat use. Check whether more demand improves supplier retention or economics. Compare similar market cells with changes in density, quality, price and subsidy exposed. An observational association does not prove a network effect. Use an experiment or credible comparison when a major investment depends on that causal claim.

## 7. AI: delivered value and the cost of successful work

Add AI economics to the actual revenue mechanism rather than replacing it. A consumer AI subscription still needs paying/retained people. An enterprise agent needs accounts and deployment/renewal. Infrastructure needs customer workloads and capacity. A research lab's capability evaluation and compute commitments do not by themselves establish product demand.

Define attempted task, successful task, acceptable quality, deadline, review requirement and recovery. Record task IDs linking retries, model calls, tools and human review. Then compute:

~~~text
Task success = accepted successful tasks / eligible attempted tasks
Cost per successful task = cost of all eligible attempts / accepted successful tasks
Task contribution = net earned task revenue - all included delivery costs
~~~

The numerator includes failed attempts and retries within the population. Report cost per attempt too so success changes can be separated from efficiency changes. Pair success and cost with task mix, latency distribution, severe failures and human review. A cheaper route that fails more often can cost more per useful outcome. Never count a review queue as completed work or compare simple and complex tasks as if their mix were unchanged.

Price purchased inference using the dated contract for the provider, model and region. Include uncached input, cache writes, cache reads, output, tool charges and any other billed unit. [Anthropic's cache documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) distinguishes uncached input, cache-creation input and cache-read input. A single total-token count cannot reproduce that bill. No provider price or savings factor is supplied here.

For owned/committed capacity, show reserved cost, delivered workload, idle/unavailable capacity, utilization and incremental cost separately. Lower marginal inference cost is not equivalent to lower cash expense while a fixed commitment remains. Separate training/research spend, internal usage and customer delivery, and make allocation assumptions visible. Use [financial resource decisions](../../financial-resource-decisions/SKILL.md) for the resulting affordability, capacity or investment choice.

## 8. Consolidate hybrids and business units

Keep each stream's volume and revenue bridge, then reconcile to company totals. Never add seats, people, devices, orders and calls into a total customer count. Deduplicate common customer identities for customer totals while retaining stream-specific payer records. Separate organic change from acquisitions, transfers, price, currency and definition changes.

For business units show local result, controllable costs, shared allocated costs, intercompany elimination, company incremental cash and displaced company activity. A transfer from one unit to another is not company growth. A bundle discount or shared contract requires an explicit revenue allocation before product-level retention is interpretable. Present both product loss and customer retained elsewhere when migration matters.

Contribution is a management-defined boundary. List included costs and reconcile excluded costs once to the company result. Do not compare a marketplace contribution including incentives with a software margin excluding support and call the difference business-model quality. Local ratios do not add. Consolidate the underlying dollars or denominators.

## 9. Trigger a deep dive from a decision

| Observed pattern | First decomposition | Question that could change action |
|---|---|---|
| Revenue grows while repeat value falls | New versus retained cohorts, price, mix, concentration | Is acquisition masking deterioration in the base? |
| Growth holds while contribution falls | Stream mix, price/discounts, cost per delivered unit, success/rework | Does another unit of growth create value under feasible quality? |
| Bookings/shipments grow while cash worsens | Acceptance, collection, inventory, supplier and capacity commitments | Is this timing that can be financed or a deteriorating mechanism? |
| Aggregate improves while a major population worsens | Equal-tenure segment rates and mix, tails | Is the aggregate hiding an important failure? |
| Platform usage rises while monetization stalls | Test/retry traffic, free/paid mix, successful workloads, partner shares | Does activity create customer value and an earned charge? |
| Unit improves while company result does not | Transfers, subsidies, cannibalization, shared-cost treatment | Is the change productive for the company? |

Set triggers using impact, source volatility and time to respond. A material obligation breach can require immediate action from a small count. A sparse cohort can require case review even when statistical evidence is weak. No universal percentage, account count or funding stage decides whether to investigate. Use [cohort deep dives](cohort-deep-dives.md) for the evidence specification and [the worked company review](../examples/company-metrics-review.md) for executable calculations.

## Earn the right to manage an input

[HashiCorp](https://www.hashicorp.com/en/how-hashicorp-works/articles/operating-cadence) describes developing leading measures over repeated reviews. [Kevin Fishner](https://review.firstround.com/focus-on-your-first-10-systems-not-just-your-first-10-hires-this-chief-of-staff-shares-his-playbook/) separated practitioner adoption, commercial results and ecosystem contribution. A download can support the adoption story while leaving commercial value unresolved.

For an immature motion, keep the outcome visible and label the proposed driver provisional. Record which cohort should move, by when, and who can act on the input. Compare successive cohorts at the same age. Retire the driver if its movement repeatedly fails to precede the expected outcome.

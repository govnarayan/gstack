# Resource choices and economic analysis

## Unit economics: define the unit first

Define the customer, account, task, transaction, deployment, or capacity unit relevant to the decision. Specify revenue boundary, discounts/refunds, variable service costs, allocated costs, period, and cohort. Show both contribution economics and full cost where each answers a different question. Allocation assumptions are not incremental cash costs.

For recurring subscriptions, use an opening-revenue cohort to reconcile expansion, contraction, and loss. Net revenue retention equals (opening recurring revenue + expansion − contraction − churn) ÷ opening recurring revenue for the same cohort. Gross revenue retention excludes expansion. Exclude new customers from both. Annual recurring revenue describes an annualized recurring run rate under a defined policy. It is not cash, total contract value, or recognized revenue.

Acquisition cost must state included Sales/Marketing labor, programs, tools, commissions, allocation, and timing. Match acquisition activity to the resulting customers or cohorts where possible. A same-month spend/new-customer ratio can mislead with long sales cycles. Separate blended from channel, segment, and marginal economics. Expansion and customer success work can have real costs even when no new logo is acquired.

Use customer contribution cash flows over time to estimate acquisition payback and lifetime value. A simplified steady-state estimate based on revenue × margin ÷ churn assumes a stable comparable cohort and constant behavior. Young cohorts, expansion, contract terms, changing usage costs, and heterogeneous churn can break it. If evidence does not support lifetime extrapolation, show observed contribution and payback to date plus scenario ranges. Do not fabricate lifetime value from near-zero churn in a short sample.

Burn multiple can be calculated as net burn ÷ net new recurring annual run rate over a clearly stated consistent measurement interval. Specify whether monthly or rolling, how net new ARR is defined, and why the measure fits the business. Zero or negative net new ARR makes the usual interpretation invalid. Report contraction directly. Burn multiple, revenue growth plus margin, and SaaS quick ratio describe different things. None is a universal health score for a lab, consumer product, physical system, or nonrecurring business.

## AI, infrastructure, and physical-system economics

Use measured or sourced company inputs for model/compute, data, storage, network, retries, cascades, tools, human review, support, and failure recovery. Report cost per successful task under agreed quality and service conditions. Raw calls or tokens can conceal retries and failed work. Separate fixed commitments from variable use, idle capacity from delivered capacity, and customer-facing usage from internal experimentation.

Sensitivity should include task mix, success/review rate, utilization, latency/reliability requirements, and commitment flexibility where relevant. Pair cost with service and quality. Determine which lever matters from the actual workload and constraints. Technical owners determine feasible changes and validate quality. The operator compares economics and trade-offs with those inputs.

Physical systems may require hardware, inventory, installation, field service, warranty, and working capital. Infrastructure may require capacity commitments, availability, customer onboarding, and power/network dependencies. Do not substitute subscription gross margin for the actual economic model.

## Headcount, capacity, and incentives

Build cost from start date, cash compensation, benefits/taxes as provided by Finance, recruiting/onboarding, tools, travel, variable pay, and ramp. Distinguish cash cost from equity expense and equity dilution. Do not assume a grant valuation or market pay percentile. HR/Finance compensation data needs source, date, role, level, location, stage, and method before market comparison.

Compare a hire with alternatives: postponing the hire, narrower scope, process change, automation, outsourcing, or a vendor. The choice depends on judgment, relationships, quality, variable demand, control, confidentiality, integration, and reversibility as well as cost. Do not assume automation is preferable or count gross hours saved as cash savings when staff and obligations remain.

For revenue capacity, model productive months, ramp, demand/pipeline, win rates, contract size, cycle, implementation, and retention. For operational capacity, model workload, service level, variability, utilization, skills, maintenance, and coverage. Confirm the bottleneck. More staff cannot repair absent demand or an unresolved dependency by itself.

For a compensation scenario, model attainment distribution, hiring timing, ramp, accelerators, incentives, split credit, and churn/credit adjustments as defined by the owners. Show downside and high-attainment cases as well as the at-target case. Check that the same deal yields the same computed pay for Sales and Finance. Do not back-solve quota, hire dates, or commission rates to make the plan pass. HR, Legal, Sales, and Finance retain approval and specialist responsibility where staffed.

## Incremental business case

Compare options and status quo over the same horizon with incremental cash flows, timing, resources, constraints, risk, and future operating burden. Exclude sunk spending from the go-forward economic comparison while retaining relevant remaining obligations and exit costs. Opportunity cost includes the best feasible use of scarce staff, capacity, cash, and leadership attention.

Return on investment requires an explicit numerator, denominator, and period. Simple payback is meaningful for level positive periodic flows. For uneven flows, calculate cumulative cash recovery by period. Discounted net present value is the sum of incremental cash flows divided by (1 + discount rate) raised to the period, including the initial outflow at period zero. Obtain the discount rate and time convention from Finance or state a justified scenario range. Do not use a generic discount rate as company policy.

Internal rate of return is a supplementary view. Multiple sign changes can create ambiguous or missing rates, and rates can misrank projects with different scale, timing, and constraints. Do not rank investments solely by return rate or a fixed payback rule. Compare value, affordability, dependencies, risk, strategic necessity, and opportunity cost, including combinations of initiatives where dependencies matter.

A negative financial value estimate may still accompany an obligation, risk-control need, strategic option, or unmodeled customer benefit. Name that reason separately, quantify what is supportable, and define the evidence and review condition. Do not manufacture revenue attribution to force every required investment into an attractive return.

For build/buy, lease/buy, or vendor cases, include integration, migration, operating labor, security/compliance input, quality, implementation risk, exit, lock-in, flexibility, and residual value where relevant. Use equal horizons and service assumptions. Shared or constrained resources can make a cheaper nominal option inferior. Technical and control owners validate specialist claims.

## Recommendation and checks

Present option costs and benefits, timing, cash low point, capacity, sensitivity, break-even, alternatives forgone, strongest objection, and reversal condition. Name the input that would change the ranking. Specify the implementation owner and authorized decision without converting a model into approval.

Rework revenue-only cases, average economics used for incremental choices, and mismatched horizons. Challenge hires credited with all team revenue, unsupported discount rates, invented benchmarks, and savings that release no cash or capacity. A return metric must not hide a binding liquidity or service constraint.

## Separate a changed business from a hiring overrun

[Brian Chesky](https://news.airbnb.com/a-message-from-co-founder-and-ceo-brian-chesky) first narrowed Airbnb's business after a demand shock, then sized the organization for the remaining work. For a persistent change in demand, draw the revised service boundary before asking each group for cuts.

[Joel Gascoigne](https://buffer.com/resources/layoffs-and-moving-forward/) described Buffer hiring ahead of realized growth. Rebuild the cash path with existing commitments and realistic collections. Show the date each intervention takes effect. Count notice periods and already accepted offers before treating an approved cut as available cash.

[GitLab's headcount process](https://handbook.gitlab.com/handbook/finance/financial-planning-and-analysis/headcount-metrics-and-processes/) separates headcount planning from its administration. Give each approved position an identifier and distinguish planned, open, accepted and started. Reconcile those states with payroll before authorizing a replacement.

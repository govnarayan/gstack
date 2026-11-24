# Worked company metrics review

All records, rates, prices and decisions below are synthetic. The first case follows a recurring-access business with an AI workflow from source records to a company decision. Later exhibits test different business mechanisms. These are calculation demonstrations, not benchmarks or evidence that an intervention works. Run `py skills/operating-cadence/scripts/check_company_metrics.py` from the repository root to independently reproduce the stated results.

## 1. A growing company with a deteriorating opening base

The review asks whether to accelerate acquisition or first inspect losses and delivery economics. The unit is a paying account. Opening/closing recurring monthly charge is measured in dollars at fixed snapshots, with no foreign currency or acquisitions. New account E is excluded from the opening cohort. There are no paused/reactivated accounts in this exhibit.

| Account | Opening monthly charge | Closing monthly charge | Opening-cohort movement |
|---|---:|---:|---|
| A | $400 | $500 | $100 expansion |
| B | $300 | $240 | $60 contraction |
| C | $200 | $0 | $200 full loss |
| D | $100 | $110 | $10 expansion |
| E | $0 | $250 | New customer, outside opening retention |
| Total | $1,000 | $1,100 | $100 net company increase |

Opening-cohort closing revenue is $850. Net revenue retention is 850/1,000 = 85%. Gross retention under the account-level cap convention is (400 + 240 + 0 + 100)/1,000 = 74%. Account retention is 3/4 = 75%. The bridge is $1,000 + $110 expansion - $60 contraction - $200 full loss + $250 new = $1,100. Opening cohort declined $150 while new acquisition added $250.

The company grew its monthly charge by 10%. Four paying accounts remain at close, three from the original four and one new. Growth, retained account count and retained revenue each need their own statement. A retained account like B can lose revenue. A few large accounts can dominate expansion. A and B together account for $740/$1,100 = 67.27% of closing monthly charges, so concentration belongs in the decision.

## 2. Link the company result to successful delivered work

For this exhibit only, the $1,100 closing recurring charges were effective for the entire current month, so recognized subscription revenue is also $1,100. No proration, refunds, taxes or other earned revenue exist. In a real review, that equality must be reconciled rather than assumed.

The AI delivery ledger contains 1,000 eligible tasks, 800 accepted successful tasks and all model calls/retries for those tasks. Prices below are invented dollars per million tokens, not a provider quote.

| Billed model category | Quantity, millions of tokens | Synthetic rate per million | Cost |
|---|---:|---:|---:|
| Uncached input | 30 | $2.00 | $60 |
| Cache write input | 20 | $2.50 | $50 |
| Cache read input | 100 | $0.20 | $20 |
| Output | 32.5 | $8.00 | $260 |
| Model total | | | $390 |

Human review/recovery costs $110 and other included delivery costs $80. Total defined delivery cost is $580, including failures and retries. Cost per attempt is $0.58; cost per accepted success is $580/800 = $0.725. Revenue less these costs is $520 contribution, or 47.27% of revenue. This contribution boundary excludes acquisition and remaining company expenses; it is not asserted to equal accounting gross profit.

The prior month's $1,000 recognized revenue carried $350 of delivery costs and $650 contribution. Current revenue rose $100 while delivery cost rose $230, so contribution fell $130. That bridge does not establish whether quality, task mix, prices or inefficient retries caused the change. It identifies the next query: costs and success by comparable task class, model route, customer cohort and review need.

A proposed cheaper route costs $460 for the same 1,000 eligible tasks but succeeds on only 500 under the same acceptance rule. Cost per success becomes $0.92, 26.90% higher than $0.725 despite lower total spend. The correct action depends on accepted quality and success, customer impact, feasible capacity and the actual cost of switching. The synthetic comparison establishes the arithmetic, not production equivalence of task difficulty.

Remaining company expenses are $320, giving an operating result of $200 under this simplified boundary. Opening available cash is $2,000, receipts are $1,300 and payments $900, giving $2,400 closing cash. Receipts include $200 prepaid for later service; all current expenses are paid and there are no other timing/noncash items. Thus cash increased $400 while current operating result was $200. The $200 difference is future-service prepayment, not extra current earned revenue.

## 3. Reject the immature activation result

The investigation checks whether weak opening-base economics came from activation. Origin is first eligible paid-account entry. Activation is accepted value in `[origin, origin + 14 days)`. Reliable observation cutoff is January 20 at 00:00 UTC.

| Account | Origin | Value evidence | State at cutoff |
|---|---|---|---|
| a | Jan 1 | Jan 2 | Mature, successful |
| b | Jan 1 | Jan 14, duplicate delivery of same event | Mature, successful once |
| c | Jan 1 | Jan 15 at 00:00 | Mature; event is on excluded upper boundary |
| d | Jan 1 | Dec 31 only | Mature; event precedes origin |
| e | Jan 10 | Jan 11 | Pending full observation despite early success |
| f | Jan 10 | None | Pending |

The completed-window rate is 2/4 = 50%, with two pending entrants. Neither 2/6 = 33.33% nor 3/4 = 75% is the completed 14-day activation rate. The first counts pending members as failures; the second includes a pending member's success without its denominator. Duplicate events do not create additional accounts. The mature sample is tiny and may have a different entry mix, so 50% is not a defensible forecast for the final six-account cohort.

## 4. Test acquisition mix before claiming the product got worse

Two complete, equal-tenure cohorts have the following 90-day repeat-value records. Segments are fixed at acquisition; they are exhaustive and mutually exclusive.

| Entry cohort | Established need: repeats/eligible | Exploratory need: repeats/eligible | Total |
|---|---:|---:|---:|
| Earlier | 90/100 = 90% | 20/100 = 20% | 110/200 = 55% |
| Later | 19/20 = 95% | 54/180 = 30% | 73/200 = 36.5% |

Both segment rates improve while the aggregate falls 18.5 percentage points. The later result at earlier 50/50 weights is 62.5%. Using the bridge in the cohort reference, within-segment movement contributes +7.5 points and mix contributes -26 points, summing to -18.5 points. The unweighted mean of later rates, 62.5%, happens to equal the fixed-mix comparison; it is not the observed later rate.

The keep case for acquiring exploratory users is possible future value, a lower acquisition price or a strategic new market. The cost is weaker observed repeat and any delivery/acquisition burden. Before changing spend, compare observed cumulative contribution and acquisition cost at equal tenure. These data reject a uniform product-decline explanation, but do not establish that mix alone caused the change or that exploratory users should be abandoned.

## 5. Turn the evidence into the next review decision

The recommendation in this synthetic case is to hold the proposed acquisition acceleration until the existing-base and delivery-cost investigation completes. Continue existing acquisition while protecting its accepted budget. The strongest objection is lost growth while the diagnosis is incomplete. A bounded acquisition test can preserve learning if it fits the same cash/service limits and measures retained contribution.

| Investigation | Reproducible query/output | Choice it can change | Owner and timing |
|---|---|---|---|
| Opening-base losses | Account-state and revenue bridge by tenure, starting plan and top-account share; inspect cancellation/recovery cases | Product, service, pricing or customer-fit response rather than a uniform retention program | Business owner + Data, before next monthly allocation decision |
| Delivery cost | Task ledger linked to every call/retry/review; cost and accepted success by fixed task class and route | Route/process change, pricing, narrower scope or additional capacity | Product/technical owner validates quality; Finance checks economics |
| Acquisition composition | Equal-age raw cells, fixed-mix comparison, acquired-user cost and cumulative contribution | Shift source mix, continue an explicit learning test or accelerate | Commercial/business owner, same decision date |

The decider receives observed results, uncertainties, forecast implications, options and cash/service consequences. The effect check uses new cohorts with complete windows and matched task mix. The original snapshot is retained. If retained contribution improves and capacity/cash supports acceleration, reopen the hold. No causal claim is inferred from a balanced bridge.

## 6. Physical systems: shipments can outpace useful installations

This separate company has 200 units in channel inventory. It ships 120 into the channel, 90 sell through and 10 return from channel to manufacturer. Closing channel inventory is 200 + 120 - 90 - 10 = 220. The increase of 20 units is not end-customer demand.

Of 90 units sold through, 70 are first accepted installations, 10 are accepted replacements and 10 await acceptance. Opening accepted installed base is 1,000 and 20 installations retire. Closing base is 1,050, not 1,060; replacements do not create additional installations. Sixty first-installation accounts have completed the 30-day paid-service attach window, with 48 attached. Attach is 80%, with ten first-installation accounts pending, rather than 48/70 = 68.57%.

A separate financial bridge for the month records $100,000 recognized hardware revenue, $60,000 product cost, $8,000 freight/installation and $4,000 warranty expense in the declared contribution boundary: $28,000 contribution. Cash receipts are $80,000, inventory payments $90,000 and freight/installation payments $8,000, with warranty unpaid this month. Net cash movement is -$18,000. The reconciliation is $28,000 contribution + $4,000 unpaid warranty - $20,000 receivable increase - $30,000 inventory cash investment beyond cost recognized = -$18,000. No other timing items are assumed. Neither a shipment count nor positive contribution establishes cash affordability. Warranty/failure comparisons require equal device exposure; this case does not estimate the adequacy of the warranty provision.

## 7. Marketplace: volume and contribution can diverge

This separate marketplace defines volume as the value of completed transactions before platform-funded incentives, with no taxes, tips, refunds or other revenue in this exhibit. Period 1 has 100 transactions averaging $100, giving $10,000 volume. Fee revenue is 10% × $10,000 = $1,000. Included incentives cost $200 and other transaction costs $300, giving $500 contribution.

Period 2 has 120 transactions averaging $100, giving $12,000 volume. The same 10% fee yields $1,200 revenue. Incentives rise to $600 and other costs to $360, leaving $240 contribution. Volume and revenue each grow 20%; contribution falls 52%. Contribution per completed transaction falls from $5 to $2. A favorable completion rate would still need supply economics, repeat demand, concentration and cash inspected before increasing the subsidy.

The two periods cannot be compared with another company's headline GMV unless the volume, revenue and cost contracts match. An API platform recording 120 calls also has no reason to inherit this transaction model: the calls may be retries or tests, and its unit of value may be a retained successful workload.

## 8. Conclusions the review refuses to publish

| Tempting statement | Evidence-based correction |
|---|---|
| Revenue growth proves a healthy base | New charges grew enough to cover a shrinking opening cohort |
| Net retention is 110% | 110% is company closing/opening charge; opening-cohort net retention is 85% |
| Lower total inference spend means better economics | Accepted-success cost rises when success falls far enough |
| A refreshed query has complete recent data | Reliable observation cutoff and event lag determine coverage |
| Later repeat fell, so every customer experience worsened | Both starting segments improved; acquisition composition changed |
| More shipped devices means more new customers | Channel inventory, replacements and unaccepted units need separate flows |
| Marketplace growth proves profitable demand | Defined contribution falls while subsidies and volume grow |
| Higher cash means more current earned revenue | Prepayment changes cash timing and future obligations |

The executable checks validate these stated identities and boundary cases. They do not validate a real warehouse, accounting policy, intervention, production quality or causal inference.

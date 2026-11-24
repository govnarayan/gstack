# Repeat purchase and account response

Use this method when customers buy intermittently, replace equipment, replenish a product, or return for a project. A purchase gap is a signal to investigate. It does not establish cancellation, dissatisfaction, or a recoverable lost sale.

## Define the opportunity to return

1. Define the counted customer, qualifying purchase, refund treatment, first-purchase cohort, observation cutoff and repeat window. Distinguish a customer placing an order from units, revenue and contribution. Keep a fixed acquisition cohort for repeat rates and a separate opening active-customer population for period bridges.
2. Establish the relevant purchase cycle from comparable customers and the customer's own history. Separate replenishment, seasonal purchases, replacement, projects and discretionary purchases. Record stockouts, service failures, channel changes and known contractual pauses. With little history, show a range and mark the forecast unresolved.
3. Compare customers with equal opportunity to return. Include only cohorts old enough to reach the chosen window. Show cohort counts, repeat-customer rates, cumulative orders and contribution per original customer. Display new, repeat and reactivated customers separately. Keep currency, pricing and product mix effects separate from changes in customer behavior.
4. Investigate apparent lapses using purchase timing, service records and customer evidence. Check whether the customer still has the need, bought elsewhere, changed channel, or encountered an avoidable failure. Record unknown causes explicitly. Do not turn a standard-deviation threshold into a universal probability of churn.
5. Choose the response from its expected incremental contribution and the cause. Options include repairing service, restoring availability, changing the offer, contacting the account, testing an incentive, waiting, or accepting the loss. Include the cost of contacting people who would have returned anyway and discounts paid to existing demand.

The output is a cohort definition contract, repeat-purchase table, reason-coded investigation queue, and response decision with an owner and review date. Use the [cohort specification](../../operating-cadence/references/cohort-deep-dives.md) for identity, maturity, missingness and query requirements.

### Build a calibrated lateness queue

Order qualifying purchases by customer and date. Calculate completed intervals between purchases, days since the latest purchase at the fixed cutoff, and the number of observed intervals. Compare like purchase occasions and remove documented returns or duplicate events under the definition contract. Keep customers with insufficient comparable history in an explicit unknown group.

Choose an expected-return range or investigation threshold using comparable history and the cost of a missed problem versus unnecessary contact. Retain its derivation and limitations. On earlier cutoff dates, test whether flagged customers returned without intervention, whether known service failures were missed and how long useful warning lasted. Tune on earlier periods and inspect performance on a later period before treating the rule as validated. When seasonality or the offer changes, reconsider the comparison. A mean and standard deviation alone do not establish a reliable individual return forecast.

Produce one row per eligible customer: purchase history and source cutoff, expected range, elapsed gap, late/on-time/unknown state, contribution or exposure, observed cause, assigned response and next check. Report the flagged share among assessable customers, the unknown share of the full population, and the same quantities for a predefined high-value segment. Keep the segment rule fixed before examining flags. Compare these signals with the planning attrition assumption over a matched horizon, while preserving the difference between lateness and actual customer loss.

For a synthetic queue, assume two high-value customers have assessable thresholds of 45 and 90 days, with elapsed gaps of 60 and 80 days. Two other customers have a 30-day threshold with a 40-day gap, and insufficient history respectively. Two of three assessable customers are flagged. One of four is unknown. In the high-value segment, one of two is flagged and neither is unknown. These are investigation counts under assumed thresholds, not a churn forecast or a validated rule. Verify the two causes before selecting a response. Changing the threshold can change the queue without changing any customer's behavior.

## Make account reviews change action

For a managed account, connect the commercial assessment to a support decision. Record the customer's objective, current value received, relationship and service evidence, recent changes, unresolved concerns and the next dated commitment. Specify the observation behind each judgment and who can verify it.

If using a health rating, define its meaning and calibrate it against real outcomes. A single overall rating and separate explanatory observations are sufficient. Add weighted component scores only when their definitions, missing-data treatment and decision value are established. Preserve the prior assessment when new evidence changes the rating.

Escalate the help required: a service fix, executive decision, product dependency, capacity allocation or revised commercial plan. An unfavorable report should prompt diagnosis and assistance. Suppressing it to protect a score defeats the review. At a staffed company, the account owner owns the relationship and the relevant function owns the intervention. BizOps can build the analysis, resolve dependencies and test the investment within delegated authority.

## Worked decision

All values below are synthetic assumptions. A consumables business has two acquisition cohorts with a 90-day expected replenishment window. Cohort A has 400 customers, all observed for at least 90 days, and 160 have purchased again. Cohort B has 500 customers, but only 200 have reached 90 days. Of those 200, 90 have repeated. The mature repeat rates are 40% and 45%. Dividing 90 by all 500 would report 18% and confuse immature exposure with worse performance. The mature subset can still differ by acquisition date or channel, so this comparison is descriptive.

The team identifies 100 mature customers with no repeat purchase and verified delivery failures. Assume a randomized repair offer increases the probability of a repeat purchase by 8 percentage points, with $50 contribution per incremental order, a $2 contact cost per eligible customer and a $100 setup cost. Expected incremental contribution is `100 × 0.08 × $50 − 100 × $2 − $100 = $100`. Break-even incremental repeat probability is `($200 + $100) / (100 × $50) = 6%`.

Proceed with a bounded test if the assumptions and service capacity hold. Record eligibility before assignment, keep an untreated comparison, use the same observation window, and include the cost of repairs in the $50 order contribution. If that figure excludes another $15 cost per incremental order, expected contribution falls to `100 × 0.08 × $35 − $300 = −$20`. The decision then flips. Report the service obligation separately from whether a promotional investment pays back: customers may still be owed a repair.

## Completion checks

Reconcile customer and order counts, maturity and observation windows. Test whether the apparent gain comes from seasonality, timing shifts, discounts, concentration or channel migration. Separate observed customer outcomes from estimated future value. Name the decision that changes when evidence improves, and close the account action only after its owner verifies the outcome.

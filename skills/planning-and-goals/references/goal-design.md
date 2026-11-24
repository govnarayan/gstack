# Goal design and management

## Select the evidence before polishing the wording

Write the intended improvement and why it matters. Then choose a commitment based on what is still unknown:

| Uncertainty | Suitable commitment | Completion evidence | What it does not prove |
|---|---|---|---|
| We do not know which customer problem to solve | Learning goal | A decision between competing explanations using agreed evidence and disconfirming cases | Interview count alone proves demand |
| We do not know whether a prerequisite will be available | Dependency proof | Named provider accepts scope, access, capacity, date, and fallback | Another team's agreement guarantees downstream impact |
| We do not know whether we can build or deliver | Accepted output milestone | Defined functionality passes the agreed acceptance test with the intended users | Shipping creates customer or economic value |
| We have a credible lever but uncertain impact | Outcome goal | A defined customer/business measure changes within a valid observation window | The intervention caused all observed movement |
| A service must remain healthy | Operating commitment | Coverage and health remain within agreed bounds, with exceptions recorded | A maintained service is automatically a strategic improvement |

These can coexist. A new capability may need an accepted milestone followed by an outcome check. Do not force a distant outcome into the current cycle when no mature observations will exist. Use a later evaluation date or an interim commitment, with the future impact test visible.

## Write an objective and test its key results

An objective names the valuable change in ordinary language. Add a short rationale connecting it to the strategy and the constraint. Key results describe the evidence needed to judge the objective. Initiatives are the current route, and tasks are execution steps. Keep those four objects distinct even when they share one page.

Apply two tests to the full result set:

1. Value test: could all the results be achieved without meaningful customer or economic value, a needed capability, or a useful decision? If yes, improve the evidence.
2. Sufficiency test: could every result be achieved while the objective's stated intent still fails? If yes, narrow the objective or add the missing evidence. A metric bundle is evidence of intent, not a logical guarantee against every future failure.

Synthetic repairs:

| Weak draft | Revision | Why it changes the decision |
|---|---|---|
| "Launch onboarding" | Delivery: the defined self-service path passes acceptance for the named account types by May 15. Outcome: the mature May-entry cohort reaches the agreed activation target within 14 days | Separates build success from actual use |
| "Improve activation by 20%" | Increase 14-day activation from 40% to 52% for eligible new accounts entering in May, observed through June 14 | Defines the population and a 12 percentage-point, 30% relative improvement |
| "Interview 20 customers" | Decide whether manual setup or missing value is the dominant barrier, using task observations, completed and failed onboarding cases, and evidence that could reverse the conclusion by April 20 | Makes the commitment a learning decision rather than an activity count |
| "Maintain 99.9% service" as a stretch | Keep the existing contractual service commitment in operating health. If improving reliability is strategic, write a separate change goal against an evidenced baseline | Prevents an obligation from being treated as an optional aspiration |
| "Hire two engineers" | Keep hiring as a resourcing milestone with an expected productive start. Define the deliverable or capacity constraint it enables separately | An accepted offer does not create immediate productive capacity |

## Build a reproducible metric contract

Record the unit, population, eligibility, numerator, denominator, anchor event, observation window, time zone, exclusions, deduplication, source/query version, freshness, data owner, business owner, and missing-data rule. State the aggregation explicitly: median, percentile, sum, weighted rate, or another justified statistic.

A baseline needs a dated comparable period and the actual numerator and denominator where relevant. When the baseline is unknown, assign a short measurement commitment and label the target provisional. Do not write zero as a placeholder or approve a claimed improvement from an invented start.

For a cohort goal, all members need the same observation opportunity. If the behavior is activation within 14 days, an account created yesterday is pending, not a failure. Define the cohort-entry cutoff early enough to observe results by the evaluation date. Lock eligibility before seeing outcomes and report the excluded and pending counts.

Keep proportions and percentage points clear. From 40% to 52% is +12 percentage points and +30% relative. A 20% relative increase from 40% is 48%. For weighted rates, pool compatible counts or show their weights. Do not average an account rate and a dollar total, or unweighted team percentages with unequal populations.

## Set a target with a believable path

Derive a proposed target from four inputs: comparable baseline, strategic value of the improvement, plausible effect of funded initiatives, and the evidence window. Explain the assumptions and uncertainty. A convenient round number or external benchmark is a hypothesis until checked against this population.

For a funnel, use compatible units, ordering, and windows. For example, 200 eligible accounts × 50% expected activation = 100 activated accounts. This forecasts an expected count, it does not prove a target is attainable. If volume changes, show the rate and count separately. State whether the goal is the count, rate, or both.

Compare three cases when uncertainty matters: the funded current path, a plausible downside tied to an actual constraint, and an incremental alternative. Do not inflate forecast drivers to make a target fit. If no credible plan reaches a desired target, choose a resourcing decision, a narrower commitment, or an explicit aspiration with bounded effort.

Label each commitment before the period starts:

- A committed result has accepted resources and dependencies, an agreed success test, and an escalation path if it becomes infeasible.
- A stretch result describes a desired improvement with material uncertainty. Record the investment appetite, learning expected, and interpretation of a miss.
- An operating obligation uses its actual service or policy standard, including exception handling.

There is no universal expected fractional attainment for stretch results. A stretch target does not authorize overtime, spending, or taking resources from committed work. Label exploratory work explicitly rather than pretending it has the same delivery certainty as a proven process.

## Score without misleading arithmetic

Preserve raw results and interpretation alongside any normalized score. For a metric with baseline B, target T, and actual A, optional improvement progress is:

~~~text
Progress = (A - B) / (T - B), provided T differs from B
~~~

This works for an increase or a decrease when the target direction matches the intended improvement. Example: 40% to 52%, actual 48%, gives 8/12 = 0.667. Reducing hours from 100 to 60, actual 80, gives (-20)/(-40) = 0.5. Use the same units throughout.

Keep uncapped progress for diagnosis: negative means regression and greater than 1 means beyond target. If the display caps scores at 0 and 1, label the capped view and retain raw actuals. This is progress toward a chosen improvement, not probability of success or percent of customers served. If T equals B, the formula is undefined. Use a maintained-threshold test instead.

Binary milestones use pass/fail against acceptance evidence. A claimed 90% completion is not a passed security review. A maintained band is judged across its required observation period, with breach duration and severity. A cumulative target can show actual divided by target when that is the agreed contract, but it should not be confused with change-from-baseline progress.

Do not average unlike key results into a reassuring objective score. If a critical service, acceptance, or quality condition is necessary, treat it as a separate gate. A high adoption score cannot offset a failed required safety condition. Weighted scores are optional, with weights and minimum conditions set in advance. Report attainment, impact, and learning separately.

## Update goals while managing work

At each review, owners provide the current actual and timestamp, mature/pending populations, expected end result, confidence with reasons, dependency status, remaining effort, and decision needed. Progress and confidence answer different questions. A metric can be 80% of the way to target and forecast to miss, or have no visible outcome yet while delivery and observation are on schedule.

Change tasks freely within the accepted mandate when a better route appears. Change the commitment through its actual approval path when a material premise, resource, dependency, or strategic choice changes. A miss is a reason to diagnose, not an automatic license to lower the target.

For a proposed change, show original version and rationale, triggering evidence, options, additional or released resources, affected dependencies, displaced work, decision maker, effective date, new version, and communication. Preserve the original baseline, target, window, and due date for closeout. If a metric definition changes, disclose the break and retain both versions or a reproducible restatement.

At close, use one disposition per original commitment: achieved, missed and stopped, missed and continued, intentionally canceled, or pending measurement. For a continuation, create a new linked commitment with its own window and remaining work. Report the prior miss. Extending a quarter into a half-year without acknowledgment conceals the result.

## Incentives and performance

The strongest case for linking attainment to pay is that explicit rewards can give a commitment weight. The strongest objection is that the person negotiating the target can benefit from an easier goal, distorted reporting, or local optimization. Test both against the actual incentive policy rather than declaring all goal-linked pay wrong.

As a default for exploratory stretch work, keep a mechanical goal score out of the pay formula. Review actual contribution, judgment, collaboration, constraints, and learning through the existing performance process. Do not pretend outcomes are irrelevant to performance. Goals can supply evidence without being the rating itself.

A sales quota, contractual bonus, commission, or revenue-share agreement is a distinct incentive contract. Read the actual terms, controllability, caps, quality conditions, and interactions with other teams. Coordinate proposed changes with the actual People, Finance, and authorized owners. Never rewrite an incentive contract through an OKR exercise.

Run a gaming check: what would a rational person do to maximize the number or payout while harming the intended outcome? Examples include rejecting hard customers to improve a service metric, increasing low-quality signups, delaying recognition, or shifting work to an unmeasured team. Fix eligibility, paired quality measures, review and incentives where the behavior is possible. Visibility alone does not prevent gaming or justify publishing sensitive individual information.

## Failure cases to reject

Require a real baseline, defined denominator and an observation window that can mature before evaluation. Hold commitments with unaccepted dependencies, double-booked capacity or an owner who cannot obtain the decision. A provisional plan may remain useful, but label the unresolved issue and who must settle it.

Do not reject a milestone merely because it is not an outcome. Do reject a milestone being claimed as proof of impact. Do not punish a valid learning result because the hypothesis was wrong. Do reject a learning plan designed so every possible observation supports the preferred answer.

## Reopen a green goal when its assumption fails

[Amanda Richardson and fellow operators](https://review.firstround.com/annual-planning-in-uncertain-times-6-tactics-for-rethinking-your-companys-end-of-year-exercise/) describe planning under changing conditions. A team can deliver milestones on time after the premise for the work has expired.

Alongside the goal, record the demand or cost assumption that paid for it. Specify where the owner will see contrary evidence. At review, show the delivered result and the remaining case for funding separately. A failed assumption goes back to the plan owner even when delivery is green.

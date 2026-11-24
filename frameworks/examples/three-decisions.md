# Three worked decisions

All organizations, observations, amounts, probabilities, and outcomes below are synthetic inputs. The examples demonstrate reasoning with the library. They do not report real businesses or benchmark performance.

## 1. A broad growth plan with no coherent customer choice

Question: Should a reporting-product company spend its next quarter entering a second market or make its current segment repeatable?

Context: `org.scope=whole_company`, `company.archetype=b2b_saas`, `company.product_maturity=finding_fit`, `company.go_to_market_motion=enterprise_sales`, `role.authority=decision_owner`, `work.domain=strategy`.

Given evidence: The team can fund one initiative. Smaller regional distributors complete a standard setup, while larger multinationals require bespoke integrations. Recent purchase and cancellation interviews identify setup reliability as the deciding issue. The company has no demonstrated capability for international procurement or bespoke delivery.

Selection: Use the [kernel](../references/company-strategy.md#kernel) to explain the obstacle, then [Playing to Win](../references/company-strategy.md#playing-to-win) to make the reinforcing choices. Market size alone would not resolve this choice. Five Forces could assess industry pressures, but there is no evidence here that industry structure is the binding problem.

Output:

| Element | Decision |
|---|---|
| Diagnosis | A broad customer promise exceeds the repeatable delivery capability. |
| Guiding policy | Make the regional-distributor offer repeatable before widening the customer promise. |
| Coherent actions | Narrow the supported setup, dedicate the quarter's initiative to onboarding, and refuse bespoke integrations outside the boundary. |
| Winning aspiration | Become the preferred reporting workflow for the defined distributor segment. |
| Where to play | Regional distributors using the supported systems. |
| How to win | Reliable setup and useful reports with limited customer effort. |
| Capabilities | Standard connectors, repeatable intake, and a support owner. |
| Management systems | Track setup completion and retained use by customer cohort, and review exceptions against the segment boundary. |
| Rejected alternative | Enter another market now. It adds procurement and delivery assumptions before the present model is repeatable. |

Strongest objection: Narrowing the offer could miss an attractive large customer and constrain short-term revenue. That cost is accepted because the proposed growth path relies on unsupported delivery capabilities.

Flip condition: Reconsider expansion when delivery evidence shows repeatable setup for the current segment and a funded, credible route to the next segment. The exact pass thresholds must be agreed using business economics and capacity before testing.

## 2. More intake hiring despite a review bottleneck

Question: Will another intake hire get customer onboarding from three weeks to one week?

Context: `org.scope=function`, `operating.maturity=emerging`, `role.authority=delegated_owner`, `work.domain=cross_functional_delivery`.

Given evidence: The process currently accepts and completes 20 comparable cases weekly with no growth in backlog. Average open work is 60 cases. Intake can handle 30 weekly, review 20, and deployment 40. Qualified demand could support 25 weekly. Review loses time seeking missing intake information.

Selection: Use [Little's Law](../references/operations-flow.md#littles-law) for the baseline and [Theory of Constraints](../references/operations-flow.md#theory-of-constraints) for the intervention. RACI could clarify an owner but cannot create review capacity. A new intake hire does not address the measured constraint.

Calculated output: Stable average time is 60 / 20 = three weeks. The current review step limits accepted demand to 20. Raising intake capacity from 30 to 40 would not raise end-to-end capacity.

Decision and operating plan:

1. Protect review time and move completeness checks into intake. The delegated process owner assigns an intake owner and review owner, within the existing staffing mandate.
2. Run a bounded test of the new intake standard. Measure completed cases, rework, rejected cases, and customer wait, not only reviewer utilization.
3. If quality holds and review sustainably reaches 25 weekly, initially keep accepted work at 20 to drain excess open work. On the simplified constant-rate assumptions, reducing open work from 60 to 25 at five net completions a week takes seven weeks.
4. After the backlog transition, accept up to the tested sustainable rate. At a stable throughput of 25 weekly and average open work of 25, implied average time is one week. Observe that result rather than treating the equation as a guarantee.

Strongest objection: The missing-input change may not create five additional completions. The test must establish that capacity before promising faster delivery.

Flip condition: If review is no longer limiting, measure the new constraint. If qualified demand drops below capacity, adding process staff loses its rationale. Escalate any staffing investment beyond delegated authority.

## 3. Commit now or buy a learning stage

Question: Should the company launch immediately, run a pilot, or do nothing?

Context: `org.scope=initiative_or_portfolio`, `work.domain=resource_allocation`, `task.consequence=material`, `role.authority=decision_owner`.

Given evidence: All figures are assumed cash flows in thousands. The illustrative discount rate is 10%. Immediate launch costs 100 now and returns 60 at each of years one and two. A pilot costs 10 now. At the end of year one, it reveals either a favorable or unfavorable opportunity. The favorable probability is assumed to be 0.4. On a favorable result, a reserved right allows investment of 80 then, followed by receipts of 80 at years two and three. On an unfavorable result, the company stops. Doing nothing is worth zero.

Selection: Use [NPV](../references/economics-investment.md#npv), [staged options](../references/economics-investment.md#real-options), and a [decision tree](../references/economics-investment.md#decision-tree). A growth-share map would not evaluate this sequential commitment.

Calculated output:

| Alternative | Calculation | NPV |
|---|---|---:|
| Immediate launch | -100 + 60/1.1 + 60/1.1² | 4.13 |
| Pilot, then invest only if favorable | -10 + 0.4 × (-80 + 80/1.1 + 80/1.1²)/1.1 | 11.40 |
| Do nothing | No cash flows | 0.00 |

Decision: The pilot has the greatest assumed NPV. The contingent policy is to pay 10 now, invest 80 only if the favorable state is observed, and otherwise stop. Preserve the reserved right and record what constitutes a favorable result before funding.

Strongest objection: The probability and payoffs are assumptions, and the pilot delays revenue. If the pilot does not provide useful information or the right to invest later is lost, the apparent option value can disappear.

Flip conditions: The pilot beats doing nothing when the favorable probability exceeds about 18.69%. It beats the immediate launch when that probability exceeds about 26.42%, holding all other inputs fixed. Below the latter threshold, immediate launch is preferable among these three alternatives. Check liquidity, required return, and the credibility of the signal before committing.

This is staged managerial flexibility valued with a decision tree. No additional option premium is added to these cash flows.

## Recheck the growth decision when the buyer changes

In the first case, suppose the second market yields ten paying customers. Eight need bespoke integrations. The two standard deployments use the original team's capacity as expected.

Reopen the resource case using both groups. Attribute the integration specialists and ongoing support to the eight bespoke accounts. If those accounts need a separate sales and service organization, take that investment back to the plan owner.

This changes what the evidence means. Ten purchases establish demand for some version of the offer. Two standard deployments establish a much narrower starting point for a repeatable launch. [Buffer's product retrospective](https://buffer.com/resources/vp-product/) describes a related buyer shift.

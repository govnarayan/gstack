# Economics and resource investment

Read only the selected card. Mechanisms summarize the cited public sources. Application procedures, examples, and fit judgments are this library's own synthesis. All examples are synthetic.

## Before selecting a card

1. Reconcile quantities, prices and commitment dates to establish a credible cost baseline. [GAO cost estimating](https://www.gao.gov/products/gao-20-195g)
2. Compare the feasible alternatives on the same future cash and benefit assumptions. [Green Book](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026)
3. Price preserving the option to accelerate and identify the first irreversible purchase.

<a id="npv"></a>

## npv: Incremental cash flow and net present value

Supports: financial-resource, portfolio-priorities, pricing-monetization.

Context: work.domain=finance, org.scope, task.consequence, role.authority.

Decision trigger: A project, pricing change, or capacity investment needs an economic comparison with doing otherwise.

Inputs and evidence: Incremental cash receipts and outlays by period, investment, working capital, taxes where relevant, terminal effects, and an appropriate discount rate.

Procedure: Define the counterfactual, period, and cash-flow boundary. Exclude sunk costs and include opportunity costs and displaced cash flows. Discount incremental cash flows consistently with timing, currency, inflation, and risk. Compare alternatives and test the assumptions that can reverse the decision. Reconcile the result with cash and resource constraints.

Output: A cash-flow model, net present value (NPV), alternative comparison, and decision-sensitive assumptions.

Illustrative decision: A synthetic project costs 100 now and returns 60 at each of the next two year ends. At an assumed 10% rate, NPV is about 4.13. A positive NPV still needs comparison with the next-best use of scarce capacity.

Failure conditions and alternatives: Accounting earnings are not cash flows. A wrong counterfactual can dominate a precise calculation. Use a decision tree or staged-option analysis when later actions depend on learning.

Source: [Aswath Damodaran, Measuring Investment Returns](https://pages.stern.nyu.edu/~adamodar/pdfiles/ovhds/ch5.pdf).

Separate a write-down from future cash. [Microsoft's phone impairment](https://news.microsoft.com/source/2015/07/08/microsoft-announces-restructuring-of-phone-hardware-business) records a revised expectation for assets already acquired. For the next decision include remaining operating cash, exit costs and recoverable value.

<a id="sensitivity"></a>

## sensitivity: Sensitivity and breakpoints

Supports: financial-resource, scenario-response, research-analysis.

Context: work.domain=finance, work.domain=decision_support, task.consequence.

Decision trigger: A recommendation appears to depend on uncertain assumptions.

Inputs and evidence: A working decision model, credible ranges, dependencies between inputs, and the decision boundary.

Procedure: List uncertain drivers and their evidence. Vary one driver at a time to identify sensitivity, then solve for the values where the preferred option changes. Test linked variables together in coherent cases. Identify whether a feasible investigation could resolve the uncertainty and state the flip condition.

Output: A driver-ranked sensitivity view, decision breakpoints, and evidence to collect next.

Illustrative decision: A synthetic service charges 100 and has variable cost 60. With fixed costs of 2,000, break-even is 50 units. At variable cost 75 it becomes 80 units. The decision depends on supported demand and cost ranges.

Failure conditions and alternatives: One-at-a-time changes can hide correlation and nonlinear effects. A range is not a probability distribution. Use scenario planning for qualitatively different futures and a decision tree for sequential choices.

Source: [Aswath Damodaran, Tools for Dealing with Uncertainty](https://pages.stern.nyu.edu/~adamodar/pdfiles/country/NoiseSkagen.pdf).

[Intel's Ohio construction update](https://www.intel.com/content/www/us/en/newsroom/news/corporate/ohio-one-construction-timeline-update.html) kept construction moving more slowly. Solve for the demand date at which accelerating beats staying on the slower schedule. Ask procurement which orders become binding before then.

<a id="decision-tree"></a>

## decision-tree: Decision tree and backward induction

Supports: financial-resource, scenario-response, risk-governance.

Context: work.domain=decision_support, task.consequence, role.authority.

Decision trigger: Decisions occur in stages and later choices depend on uncertain events.

Inputs and evidence: Choices and timing, mutually exclusive event outcomes, conditional probabilities, cash flows or utilities, and feasible later actions.

Procedure: Draw choices and chance events in time order. Put costs and benefits at the point they occur and avoid double counting. At chance nodes calculate probability-weighted value. At decision nodes select the best feasible branch, working backward from terminal outcomes. Test probabilities and consequences that could alter the choice.

Output: A decision tree, preferred contingent policy, and probability or payoff breakpoints.

Illustrative decision: A synthetic test costs 10. With probability 0.4 it reveals a launch opportunity worth 50 net at the later decision date. Otherwise the team stops. Ignoring discounting, the policy is worth 10 net versus zero for doing nothing.

Failure conditions and alternatives: Invented probabilities create false precision. Expected value can conceal unacceptable downside or liquidity constraints. Use minimax regret when probabilities are not credible and staged-option analysis to examine the actual right to wait or stop.

Source: [MIT OpenCourseWare, Decision trees 1](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/4dd30003fe23dc89d27f55b500c15d15_MIT15_053S13_lec18.pdf).

Use [the Webb oversight report](https://www.gao.gov/assets/gao-22-105212.pdf) to test whether the branches compete for the same reserve. At each decision node identify what managers knew then. Do not use the eventual launch date as earlier evidence.

<a id="real-options"></a>

## real-options: Staged investment and real options

Supports: financial-resource, portfolio-priorities, product-delivery.

Context: work.domain=resource_allocation, company.product_maturity, task.consequence, role.authority.

Decision trigger: An irreversible commitment can be delayed, expanded, or abandoned after learning.

Inputs and evidence: Investment stages, rights and exclusivity, information arrival, later costs, expiry, competitive response, and cost of delay.

Procedure: Identify the actual managerial flexibility: defer, expand, contract, or abandon. Specify what information arrives before the next commitment and who retains the right to act. Compare commitment now with a contingent staged policy, including holding costs, competitive erosion, and foregone cash flow. Use a transparent decision tree when formal option pricing assumptions are unavailable.

Output: A staged funding agreement with continuation, stop, and expiry conditions plus its economic comparison.

Illustrative decision: A synthetic team pays 20 for a pilot and reserves a capacity slot. It can invest 80 more after verified demand. Without the reservation, competitors might absorb capacity, so the claimed option may not exist.

Failure conditions and alternatives: Uncertainty alone does not create option value. Nonexclusive opportunities and costly delay can remove it. Do not add a generic option premium to NPV or count the same flexibility twice.

Source: [Aswath Damodaran, Option Pricing Applications](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/option.pdf).

[Intel's Ohio construction update](https://www.intel.com/content/www/us/en/newsroom/news/corporate/ohio-one-construction-timeline-update.html) preserved some ability to accelerate. Price what it costs to keep the option alive and identify the last reversible order. Calling a delay an option says nothing about its value.

<a id="contribution-breakeven"></a>

## contribution-breakeven: Contribution economics and break-even

Supports: financial-resource, pricing-monetization, commercial-growth.

Context: work.domain=finance, company.go_to_market_motion, company.product_maturity.

Decision trigger: More sales or a lower price might increase revenue while worsening economics.

Inputs and evidence: Realized price, variable costs at the relevant volume, fixed and step costs, product mix, capacity, and demand evidence.

Procedure: Define the unit and time period. Calculate contribution per unit as realized price less incremental variable cost. Divide relevant fixed costs by unit contribution to find break-even volume. Include step costs and mix changes, then compare with reachable demand and capacity. For a change, use avoidable costs and the incremental counterfactual.

Output: A unit-economic bridge, break-even or target-profit volume, and the conditions for an economically useful change.

Illustrative decision: A synthetic service charges 120, costs 70 per job, and needs 5,000 per month in fixed costs. It needs 100 jobs per month to break even. A price cut to 110 raises the threshold to 125 if costs are unchanged.

Failure conditions and alternatives: A positive unit contribution does not establish full business viability. Step costs and capacity can invalidate linear extrapolation. Use NPV when timing and initial investment matter.

Source: [OpenStax, Calculate a Break-Even Point in Units and Dollars](https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars).
[DoorDash's annual results](https://ir.doordash.com/news/news-details/2025/DoorDash-Releases-Fourth-Quarter-and-Full-Year-2024-Financial-Results/) reports multiple margins against order value. Reconcile fees, incentives and variable fulfillment cost on the same order population. Test incremental contribution at the next unit of capacity.

# Portfolio allocation and operating interfaces

Use this reference to decide how an AI business should allocate people, compute and commercial commitments across coupled work. Produce an explicit constrained choice. The method is an adaptable planning aid, not a requirement to create a committee or use a scoring framework.

## Establish the actual constraint

Determine what limits the next business outcome: research uncertainty, validated quality, serving capacity, engineering integration, data rights, evaluation capability, support load, cash or buyer adoption. Separate binding constraints from inconvenient work. Adding compute does not resolve an unproven customer need. A better model does not remove a contract restriction on the required data.

Map resources by period, not just total dollars. Include the people with rare skills, evaluation environments, procurement lead time, customer access and shared infrastructure. State which resources can substitute and which cannot. A training commitment and a customer launch may compete for the same capacity at different times.

| Initiative | Business outcome | Evidence/uncertainty | Required resources by period | Dependencies | Incremental benefit | Continuing burden | Commitment/option value | Displaced work |
|---|---|---|---|---|---|---|---|---|
| Quality, cost, capacity, reliability or research | Accepted customer or operating result | Measured, estimated or unknown | Named roles, compute and cash | Upstream evidence or system | Common horizon and boundary | Operations, support and maintenance | Reversibility and consequences | Explicit alternative |

Keep mandatory obligations separate from optional investments. An obligation still needs the least costly feasible response and a capacity plan, but a high speculative return elsewhere does not erase it. Similarly, do not disguise every preferred project as mandatory.

## Compare feasible portfolios

For recurring improvements, estimate incremental contribution or capacity released within the relevant horizon, deduct implementation and maintenance and show the uncertain range. For uncertain research, show the value of learning, next evidence milestone, budget at risk and downstream option, without pretending the outcome is a committed feature.

Check combinations as well as individual rankings. Shared fixes can unlock several initiatives, while overlapping benefits can be double-counted. An initiative that ranks highly alone may be infeasible alongside another using the same specialists.

Synthetic quarterly example, with all values assumed for instruction:

| Initiative | Engineering weeks | Expected quarterly net benefit after ongoing cost, before one-time build | Other constraint |
|---|---:|---:|---|
| A: routing improvement | 4 | $30,000 | Requires quality acceptance |
| B: enterprise integration | 7 | $65,000 | Customer date and research dependency |
| C: service recovery repair | 3 | $20,000 | Required to make the current promise supportable |

Assume 10 engineering weeks available and C must be completed. A+B+C requires 14 weeks and is infeasible. C+B uses all 10 weeks for an expected $85,000 benefit. C+A requires 7 weeks for an expected $50,000, leaving 3 weeks for reserve or another bounded project. The $35,000 difference is not free value: B's quality, customer and research dependencies must be resolved, and the portfolio uses every planned week. If B has no viable fallback by its decision date, choose C+A or change the commitment. Do not translate an assumed benefit into booked revenue.

This arithmetic is not sufficient for the final decision. Apply obligation, quality and timing constraints first, then evaluate uncertain benefit, reserve needs and reversible staging. If benefit estimates are probability-weighted, disclose the probabilities and show outcomes without them. When no credible probability exists, use scenarios and the evidence needed to choose among them.

## Organization interfaces without surrendering the work

| Interface | Senior IC produces | Functional owner validates or decides |
|---|---|---|
| Research | Experiment/dependency economics, evidence dates and affected commitments | Scientific result, experimental interpretation and research plan |
| Product | Task/cohort value, acceptance trade-offs and scope scenarios | Product priority and user acceptance |
| Engineering | Reconciled demand, constraints, implementation options and acceptance fixtures | Architecture, effort, integration feasibility and operation |
| Finance | Cost bridge, unit economics, sensitivity and resource scenarios | Ledger reconciliation, accounting treatment and spending authority |
| Commercial | Promise inventory, contribution and capacity exposure | Pricing, contract terms and customer communication |
| Security/legal/safety | Specific unresolved decision and bounded proposed use | Applicable controls, rights and specialist approval |

Ask for precise missing inputs rather than outsourcing the analysis. For example: request measured throughput under the stated task mix, not a general feasibility opinion. Reconcile an Engineering estimate with the actual period's available weeks. Reconcile a commercial forecast with launch cohorts, limits and support capacity. Record disagreements and their effect on the recommendation.

In a small team, one executive or engineer may hold several responsibilities. In a larger company, use the existing decision structure and provide a compact exception or allocation decision. Size alone does not determine the interface: scope, risk, staffing and authority do.

## Decision record and follow-through

Deliver the selected portfolio, rejected feasible alternative, binding constraint, displaced work, economics, dependencies and authority. Include decision triggers rather than a status-only cadence. Each trigger needs an observable condition, owner and response. Examples include a missed evidence milestone, a service-cost threshold crossing, a capacity contract deadline or a materially worse customer cohort.

After approval, convert the choice into actual resource reservations and measurable acceptance, within delegated authority. Verify that the promised engineering weeks, compute allocation and rollout exposure exist in the operating plan. Inspect the next experiment or release against the decision record. An allocation memo whose resources never change is not implemented.

Keep a forecast-to-actual bridge: volume/mix, quality, price, service cost, build effort, timing and adoption. Attribute misses to these separate factors rather than using one undifferentiated variance. Reallocate or retire work when the evidence changes. Carry forward unresolved obligations and partial side effects so stopping a project does not silently abandon customer work.

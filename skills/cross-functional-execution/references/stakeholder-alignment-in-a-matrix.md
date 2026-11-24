# Align stakeholders in a matrix

Start with a decision that competing managers cannot settle inside their own teams. Map who owns the outcome, the people doing the work and who controls the scarce resource.

At Google, three people claimed ownership of an AdSense decision in front of Eric Schmidt. He stopped the meeting until the team named one owner. The eventual choice was undisclosed. [Rajaram](https://review.firstround.com/square-defangs-difficult-decisions-with-this-system-heres-how/)

## Prepare the call

1. Write the precise choice, latest safe decision date, rollback cost and consequence of delay. Separate inseparable trade-offs from issues that can have different decision owners. [Decision roles](decision-rights-rapid-raci.md)
2. For each affected group record its measure of success, scarce resource, authority, evidence, concern and implementation obligation. Mark an inferred position until the person confirms it.
3. Meet the people closest to the failure first. Then test the constraints with resource owners and formal approvers. Give those least able to object publicly a private route. [Square case](https://review.firstround.com/square-defangs-difficult-decisions-with-this-system-heres-how/)
4. Send an early proposal with alternatives. Ask what would make each option unacceptable and whether a specific change would earn support. Record revisions, unresolved dissent and commitments. [Kaplan-Moss](https://jacobian.org/2021/jan/18/consensus-before-a-decision/)
5. Ask a claimed veto holder to identify the charter, policy, budget or obligation behind the objection. Record the condition for clearance and who may accept residual risk. [Google launch practice](https://sre.google/sre-book/reliable-product-launches/)
6. When peers cannot reconcile objectives by the last safe date, present the conflict to their common sponsor. Show each viable option, cost, delay, displaced work and dissent. [Amazon](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders)
7. After the call, ask resource owners to confirm the actual change in staffing, schedule or policy. Update the decision and dependency records. Reopen only for a stated trigger.

Kaplan-Moss estimated 30 to 40 hours of advance conversations to narrow his team’s priorities. Use that investment when losing one group’s support would invalidate the choice.

For a reversible change inside one team’s authority, consultation can cost more than a bounded trial. A formal sign-off still applies when the team crosses an approval boundary.

## Worked example

A synthetic product lead promises a July launch. Security owns the release approval. Platform Engineering has one migration specialist already assigned to a customer deadline.

Sales wants the date kept. Its concern is a renewal milestone. Security can stop exposure of customer data. Platform can refuse to supply an engineer absent a priority change.

First confirm the customer’s actual need with Sales. Next test a read-only pilot with Security. Finally ask Platform what a pilot displaces before requesting approval.

The customer accepts a demonstration with synthetic data. Security confirms the limited setup needs no production rollout. Platform can support it without moving the migration.

The sponsor authorizes the demonstration only. Record the production launch as undecided, the platform owner’s capacity limit and the date the buyer needs a production commitment.

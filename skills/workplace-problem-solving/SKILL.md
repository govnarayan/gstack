---
name: workplace-problem-solving
description: Work through an actual operating problem by selecting relevant angles, testing competing explanations and recommending a decision, pilot or next piece of evidence.
metadata:
  capabilities: [workplace-problem-solving]
  context:
    required: [work.domain=decision_support]
    adapts_by: [org.scope, role.authority, task.consequence]
---

# Workplace problem solving

State who needs to decide what, by when, and what happens if nobody acts. A request for analysis can conceal a disagreement about ownership, resources or acceptable risk.

Read the request, existing company context, original decision and records of what actually happened. Research public company and people evidence. Establish whether the caller can act or is advising someone else.

Give a short baseline with facts, missing evidence and one rival explanation. Use the smallest set of angles that could change the call. State what you deliberately left out and why.

## Select angles by problem

| What must change? | Questions that matter first | Usually leave out until a trigger appears |
|---|---|---|
| Repair an operating failure | Where did the downstream customer first experience it? How often by path? What did participants know then? Which rival cause fits a successful case? | Market sizing and broad reorganization. Revisit structure if the failure persists under clear ownership. [Verble](https://www.lean.org/the-lean-post/articles/how-to-breakdown-a-complex-challenge-for-a3-problem-solving/) |
| Align work across teams | Which promises conflict? Who controls scarce capacity? Which incentives or vetoes survive a change in sequence? Who must accept the handoff? | Industry growth unless it changes a deadline. Escalate to the actual sponsor when peers cannot change their commitments. [Stripe operator account](https://every.to/p/operating-well-what-i-learned-at-stripe) |
| Enter a market or launch an offer | Who buys, what do they use now, how can we reach them, and can we serve them profitably? What local supply, policy or trust constraint binds? | Detailed team charts until a specific capability blocks entry. Separate proof of demand from proof of delivery. [DoorDash launch](https://ir.doordash.com/news/news-details/2021/DoorDash-Expands-To-Japan/default.aspx) |
| Allocate money or people | What additional outcome changes, for whom and when? What stops? What is the cash floor? Which indirect benefit or cost would reverse the ranking? | Total historical spend unless recoverable. Model uncertain benefits as a range and avoid counting them twice. [Planning practice](https://msiliski.medium.com/product-planning-a8c18d4018fa) |
| Choose a pilot | What uncertainty would change the decision? Who shares resources across the test groups? What is reversible? Who owns costs, guardrails and follow-up? | A full rollout plan before a pilot can discriminate between options. If evidence arrives too late, compare bounded commitment with delay. [DoorDash experiments](https://careersatdoordash.com/blog/balancing-network-effects-learning-effects-and-power-in-experiments/) |
| Recover from an incident | Which harm must stop now? What did responders see at each step? What made the action reasonable then? Which safeguard changes recurrence? | Individual blame and retrospective certainty. Follow the incident owner during containment. [Etsy](https://www.etsy.com/ca/codeascraft/debriefing-facilitation-guide) |

A problem can change type. A proposed product improvement becomes a resource decision when the only qualified engineer already owns a contractual deadline.

## From evidence to recommendation

1. Ask the decision owner to describe an observable success. Replay the same scenario with two affected groups and check whether their definitions match. [Siliski](https://msiliski.medium.com/good-goals-249db6df265d)
2. Compare a failed example with one that worked. Observe the actual handoff and identify the first difference relevant to the recipient. [Verble](https://www.lean.org/the-lean-post/articles/how-to-breakdown-a-complex-challenge-for-a3-problem-solving/)
3. Name a competing explanation and the cheapest evidence that separates them. Identify which data or testimony existed at the time. [Etsy debrief](https://www.etsy.com/ca/codeascraft/debriefing-facilitation-guide)
4. Present the best feasible alternative with the same time horizon, capacity and cost assumptions. Include the work displaced and the cost of waiting.
5. State the recommendation, strongest objection, reversal condition and decision deadline. Name the record and owner that changes next. Separate a proposed action from an approved one.

## Three worked decisions

**Conflicting roadmaps.** A synthetic 90-person subscription company promises a renewal integration while Platform plans a migration. Select dependencies, buyer commitments, incentives, scarce engineering time and sequencing.

Drop market size because both options serve the same contracted customer. Ask which demonstration the buyer accepts, who can approve an exception and what capacity becomes available after migration.

The buyer accepts a sandbox demonstration. Recommend the demonstration now and reserve production integration for the next capacity review. Reopen if procurement requires production evidence before the renewal.

**Market entry.** A synthetic 26-person marketplace considers a second city. Select reachable demand, supplier density at peak times, fulfillment cost, customer trust and downside cash.

Drop executive reporting lines because the same manager owns both candidate launches. Ask how many orders the promised service window needs and whether suppliers can cover it without subsidies.

A pilot requires 40 orders each Saturday to cover a $400 shift at $10 contribution per order. Only 26 customers precommit. Defer the fixed shift.

Offer a smaller service window and test paid commitments before signing a second supply contract. Reopen at 40 paid orders or a supplier quote that lowers the break-even point.

**A failing handoff.** A synthetic 180-person business sees implementations slip despite completing its kickoff checklist. Select customer impact, dependencies, elapsed time and receiver acceptance.

Drop a hiring plan until evidence shows a capacity shortage. Ask what the receiving engineer had at assignment and compare a timely implementation from the same segment.

Seven of ten delayed cases lacked a customer test account. None of ten timely cases did. Assign verification before handoff and compare matched cases next month.

That pattern justifies a reversible pilot. It does not establish that every delay has the same cause. Stop if verified access improves without shortening the customer’s wait.

## Connections

An unresolved market choice goes to [strategy](../strategy/SKILL.md) with the competing customer, offer and capability assumptions. A contested authority boundary goes to [decision rights](../cross-functional-execution/references/decision-rights-rapid-raci.md).

Use [matrix stakeholder alignment](../cross-functional-execution/references/stakeholder-alignment-in-a-matrix.md) when the decision needs another group’s resources. Record its specific commitment. Propose any missing connection with its mechanism, affected record and owner.

- [Strategy](../strategy/SKILL.md). Send the decision brief with customer alternatives and the reversal condition to the strategy owner.
- [Cross-team delivery](../cross-functional-execution/SKILL.md). Send the decision log with the deciding role and latest safe date to the program sponsor.

## Debrief after containment

In a one-hour debrief, Etsy suggests spending 35 to 40 minutes reconstructing what people saw and when. Record proposed fixes as they arise. Reconvene a smaller group about two working days later to assess them. Close by asking what someone learned that will change their work and who would attend another debrief. [Etsy facilitation guide, pages 16 to 18 and 27](https://extfiles.etsy.com/DebriefingFacilitationGuide.pdf).

# Reviews and operating health

## 1. Diagnose the information-to-action gap

Read the planning commitments and actual outputs from recent reviews. Trace one material exception from source data to discussion, decision, assigned work, completion evidence, and effect on the result. A meeting inventory alone cannot show whether a rhythm works.

For each existing forum, record purpose, owner, participants, sources, preparation burden, actual decisions, authority and unresolved items. Compare intended and actual use. Separate a missing signal from a delayed decision, insufficient authority, poor follow-through, or the wrong strategic premise. Each needs a different repair.

Use three distinct review questions:

| Question | Evidence | Decision |
|---|---|---|
| Are stable operations healthy? | Demand, coverage, quality, service distribution, incidents and customer experience | Restore service, investigate, adjust coverage or seek an authorized standard change |
| Is priority work advancing? | Accepted delivery, mature outcomes, remaining effort, dependencies, forecast and learning | Continue, narrow, accelerate, defer, stop or resolve a dependency |
| Is the direction still right? | Customer behavior, economics, changed beliefs, alternatives and disconfirming evidence | Retain the choice, revise it, or run a bounded test |

These questions may use the same room. Keep their outputs distinct. A goal can be achieved while its strategic theory fails, and a well-executed test can justify stopping the initiative.

## 2. Choose frequency from the decision window

Set the rhythm from how fast valid evidence arrives, how long a response takes, and when a decision becomes costly to delay. Data refresh and leadership meetings need not have the same frequency. A continuously monitored service can have an immediate incident route and a weekly trend review. A long development project can need weekly dependency resolution while its outcome is judged later.

A useful test is whether evidence latency plus review wait plus action lead time fits inside the latest safe response window. Illustrative case: a service problem becomes costly after 5 days. Data arrives after 1 day, action takes 2, and a weekly forum can add 7 days. The worst case is 10 days, so the forum alone is too slow. Add an alert and immediate authorized route. Do not claim a weekly meeting solved the issue.

Choose meeting duration and pre-read timing from the work required and the actual readers. Mark a proposed duration as a pilot. Do not prescribe pages or hours by funding series. Combine forums when the same people use the same evidence for the same choices, and remove duplicated status presentation.

## 3. Give each business review a different job

| Review | Main question | Inputs | Participants by decision need | Required output |
|---|---|---|---|---|
| WBR | What changed enough to require action now? | Comparable short-period trends, current goal actuals and forecasts, service exceptions, dependencies, overdue decisions | Owners who can explain the evidence and settle or escalate immediate choices | Action or investigation with owner/date, resource choice, escalation, or supported no-change conclusion |
| MBR | What recurring pattern or driver changes the expected result? | Closed-period actuals, segment/cohort analysis, driver bridge, forecast error, resource use and unresolved weekly hypotheses | Business/functional owners, Finance or Data where their evidence is required, affected partners | Revised forecast, tested diagnosis, scope/resource recommendation, and deeper evidence plan |
| QBR | What did the cycle achieve and what should the next plan fund? | Original goal contracts and amendments, final/provisional results, annual/rolling plan, service health, stopped work and capacity | Outcome owners, resource owners, integrator and actual approver | Closeout against original commitments, strategy question disposition, next funded portfolio, new commitments and communicated changes |
| Strategy review or named segment | Are the assumptions and chosen mechanism still right? | Belief register, customer and competitive evidence, economics, counterevidence and credible alternatives | The people who own the strategic choice and its evidence | Retain/revise a specific choice or commission a bounded test with a decision date |

These are proposed purposes, not universal meeting requirements. A monthly deep dive may replace that week's WBR. A QBR may contain a separate strategy segment instead of creating another standing forum. Do not use a quarterly financial review as evidence that someone reconsidered the strategy.

## 4. Prepare a decision-ready pack

Start with decisions needed, material exceptions and changed assumptions. Then show stable outcomes, drivers and guardrails. Use a memo, a table, slides or a hybrid according to the decision and reader. The format must expose reasoning, uncertainty and calculation, not win an argument by volume.

Each decision item includes:

1. Observation: actual, plan, trend, comparable population/window, source and freshness.
2. Interpretation: leading hypothesis, strongest alternative, what is known versus inferred, and evidence needed to distinguish them.
3. Choice: feasible options, recommendation, resource and service consequences, decision owner, latest safe decision date, and effect check.

The goal update shows original target and current forecast separately. Explain remaining effort, dependency status and time to observe the outcome. A color without those facts cannot support a resource choice. Pending evidence stays pending, and a stale number stays visibly stale.

Prepare owners to answer "what changed, why might it have changed, what can we do, and when must we decide?" An unknown cause is a valid answer paired with an investigation. Do not require a confident causal story as the price of raising an exception.

### Build the pack from standing sweeps

Most of the pack can be assembled by the same checks every week, run by an analyst or an AI assistant before the meeting. Each sweep reads the trackers the team already keeps and feeds one part of the pack. Each item it finds is tied to the ownership record the program already uses. That may be a RACI, a RAPID or DACI record, or a list of directly responsible individuals (DRIs). Without that link, the sweep produces a list nobody owns.

| Sweep | When | What it finds | Feeds | Ownership link |
|---|---|---|---|---|
| Status changes | Weekly, before the WBR | What shipped and what slipped, each slip with its stated reason | Prior actions | Accountable owner of each deliverable |
| Number moves | Weekly | Metrics outside their normal range against a four-week average, each with a likely cause marked as a guess | Exceptions | Metric owner |
| Blocked work | Weekly | Items blocked or unchanged for a week, who each waits on and for how long, oldest first | Exceptions | Accountable person for the blocked item, and the person it waits on |
| Dropped handoffs | Weekly | Work handed between teams in the last 30 days with no movement for seven days | Exceptions | Sender and receiver as recorded in the ownership record |
| Decisions due | Weekly | Decisions whose latest safe date falls before the next review | Decision requested | The named decider, plus anyone holding a veto, such as an Agree role in RAPID |
| Budget variance | Monthly, for the MBR | Lines off budget by more than the set limit, in dollars and percent. A reason is given only when a transaction shows it, otherwise "unexplained" | Variance table | Budget owner |
| Contract renewals | Monthly | Cancel-by dates from each notice period, flagging any within 14 days | Decision requested | Contract owner and the approver for spend |
| Duplicated work | Monthly | The same recurring task done by hand by several people, with people and hours counted | Change work proposal | Proposed single owner |

Three rules keep the sweeps trustworthy. Test each one on a past week where you already know the answer. Label every guess and estimate as one. A sweep only reports, so it never sends a nudge, changes a tracker or reassigns work.

The sweeps also check the ownership records. A blocked item with no accountable person is itself an exception. So is a decision logged by someone other than the named decider, such as an Input holder in RAPID or a Contributor in DACI. The [program check](../../cross-functional-execution/scripts/program_check.py) already flags that second case. These sweeps follow routines published on [myrunbook.ai's operator page](https://myrunbook.ai/operator), adapted to the review pack and the decision records used here.

Distribute material early enough for the actual reviewers to read it and challenge definitions. Resolve simple clarification asynchronously. At the meeting, confirm the shared facts, state the choice, hear relevant disagreement, and let the named authority decide. Do not equate attendance, silence, majority vote, or an executive's interest with approval.

## 5. Run the review and preserve the operating record

Open with prior material actions and changes in decision status. Mark each as completed with evidence, overdue with a decision, canceled with authority and reason, or still pending. Avoid repeating every metric. Discuss material anomalies, customer harm, worsening forecasts, hidden dependencies and counterevidence even when headline attainment is green.

For a short review, a proposed flow is prior commitments, exceptions, decisions, and owner/date confirmation. For a deeper review, add diagnosis and alternatives before decisions. Adjust the allocation when the work needs it.

Capture one operating record linked to the relevant plan and goal versions:

| Record | Fields |
|---|---|
| Metric snapshot | Definition/version, population, raw counts, period, source, timestamp and caveats |
| Goal update | Original contract/version, actual, forecast, remaining effort, dependencies and confidence reasons |
| Decision | Question, evidence, options, dissent, choice, actual approver, effective date, displaced work and revisit trigger |
| Action or investigation | Owner, due date, completion evidence, effect-check date, status and escalation |
| Amendment | Previous commitment, trigger, authorized change, new version and people informed |
| Learning | Hypothesis, observation, alternative explanation, limit and next test |

Separate approval of a plan from approval to spend, change a service standard, or make an external commitment. Keep the existing functional approval route. Communicate the decision to affected teams, including those absent from the forum, and verify their accepted dependencies are updated.

A supported decision to continue unchanged is a real output. Do not create unnecessary work merely to give every meeting a decision count. Information sharing, learning, coordination and relationships can also justify a forum when its actual purpose and cost are explicit.

## 6. Separate operating obligations from change work

Classify the work, not the function. Routine support is service. Replacing its tooling is a change initiative. Data infrastructure can include reliability obligations, recurring demand, capability investment and experiments. These categories need different evidence and may draw on the same people.

For an operating obligation, name the actual owner, population, demand, service definition, coverage, backup, exception trigger, response authority and recovery evidence. For an improvement, name the intended change, resources, dependencies, acceptance and effect check. An important service should not need a new quarterly objective to remain visible.

A staffed floor is one possible protection, not proof of adequate coverage. Evaluate the staffing and skill required for routine demand, demand spikes, absence, and an incident during a launch. Compare the floor with rotations, staged rollout, smaller scope, temporary qualified support, postponement, and explicitly accepted degradation where the owning policy permits it. Use actual demand and service evidence. Test the selected mechanism during representative execution before claiming it works.

Build a combined table by role and period. Show service coverage, reserve, launch work, new service demand and the remaining gap. A document that separates "foundations" from "priorities" does not reserve the same person's time twice. If leadership consumes a reserve, record it and tighten the response route. A named trade-off still has the consequence it names.

When a service exception appears, use the operational response immediately. The next WBR asks whether it was restored, whether its root cause affects the plan, and whether the capacity choice is sustainable. Do not keep unsafe or contractually unacceptable degradation running merely because leadership accepted a planning risk.

## 7. Run a strategy check that can disagree with the scoreboard

Maintain a short belief register: claim, evidence for it, confidence rationale, disconfirming observation, owner and decision date. Review the beliefs that carry the plan, rather than every sentence of the strategy.

Ask: did the intended customer benefit occur? Did the mechanism drive it or did mix and timing explain it? Are economics and service viable? What credible alternative now looks better? What would we stop if the original belief were wrong? If the evidence is insufficient, choose a bounded test and limit the irreversible spend until it resolves.

A material strategic event can require an off-cycle decision. A competitor announcement alone may warrant monitoring, while an evidenced changed customer requirement may require replanning. Define triggers with owner, observable threshold, response, approval and communication. Distinguish ordinary execution variance from a changed strategic premise.

At QBR, compare attainment, strategic validity and individual contribution separately. Close original goals against their original contracts, choose stop/continue/revise, fund the next portfolio and update related forecasts. Carrying a goal forward creates a new linked commitment. It does not repair the prior result by renaming its period.

## 8. Variants and usefulness test

For a startup, one founder-led forum with a shared plan can suffice. Add structure when consequential conflicts otherwise remain unresolved past their safe decision date. A delegated coordinator needs a mandate and escalation route, not assumed allocation power.

For a matrix or public-company unit, settle local questions locally and escalate cross-unit resources or corporate assumptions through the actual owner. Use controlled access for sensitive commercial, personnel or nonpublic information. Internal operating data is not automatically approved external disclosure.

For different work clocks, align the dependencies: a research evaluation may change product possibilities, implementation promises may lag sales, and seasonal demand may change comparison windows. Do not infer one cadence from an industry label.

Inspect a representative real review after introducing the change. Check which signals arrived late, decisions waited, actions lacked evidence, definitions changed, and original goals were silently rewritten. Measure preparation effort and total attendee time along with decision delay and missed signals. Compare with the prior burden and review again after an agreed trial. Attendance, number of documents, and green status are insufficient proof.

If AI prepares the pack, trace material assertions and arithmetic to original sources, inspect missing sources and dissent, and preserve uncertainty. Pilot on a real review alongside the existing check before changing meeting frequency. Avoid an invented promise that automation halves meetings or makes longer documents better.

## Give the exception somewhere to go

[Andrew Bosworth](https://boz.com/articles/reviews) distinguishes a review for information, discussion or decision. For a decision, bring the person who can change the commitment. For an unresolved cause, bring whoever can distinguish the competing explanations. Send stable information in writing.

[Cedric Chin's account with Colin Bryar](https://commoncog.com/the-amazon-weekly-business-review/) explains that Amazon opens its weekly review with financial results before examining controllable inputs. Put the financial exception and its suspected operating cause on adjacent pages. A booking shortfall without a verified driver goes to investigation. A confirmed demand change that invalidates the plan goes to finance.

[Colin Bryar and Bill Carr](https://workingbackwards.com/concepts/amazon-operating-cadence/) describe updating the operating plan with newer actuals. Close the loop by recording the revised assumption, the budget decision and the next review that will see its effect.

## Decide which recurring meeting earns its next occurrence

[Emilie Choi on The Peel](https://www.thespl.it/p/the-coo-playbook-with-emilie-choi) describes her chief of staff checking for repeated representation from the same function. In a remote organization, distribute decisions and actions to people who only need the result.

For one series, compare attendee-hours, distinct input, decisions taken and work delayed without the meeting. Trial a written update for one cycle. Restore the meeting if a decision stalls or a material objection reaches the owner too late.

For an in-person working session, name what the group will ship and who will accept it before booking travel. Keep annual trade-off discussions when leaders must resolve competing priorities together.

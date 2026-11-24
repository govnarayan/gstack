# Delivery and decision methods

## Diagnose the initiative

Start with the company priority and the actual coordination failure. Is the operator filling a temporary gap, resolving a cross-team dependency, implementing a new system, or improving an ongoing operation? Inspect existing plans and authority before creating a parallel structure.

For a simple reversible task, a clear outcome, owner, and check can suffice. Use a fuller charter when the work crosses boundaries, consumes material resources, carries substantial consequences, or has conflicting interpretations. A charter supports judgment. It is not a universal prerequisite to every action or an emergency-response gate.

## Make scope and authority explicit

Capture the problem, intended outcome, beneficiary, success evidence, included and adjacent excluded work, constraints, sponsor, delivery owner, decision owner, and dependency owners. Distinguish fixed constraints from scope or sequencing the delivery owner may change. A missing baseline can be an investigation phase. A missing sponsor or approval cannot be invented.

The delivery owner holds the integrated view and drives resolution. Functional owners retain their own decisions and work. The sponsor authorizes resources or resolves conflicts beyond the delivery owner's mandate. These roles may be held by one person in a startup. In a large matrix, they can differ substantially.

Authority and mandate must travel together: what is the operator accountable for, what may they require from others, what may they decide, and where do unresolved conflicts go? When tracking fails, compare missing authority with excessive process burden. Before adding a stronger owner, test whether the underlying mechanism is worth enforcing.

A responsibility table can help when interfaces are contested, but names and actual rights matter more than an acronym. Record who proposes, contributes facts, must approve, decides, executes, and receives the result. Do not require all work to use a committee, or eliminate real shared governance to force one individual decider.

## Dependencies and capacity

Identify milestones that produce verifiable evidence. Trace the chain from the final outcome backward through approvals, technical readiness, staffing, data, customer readiness, and service coverage. Name the dependency that would change the finish date if it slipped. For each material dependency, record the provider, recipient, acceptance test, committed date, confidence, and fallback.

Challenge capacity using actual skills and availability after ongoing work, leave, recruitment, ramp, and other commitments. People with different skills are not interchangeable units. A promise from a lead without available delivery capacity is still a risk. Use ranges and scenario alternatives where uncertainty is material.

Escalate before the latest useful decision time, with choices. For example: reduce launch scope to preserve service, move the date, add credible temporary coverage, or accept a named risk within authority. Explain what each option gives up. A red status without a decision or investigation path is incomplete.

### Calculate the feasible date and interface

For a consequential schedule, express durations and dates in a consistent working calendar. For each activity, earliest start is the latest finish of its prerequisites, adjusted for actual resource availability. Earliest finish adds its duration. Work backward from the required finish to derive latest permissible finishes and starts. The difference between earliest and latest start is schedule slack under those assumptions. A chain with no slack controls the modeled finish. Preserve the approved baseline separately from today's forecast.

These are basic dependency calculations. Unrepresented approvals, shared scarce people, time-zone windows, procurement lead time, weekends and uncertain duration can make a seemingly feasible path impossible. Check resource conflicts across simultaneous branches, and recompute after a material change. Do not add optimistic task estimates and call the sum a reliable commitment. The [GAO schedule guide](https://www.gao.gov/products/gao-16-89g) explains integrated schedules, critical path, resources and schedule risk in detail. Its full program controls are broader than most internal initiatives need.

Give a blocking interface a concrete contract: provider, recipient, deliverable and version, acceptance evidence, ready date, accepting owner, change notification, and fallback. “Security done” is not an interface. “The Security owner supplies the review disposition for release candidate 7 by workday 6; Engineering confirms all launch-blocking findings are resolved; unresolved exceptions go through the company's existing acceptance authority” is usable. Neither the coordinator nor a schedule calculation can waive that authority.

## Operational readiness and process improvement

Delivery is not limited to meetings and tracking. Within the assigned mandate, help design, implement, and improve operating mechanisms. These can include support triage, self-service, onboarding, data handoffs, approval routing, launch support, or systems removing manual work. Coordinate with the functional and technical owners who will run it.

Readiness asks whether the company can operate the change safely and usefully after it launches. Check the dimensions relevant to the assignment:

| Dimension | Evidence to seek | Decision it supports |
|---|---|---|
| Service demand and coverage | Expected workload, peak scenario, specialist coverage, backlog and recovery plan | Limit rollout, add coverage, or accept bounded service risk |
| Quality and customer impact | Acceptance tests, error or rework rates, complaint paths, accessibility where relevant | Fix before launch, stage exposure, or monitor an accepted limit |
| Systems and data | Working access, reliable data flow, permissions, fallback, monitoring, and reconciliation | Proceed, narrow scope, or repair a missing operating dependency |
| People and ownership | Trained operators, clear handoffs, support material, escalation and backup owners | Transfer to a permanent owner or keep temporary coverage |
| Change and adoption | Affected teams, communication, training, feedback, and changed incentives | Adjust rollout or invest in adoption rather than call installation success |

Do not treat a system installation as proof the process improved. Establish a baseline such as elapsed time, error rate, service quality, manual effort, or user outcome. Inspect the current process directly, including exceptions and rework. Identify where delays or failures occur, then compare an implementation change with simpler alternatives. A new tool can automate a broken rule just as easily as improve it.

For a pilot, name the population or scope, success test, guardrails, observation period, owner, rollback or fallback, and what evidence supports wider adoption. Automating a step does not transfer accountability to software. Verify that the output reaches the next owner in usable form, including failures and uncommon cases. Feedback from the operating team should change requirements when the pilot exposes a real gap.

## Decision support and records

For a consequential or contested choice, frame the decision as a concrete question. State the recommendation, strongest counterargument, alternatives including delay or no change, evidence, cost of delay, reversibility, affected stakeholders, and required approval. Scale the analysis to consequence and uncertainty. Reversible does not automatically mean harmless or cheap.

A decision right specifies the boundary, not just a person's name. A product lead might choose scope inside an agreed budget but lack authority to change a contractual promise. A public-company initiative can involve several established approvals. Record the actual arrangement and unresolved claims to authority.

Separate suggestions, discussion, provisional agreement, and authorization. Extracting phrases such as “we should” or “agreed” from notes is a way to find candidate decisions, not proof that the right person approved them. Resolve uncertain status with the source or decider.

A useful decision record holds date, question, decision, authority, rationale, evidence, and dissent. Add execution owner, next step, due date, review trigger, and source and prior-decision links. Preserve the old record when a new decision supersedes it, marking the active version. A previously rejected option can be revisited when evidence, context, or authority changes. History should prevent accidental relitigation rather than block warranted learning.

Check contradictions across current records and duplicated action ownership. An overdue review needs a resolution or explicit extension by the right owner. Do not silently convert a recommendation into an approved entry or infer consensus because no objection was captured.

## Stakeholders and communication

Map affected people and their actual interests, knowledge, dependencies, and decision rights. Influence and interest can help decide engagement intensity, but low formal power does not reduce the importance of an affected operator, customer, or control owner. Mark unknown stance as unknown. Avoid guessing motives or distributing private assessments of colleagues.

Use an update that states outcome progress, changed risks or assumptions, dependency needs, decisions, and next evidence. Match detail to audience. Executive updates emphasize choices and consequence. Delivery updates emphasize scope, interfaces, timing, and acceptance. Respect the company's terminology and information access.

## Closure and handover

Plan an enduring owner early. A temporary operator assignment should not become permanent through neglect. Equally, do not force handover when leadership intentionally delegated continuing responsibility. State the mandate and criteria for transfer.

Closure evidence includes agreed acceptance, verified deliverables, outcome or learning evidence, operating documentation, trained owners, access, known issues, unresolved risks, support and escalation, and the next review date. Match the handover to the work. If downstream outcomes take time, separate delivery acceptance from the later impact check.

Inspect the process after transfer: does the owner actually use it, do exceptions route correctly, and do service or outcome measures improve? If a corrective action changes a rule or control, verify its next real use rather than treating a written change as completion.

## Failure modes and countercases

Watch for functional trackers with incompatible dates, hidden scope changes, and green status concealing a blocking dependency. Inspect activity-only milestones, launch plans omitting operating demand, and temporary owners absorbing permanent work.

Fixed status colors, arbitrary utilization bands, story points, and composite health scores cannot determine readiness without context. A weighted average must not hide a single unacceptable risk. Small teams may resolve coordination with direct conversation. Large initiatives may need formal approvals and audit trails. Choose the structure for the decision and consequence.

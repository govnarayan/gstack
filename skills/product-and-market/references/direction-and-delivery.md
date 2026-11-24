# Product direction and delivery records

## Product outcomes and choices

Start with the stated company choices, customer problem, and product outcome. Distinguish outcomes from shipped features and from service obligations. A reliability requirement or a promised migration can be necessary even when it ranks poorly on a growth score. Identify what is committed, what is being tested, and what remains optional.

Compare product options on customer contribution, reachable population, uncertainty, resources, dependencies, operating burden, and opportunity cost. Include a status-quo or smaller-scope alternative. Technical and commercial owners supply feasibility, effort, selling implications, and ongoing service requirements. Keep ranges and named assumptions when estimates are weak.

Use a numerical prioritization method only if it clarifies the choice. A reach × impact × confidence ÷ effort score needs a common reach period, consistent impact scale, defined confidence, and comparable effort units. Avoid counting the same reach or confidence twice. Test whether plausible changes reverse the ranking. Distinguish customer-problem scoring from solution scoring and from mandatory constraints. Shared dependencies and mutually exclusive options make independent item rankings insufficient.

A roadmap shows intended outcomes and bets, sequence, dependencies, capacity, explicit non-goals, and conditions for changing course. Match timing precision to evidence. Separate delivery commitments from discovery options. Do not use relative dates to hide an actual contractual deadline. Do not convert a rough plan into a commitment without the owner's confirmation of feasibility and resources.

Explain how product work contributes to company outcomes without mechanically dividing company targets among teams. Keep service health distinct from change goals. If a company already uses a cascade, assess whether the causal links, shared work, and authority are real. Neither a high alignment score nor full goal coverage proves an executable plan.

## Translate field evidence into choices

Recurring customer and field blockers can require product, policy, technical, enablement, or commercial changes. Classify the underlying need before committing a feature. Keep the customer's exact requirement, use case, account/segment, recurrence across independent accounts, affected buying stage, economic exposure, current workaround, and urgency together.

Compare responses: clarify an existing capability, improve proof or enablement, change a policy, build product functionality, provide a bounded service exception, or decline the use case. Distinguish repeated requests from verified deal blockers. Record conditional customer commitments and check whether solving the blocker would actually unlock adoption. Do not sum overlapping pipeline as certain revenue.

For security, privacy, policy, or deployment requirements, the accountable specialists determine what is accurate, permitted, and feasible. The operator makes the evidence, alternatives, dependencies, cost, owner, and decision legible. The resulting record names the chosen response, what field teams may communicate, unresolved restrictions, release/readiness conditions, and how the originating teams learn the result.

## Choose the lightest sufficient record

| Situation | Useful record | Content that must survive simplification |
|---|---|---|
| Small reversible product improvement | Short brief or backlog item | Why, intended behavior, observable acceptance, owner, key constraint |
| Cross-team or consequential feature | Product requirements document | Evidence, target users, outcome, scope/non-goals, dependencies, requirements, risks, acceptance, release conditions |
| Unclear customer value in a proposed major bet | Future announcement and FAQ as a thought experiment | Real problem evidence, proposed benefit, unknowns, cost/operating objections, decision requested |
| Migration, retirement, or breaking change | Transition record | Affected groups, obligations, replacement, dates, support, data handling, rollback or recovery |

A requirements record can include summary, stakeholders, background, objective, segment, value proposition, solution, and release. Choose the elements that clarify the decision without requiring a fixed section count. A code-derived specification describes observed behavior. It does not establish customer intent or authorize preserving every existing behavior.

A complete requirements record defines the problem and evidence, actors, desired result, current behavior, proposed behavior, in-scope and excluded cases, constraints, dependencies, unresolved decisions, and acceptance. Keep system architecture and implementation plans with technical owners. Identify legal, privacy, accessibility, safety, reliability, and support requirements when they affect the product decision. Do not invent compliance assertions to fill a template.

User stories, situation-based job stories, and why/what/acceptance records are alternative forms. Choose the form that makes the work clear. Split by a valuable and testable user outcome rather than a layer such as database, interface, or reporting unless a technical dependency requires that work. Do not pretend every item can be delivered in any order. Record real dependency and sequencing constraints.

Postpone performance, security, or scalability work only when the responsible specialist confirms the smaller release still meets required obligations and usable service conditions. Mandatory security, privacy, safety, or reliability cannot become optional polish to make a release slice appear small.

Acceptance describes observable behavior, starting conditions, affected user, normal and important failure cases, and evidence needed for sign-off. Distinguish acceptance of delivered behavior from evidence that the product outcome improved. An enabled feature can pass acceptance and still fail the business hypothesis. QA and Engineering own specialist testing and release engineering where staffed. The operator ensures the agreed criteria, owners, and evidence are clear.

Preserve one traceable chain from raw evidence to problem, candidate mechanism, assumption test, chosen commitment, requirement, and post-release decision. Record which evidence supports each link and which promise remains untested. [The investment-to-release case](investment-to-release-case.md) fills this chain and demonstrates why a positive user result can coexist with a failed economic condition and a smaller next commitment.

## Launch, learn, migrate, retire

Release readiness includes product behavior, instrumentation, commercial enablement, service readiness, capacity, dependencies, customer commitments, decision owner, and rollback or recovery conditions. A launch date is a constraint to evaluate, not evidence of readiness. Product-delivery records should expose blockers and decisions rather than create another parallel project tracker.

Release notes state what actually shipped, who can access it, what changed for them, material limits, and required action. Do not turn an implementation change into an unsupported claim of a quantified customer benefit. A future announcement used for planning must be visibly marked hypothetical and must never invent a customer quote or imply availability.

Compare results with the baseline and stated outcome, using meaningful cohorts and the expected time to value. Explain what the launch taught, what failed, and which choice changes. Keep corrective work, service health, and new investment visible separately. For retirement, include dependency users, contract and service implications, replacement and migration, data/export needs, support burden, completion criteria, and approval by the owners of those obligations.

## Output tests

A reviewer should identify the customer problem, intended result, rejected alternative, and resource trade-off. The record must show promises, scope authority, completion evidence, and conditions for revisiting the investment. Rework a record that has polished feature lists without evidence, scores without comparable inputs, dates without capacity, invented technical certainty, or an acceptance test masquerading as demand validation.

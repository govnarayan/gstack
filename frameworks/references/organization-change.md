# Organization and change

Read only the selected card. Mechanisms summarize the cited public sources. Application procedures, examples, and fit judgments are this library's own synthesis. All examples are synthetic.

## Before selecting a card

1. Compare how the sender and receiver describe ownership to uncover an unassigned duty. [Atlassian responsibilities](https://www.atlassian.com/team-playbook/plays/roles-and-responsibilities)
2. Check whether the person can perform the new task and what reinforces it after training. [Prosci ADKAR](https://www.prosci.com/methodology/adkar)
3. Replay an exception where the old structure failed and identify the individual who can commit resources.

<a id="seven-s"></a>

## seven-s: McKinsey 7-S

Supports: organization-design, strategy-review, people-operations.

Context: work.domain=organization, org.scope, operating.maturity, role.authority.

Decision trigger: A strategy or reorganization fails even though the reporting chart looks sensible.

Inputs and evidence: Strategy, structure, systems, shared values, skills, staff, management style, and observed behavior.

Procedure: Describe the current state of the seven interdependent elements. Specify the behavior and capabilities the strategy needs. Identify the most consequential inconsistencies between elements and design a small coherent set of changes. Test actual behavior and results rather than scoring seven boxes and declaring alignment.

Output: An alignment diagnosis, coordinated changes, accountable owners, and evidence of behavior change.

Illustrative decision: A synthetic company moves toward recurring services but rewards only initial sales. Changing teams alone leaves the old behavior intact, so compensation, service skills, and renewal information also need review.

Failure conditions and alternatives: The framework identifies relationships but does not establish causation or dictate the right design. Do not assume every element has equal urgency. Use the Star Model for controllable design choices and ADKAR for individual adoption barriers.

Source: [McKinsey, Enduring Ideas: The 7-S Framework, A New Operating Model for a New World](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/a-new-operating-model-for-a-new-world).

[Shopify's production engineering team](https://shopify.engineering/why-shopify-moved-to-the-production-engineering-model) describe friction between deployment and runtime ownership. Trace one failure through the handoff. Change the decision right or capability that failed before proposing changes across every dimension.

<a id="star-model"></a>

## star-model: Galbraith Star Model

Supports: organization-design, people-operations, cross-functional-delivery.

Context: work.domain=organization, org.scope, role.authority, operating.maturity.

Decision trigger: Leaders are redesigning an organization around a strategy and need more than a new chart.

Inputs and evidence: Strategy-derived design requirements, decision and information flows, current structure, rewards, talent, and delivery constraints.

Procedure: Translate strategy into design requirements. Compare structure choices, then design lateral and vertical processes, rewards, and people policies that support the chosen structure. Examine how the five design areas reinforce or conflict. Pilot consequential interfaces and verify behavior against the strategic need.

Output: A coherent organization design with explicit trade-offs across strategy, structure, processes, rewards, and people.

Illustrative decision: A synthetic business adds customer-segment teams while retaining scarce specialists centrally. It specifies shared specialist priorities and team incentives so the structure does not create competing queues.

Failure conditions and alternatives: There is no universally correct org shape. Structure moves without process, reward, or people changes can preserve the old behavior. The Star Model is Galbraith's named framework. This text does not reproduce his diagrams or templates.

Source: [Jay R. Galbraith, The Star Model](https://jaygalbraith.com/wp-content/uploads/2024/03/StarModel.pdf).

[Microsoft's engineering realignment](https://news.microsoft.com/source/2015/06/17/microsoft-aligns-engineering-teams-to-strategy/) named executives for combined groups. After a reporting change, test who controls shared staffing and who answers for service failures. A public announcement establishes structure but cannot verify those operating changes.

<a id="operating-model"></a>

## operating-model: Operating model: integration and standardization

Supports: organization-design, business-model, decision-rights.

Context: work.domain=organization, org.scope, company.product_maturity, operating.maturity, role.authority.

Decision trigger: Business units must decide what to share, standardize, or keep independent.

Inputs and evidence: Customer and data dependencies, process similarities, local variation, economies of sharing, strategy, and existing governance.

Procedure: Distinguish process integration from process standardization. Compare diversification (low/low), coordination (high integration/low standardization), replication (low integration/high standardization), and unification (high/high). Choose requirements by scope, then specify data, process, decision, and platform ownership. Compare transition cost and what useful local variation would be lost.

Output: An operating-model choice by defined scope with shared standards, local discretion, and ownership.

Illustrative decision: A synthetic group needs a shared customer view across distinct services but different delivery processes. Coordination is a candidate. Mandating identical delivery workflows would be a separate decision requiring evidence.

Failure conditions and alternatives: This is the Ross, Weill, and Robertson enterprise-architecture lens, not a complete org-design taxonomy. One firm may have different models at different scopes. Pair with Star Model and explicit decision rights.

Source: [MIT CISR, Jeanne Ross, Operating Models teaching material](https://ocw.mit.edu/courses/15-571-generating-business-value-from-information-technology-spring-2009/147d6ab54c2bc472b0bd57a8d9ac67bd_MIT15_571s09_lec03.pdf).

[Intercom's onboarding designers](https://www.intercom.com/blog/designing-modular-user-onboarding) retained product contributions while standardizing common patterns. Decide which fields or steps must match everywhere and which local owners may change. Verify the full customer journey across both.

<a id="adkar"></a>

## adkar: ADKAR individual change

Supports: people-operations, organization-design, cross-functional-delivery.

Context: work.domain=organization, operating.maturity, org.scope, role.authority.

Decision trigger: A defined organizational change is not becoming normal individual behavior.

Inputs and evidence: Affected groups, awareness of need, willingness, knowledge, demonstrated ability, and incentives or reinforcement.

Procedure: For each affected group assess Awareness, Desire, Knowledge, Ability, and Reinforcement. Locate the earliest material adoption barrier and address its cause. Distinguish knowing instructions from being able to perform in real conditions. Verify sustained behavior and reinforce it through management practice and feedback.

Output: A targeted adoption plan and observed evidence of changed behavior.

Illustrative decision: A synthetic team attended system training but cannot complete tasks because permissions are missing. Another presentation does not address the ability barrier. Fix access and test task completion before calling adoption complete.

Failure conditions and alternatives: Resistance can reflect a poor change, conflicting incentives, missing capacity, or lost authority. Do not diagnose individuals as the problem by default. Use 7-S or Star Model when the organizational design itself is inconsistent.

Source: [Prosci, Use the ADKAR Model for Change Success](https://www.prosci.com/blog/adkar-model).
[Spotify's migration leads](https://engineering.atspotify.com/2020/06/tech-migrations-the-spotify-way) gave teams migration visibility and sequenced competing work. Before diagnosing resistance, check whether the team has capacity and a usable migration path. Test adoption again after removing that obstacle.

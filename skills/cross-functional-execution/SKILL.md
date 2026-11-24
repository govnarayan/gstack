---
name: cross-functional-execution
description: Make internal initiatives executable across functions, clarify decision rights, and prepare scenario responses. Use for shared dependencies, launch or operating readiness, systems and process improvements, contested decisions, or delivery without a natural owner. Does not assume functional authority or replace specialist incident response.
metadata:
  capabilities: [cross-functional-delivery, decision-rights, scenario-response, risk-governance, program-management]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - role.authority=decision_owner|delegated_owner|influence_without_authority|coordinator
      - work.domain=cross_functional_delivery|decision_support|strategy|risk_and_controls
    adapts_by:
      - org.stage
      - org.size_band
      - org.public_status
      - org.scope
      - company.archetype
      - company.product_maturity
      - company.go_to_market_motion
      - operating.maturity
      - governance.regime
      - data.sensitivity
      - task.consequence
    excluded_when:
      - Investor Relations ownership or ownership of another staffed function is the assignment
      - The assignment is outside US venture-backed startups or US public companies
---

# Cross-functional execution

Turn a priority into a shared outcome, an authorized owner, committed dependencies, evidence of completion, and a permanent operating home. The strongest argument against central coordination is that it can duplicate functional leadership and make the operator the bottleneck. Use it where a real dependency, decision, readiness gap, or unowned outcome needs a common view.

Read [delivery and decision methods](references/delivery-and-decisions.md) for initiative scoping, authority, dependencies, operational readiness, systems improvement, and handover. Read [scenario response](references/scenario-response.md) for compound risks, triggers, response choices, and learning after an event. See [source credits](../../SOURCES.md) for methodological influences.

For an acquisition, separation or major operating transition, use [transitions and continuity](references/transitions-and-continuity.md). It makes process choices by current, interim and end state and reconciles temporary service direction and exit dependencies. It distinguishes standalone, one-time and stranded costs and protects customer continuity before optional growth.

Use [commercial operating interfaces](references/commercial-operating-interfaces.md) when account ownership, coverage, incentives, brand or customer-service choices must fit together across functions. Functional owners retain the decisions while the operator builds and verifies the joined plan.

Use [growth-barrier removal](references/growth-barrier-to-decision.md) when no function owns the whole blocked customer outcome. Compare competing causes and interventions, take a bounded operating assignment, reconcile scarce capacity, escalate before the last useful decision and verify customer use before transferring ownership.

A program is several projects and operating changes that must land together. For one, use [program management](references/program-management-system.md) to choose the approach and tools and to set up the context, people, authority, artifacts and cadence. Use [decision rights](references/decision-rights-rapid-raci.md) to choose RAPID, RACI, DACI or a single owner by situation, because they solve different problems. The [worked program](references/worked-program.md) completes every artifact for one synthetic launch, and `python scripts/program_check.py examples/usage-pricing-program.json` recomputes its schedule, capacity, logs and options.

For work with a fixed date or shared service capacity, execute the [schedule, readiness, and response case](references/worked-delivery.md). It calculates the dependency path, rollout limit, latest useful trigger and control evidence, then produces a decision and handover. Replace its synthetic inputs with the actual owners' evidence rather than borrowing its thresholds.

## Decide what is missing

1. An unclear result needs a success test and scope, not merely a tracker.
2. Disputed decisions need an explicit authority path, affected functions, evidence, and deadline. Meeting attendance is not consent.
3. Committed dates with uncommitted dependencies need reconciliation and feasible alternatives.
4. Launches and process changes need service capacity, quality, support, systems, and handover readiness alongside delivery milestones.
5. Uncertain events need observable triggers and response owners. Do not wait for a scenario model to resolve an active incident.

## Adapt to mandate and scale

At a small startup, leadership may explicitly delegate hands-on coordination, systems work, customer support improvements, or an operational task. State whether the mandate is temporary or continuing. In a public company or scaled business unit, work through established functional owners and approval routes. Do not infer permission to make legal, HR, financial, security, disclosure, or technical decisions.

For a coordinator or an operator influencing without authority, make choices reviewable and escalate conflicts to the authorized sponsor. For a delegated owner, record the boundaries within which they may act. If a committee or board is the authorized decider, record its actual approval requirements rather than imposing a single-person model.

Cross-functional priorities can include work without a natural home. Keep them connected to strategic direction and ongoing operations. When a launch consumes shared capacity, compare service demand, specialist coverage, and delivery commitments. A separate tracker or staffing floor needs evidence that it protects service under the expected load.

## Operating risk coordination

Keep material operating risks, control owners, evidence gaps, accepted risk, escalation, and remediation visible. For an audit or control dependency, coordinate scope, owner, evidence freshness, deadlines, and closure tests with the responsible function. Functional experts interpret obligations and judge control sufficiency. An internal tracker does not certify compliance. The response reference includes the control and evidence record.

## Completion standard

Another stakeholder can explain the outcome, owner, next dependency, decision needed, operational risks, and evidence required to finish. Closure includes acceptance, remaining risks, ongoing ownership, and a review of whether the intended result occurred. Record recommendations, tentative proposals, authorized decisions, and verified results distinctly.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Sequence work against available people to establish the earliest feasible finish. [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g)
2. Identify the actual approver and latest safe decision date so the critical dependency can move. [Atlassian DACI](https://www.atlassian.com/team-playbook/plays/daci)
3. Replay the handoff with the receiver and record the acceptance evidence. [Application](references/program-management-system.md)

## Connections

- [Weekly reviews](../operating-cadence/SKILL.md). Send the weekly pack with the blocked item, owner or decision due to the review owner.
- [Executive support](../executive-support/SKILL.md). Send the executive brief with the options and consequence of delay to the chief of staff.
- Use [stakeholder alignment in a matrix](references/stakeholder-alignment-in-a-matrix.md) when reporting lines divide authority.

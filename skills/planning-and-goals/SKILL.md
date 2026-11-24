---
name: planning-and-goals
description: Turn company or team strategy into an annual or rolling plan, goals, and funded priorities. Use for planning cycles, OKR design, competing initiatives, or plans that exceed capacity. Does not replace strategy formation or specialist financial modeling.
metadata:
  capabilities: [annual-plan, goals-and-okrs, portfolio-priorities]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=planning|resource_allocation
    adapts_by:
      - org.stage
      - org.size_band
      - org.public_status
      - org.scope
      - company.archetype
      - company.product_maturity
      - company.go_to_market_motion
      - role.authority
      - operating.maturity
      - governance.regime
      - data.sensitivity
      - task.consequence
    excluded_when:
      - Investor Relations ownership or ownership of another staffed function is the assignment
      - The assignment is outside US venture-backed startups or US public companies
---

# Planning and goals

Build a feasible plan and keep it useful through execution. Objectives and key results (OKRs) describe a desired change and the evidence of progress. They do not choose the strategy, fund the work, or resolve conflicts by themselves. The strongest case against formal OKRs is that a team still discovering the right problem can become efficient at pursuing the wrong target.

## Start with the decision

Read the current strategy, resource plan, goal list, service obligations, and latest review before proposing substantive changes. Recap what those sources ask for separately from recommendations. Ask only for missing inputs that could change the approach. These include the decision due, company and team scope, product maturity, actual bottleneck, obligations and who can approve a trade-off. State what is missing rather than inventing a baseline.

Consider direction, goal form, capacity, measurement, and follow-through separately. A tracking failure can arise from an unsupported goal, missing authority, excessive process, or no feasible delivery path. Do not prescribe a new tool before identifying the failure.

## Execute the planning cycle

1. Establish the strategic choice and evidence that would invalidate it. Read [planning methods](references/planning-methods.md) for the upstream layers, annual or rolling plans, and resource arbitration.
2. Choose the kind of commitment appropriate to the uncertainty. Read [goal design and management](references/goal-design.md) for outcome, learning, dependency and delivery goals, target construction, coherent scoring, and change control.
3. Translate the choice into funded initiatives and actual team contributions. Reconcile obligations and shared specialist time before calling the goals committed.
4. Prepare the plan and goal records using [the planning pack](templates/planning-pack.md). For a narrow request, fill the relevant section. Do not create every artifact automatically.
5. Inspect progress through [operating cadence](../operating-cadence/SKILL.md). Close each cycle against its original commitments, then choose what continues, changes, waits, or stops.

Use the [worked planning example](examples/onboarding-plan.md) to see the full chain, including rejected alternatives and a mid-cycle capacity shock. Its follow-through appears in the operating-cadence example. All example numbers are synthetic.

## Adapt the machinery

When the company already uses V2MOM or another planning system, read [native planning and V2MOM](references/native-planning-and-v2mom.md). Preserve its ranked choices, obstacles, measures and change rights. An OKR view uses the same underlying commitments rather than creating a competing plan.

For a founder-held startup, one shared document can hold direction, current bets, operating obligations, and decision history. Add team-level goal sets only when they resolve a coordination problem the shared set cannot. There is no universal headcount threshold or required objective count.

For a multi-unit or matrix organization, distinguish outcome ownership, control of resources, dependency acceptance, and tie-breaking authority. At public-company scope, work within the established Finance, functional, and governance calendar. A local goal change does not amend an approved budget or an external commitment.

For research, infrastructure, consumer, enterprise, and AI-dependent work, inspect the actual evidence window and dependencies. Different parts of one company can use different clocks. A capability milestone can trigger a review without replacing all calendar commitments.

## Completion standard

Deliver the recommendation, strongest alternative, and condition that would change the choice. Include strategic rationale, funded and rejected work, resources by period and scarce skill, and accepted dependencies. Specify exact goal definitions, baseline and target evidence, original dates, owners, approval status, review rhythm and revision triggers. Run the supplied inputs through the procedure. Demonstrate at least one rejected infeasible or misleading case before claiming the method works.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Name an observable signal and an owner so activity cannot stand in for customer value. [Atlassian goals, signals and measures](https://www.atlassian.com/team-playbook/plays/goals-signals-measures)
2. Compare the funded initiative with continuing current work to identify what loses resources. [Green Book](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026)
3. Review the funding premise even when delivery is on schedule. [Application](references/goal-design.md)

## Connections

- [Weekly reviews](../operating-cadence/SKILL.md). Send the goal contract with its version and source to the review owner.
- [Cross-team delivery](../cross-functional-execution/SKILL.md). Send the program tracker with the accountable owner and approver to the program lead.
- [Workforce design](../organization-and-change/SKILL.md). Send the workforce plan with the role, manager and funded start date to the workforce planning owner.

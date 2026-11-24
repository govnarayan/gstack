---
name: organization-and-change
description: Diagnose and design responsibilities, team interfaces, leadership capacity, workforce plans, and organizational change for internal Strategy & Operations, BizOps or Chief of Staff work. Use for organization design, role clarity, management support, hiring and onboarding design, and change adoption, with People and functional owners where staffed.
metadata:
  capabilities: [organization-design, people-operations, operating-model-design]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=organization
      - role.authority
    adapts_by:
      - org.stage
      - org.size_band
      - org.scope
      - org.public_status
      - company.product_maturity
      - operating.maturity
      - governance.regime
      - data.sensitivity
      - task.consequence
    excluded_when:
      - employment-law advice or independent ownership of staffed HR functions
---

# Organization and change

Design teams around the work the company needs to do. Clarify what each team owns, where it depends on others and whether managers have the capacity to lead. Check whether the new design solves the original problem.

## Diagnose the actual problem

Read the strategy, work and ownership map, recent decisions, staffing plan, and affected teams' accounts before recommending a structure. Distinguish the overall company's stage and size from the team or business unit served. Identify the sponsor, decision authority, affected functional owners, budget constraint, and operating maturity.

Separate five possible causes: unclear direction, poor interfaces or decision rights, insufficient capacity or capability, management behavior, and a mismatch in grouping or reporting lines. Use real stalled work, duplicate effort, repeated escalations, overloaded managers, and customer or operating consequences as evidence. A complaint about an organization chart does not establish that a reorganization is the remedy.

Describe the problem in the user's terms and compare the smallest intervention that could fix it with a broader structural change. State the strongest case for keeping the current organization, its opportunity cost, and the condition that would make change worthwhile. Avoid diagnosing named individuals from a metric or secondhand account.

## Make responsibilities and interfaces explicit

Define the outcome and recurring work first, then accountable owners, decision rights, dependencies, and escalation. Test whether the owner has the information, capacity, and permission to deliver. Shared participation need not mean shared final authority. For a matrix, specify who decides priorities, assigns capacity, evaluates performance, and resolves conflict.

Keep shared direction, current priorities, and ongoing operating obligations visible. Distinguish internal operating responsibilities from external commercial responsibilities. During a major launch, test how shared capacity will cover ongoing services rather than assuming a staffing floor protects them under every demand scenario.

For role redesign, specify scope, expected outcomes, reporting relationship, authority, required capability, interfaces, and success evidence before choosing the title. When a generalist temporarily fills a gap, define the transfer trigger. A staffed function should not become a parallel CoS department.

## Compare design choices

Read [organization choices and workforce planning](references/organization-and-workforce.md) for functional, product or segment, matrix, manager-capacity, and staffing decisions. Read [management support and change](references/management-and-change.md) for hiring design, onboarding, feedback, culture, and implementation.

Use [operating model design](references/operating-model-design.md) when strategy needs enterprise, functional and team choices about capabilities, authority, delivery and value preservation. It separates capability differentiation and business-specific context from shared standards, location and reporting lines, then produces a decision record tested on actual work.

The [operating model case](references/operating-model-worked-case.md) runs the whole sequence for two business lines on one platform. The sequence covers diagnosis from traced value flows, options, capability placement, current, interim and target states, a service agreement, securing agreement, implementation and annual review. The case separates the operating model from the org chart and the meeting cadence. The [org design case](references/org-design-worked-case.md) then sizes work and reads span and layer flags. It sequences hiring, costs the transition, writes role profiles and an interface agreement, and tests a pooled-versus-dedicated staffing conflict. Recompute it with `python scripts/org_design_check.py --roster examples/org-roster.csv --plan examples/org-design-plan.json`.

Read [operating model choices and evidence](references/operating-model-choices-and-evidence.md) to choose a lens before designing. It compares the main frameworks and sets out the standardization and integration choice. It also covers grouping by interdependence, product and self-managed models, the management system, AI-era claims and the evidence.

Read [structure choices and evidence](references/structure-choices-and-evidence.md) before recommending a structure. It covers functional versus general-manager designs, team types and interaction modes, Conway's law, ownership and duplication, and what reorganization surveys show.

For a consequential recommendation, use [the diagnosis and transition case](references/diagnosis-and-transition-case.md) to turn work episodes into competing causes. It replays capacity and disputed authority, populates the interface record, and tests observed adoption. It demonstrates the complete chain, including the point at which pooling stops fitting. Adapt its method, never copy its synthetic inputs or thresholds.

Keep the current arrangement as an option. Compare plausible alternatives against the named problem, decision speed, expertise, coordination burden, duplicated cost, leadership capacity, and transition disruption. These are decision dimensions, not an automatic weighted score. Show the trade-offs and the uncertainty that changes the recommendation.

Design beyond reporting lines: recurring outputs, shared services, escalation, resource commitments, manager expectations, and how teams learn the business context. Test the proposal on a real piece of work crossing the affected boundary. Name who would decide each disputed point and what would happen when capacity is exhausted.

## Adapt to company and served scope

| Context | Design implications |
|---|---|
| Under 20 or finding product fit | Direct coordination and broad roles can work. Make a few consequential ownership boundaries clear. Specialization can still be essential where expertise is central to the product or risk. |
| 20–60, emerging | Examine where informal context stops reaching people. Introduce managers, written expectations, or interfaces only for demonstrated load and coordination gaps. Funding stage alone does not prescribe the structure. |
| 61–300, repeatable | Develop managers, hand off generalist work, define shared-service obligations, and reconcile hiring with actual capacity. Avoid importing layers solely to provide promotions. |
| 301–5,000 or 5,001+, multiple units | Local optimization can impose costs elsewhere. Map enterprise constraints, shared platforms, geographic interfaces, and competing resource owners. A unit-level sponsor may lack company-wide authority. |
| Public or scaled-governed | Work through People, Finance, Legal, Communications, and functional leaders. Support design, evidence, coordination, and management decisions within the assigned mandate. Do not assume HR, compensation, accounting, legal, or disclosure ownership. |

Headcount bands are prompts to inspect load, not verified thresholds at which everyone needs a layer, a meeting, or a matrix. Change the recommendation when measured coordination or manager capacity crosses the company's own acceptable limit, not when a generic benchmark is reached.

## Limits and completion evidence

Small startups may explicitly delegate functional work to a generalist. Keep specialist judgment and approvals attached where required. Do not create employment terms, compensation promises, separation plans, investigations, or legal conclusions from generic source advice. At a staffed company, the responsible function owns those decisions and records.

Protect personal information and avoid exposing identifiable survey or feedback results to an audience that cannot use them appropriately. Do not promise anonymity a small group cannot provide. Separate approved role changes from proposals and recommendations.

Before calling a design successful, observe its use on actual work. Check whether the target problem improved, authority held under pressure, ongoing services remained healthy, and affected people can operate with the new responsibilities. If it failed, distinguish an unsound design from missing capacity, a leader bypassing it, or an incomplete transition. An announcement, org chart, or completed training does not establish adoption.

See [source credits](../../SOURCES.md) for methodological influences. Staffing and management judgments require evidence about the actual work and people.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Compare perceived and actual owners of a recent failure so a redesign addresses an observed problem. [Atlassian roles and responsibilities](https://www.atlassian.com/team-playbook/plays/roles-and-responsibilities)
2. Check whether the person can perform the new work and receives reinforcement so adoption can be verified. [Prosci ADKAR](https://www.prosci.com/methodology/adkar)
3. Replay an exception and inspect who can commit scarce staff, funds and decisions. [Application](references/operating-model-design.md)

## Connections

- [Talent](../talent-and-hiring/SKILL.md). Send the role scorecard with outcomes, authority and proposed level to the hiring manager.

---
name: company-context
description: Establish or update the company, team, role, and decision context needed for internal Strategy & Operations, BizOps or Chief of Staff work. Use when the operating problem or mandate is unclear, or advice must adapt to company size and stage.
metadata:
  capabilities: [company-context]
  context:
    required: [market.jurisdiction, role.mandate, org.scope]
    adapts_by: [org.stage, org.size_band, org.public_status, company.archetype, company.product_maturity, company.go_to_market_motion, role.authority, operating.maturity, governance.regime]
    excluded_when: ["market.jurisdiction!=US"]
---

# Company context

Establish enough verified context to make the requested decision. Read existing project state and source material before asking for information. Continue useful work with explicit assumptions when a missing field does not change the decision.

The current GStack scope is US venture-backed startups and US public companies. Funding stage and headcount are separate. The size of the served team is separate from company headcount. A title does not establish function breadth or authority.

## Context that changes the answer

First read the conversation, remembered context, project files and current company record. Check which facts are dated and which refer only to one team.

Next read the company's own product materials, financing announcements, filings and recent changes. Where it matters, check the public role and remit of the people involved.

Record what each source actually establishes. A financing announcement dates a round. It cannot establish today's cash balance, and a company headcount cannot establish the team's capacity.

Establish who is asking. A candidate can test a public hypothesis in an interview. A consultant needs sponsor confirmation. An employee may have direct access and still lack approval authority.

State a short baseline before advising. Name the company, date, scope, requester, decision owner, evidence and the one uncertainty most likely to change the answer.

Ask only questions that remain consequential after that work. If the requester cannot access an internal fact, give the bounded public conclusion and identify how it could be tested.

Record the operating question in the user's terms, its decision owner, and what action the answer is meant to support. Identify:

- Company stage, company headcount, served scope, and operating maturity.
- Product maturity and commercial motion. A research program, an enterprise sales business, and a self-service product need different evidence.
- What the operator owns, advises on, coordinates, or escalates. Record budget, hiring, priority, and information-access rights when relevant.
- Existing strategy, plans, metrics, forums, functional owners, and constraints. Identify what is already working before proposing new structure.
- Current performance, near-term commitments, capacity constraints, and the change that prompted the task.

Use the vocabulary in [context record](references/context-record.md). Do not force every field into every task. Unknown values stay unknown. Never infer revenue, runway, founder psychology, or performance from a stage label, headcount, or conversational style.

Use [diagnosis and worked case](references/diagnosis-and-worked-case.md) when the request jumps from a symptom to a proposed management fix. It shows how to distinguish authority, capacity, information, and strategy problems using actual work, select the next useful evidence, and make a bounded recommendation. Its synthetic case produces a decision brief rather than a completed company questionnaire.

## Adapt to the actual organization

At a small startup, leadership may delegate work spanning several unstaffed functions. Clarify the delegation and the immediate outcome. Avoid building a management system ahead of a demonstrated coordination problem.

At a scaling company, inspect interfaces between teams, managers, resources, and decisions. Add structure where missing coordination is causing observable delay, rework, conflict, or risk.

At a public company, identify the business unit, function, initiative, and executive sponsor. Work with established Finance, HR, Legal, Product, Engineering, and other owners. Internal CoS/S&O support does not confer Investor Relations or other functional ownership.

## Evidence and maintenance

For consequential context, record source, date, scope, and whether it is observed, reported, inferred, or proposed. Refresh a field when the decision depends on information that may have changed. Do not apply a fixed expiry period to every fact.

When sources disagree, preserve the competing statements and identify the canonical source or owner that can resolve them. A newly mentioned estimate does not automatically supersede an approved plan or verified record.

Update durable company context only within the user's authorized task. Preserve the user's wording when recording their statements. Keep recommendations distinct from their stated preferences.

## Useful output

Give the operating question, relevant context, mandate, constraints, and material unknowns in a short decision brief. If the context itself exposes a problem, explain its mechanism and what evidence would distinguish competing diagnoses. Do not turn missing documentation alone into a diagnosis of poor management.

See [source credits](../../SOURCES.md) for methodological influences.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Check the served population and constraints so the baseline has a scope. [GOV.UK discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
2. Verify responsibility against a real approval so a title cannot substitute for authority. [Atlassian roles and responsibilities](https://www.atlassian.com/team-playbook/plays/roles-and-responsibilities)
3. Date the record and identify which unverified claim could reverse the decision. [Application](references/diagnosis-and-worked-case.md)

## Connections

- [Problem solving](../workplace-problem-solving/SKILL.md). Send the company record with the requester, served scope and verified authority to the assignment sponsor.

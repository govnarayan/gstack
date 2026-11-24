---
name: financial-resource-decisions
description: Model financial outcomes, cash runway, budgets, unit economics, headcount, and resource trade-offs for internal Strategy & Operations, BizOps or Chief of Staff decisions. Supports delegated startup analysis and collaboration with Finance rather than accounting, controller, or Investor Relations ownership.
metadata:
  capabilities: [financial-resource]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=finance|resource_allocation|decision_support
    adapts_by:
      - org.stage=seed|series_a|series_b_c|series_d_plus|pre_ipo|public|unknown
      - org.size_band=under_20|20_60|61_300|301_5000|5001_plus|unknown
      - org.public_status=private|public|unknown
      - org.scope=whole_company|business_unit|function|initiative_or_portfolio
      - company.archetype=frontier_ai_lab|ai_product|ai_infrastructure|ai_physical_systems|b2b_saas|other_technology
      - company.product_maturity=pre_pmf|finding_fit|post_pmf|scaling_product|multi_product|unknown
      - company.go_to_market_motion=enterprise_sales|product_led|consumer|marketplace|platform_or_ecosystem|hybrid|unknown
      - role.authority=decision_owner|delegated_owner|influence_without_authority|coordinator
      - operating.maturity=founder_held|emerging|repeatable|scaled_governed
      - governance.regime=venture_private|public_company|regulated
      - data.sensitivity=public|internal|confidential|restricted|unknown
      - task.consequence=reversible|material|high_impact|unknown
    excluded_when:
      - market.jurisdiction!=US
---

# Financial resource decisions

Decide what the company can afford and what it should fund. Use the forecast, budget and available capacity to compare investments and show which assumptions would change the decision.

Establish the choice, scope, period, available cash or budget, constraints, accountable Finance partner, and decision rights. Read current actuals, definitions, contracts and commitments, approved plan, and existing models first. Reconcile versions before creating another view.

Read [models and financial analysis](references/models-and-financial-analysis.md) for assumptions, forecasting, variance, cash, and model checks. Read [resource and economic choices](references/resource-and-economic-choices.md) for unit economics, headcount/capacity, business cases, and sensitivities. Read [context and authority](references/context-and-authority.md) when stage, size, maturity, scope, or governance changes the method. [Source credits](../../SOURCES.md) identify methodological influences.

Read [value realization](references/value-realization.md) when claimed savings, added contribution, acceleration or released capacity determine the case, or when checking results after implementation. Separate already-planned improvements from incremental benefits, remove overlap, reconcile lost benefits and actual costs, and preserve the original case, current forecast and observed result in a line-level register.

For a resource commitment, work through [the linked cash and capacity case](references/cash-and-capacity-case.md). Demand and ramp constrain completion, which drives economics. Reconcile revenue to collections. Compare alternatives against the same service obligations. Reproduce the low point and decision breakpoint before adapting it. Its synthetic inputs are not defaults for a live model.

In a small startup, perform explicitly delegated analysis and financial preparation. At a public company, partner with established Finance and functional teams. Accounting policy, close, treasury execution, tax, legal terms, compensation approval, corporate disclosure, and Investor Relations remain with their owners. This skill may prepare inputs or coordinate a decision when assigned. It does not confer authority over those functions or offer personal investment advice.

Present the recommendation, strongest objection, alternatives, incremental cash and economic effects, decision-sensitive assumptions, evidence gaps, and condition that would reverse the choice. Make all headline results reproducible from stated inputs. Never replace a missing value with a source's example, hide a financing assumption in base cash, or label a benchmark breach a verdict.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Trace cost assumptions to baseline quantities and dates so the estimate can be reconciled with actuals. [GAO Cost Guide](https://www.gao.gov/products/gao-20-195g)
2. Compare alternatives and forgone benefits so the cheapest option does not win by default. [Green Book](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026)
3. Hold contracts constant and move collections to isolate a financing benefit from operating improvement. [Application](references/cash-and-capacity-case.md)

## Connections

- [Planning](../planning-and-goals/SKILL.md). Send the plan with approved spending and roles to the planning lead.
- [Financial decisions](SKILL.md). Send the cash forecast with its minimum balance and date to the treasury owner.
- [Financing](../fundraising-and-capital/SKILL.md). Send the financing plan with the latest start and minimum primary proceeds to the CEO and finance lead.

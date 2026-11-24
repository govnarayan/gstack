---
name: product-and-market
description: Assess customer problems, market evidence, product direction, roadmaps, and delivery briefs for internal Strategy & Operations, BizOps or Chief of Staff work. Use for product investment and execution decisions rather than corporate strategy or technical implementation.
metadata:
  capabilities: [customer-problem, market-competitive, product-direction, product-delivery]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=product_and_market|cross_functional_delivery
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

# Product and market

Use customer and market evidence to decide which problems to solve, what to build and what the team should test before committing.

Identify the decision, served scope, product maturity, evidence available, and decision owner. Read existing research, product commitments, and constraints before proposing changes. Distinguish who uses the product, who pays, who approves, and who bears implementation risk. A founder title or a public-company employer does not settle these questions.

Read only the relevant references:

1. [Discovery](references/discovery.md) for customer problems, evidence synthesis, competing solution hypotheses, and tests before investment.
2. [Market evidence](references/market-evidence.md) for segmentation, market sizing, competitive alternatives, and the limits of each conclusion.
3. [Direction and delivery](references/direction-and-delivery.md) for product outcomes, roadmap trade-offs, briefs, requirements, acceptance, launch, and retirement.
4. [Context and authority](references/context-and-authority.md) when company stage, served scope, product maturity, commercial motion, or role authority changes the method.
5. [Opportunity screening and diligence](references/opportunity-screening-and-diligence.md) for an available shortlist, critical evidence tests, changed commitments and value obligations when sourcing an external capability or opportunity.
6. [Source credits](../../SOURCES.md) for methodological influences.

For an investment or cross-team release decision, apply [the evidence-to-release case](references/investment-to-release-case.md). It carries a consumer AI decision through observations, alternatives, a failed cost condition, a smaller commitment, requirements, and a subsequent test. Its hardware, marketplace, infrastructure and platform variants change the actual evidence and capacity calculation. Use the relevant variant and replace all synthetic inputs.

Keep customer evidence, product choices, and corporate choices separate. A large market does not establish demand for this product. A feature request does not establish the problem or its priority. Product recommendations must fit stated company choices. Escalate a proposed change to company direction as a distinct leadership decision with its own trade-offs.

An explicitly delegated operator in a small company may conduct discovery, write product records, and coordinate a launch. At a public company, work with Product, Design, Engineering, Sales, Finance, and relevant control owners within their mandates. Technical feasibility, system design, specialist research, and production testing remain specialist inputs. Do not infer functional ownership from this skill.

Deliver the requested artifact with evidence, assumptions, alternatives, non-goals, dependencies, owner, and the next decision or test. Describe what would reverse the recommendation. Do not call a hypothesis validated because it has a polished document, a numerical score, or simulated users.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Trace the problem through the current service before approving the build. [GOV.UK discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)
2. Observe the workaround of someone excluded from today's service to catch a missing requirement. [GOV.UK user research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery)
3. Compare activated users with all starters and subsequent paid use before scaling. [Application](references/discovery.md)

## Connections

- [Commercial operations](../commercial-strategy/SKILL.md). Send the offer record with the eligible segment and price to the commercial lead.

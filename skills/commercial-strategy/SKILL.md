---
name: commercial-strategy
description: Diagnose commercial growth and evaluate positioning, distribution, conversion, retention, pricing, and packaging for internal Strategy & Operations, BizOps and Chief of Staff decisions. Supports delegated startup execution and collaboration with staffed commercial functions.
metadata:
  capabilities: [commercial-growth, pricing-monetization]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=product_and_market|business_model
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

# Commercial strategy

Choose the commercial investment that best advances the stated business outcome within the resource constraint. Build the analysis, model, and experiment needed to act. A list of acquisition, retention, and pricing ideas is not a recommendation.

## Establish what growth means

Identify the counted unit, objective, horizon, customer population, and available capacity. Paid members, active users, revenue, retained contribution, and a particular plan's adoption are different outcomes. In a membership business, a tier upgrade or family invitation need not create a new paying subscription.

State a working objective when the prompt is broad and continue with explicit assumptions. Ask only for missing information that changes the choice. Separate observed company data, user-supplied assumptions, public facts, and hypotheses. Do not invent an internal funnel or an expected lift.

Make the customer's alternatives explicit: free/default behavior, doing nothing, substitutes, competing offers, and existing bundles where relevant. State why the selected customer would switch or pay. Missing customer evidence is a research question, not permission to assume that a feature bundle creates demand.

## Build a coherent growth argument

1. Reconcile the business. Build opening-to-closing customer and revenue bridges, with definitions, cohorts, denominators, and measurement windows. Explain gains, losses, tier movements, and mix separately.
2. Diagnose the constraint. Compare weak customer fit, insufficient relevant reach, conversion friction, failed first value, poor retention, service problems, and uneconomic usage. Identify evidence that distinguishes these explanations.
3. Compare investments. Define each intervention's population, mechanism, incremental effect, lag and retained economics.

   Record one-time and ongoing cost, dependencies and displaced work. Include the strongest alternative and keeping the current approach.
4. Select conditionally. Make the recommendation under the stated objective and name the evidence or threshold that reverses it. Keep a subscriber-count result distinct from an upgrade or price result.
5. Design the proof. Define eligibility, assignment, exposure, customer outcome, contribution, guardrails, duration rationale, owner, and stop/expand conditions. Attribution and a before/after chart alone do not establish incrementality.

The [framework selector](../../frameworks/README.md) helps choose a method for the disputed business question. Use the method to change the decision rather than complete a collection of canvases.

## Choose the relevant operating method

| Decision | Read | Produce |
|---|---|---|
| Grow a consumer membership or subscription bundle | [Subscription growth](references/subscription-growth.md) | Paid-membership bridge, job/state segmentation, competing growth bets, cohort economics, and causal test |
| Diagnose acquisition, activation, retention, or enterprise pipeline | [Growth and commercial operations](references/growth-and-commercial-operations.md) | Bottleneck diagnosis, cohort/funnel analysis, capacity reconciliation, and investment choice |
| Select distribution, field enablement, or release support | [Channel and enablement choices](references/channel-and-enablement-choices.md) | Reach and incrementality model, channel/offer alternatives, readiness decisions, and test |
| Make a partner relationship deliver commercial value | [Partnership operating model](references/partnership-operating-model.md) | Reciprocal commitments, capability evidence, activation, retained economics, operating ownership and exit conditions |
| Activate parent or sibling-unit distribution | [Parent distribution activation](references/parent-distribution-activation.md) | Eligible customer population, product-overlap decision, working commercial handoff, group incrementality and delivery cap |
| Investigate intermittent purchasing or an account needing help | [Repeat purchase and account response](references/repeat-purchase-and-account-response.md) | Mature repeat-purchase cohorts, reason-coded investigation, account evidence and an owned response with incremental economics |
| Change price, charging unit, packages, or discounts | [Pricing and monetization](references/pricing-and-monetization.md) | Buyer evidence, paired economic scenarios, break-even, migration exposure, and rollout decision |
| Adapt to size, product maturity, motion, or authority | [Context and authority](references/context-and-authority.md) | Specific scope, owners, constraints, and operating adaptations |

## Make the calculations usable

Calculate retained customers and incremental contribution over the same horizon. Include acquisition cost, incentive/discount costs, partner or platform share, support, refunds, and variable service costs where relevant. Separate average economics from the next increment of spend. For AI offers, inspect heavy-user costs and successful task value rather than only tokens or feature adoption.

For a narrow constant-rate comparison, the [subscription cohort calculator](scripts/subscription_cohorts.py) accepts a case file and produces monthly counts and contribution. The [synthetic example](examples/subscription-growth.json) demonstrates a count objective favoring retention while a contribution objective favors acquisition. Its assumptions are explicit and are not a company forecast. Use a full cohort model when billing, margin, survival, or treatment interactions vary.

A senior operating deliverable includes the data table or query specification, recomputable model, decision brief, and experiment/implementation record needed for the assignment. Do not stop at asking Marketing or Finance to perform the analysis. Where inputs are missing, construct the model with visible blanks and identify which missing value changes the recommendation.

When a cohort result determines the choice, include its compact definition contract in the brief. Specify counted identity, origin, fixed eligibility/segment, paid or value event, tenure/window, mature denominator, missing/pending treatment and source cutoff. A promise to inspect cohorts or a list of requested fields is not that completed contract. Use the [cohort specification](../operating-cadence/references/cohort-deep-dives.md) for the full analysis.

## Scope and completion

An operator can research, model, draft, test, and execute explicitly delegated work. At a staffed company, collaborate with Sales, Marketing, Customer Success, Product, Finance, and specialist owners within actual authority. Analysis does not authorize campaign spend, outreach, contract changes, or public pricing changes.

Before delivery, test for double-counting, denominator changes, overlapping audiences, selection effects, cannibalization, capacity limits, and improvement that vanishes after discounts or service costs. Explain the strongest objection and the practical condition under which another investment wins. See [source credits](../../SOURCES.md) for methodological influences.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Require evidence of a buyer commitment before moving the forecast category. [GitLab commercial stages](https://handbook.gitlab.com/handbook/sales/commercial/comm-sales-opp-stages/)
2. Connect the buyer's job and current alternative to the offer so the stage reflects a viable sale. [Strategyzer Value Proposition Canvas](https://www.strategyzer.com/library/achieve-product-market-fit-with-our-brand-new-value-proposition-designer-canvas)
3. Reconcile cancellations already under notice with the renewal forecast. [Application](references/subscription-growth.md)

## Connections

- [Sales operations](references/sales-operations.md). Send the compensation plan with the revised credit basis and rate to the sales operations lead.
- [Financial decisions](../financial-resource-decisions/SKILL.md). Send the revenue forecast with bookings, mix and selling cost to the finance lead.
- [Weekly reviews](../operating-cadence/SKILL.md). Send the weekly pack with the slipped deal, amount and decision date to the revenue operations lead.
- Use [customer success](references/customer-success-playbooks.md) to review onboarding, renewals and escalations.

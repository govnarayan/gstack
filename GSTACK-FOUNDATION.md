# Company and role context

The same decision can call for a different approach at a seed startup and a public company. GStack adapts its guidance to the company, the team being served, and the operator’s authority.

Start with the operating question, the scope being served, and the operator's actual authority. A title alone does not establish what someone owns. Company headcount and served-team size can differ substantially.

## Context identifiers

| Identifier | Values |
|---|---|
| `org.stage` | `seed`, `series_a`, `series_b_c`, `series_d_plus`, `pre_ipo`, `public`, `unknown` |
| `org.size_band` | `under_20`, `20_60`, `61_300`, `301_5000`, `5001_plus`, `unknown` |
| `org.public_status` | `private`, `public`, `unknown` |
| `org.scope` | `whole_company`, `business_unit`, `function`, `initiative_or_portfolio` |
| `company.archetype` | `frontier_ai_lab`, `ai_product`, `ai_infrastructure`, `ai_physical_systems`, `b2b_saas`, `other_technology` |
| `company.product_maturity` | `pre_pmf`, `finding_fit`, `post_pmf`, `scaling_product`, `multi_product`, `unknown` |
| `company.go_to_market_motion` | `enterprise_sales`, `product_led`, `consumer`, `marketplace`, `platform_or_ecosystem`, `hybrid`, `unknown` |
| `market.jurisdiction` | `US` for the target company in this version of GStack |
| `role.mandate` | `strategy_and_operations`, `business_operations`, `chief_of_staff`, `special_projects` |
| `role.authority` | `decision_owner`, `delegated_owner`, `influence_without_authority`, `coordinator` |
| `operating.maturity` | `founder_held`, `emerging`, `repeatable`, `scaled_governed` |
| `governance.regime` | `venture_private`, `public_company`, `regulated` |
| `work.domain` | `strategy`, `planning`, `resource_allocation`, `business_model`, `performance_and_metrics`, `analytics`, `decision_support`, `executive_communications`, `cross_functional_delivery`, `organization`, `product_and_market`, `finance`, `technical_infrastructure`, `risk_and_controls` |
| `data.sensitivity` | `public`, `internal`, `confidential`, `restricted`, `unknown` |
| `task.consequence` | `reversible`, `material`, `high_impact`, `unknown` |
| `systems.connector` | A named platform or integration, such as `google_workspace`, `slack`, or a data warehouse. Connector requirements describe the tools a capability uses, not the company operating context. |

Stage, size, public status, and operating maturity are separate dimensions. Headcount bands help select relevant guidance. They do not establish a threshold at which a company must add a management layer, formal goals, or a meeting.

## Applying context

A skill declares the inputs it needs, the context that changes its advice, and conditions outside its scope:

```yaml
metadata:
  context:
    required: [org.scope, role.authority]
    adapts_by: [org.stage, org.size_band, operating.maturity]
    excluded_when: []
```

Use the fields that affect the decision. Keep missing facts marked unknown. For consequential inputs, record the value, source, date, and whether it is observed, reported, inferred, or proposed.

## Authority and scale

| Context | Operating implications |
|---|---|
| Small startup | Broad roles and direct coordination can be appropriate. Clarify delegated ownership, specialist decisions, and resource constraints. Add structure for an observed problem. |
| Scaling company | Make team interfaces, competing commitments, management capacity, and decision rights explicit. Develop owners who can sustain the work. |
| Public company or business unit | Identify the sponsor, local authority, enterprise dependencies, and established functional owners. Use existing planning and approval arrangements. |

At staffed companies, work with Finance, People, Legal, Product, Engineering, Sales, and other functions within the assigned mandate. Preparing analysis or coordinating a program does not confer their decision rights.

Data access and decision authority are separate. Use company policy to determine which information can enter a model or connected tool and who can approve consequential actions.

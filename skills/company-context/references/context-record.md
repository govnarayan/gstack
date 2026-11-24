# Context record

Use only the fields that affect the task. The identifiers match the library context vocabulary.

| Field | Evidence to capture |
|---|---|
| `org.stage` | Current venture stage or public status, with date. Do not derive headcount from stage. |
| `org.size_band` | Company headcount band. Also retain the actual reported number if useful and authorized. |
| `org.scope` | Whole company, business unit, function, or initiative/portfolio. Record served-team size separately in prose. |
| `org.public_status` | Private or public. This does not describe the operator's mandate. |
| `company.archetype` | Frontier AI lab, AI product, AI infrastructure, AI physical systems, B2B SaaS, or other technology. |
| `company.product_maturity` | Pre-PMF, finding fit, post-PMF, scaling product, multi-product, or unknown. State the evidence for product-market fit. |
| `company.go_to_market_motion` | Enterprise sales, product-led, consumer, marketplace, platform/ecosystem, hybrid, or unknown. |
| `role.mandate` | Strategy & Operations, BizOps, Chief of Staff, or assigned special projects. Record the actual accountabilities. |
| `role.authority` | Decision owner, delegated owner, influence without authority, or coordinator. Specify the decision area. |
| `operating.maturity` | Founder-held, emerging, repeatable, or scaled/governed. Diagnose from behavior, not age. |
| `governance.regime` | Venture-private, public-company, regulated. |
| `market.jurisdiction` | US describes the target company. Record affected operating markets separately when relevant. A US company can assign international strategy or operations work within the role's mandate. |
| `data.sensitivity` | Public, internal, confidential, restricted, or unknown, using company policy. |
| `task.consequence` | Reversible, material, high-impact, or unknown. State the actual consequence. |

For each material field retain `value`, `source`, `as_of`, and `status`. Distinguish a company fact from a proposed operating design. Keep a compact current record with links to supporting evidence instead of copying the entire source corpus.

The size bands are under 20, 20–60, 61–300, 301–5,000, and 5,001+. They are routing bands. The practical trigger for more structure is an observed coordination or control problem whose cost exceeds the burden of the intervention. Multiple leadership layers or a cross-unit initiative can require explicit interfaces even within a small served team.

## Distinguish the market view from the mandate

[Charles Phillips and fellow executives](https://press.stripe.com/scaling-people/interviews) describe learning the business from customers and external expectations. Pair an internal account of what a team delivers with one customer-facing commitment. Record any mismatch before making it an operating target.

[Molly Graham](https://review.firstround.com/podcast/molly-grahams-management-lessons-from-google-facebook-quip-lambda-school/) describes responsibilities shifting as a company grows. Retain the effective date of a transfer. If a document and the team disagree about who approves work, inspect the last approval before updating the mandate.

## Reconcile conflicting records

Record each source’s date, effective date and scope. A funding announcement can confirm a financing event. Use the cash forecast to assess funds available for the decision.

A candidate can test a public hypothesis with the hiring manager. A consultant can confirm authority with the sponsor. An employee can provide internal evidence while another leader retains approval.

If the conflict changes the decision, state what the available evidence supports and name the internal record that would resolve it.

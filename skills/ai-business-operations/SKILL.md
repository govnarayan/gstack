---
name: ai-business-operations
description: Execute AI-company operating analysis for Strategy & Operations, BizOps and Chief of Staff decisions about service economics, inference capacity, research-to-product commitments, evaluations, reliability, releases, and portfolio allocation. Use when AI-specific constraints change the operating choice.
metadata:
  capabilities: [ai-technical-fluency]
  context:
    required: [company.archetype, org.scope, role.authority]
    adapts_by: [org.stage, org.size_band, company.product_maturity, company.go_to_market_motion, governance.regime, task.consequence]
    excluded_when: ["market.jurisdiction!=US"]
---

# AI business operations

Make operating decisions about an AI business. Compare cost, capacity and service quality when deciding where to invest or whether to release. Research, Engineering and Safety validate their assumptions and retain their approval rights.

This skill concerns operating an AI business. Automating billing, reporting or other internal processes across industries belongs in [AI-augmented operator](../ai-augmented-operator/SKILL.md). An AI company can need both analyses, but internal labor savings do not establish the economics or reliability of its customer product.

## Identify what kind of AI business is being operated

Establish the operating unit and decision, not just the company label. A model developer may face research uncertainty and training/inference allocation. An application company may face provider dependence, task quality and support cost. Infrastructure economics require delivered capacity and service performance. Physical systems add hardware, deployment and intervention constraints. A company can span these contexts.

Specify the customer task, acceptance standard, demand population, commercial commitment, decision deadline and authorized owner. Separate a model capability from product value and a demonstration from repeatable service. Read the relevant references on demand. They offer calculations and reusable artifacts, not a fixed user conversation or a new software platform.

## Reconcile service economics with demand and capacity

Build the workload cohort table, cost bridge and capacity scenarios in [service economics and capacity](references/service-economics-and-capacity.md). Calculate accepted customer outcomes per unit of spend, preserving unsuccessful attempts, retries, fallbacks, tools, support and review. State the accounting boundary before using the term gross margin.

Model the demand shape as well as total volume. Separate normal growth, peak periods, launches and discrete customer commitments. Use observed processing time and tested usable capacity where available. Identify the volume or concurrency threshold where a cheaper route, self-hosting, reserved capacity or a service promise changes the recommendation. State what is unknown rather than treating theoretical throughput as delivered capacity.

The strongest case against a cost reduction is that it can lower accepted completion, increase review or break latency commitments. Compare options on the same population, quality requirement and service target before recommending one. Do not substitute per-token price for cost per accepted task.

## Convert research uncertainty into usable product decisions

Use [research dependencies and release operations](references/research-and-release-operations.md) to separate uncertain discovery, demonstrated capability, product integration and customer readiness. Build a dependency map with evidence milestones, last responsible decision dates, fallback paths and the commitments contingent on each result. Do not turn an uncertain experiment into a promised delivery date.

Construct a release evidence packet: versioned candidate, task dataset, repeated-trial results where needed, failure segments, service/cost observations, permissions, rollout population, monitoring and tested recovery. Choose pass conditions from the product and risk context. An average evaluation score cannot waive a failed material case or demonstrate a production service target.

## Allocate resources across coupled choices

Use [portfolio allocation and operating interfaces](references/portfolio-allocation-and-interfaces.md) to compare quality improvement, cost reduction, reliability, capacity and research projects against the same binding constraints. Show what each option displaces. Separate expected gains from commitments, and quantify the evidence that would change a decision. Preserve a repair/current-system option when comparing build, buy or replace.

Own the demand reconciliation, cohort analysis, scenario calculations, dependency and resource maps, recommendation and acceptance checks. Where data is absent, produce the instrumented test or specific source request needed to resolve it. Do not stop at asking Product and Engineering to supply a conclusion.

Technical owners certify architecture, research results and service feasibility. Finance validates accounting treatment. Product owns task value and release acceptance. The commercial owner controls customer promises. One person may hold several roles, but the decision artifact must make authority explicit. A senior individual contributor can exercise a delegated mandate without pretending to own every functional judgment.

Read [evidence and source limits](references/evidence-and-sources.md) for evaluation distinctions and primary methodological sources. Use current company data and verify provider capabilities, prices and contract terms for each real decision. The examples in the references are synthetic calculations, not external performance claims.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Name the user, risk owner and stop condition so an average score cannot clear an unacceptable failure. [NIST AI RMF playbook](https://airc.nist.gov/airmf-resources/playbook/)
2. Replay the workload across competing designs to expose quality, latency and cost trade-offs. [CMU SEI architecture tradeoff analysis](https://www.sei.cmu.edu/documents/196/1998_019_001_29711.pdf)
3. Calculate cost per accepted task and check the binding resource before buying capacity. [Application](references/service-economics-and-capacity.md)

## Connections

- [Automation support](../ai-augmented-operator/SKILL.md). Send the process baseline with the unit of work, exceptions and labor minutes to the process owner.

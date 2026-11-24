---
name: operating-cadence
description: Design or improve internal operating reviews, performance information, and the rhythm linking priorities with ongoing business health. Use for WBRs, MBRs, QBRs, metric disagreements, forecasts, meeting overload, or launches starving foundational work. Does not own staffed functional operations or external disclosure.
metadata:
  capabilities: [operating-cadence, performance-information, run-change-separation]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=planning|performance_and_metrics|decision_support|cross_functional_delivery
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

# Operating cadence

Create an operating rhythm that detects a consequential change early enough for someone to act. Weekly business reviews (WBRs), monthly business reviews (MBRs), and quarterly business reviews (QBRs) serve different decisions. A calendar of meetings is not an operating system until evidence, authority, follow-through, and goal revision work together.

The strongest argument against adding reviews is that preparation and meetings can consume the capacity they are meant to improve. Start with the missed signal, delayed decision, disputed number, neglected obligation, or repeated surprise. Read the current plan and recent actual reviews, then recap their requests before recommendations.

## Run the method

1. Map the operating questions, existing sources, decision owners and useful response time. Use [reviews and operating health](references/reviews-and-health.md) to choose the rhythm and separate execution review from strategy reconsideration.
2. Make the evidence comparable. Use [performance information](references/performance-information.md) for metric contracts, cohorts, denominators, variance, forecasts and uncertainty.
3. Prepare the smallest useful [review pack](templates/review-pack.md) from the standing sweeps in the reviews reference. Each item names its owner and decider from whatever record the company uses, such as a RACI, RAPID, DACI or a list of directly responsible individuals. The pack states what changed, what is inferred, and what decision is needed.
4. Resolve the actual choice. Capture owner, authority, due date, displaced work and effect check. Escalate conflicts the attendees cannot settle before the latest safe decision date.
5. Inspect execution and close commitments with evidence. Replan through [planning and goals](../planning-and-goals/SKILL.md), preserving the original result and any replacement commitment.

Run the [worked weekly sweeps](examples/weekly-sweeps-week.md) on either tracker export. Reconcile the two planted ownership exceptions before the meeting.

The [worked review sequence](examples/onboarding-reviews.md) runs a synthetic plan through weekly exceptions, a monthly diagnosis, quarter close and a new goal. It includes raw counts, forecast changes, service trade-offs and rejected interpretations.

For a whole-company or business-unit scorecard, read [company metrics by business model](references/company-metrics.md). It separates SaaS, consumer, hardware, marketplace, developer/platform, AI, and hybrid business mechanisms. For a retention, monetization, or customer-mix question, use the [cohort deep-dive specification](references/cohort-deep-dives.md), then inspect the [worked company review](examples/company-metrics-review.md). These are company-level analyses, not a requirement to collect every function's activity metrics.

## Adapt the design

A small company may combine business health, bets and strategy in one short forum with distinct questions. Add separate meetings only when different owners, evidence windows, or decisions justify them. A service incident needs its functional response immediately, not a wait for the next review.

For matrix or public-company scope, name local control, functional resource rights, escalation and parent approvals. A process coordinator can collect evidence and convene the decision without having authority to move staff, amend budgets or publish forecasts.

For AI-assisted preparation, verify source coverage, freshness, calculations and material omissions against the underlying evidence. Measure actual preparation saved, corrections required, missed signals and decision delays before reducing the review rhythm. There is no default percentage reduction in meetings or required increase in memo length.

## Completion standard

Show the observed operating problem, alternatives, chosen forum or asynchronous route, participants, evidence contract, preparation deadline, decisions expected, escalation, operating record and usefulness review. Run a sample pack through the process. Check the output against original commitments and raw data rather than judging completion by attendance or a green dashboard.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Set the reliability tolerance and the decision it triggers so an exception can change priorities. [Google SRE implementing SLOs](https://sre.google/workbook/implementing-slos/)
2. Tie the measure to the service outcome so the dashboard exposes a problem worth investigating. [UK service performance manual](https://www.gov.uk/service-manual/measuring-success/using-data-to-improve-your-service-an-introduction)
3. Route a confirmed driver change to the forecast owner and an unverified explanation to investigation. [Application](references/reviews-and-health.md)

## Connections

- [Analysis](../self-serve-analytics/SKILL.md). Send the analysis request with the metric version and comparison window to the analyst.
- [Financial decisions](../financial-resource-decisions/SKILL.md). Send the forecast with the changed volume, cost driver and timing to the finance lead.
- [Planning](../planning-and-goals/SKILL.md). Send the plan with the old target, authorized revision and effective date to the planning lead.

---
name: self-serve-analytics
description: Answer business questions from internal data with AI-assisted SQL and code, then validate, explain and publish the result. Use for querying a warehouse or product database, defining metrics, cohort and funnel analysis, reconciling numbers, and building or maintaining decision dashboards. Covers what an operator must understand to review AI-generated queries. Does not replace data engineering, grant access the operator lacks, or certify financial reporting.
metadata:
  capabilities: [self-serve-analytics]
  context:
    required:
      - market.jurisdiction=US
      - role.mandate=strategy_and_operations|business_operations|chief_of_staff|special_projects
      - work.domain=analytics|performance_and_metrics|decision_support
    adapts_by:
      - org.stage
      - org.size_band
      - org.public_status
      - operating.maturity
      - governance.regime
      - data.sensitivity
      - task.consequence
      - systems.connector
    excluded_when:
      - The assignment is to own data infrastructure, pipelines or the warehouse as a data engineer
      - The output is an audited financial statement, a regulatory filing or a public disclosure figure
---

# Self-serve analytics

Answer a business question with company data you have permission to use. Define the measure, check the query and reconcile the result before sharing it. Bring in the data team when the answer needs a new pipeline, a disputed definition or a number others will rely on.

## Work through five steps

1. **State the question as a decision.** Who will act on the number, what would change their choice, and how precise it must be.
   "How is activation?" is not a question. "Did the September signup cohort activate at a lower rate than June, enough to delay the pricing change?" is.
2. **Inspect the data before writing logic.** Find the tables and their grain (what one row represents).
   Also find keys, date fields and their time zone, status values and known exclusions such as test accounts. Use [query workflow and review](references/query-workflow-and-review.md).
3. **Draft with AI, then review against a checklist.** Give the assistant the schema, the grain, the metric definition and the exclusions. Read the draft clause by clause.
   The [AI-assisted SQL guide](references/ai-assisted-sql.md) lists the defects that recur and what you must understand to catch them.
4. **Validate the number independently.** Reconcile to a total you trust, recompute one cohort by a second route, check denominators and row counts after each join. A query that runs is not a query that is right.
5. **Publish with its definition, freshness and owner.** Use [dashboards and maintenance](references/dashboards-and-maintenance.md) for decision-useful layout, partial periods, small samples and upkeep.

For numbers that are computed correctly but still mislead, read [metric trees and analysis traps](references/metric-trees-and-analysis-traps.md). It covers formula versus belief edges, mix effects, history-correct segments, time zones, experiment splits and immature cohorts.

## Run the end-to-end case

The [worked case](references/worked-analytics-case.md) builds a synthetic warehouse and runs five business queries in two versions, an unreviewed AI draft and a reviewed query. It checks both against an independent recomputation and generates a dashboard. The drafts fail ten checks. One join repeats every invoice about ten times and inflates Q3 revenue roughly twentyfold. One NULL mistake reports 8 paying accounts instead of 207. Run it:

```sh
python skills/self-serve-analytics/scripts/analytics_demo.py --out <scratch folder> --strict
python -m unittest discover -s skills/self-serve-analytics/tests
```

## Adapt to the company

| Context | What changes |
|---|---|
| Early startup, product database only | Query a read replica, never production primary. Few definitions exist, so write the first ones down. Spreadsheets and a notebook may be enough. |
| Growth stage with a warehouse and BI tool | Reuse modeled tables and governed metrics before writing raw joins. Ask the data team which tables are trusted. Cost and permissions start to matter. |
| Scaled or public company | Metric definitions, access tiers and certified dashboards exist. Self-serve work explores and explains. Reported figures come from certified sources. Customer, employee and financial data carry handling rules. |

Read [access, cost and governance](references/access-cost-and-governance.md) before running queries on a new system. Read-only access, query cost limits, sensitive-data rules and the choice between a notebook, a BI tool and a governed metric layer are decided there.

## Limits

Generated code and a passing synthetic case do not establish independent SQL proficiency or results at an employer. They show that the review method catches common defects. Financial figures used for reporting, compensation or disclosure need the owning function's certified source. Do not paste restricted data into an AI tool the company has not approved, and do not widen your own access to finish a query.

## Decision checklist

Use the [shared baseline](../../GSTACK-CORE.md#before-giving-advice) to establish who is asking and which facts could change the answer.

1. Define the population, decision and acceptable error so the source can be checked for fitness. [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework)
2. Assign a defect owner and correction test so a definition error does not recur silently. [Data quality issues framework](https://www.gov.uk/government/publications/implement-a-data-quality-action-plan/data-quality-issues-framework)
3. Reconcile raw event timestamps with both boundaries of the eligibility window. [Application](references/query-workflow-and-review.md)

## Connections

- [Weekly reviews](../operating-cadence/SKILL.md). Send the weekly pack with the metric version and restated baseline to the metric owner.

# Access, cost and governance

Settle these before the first query on a new system. They decide what you may touch, what it will cost and which numbers others may rely on. Prices and product details below were read from official pages on 2026-11-14 and change often. Check them again before a purchase or budget decision.

## Access: read-only, least privilege, approved route

1. **Ask for read-only access through the owner's normal process.** Do not borrow credentials, service accounts or a colleague's session. Do not widen your own grants to finish a task.
2. **Prefer modeled or replica data.** Query the warehouse or a read replica, not a production application database. A heavy query on production can slow the product for customers.
3. **Know the mechanism, so you can ask for the right thing.**
   - PostgreSQL: a role with `SELECT` on the needed tables, plus `ALTER DEFAULT PRIVILEGES` so future tables are covered ([docs](https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html)).
   - Version 14 added the predefined `pg_read_all_data` role, which reads every table, view and sequence (see the predefined roles page in the PostgreSQL docs). That is broader than most analysts need.
   - `statement_timeout` aborts runaway queries (see the client connection defaults page in the PostgreSQL docs).
   - Snowflake: a role with `USAGE` on the database and schema and `SELECT` on tables ([privileges](https://docs.snowflake.com/en/user-guide/security-access-control-privileges)).
   - Future grants cover new objects in Snowflake ([GRANT](https://docs.snowflake.com/en/sql-reference/sql/grant-privilege)).
   - BigQuery: dataset-level viewer access plus permission to run jobs in a billing project.
4. **Sensitive data stays inside approved tools.** Customer personal data, employee data, health or financial account data and anything under a customer contract have handling rules.
   Use aggregated or de-identified tables where they exist. Paste schemas, not rows, into an AI assistant unless the company has approved that assistant for the data class. Small groups can re-identify people from "anonymous" aggregates, so suppress cells below a minimum count when sharing.

## Cost: know what a query spends

Warehouses charge for work, and a careless query can be expensive.

| Warehouse | What you pay for | Controls to use |
|---|---|---|
| BigQuery on-demand | Bytes scanned, $6.25 per TiB in US regions, first 1 TiB per month free ([pricing](https://cloud.google.com/bigquery/pricing)) | Dry run shows bytes before running. "Maximum bytes billed" makes an over-limit query fail without charge. `LIMIT` does not reduce bytes read on non-clustered tables ([cost practices](https://cloud.google.com/bigquery/docs/best-practices-costs)). Select only needed columns and filter on partition columns |
| Snowflake | Warehouse running time in credits, per second with a 60-second minimum per start (see the warehouses overview in the Snowflake docs) | Use the smallest warehouse that works, keep auto-suspend on, and ask whether a resource monitor caps your role (see the resource monitors page in the Snowflake docs) |
| Postgres replica | Shared server capacity | Timeouts, off-peak heavy queries, indexes owned by the data team |

A scheduled dashboard query runs every refresh. Multiply its cost by refreshes per day before scheduling it hourly.

## Definitions: one meaning per metric

Two analysts computing "active customers" two ways is the most common source of conflict in reviews. Use the strongest mechanism the company has:

1. **Governed metrics** in a semantic layer. dbt's MetricFlow defines metric logic once, in version control. Every tool then queries the same definition ([dbt docs](https://docs.getdbt.com/docs/build/about-metricflow)).
   Looker's modeling layer and similar BI features serve the same purpose.
2. **Modeled tables** with tests. dbt ships four generic tests (unique, not_null, accepted_values, relationships).
   It also checks source freshness against warn and error thresholds (see the dbt data tests page and [freshness](https://docs.getdbt.com/reference/resource-properties/freshness)).
3. **A written metrics catalog**: name, definition, population, exclusions, grain, owner, source table, known caveats.
4. **Nothing yet.** Then your definition is provisional. Label it, get the metric owner's agreement, and add it to the catalog.

When your number disagrees with a governed one, assume yours is wrong until reconciled.

## Choose the tool by the job

| Job | Fits | Watch for |
|---|---|---|
| One-off question, exploration | SQL editor in the warehouse, or a notebook (Hex, Jupyter) | Results that live only on your laptop |
| Recurring view for a team | BI tool on governed models: Looker, Tableau, Power BI, Metabase | Dashboards built on raw tables with private logic |
| Analysis mixing SQL, Python and narrative | Notebook tools such as Hex | Notebooks becoming production reports without tests |
| A model leaders will plan against | Spreadsheet fed by a reviewed query, with inputs separated from logic | Manual pastes that go stale |

List prices read on 2026-11-14 help size a request. They do not choose a vendor.

| Tool | Published list price |
|---|---|
| [Metabase](https://www.metabase.com/pricing/) | Open source free, cloud Starter $90 per month billed yearly for 5 users |
| [Tableau Cloud](https://www.tableau.com/pricing/cloud) | Standard: $75 Creator, $42 Explorer, $15 Viewer per user per month, billed annually |
| [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing) | Pro $14, Premium Per User $24 per user per month, paid yearly |
| [Hex](https://hex.tech/pricing/) | Professional $36, Team $75 per editor per month |
| [Looker](https://cloud.google.com/looker/pricing) | Quoted by sales. Platform editions include ten standard and two developer users |
| [Mode](https://mode.com/compare-plans/) | Part of ThoughtSpot. Paid plans are not priced publicly |

Use the tool the company already licenses unless it cannot do the job. A second BI tool doubles the places a metric can drift.

## Who owns what

| Party | Owns |
|---|---|
| Data or analytics engineering | Pipelines, modeled tables, tests, semantic layer, access grants |
| Metric owner (often Finance or the function) | The definition and the certified number |
| Security, Legal, Privacy | Data classes, approved tools, retention and sharing rules |
| The operator | The question, the analysis, its checks, and labeling provisional results as provisional |

At an early startup one person may hold several of these. Write down which hat a decision was made in.

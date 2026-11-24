# Process portfolio and baseline

Use this reference to choose where operating capacity should come from, estimate the economics and distinguish a labor bottleneck from waiting, policy or data problems. The tables are reusable working artifacts. Empty values remain unknown until evidence supplies them.

## Process portfolio

Inventory the end-to-end process rather than collecting isolated writing tasks. Include the upstream demand trigger and downstream acceptance. Map the same population across systems so that an item is not counted as new work every time it moves teams.

| Candidate | Completed business outcome | Monthly units and arrival pattern | Human minutes per unit | Waiting time and cause | Errors/rework | Current owner/system | Smallest useful intervention | Build/maintain/review resources |
|---|---|---|---|---|---|---|---|---|
| Fill from records | Evidence of acceptance | Include peak and seasonal demand | Separate active time from elapsed time | Approval, missing input, queue or service delay | Count and business consequence | Include authoritative record | Remove, clarify, script, AI-assist or automate | Hours and constrained roles |

For each candidate calculate a range for monthly net human hours released:

`baseline active hours - proposed active hours - continuing maintenance hours`

Proposed hours include input cleanup, all reviews, corrections, retries requiring human attention and exception resolution. Add a separate implementation investment. Do not subtract a one-time build twice. Use a low/base/high case for volume, exception share, review minutes and maintenance, then show the break-even values. A weighted score can help compare similar candidates only after hard constraints are visible. Do not let a large time estimate compensate for missing authority or unacceptable errors.

Before selecting a candidate, test these failure explanations:

1. Unnecessary work should disappear. A duplicated status report does not need an autonomous author if the recipient no longer uses it.
2. Policy or another team's response may block the queue. Faster extraction does not shorten a two-week approval wait unless that wait changes.
3. Source records may lack reliable joins. Repair the identifier or reconciliation before generating recommendations from mismatched records.
4. A simple average can hide variation. Separate routine, complex and exceptional cases before projecting savings.
5. Low volume or frequent changes can defeat the economics. A lightweight assistant can be preferable to a maintained integration.

Choose a portfolio that fits available build and review capacity. Sequence shared data repairs before several dependent automations. Avoid crediting the same saved analyst hour to both the source-data project and each downstream project. Include the displaced work: what analysis, customer response or operating decision will the released time fund, and who has enough uninterrupted capacity to do it?

## Baseline record

Define the observation window, source population, exclusions and success standard before comparing methods. Sample across relevant volume segments and preserve sampling weights. If a month-end spike dominates the workload, observing a quiet week does not support a monthly staffing conclusion.

| Field | Required definition or evidence |
|---|---|
| Unit and population | Unique item key, trigger, time window and eligibility conditions |
| Completion | Required accepted output and receiving system or owner |
| Volume | Arrivals, completions, unresolved items and carryover, reconciled by key |
| Touch time | Active minutes by role, including review and rework |
| Elapsed time | Trigger to accepted completion, with median and a chosen high percentile |
| Error | Incorrect result, unauthorized action, missing item, duplicate, late completion and severity |
| Cost | Loaded labor assumption, actual tool charges and the chosen cost boundary |
| Evidence | Record/query/source location, observation date, sample size and missingness |

Reconcile flow with `opening backlog + new arrivals - completed - valid cancellations = closing backlog`. Preserve valid cancellations separately from successes. A process that looks faster because difficult items remain open has not established higher completion capacity.

Observe active time directly where feasible. Self-reported estimates can seed a hypothesis, but label them. Keep labor rate changes separate from workflow changes. Record how work is batched and interrupted because releasing scattered minutes may not free a full working day.

## Economic decision sheet

| Quantity | Calculation | Interpretation |
|---|---|---|
| Baseline labor cost | Baseline hours x loaded hourly cost | Assumption-based value of capacity used |
| New monthly cost | Proposed human hours x loaded rate + continuing tools/services + maintenance labor | Include failed and unresolved cases |
| Net monthly value | Comparable baseline cost - new monthly cost | Capacity value, unless cash spend actually falls |
| Payback | One-time implementation cost / positive monthly value | Undefined when monthly value is zero or negative |
| Break-even volume | Fixed monthly burden / positive net value per unit | Valid only within the modeled case mix and capacity range |
| Usable capacity | Net hours released, by role and time block | Test against work waiting to use it |

Keep quality and authority constraints outside the dollar total unless the business can credibly estimate their losses. Where an error cost is unknown, show the error rate and severity, state the missing value and test the decision under explicit loss assumptions.

Adoption needs its own funnel: eligible units, units offered the new method, units using it, accepted completions, bypasses and reasons. Low adoption may mean a missing exception path, excessive review burden, distrust or a mismatch with the actual task. Diagnose from observed behavior rather than treating training attendance as adoption.

## Decision artifact

Deliver a selected process and two credible alternatives, the baseline evidence, expected net capacity range, quality limits, implementation burden and the condition under which the selection changes. Name the strongest reason to keep the current method. State the next uncertainty the pilot will resolve and the smallest reversible test that resolves it. Use actual company thresholds rather than importing a universal minimum return or target multiplier.

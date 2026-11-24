# Service economics and capacity

Use this reference for AI-product pricing, provider routing, service expansion, capacity commitments or infrastructure choices. Produce a reconciled model rather than a collection of token prices. All example numbers below are synthetic assumptions.

## Define the customer outcome and cost boundary

Identify the unit customers pay for and the unit that succeeds. A submitted document, model call, accepted answer, resolved case and paying account are different denominators. Record refunds, abandonment and work completed by support. State whether acceptance includes human correction and whether it arrives within the promised time.

Construct a workload table from permitted usage records:

| Cohort | Submitted tasks | Accepted tasks | Model calls and route | Input/output usage | Retries/fallbacks | Tools/retrieval | Human minutes | Latency distribution | Revenue basis |
|---|---|---|---|---|---|---|---|---|---|
| Routine/complex/long-input/etc. | Reconcile to arrivals | Define quality and deadline | Include all attempts | Include cache or batch treatment if relevant | Count separately | Actual usage | Review plus support | Median, selected high percentile, unresolved | Task, seat, subscription or contract |

Reconcile `submitted = accepted + failed + abandoned + unresolved` for a fixed population. Preserve reruns as attempts attached to the originating task rather than pretending they are new customers. Break out paid, free, trial and internal usage if their economics differ.

Build a cost bridge:

`all inference attempts + paid tools/retrieval + direct storage/network + direct review/support + allocated serving capacity = defined service cost`

List excluded costs alongside the result. Accounting treatment of support, capacity and development is company-specific. Have Finance reconcile the bridge to the ledger before calling it reported gross margin. A decision contribution margin that excludes shared fixed cost is useful when labeled, but is not interchangeable with full company profitability.

Compute `service cost / accepted tasks`, `service cost / submitted tasks`, cohort contribution and cost per paying account. Compare revenue and service cost on the same period and population. For seat pricing, show usage concentration and the expensive customer tail rather than allocating costs evenly to seats.

## Worked synthetic routing choice

Assume 100,000 monthly submitted tasks split into 80,000 routine and 20,000 complex tasks. The price collected is $0.10 per submitted task, so revenue is $10,000. Ignore refunds only as an explicit simplifying assumption.

| Cost or outcome | Current route | Proposed cheaper route |
|---|---:|---:|
| Initial routine inference | 80,000 x $0.012 = $960 | 80,000 x $0.006 = $480 |
| Initial complex inference | 20,000 x $0.060 = $1,200 | $1,200 |
| Additional fallback calls | 5,000 x $0.060 = $300 | 15,000 x $0.060 = $900 |
| Other variable tools | 100,000 x $0.003 = $300 | $300 |
| Direct human review | 1,000 x 3 minutes x $40/hour = $2,000 | 1,500 x 3 minutes x $40/hour = $3,000 |
| Allocated fixed serving cost | $1,500 | $1,500 |
| Total defined service cost | $6,260 | $7,380 |
| Accepted tasks after review | 95,000 | 94,000 |
| Cost per accepted task | $0.0659 | $0.0785 |
| Defined service margin | 37.4% | 26.2% |

The cheaper initial call saves $480, but additional fallbacks cost $600 and extra review costs $1,000. Total cost rises $1,120 while accepted outcomes fall by 1,000. Reject the proposed route under these assumptions. A quality improvement could change the decision, but it must be demonstrated on the same workload. The table does not establish a causal effect or recommend a provider.

At unchanged quality and other costs, the route can tolerate at most $480 of added fallback and review cost combined. Each extra reviewed task costs $2 in this example. If fallback increases are zero, the savings disappear at 240 additional reviewed tasks. If there are 4,000 additional fallback calls costing $240, only 120 additional reviews fit the remaining savings. Use such flip conditions to choose a test, not just a point estimate.

## Demand and capacity worksheet

Monthly cost and peak capacity answer different questions. Build a demand envelope with normal load, busy periods, launches, large customer commitments and recovery after an outage. Name uncertainty and source evidence for each. Do not sum peaks that cannot coincide, or assume mutually exclusive peaks when they can.

| Input | Needed definition |
|---|---|
| Arrival demand | Tasks/second or tasks/minute by cohort and time window |
| Work per task | Calls, tokens, service seconds, tool use and retries by route |
| Usable capacity | Measured throughput at the required quality/latency, not theoretical maximum |
| Headroom | Explicit allowance for variability, failover and operations, validated by load tests |
| Dependency limits | Provider quotas, request/token limits, queue limits and downstream bottlenecks |
| Procurement | Lead time, minimum commitment, cancellation, transfer and expiration conditions |
| Recovery | Backlog volume, drain capacity, priority policy and user deadline |

For a simplified homogeneous workload, concurrent service demand is approximately arrival rate multiplied by mean service time, when the system is stable and units match. This is a sizing estimate, not a tail-latency guarantee. Test mixed task lengths and saturation. A provider request quota and a token quota may bind at different workload mixes.

Synthetic example: 12 tasks/second with mean 4 service-seconds/task implies 48 concurrent service slots occupied on average. A proposed planning allowance of 25% yields 60 slots. The allowance is an assumption requiring testing, not a universal rule. If the tested usable system supports 50 such slots at the required service level, planning demand exceeds it by 10 slots. The choice is capacity, demand scheduling, route optimization or a narrower commitment, not relabeling the average as enough.

Consider a 10,000-task backlog, arrivals of 12/second and tested service capacity of 15/second. Net drain is 3/second, so clearing takes about 3,333 seconds or 55.6 minutes, ignoring changes in task mix. At capacity of 12/second there is no drain. At 11/second the backlog grows. Include customer deadlines and priority cohorts before promising recovery.

## Build, buy and commitment analysis

Compare current operation, targeted repair, purchased service and owned infrastructure over a matched service requirement and time horizon. Include integration, migration, testing, idle capacity, failover, operations, security requirements and exit. For owned capacity, separate committed cost from avoidable incremental cost. Lower utilization raises allocated unit cost even if device price is unchanged. Do not count the same capacity as fully available to research and customer serving simultaneously.

For a simplified fixed/variable comparison, break-even volume is `(owned fixed cost - vendor fixed cost) / (vendor variable cost - owned variable cost)` only when the denominator is positive and both meet the same quality, service and capacity requirements. Recalculate at the next capacity step and include the staff needed to operate it. A crossover outside usable capacity is not a feasible break-even point.

Deliver cohort economics, demand/capacity scenarios, commitment exposure, service evidence, sensitive assumptions and a recommendation with flip conditions. Have technical owners confirm measured capacity and Finance confirm the cost boundary. The operator owns the calculations and reconciliation.

## Price the completed task and its binding resource

[Netflix's inference team](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c) describes running small models locally when avoiding a network call matters. Its choice of serving software changed as open alternatives caught up and workloads diversified. Replay the actual mixture of requests before renewing a specialized system.

[Justin Uberti and Zahan Malkani](https://openai.com/index/continuous-voice-interaction-with-gpt-live/) describe the resources behind a live voice session. A user occupies session capacity while waiting for results. Measure concurrent sessions, queue delay and network time before buying more model compute.

[Anthropic's research team](https://www.anthropic.com/research/multi-agent-research-system) found substantial extra token use in multi-agent research. Compare cost per accepted result, including retries and reviewer time. Reserve parallel work for questions with independent branches where better coverage offsets that cost. Use your measured mix and acceptance rate for the purchase decision.

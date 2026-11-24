# Process, constraints, and capacity

Read only the selected card. Mechanisms summarize the cited public sources. Application procedures, examples, and fit judgments are this library's own synthesis. All examples are synthetic.

## Before selecting a card

1. Trace material and information from arrival through acceptance to locate the wait. [Lean Enterprise Institute value stream map](https://www.lean.org/lexicon-terms/value-stream-mapping/)
2. Choose a balancing measure to detect a faster local step that leaves downstream work worse off. [IHI establishing measures](https://www.ihi.org/library/model-for-improvement/establishing-measures)
3. Count arrivals, finished work and remaining inventory within the same boundary and period.

<a id="theory-of-constraints"></a>

## theory-of-constraints: Theory of Constraints focusing steps

Supports: cross-functional-delivery, financial-resource, product-delivery.

Context: work.domain=cross_functional_delivery, org.scope, operating.maturity.

Decision trigger: Local teams improve utilization while end-to-end output remains stuck.

Inputs and evidence: System goal, demand, capacities, queues, blocked and starved time, output quality, and governing policies.

Procedure: Define the system and its goal. Identify the current limiting constraint. Exploit it with existing resources, then subordinate other work to that constraint. Elevate its capacity when justified. Repeat after the constraint moves and challenge policies that preserve yesterday's bottleneck.

Output: A constraint diagnosis, immediate protection actions, coordinated release policy, and a capacity-investment decision.

Illustrative decision: A synthetic onboarding flow can intake 30 cases a week, review 20, and deploy 40. If demand is 25 and review is the binding constraint, more intake staff adds a queue. Protect review time and improve case completeness first.

Failure conditions and alternatives: The constraint may be market demand or a policy rather than a busy machine. Multiple classes, shifting constraints, and quality failures need closer modeling. Value-stream mapping reveals the wider flow.

Source: [TOCICO, Introduction to Theory of Constraints, Alan Barnard](https://learningcenter.tocico.org/courses/Introduction-to-the-Theory-of-Constraints).

Use [Frederick Ryckman's hospital account](https://www.ihi.org/library/blog/optimizing-flow-everyones-job-how-cincinnati-childrens-improved-efficiency-their-0) to ask where smoothing scheduled arrivals could free capacity for unscheduled work. Before buying more capacity, test whether a changed schedule moves waiting elsewhere.

<a id="littles-law"></a>

## littles-law: Little's Law

Supports: cross-functional-delivery, performance-information, product-delivery.

Context: work.domain=performance_and_metrics, org.scope, operating.maturity.

Decision trigger: The team needs to relate work in progress, throughput, and time in the system.

Inputs and evidence: Consistent system boundaries, time units, average work in progress, completed throughput, and entry/exit timestamps.

Procedure: Define what counts as a unit and when it enters and exits. Use a consistent observation window and check flow balance. For stable long-run averages, relate work in progress L, effective throughput lambda, and time W through L = lambda × W. Compare implied and observed time and investigate any boundary or data mismatch before changing policy.

Output: A flow baseline and an explicit work-in-progress or capacity hypothesis.

Illustrative decision: A synthetic process averages 60 open cases and completes 20 cases weekly. Implied average time is three weeks under the stated stable-flow assumptions. A one-week target at the same throughput implies 20 average open cases, but achieving that requires a feasible release and service policy.

Failure conditions and alternatives: This is an accounting relationship, not proof that cutting the queue causes capacity to rise. Growing backlogs, lost cases, changing mix, and inconsistent windows require care. Use constraint analysis to choose interventions.

Source: [MIT, Cathy Wu, Queuing models](https://web.mit.edu/1.041/www/lectures/L8-queuing-models-2026sp.pdf).

Use [the Crossrail progress review](https://www.nao.org.uk/reports/crossrail-progress-update/) as a boundary case. A project handing off different systems has changing arrivals and acceptance criteria. Count starts, completions and unfinished work over the same boundary before estimating delay.

[Samsung's factory scheduling study](https://ieor.berkeley.edu/wp-content/uploads/2019/10/SLIM.pdf) used target cycle time at constant output to set work-in-process targets. Lines 4 and 5 fell from 4.5 to 2.0 days per layer. Check actual output separately before attributing every time gain to inventory reduction.

<a id="value-stream-mapping"></a>

## value-stream-mapping: Value-stream mapping

Supports: cross-functional-delivery, product-delivery, organization-design.

Context: work.domain=cross_functional_delivery, org.scope, operating.maturity.

Decision trigger: Lead time is poor but no single team sees the full customer-to-delivery path.

Inputs and evidence: Direct observation of work and information flow, queues, touch time, handoffs, rework, demand, and quality.

Procedure: Choose one product or service family and follow real work end to end. Map current material or work flow together with information and approvals. Measure waiting, processing, and rework. Design a feasible future flow, identify the governing constraint, and assign experiments and owners to reach it.

Output: A current-state map, future-state map, and sequenced improvement plan.

Illustrative decision: A synthetic contract process spends two hours in active work and six days waiting for incomplete inputs and approval. The first change is clearer intake and an approval route, then measurement of the revised flow.

Failure conditions and alternatives: A workshop map based only on opinions misses actual work. Optimizing touch time may leave most delay unchanged. Use A3 for one stubborn cause and Little's Law to reconcile flow measures.

Source: [Lean Enterprise Institute, Value Stream Mapping Overview](https://www.lean.org/lexicon-terms/value-stream-mapping).

[Spotify's migration leads](https://engineering.atspotify.com/2020/06/tech-migrations-the-spotify-way) describe several migrations competing for teams. Map the waiting team and all its incoming requests. Shortening the platform team's task can leave delivery time unchanged.

<a id="pdsa"></a>

## pdsa: Plan-Do-Study-Act

Supports: cross-functional-delivery, performance-information, product-delivery.

Context: work.domain=cross_functional_delivery, operating.maturity, task.consequence.

Decision trigger: A known process needs an evidence-based improvement experiment.

Inputs and evidence: A problem statement, causal hypothesis, prediction, baseline, test boundary, and balancing measures.

Procedure: Plan a change with a specific prediction and measurement. Do a bounded trial and record deviations. Study the results against the prediction, including adverse effects. Act by adopting, adapting, or abandoning the change and state the next learning cycle. Preserve the link between theory and observed outcome.

Output: A test record, revised understanding, and a scale, change, or stop decision.

Illustrative decision: A synthetic support team predicts that a clearer form will reduce clarification requests without increasing abandoned submissions. It tests one request category and checks both outcomes before widening the change.

Failure conditions and alternatives: A before/after change can reflect seasonality or mix. Plan a credible comparison. Deming emphasized Study, and this card does not relabel his PDSA as PDCA. Build-Measure-Learn addresses uncertain business-model assumptions.

Source: [W. Edwards Deming Institute, PDSA Cycle](https://deming.org/explore/pdsa/).

[DoorDash's switchback tests](https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/) explain why shared couriers complicate randomized tests. In a small trial, identify who else receives the treatment indirectly and how to tell whether the result survives normal load.

[A hospital discharge study](https://link.springer.com/article/10.1186/s12913-024-10960-x) assigned obstacles from rounds to named owners. Discharges by noon rose from 808 of 8,514 to 8,746 of 32,591 across intervention periods. Track readmission and length of stay alongside speed. The single-center comparison cannot isolate which change caused the gain.

<a id="a3"></a>

## a3: A3 problem solving

Supports: cross-functional-delivery, facilitation, performance-information.

Context: work.domain=cross_functional_delivery, operating.maturity, role.authority.

Decision trigger: A recurring operational problem needs an agreed causal explanation and follow-through.

Inputs and evidence: Observed current condition, target gap, process facts, cause evidence, alternative countermeasures, and responsible owners.

Procedure: Describe context, current condition, and a measurable target. Investigate causes with direct evidence rather than jumping to a solution. Compare countermeasures and explain how each addresses a cause. Set an implementation and follow-up plan, then compare actual results with the target and revise the reasoning.

Output: A compact problem-solving narrative, countermeasure plan, and follow-up result.

Illustrative decision: A synthetic invoicing team traces late invoices to missing purchase-order data rather than lack of reminders. It tests a required intake field and a documented exception owner, then tracks lateness and rejected submissions.

Failure conditions and alternatives: A filled page is not the method. Do not use the format to sell a predetermined solution or substitute speculation for root-cause evidence. Use value-stream mapping when the wider process is not understood.

Source: [Lean Enterprise Institute, How to Use the A3 Process](https://info.lean.org/hubfs/ebook%20files/How-to-use-A3-PDF-final.pdf).
Use [Frederick Ryckman's hospital account](https://www.ihi.org/library/blog/optimizing-flow-everyones-job-how-cincinnati-childrens-improved-efficiency-their-0) to test a local explanation against neighboring workloads. Put the arrival pattern beside staffed capacity and downstream waiting. Revisit the diagnosis if the queue moves without improving total time.

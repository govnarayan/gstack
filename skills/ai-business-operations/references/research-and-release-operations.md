# Research dependencies and release operations

Use this reference when uncertain AI capabilities, model changes or shared infrastructure affect customer commitments. Produce a dependency map and evidence packet the decision owner can use. Technical and safety approvals remain with authorized owners.

## Separate four different uncertainties

| Layer | Question | Evidence that changes the plan | Commitment that remains contingent |
|---|---|---|---|
| Research | Can the method achieve the capability? | Reproducible experiment and relevant evaluation | Capability and discovery timing |
| Product integration | Can that capability perform the actual task? | Representative user/task outcomes with tools and context | Feature scope and acceptance |
| Service | Can the system deliver repeatedly at load? | Quality, latency, capacity, reliability and recovery evidence | Service target and launch volume |
| Commercial adoption | Will the intended buyer use and pay for it? | Actual behavior, willingness to pay and retention evidence | Revenue and adoption forecast |

Do not let evidence from one layer stand in for another. A benchmark improvement does not by itself establish customer value. A successful product pilot does not establish serving capacity. A signed contract does not resolve an uncertain research dependency.

## Dependency artifact

| ID | Required outcome | Predecessor | Evidence milestone | Owner | Resource needed | Last responsible decision date | Fallback | Downstream promise affected |
|---|---|---|---|---|---|---|---|---|
| Fill from actual plan | Observable result | Explicit dependency | What would validate or reject it | Accountable role | Team time, compute or data | Date a different path must start | Reduced scope, alternate route, later date or stop | Named contract, launch or capacity commitment |

For research, use time-bounded experiments with success, failure and inconclusive results defined in advance. A milestone can be a decision that a path is unpromising. Track cost spent and evidence gained separately from delivery progress. Treat estimated experiment success probabilities as assumptions unless a justified base rate exists. Show sensitivity rather than inventing precision.

For a product deadline, calculate backward from integration, evaluation, security review, rollout and procurement. The last responsible decision date is when an alternative must begin to preserve a viable outcome. It is not a command that research must succeed by then.

Synthetic example: a customer pilot is planned for day 60. Integration needs 14 days, evaluation 7 days and bounded rollout 7 days. A research-dependent capability must therefore be evidenced by day 32 if these durations are sequential. If a fallback needs 20 days plus the same 14 days of evaluation/rollout, the fallback must start by day 26. Waiting until day 32 for research without starting the fallback creates a six-day gap in the stated plan. The operating choice is to fund parallel fallback, narrow the pilot or renegotiate timing. Adding a status meeting does not resolve the dependency.

If activities can overlap, justify the overlap and show what rework or failed-test risk it introduces. Do not double-count a shared engineer's capacity across concurrent paths.

## Release evidence packet

Identify the exact release configuration: model and provider route, prompts, tools, retrieval sources, policies and system versions that affect outcomes. Preserve the old configuration for comparison where policy permits.

| Evidence | Required content |
|---|---|
| Customer task | Intended population, acceptance rubric, prohibited behavior and affected commitments |
| Evaluation dataset | Provenance, representativeness, development versus held-out cases, cohort coverage and known blind spots |
| Results | Baseline/candidate, all attempts, repeated-trial consistency where relevant, failures by severity and segment |
| Service performance | User-relevant latency, completion, dependency failures, load conditions and observation window |
| Economics | Cost per accepted task, usage concentration, retries, tools and human burden |
| Risk/authority | Applicable privacy, security, policy, safety and commercial approvals |
| Rollout | Eligible population, exposure limits, owner and expansion criteria |
| Detection/recovery | Signals, thresholds, alert owner, stop action and tested restoration path |

Distinguish exact checks from graded judgment. Exact checks can verify forbidden writes, calculations and target records. Human or calibrated model review can assess useful reasoning, grounding and task completion where multiple outputs are valid. Keep disagreements visible. Do not replace the product acceptance standard with whatever a benchmark happens to measure.

Choose a material-case rule with the accountable owner. An average gain may coexist with unacceptable deterioration in a particular customer cohort or a rare high-impact failure. A small test with no failures is limited evidence, not proof of zero risk. Explain what monitoring and exposure limits compensate for the unknowns.

## Service targets and release decisions

Specify a user-relevant indicator, its target and measurement window, population/exclusions and contractual consequence if one exists. Availability of a model endpoint is not necessarily successful completion of the customer's task. Latency averages do not describe the slowest affected cohort.

A synthetic target might be an agreed share of accepted tasks completed within a specific deadline over a named window. The numerical target must come from the product's users, commitments and economics. Do not import an infrastructure target into a business task without examining those differences.

Use an operating decision table:

| Observation | Decision to evaluate | Evidence needed |
|---|---|---|
| Candidate improves quality but raises cost | Price, route, narrow scope or accept lower contribution | Cohort willingness to pay and full cost |
| Quality passes offline but degrades at load | Hold exposure, repair capacity or integration | Load-linked failure and latency evidence |
| Aggregate improves, material cohort regresses | Exclude cohort, repair or retain baseline | Cohort-specific acceptance and risk owner approval |
| Dependency/provider changes | Re-test affected behavior before expansion | Version mapping and relevant regression cases |
| Monitoring misses a seeded failure | Repair detection before relying on it | Observed alert, owner response and recovery |

An incident record should identify customer impact, affected versions, time range, actions taken, unreconciled work and restoration evidence. Distinguish rolling back a configuration from reversing external side effects. Restoring a previous model does not undo messages already sent or records already changed. Define reconciliation and customer remediation ownership.

The senior IC's deliverable is the evidence packet, quantified commitment gap and actionable resource choice. Technical owners validate experiments and service feasibility. Product and designated risk owners decide acceptance and exposure within their authority. Commercial commitments change only through the authorized owner.

Public methodology: [Anthropic's evaluation guidance](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) informs task outcomes, repeated trials and complementary checks. [Google's service-objective guidance](https://sre.google/sre-book/service-level-objectives/) distinguishes measured indicators, objectives, agreements and distributions. Neither supplies a universal release threshold or company operating cadence.

## Decide in advance what can stop a release

[OpenAI's rollback account](https://openai.com/index/expanding-on-sycophancy/) documents a release where favorable aggregate signals coexisted with expert concerns about excessive agreement. The company rolled it back. Record the strongest objection, the exposed user group and the behavior that would block rollout before looking at the overall score.

[Anthropic's evaluation guide](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) recommends inspecting the actual end state and repeated trials. For a scheduling assistant, verify the correct meeting exists once with the intended attendees. A polished confirmation can accompany a missed or duplicate booking.

Compare the affected slice with the previous release under matched conditions. Name who can halt expansion, where the previous version is available, and what evidence permits another attempt.

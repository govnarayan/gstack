# Evaluation and rollout

Use this reference to decide whether a proposed method deserves more autonomy or wider adoption. Evaluate the complete operating task, including what happens after the model produces an answer.

## Evaluation dataset

Build cases from permitted historical records or explicitly synthetic fixtures. Separate cases used to improve the method from cases withheld for assessment. Preserve the denominator and version the dataset. Synthetic cases demonstrate behavior under designed conditions, not real-world prevalence or productivity.

| Case field | Content |
|---|---|
| ID and segment | Routine, complex, ambiguous, high-impact, peak-volume or dependency failure |
| Inputs | Source snapshots, versions, permissions and starting state |
| Expected outcome | Accepted final record or correct abstention/escalation |
| Forbidden outcome | Duplicate, unsupported change, unauthorized destination or silent omission |
| Checks | Exact calculations/state assertions plus a judgment rubric when necessary |
| Human reference | Who established correctness, disagreement and resolution |
| Run evidence | Method versions, tool calls/results, attempts, elapsed time, human time and cost |

Include missing values, conflicting records, changed sources, unavailable dependencies, duplicate arrivals, expired approval, attempted instruction injection and interrupted execution when they are credible for the task. Test both a rejected action and the authorized recovery. An evaluation that rewards always escalating cannot establish useful automation.

For extraction and arithmetic, compare field values and reconciliations. For research, inspect source grounding, coverage, counterevidence and the inference from evidence to recommendation. For actions, query the final system state and count side effects. A generated claim of completion is not a completion check.

For judgment, specify what distinguishes an acceptable recommendation from a misleading one, allow valid alternatives and calibrate reviewers on disagreements. If a model grades outputs, check a human-reviewed subset and important failures. Do not let an uncalibrated grader define success.

## Compare methods fairly

Run baseline and candidate on comparable cases and conditions. Randomly assign permitted live cases or use counterbalanced trials where feasible, with independent quality review. Record who operates each method, learning effects, interruptions and setup time. If only a sequential before/after comparison is possible, state the confounding changes and limit the conclusion.

Repeat variable model tasks where repeatability affects the operation. Keep every attempt's cost and outcome. Separate success on the first attempt, eventual completion within the allowed budget and consistent success across repeated trials. Report outcomes by relevant segment and severity, not just an overall average. Do not infer that a rare error is absent because a small sample contains none.

| Measure | Numerator / denominator or definition |
|---|---|
| Acceptable completion | Accepted completed items / all assigned eligible items |
| Autonomous completion | Accepted items without human intervention / all assigned eligible items |
| Error escape | Incorrect items reaching downstream use / items reaching downstream use, by severity |
| Review burden | All review and correction minutes / assigned items |
| Net capacity | Comparable baseline human hours minus all candidate human hours and maintenance |
| Elapsed completion | Arrival to accepted completion, including waits and unresolved cases |
| Cost per success | All attempt, tool, human and maintenance costs in the defined boundary / accepted completions |
| Adoption | Items actually using the method / eligible items offered it |

Record unresolved item ages rather than dropping them from completion-time reporting. Test whether speed gains depend on the operator accepting more errors or moving work to another team.

## Implementation sequencing

Use the smallest evidence-producing increment. The following are possible stages, not mandatory gates for every low-impact draft:

| Stage | Real output | Evidence needed before expanding |
|---|---|---|
| Baseline and contract | Reconciled population, rules and target records | Bottleneck and authority understood |
| Offline exercise | Candidate outputs on frozen cases | Known errors visible, checks valid, failed cases retained |
| Shadow run | Proposals alongside current process, no business writes | Agreement and differences explained, real service failures observed |
| Assisted use | Humans approve actual actions | Total review effort and downstream acceptance measured |
| Bounded automation | Only delegated cases act automatically | Limits enforced, exceptions staffed, recovery and pause tested |
| Expansion or retirement | Wider eligible population or simpler replacement | Net capacity and quality persist under actual demand |

For each increment, name a responsible person, required upstream fix, acceptance evidence, decision date and stop condition. Expansion can mean more volume, more fields, more destinations or less review. Test each changed boundary rather than treating all expansion as the same choice. Policy-sensitive writes and consequential commitments require the applicable authorization throughout.

Before production, exercise a failure with writes disabled or in an approved test environment. Interrupt after a remote action but before recording its receipt. Restart and inspect whether the implementation reconciles without a duplicate. Seed stale data and inspect whether old approval is rejected. For low-impact analysis, a simpler artifact read-back may be enough.

## Adoption and continuing operation

Observe bypasses and workarounds. Interview the people correcting outputs and the downstream recipients accepting them. Compare actual review minutes with the pilot assumption. Include training, exception staffing and maintenance in the continuing economics. A nominally automated process whose results are manually recreated has low adoption even if the tool shows many runs.

Assign an owner to changed policies, source schemas, connectors, prompts and model versions. Re-run relevant regression cases after changes, inspect a bounded real run and verify monitoring before relying on new metrics. Keep the former manual path usable until recovery is credible. Decide whether to repair, narrow scope or retire the automation when quality or economics degrade.

Deliver a decision sheet with observed outcomes, uncertainty, failed segments, released capacity by role, continuing burden and the next boundary proposed for expansion. Cash savings require evidence of spend actually reduced. A controlled comparison can support a measured productivity claim within its tested population, not a universal multiplier.

Public methodology: [Anthropic's evaluation guidance](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) distinguishes tasks, trials, checks, traces and actual outcomes. The operating measures and rollout choices here adapt those ideas to internal business processes.

## Compare the result with a human doing the same work

[Anthropic's evaluation guide](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) distinguishes the claimed result from the observed system state. On a known week, compare each proposed exception with the original tracker. Score missed exceptions and invented exceptions separately.

[METR's developer experiment](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) found experienced developers took longer using early AI tools on their own repositories. That setting differs from a recurring operations review. Measure elapsed time, correction time and accepted results on comparable cases before claiming savings. If corrections consume the time saved, keep the comparison in draft mode.

## Test whether an assisted memo changes the decision for the wrong reason

[Emilie Choi on The Peel](https://www.thespl.it/p/the-coo-playbook-with-emilie-choi) recounts a country-entry memo whose risk detail obscured why the team wanted to enter. After the opportunity was reframed, the proposal was approved. The interview establishes a change in approval. The investment return remains unknown.

Give the writer the same underlying evidence twice. Ask for the customer opportunity, downside range, unresolved facts and next commitment. Have the recommender defend both upside and downside without the draft. If they cannot explain the trade, send the memo back before an executive review.

# Process contract and run operations

Use this reference when translating an operating process into something that can run repeatedly and recover. Produce a filled contract and inspect it against one routine case, one ambiguous case and one failed dependency. It is a specification for existing systems or a bounded implementation, not a requirement to build an orchestration application.

## Decompose the work

| Step | Input and source | Method | Output | Check before next step | Owner of exception |
|---|---|---|---|---|---|
| Identify item | Authoritative key and source version | Exact lookup/rule | One eligible record | Unique, current, permitted | Process owner |
| Calculate | Typed amounts, units and dates | Script or formula | Reconciled figures | Totals, units, rounding and missing fields | Analyst |
| Interpret | Approved documents and bounded question | Language model if it outperforms alternatives | Structured proposal with evidence spans | Allowed values, citations and contradiction checks | Domain reviewer |
| Decide | Checked proposal and applicable policy | Rule within delegated bounds, otherwise human | Decision plus policy version | Authority, limits and current facts | Decision owner |
| Act | Approved decision and target record version | Authorized system operation | Receipt or unresolved result | Read-back of actual target state | Technical operator |

Do not use a language model to replace a deterministic join, calculation or permission check. Conversely, a long rules table may be a poor fit for variable language interpretation. Test both against the same cases. If the next step depends on a model-generated field, validate the field before it reaches an external write.

## Data and action contract

Fill the following for each system boundary. A boundary is a read, write or transfer between sources with different owners or controls.

| Contract field | What to specify |
|---|---|
| Authority | Business owner, technical operator and exact delegated action |
| Input | Source system, record key, schema, units, source version and timestamp |
| Freshness | Maximum source age and what to do when exceeded |
| Identity | Business item key, run ID and stable identity for each intended action |
| Read scope | Permitted records/fields and authoritative source for conflicts |
| Write scope | Target system, permitted fields, amount/volume limits and blocked actions |
| Validation | Required fields, allowed values, reference integrity and preconditions |
| Evidence | Source references, calculation version, policy/prompt/model/tool versions where relevant |
| Concurrency | Expected record version or other check that stops overwriting a newer change |
| Approval | Named authority, approved payload, expiry and conditions requiring new approval |
| Completion | Target state and receipt to verify, independent of generated completion text |
| Data handling | Approved environment, retention, redaction and access requirements |

Persist enough to explain what happened without copying sensitive source content unnecessarily. Keep observed facts, inferred classifications, policy decisions and executed actions in separate fields. When facts disagree, preserve the conflict and authoritative resolution instead of silently overwriting it.

An example run record:

```json
{
  "item_id": "EX-104",
  "run_id": "run-104-2",
  "source_version": 7,
  "state": "awaiting_approval",
  "proposed_action": {"kind": "create_review_task", "queue": "billing"},
  "action_id": "EX-104:create-review-task:policy-3",
  "evidence_refs": ["invoice:104:v7", "order:201:v4"],
  "check_results": {"totals_reconcile": true, "duplicate_found": false},
  "approver": null,
  "receipt": null,
  "attempts": 1,
  "exception": null
}
```

This is an illustrative schema, not a required product interface. Add timestamps, costs and versions needed for the actual process. Do not store hidden model reasoning as an audit requirement. Store inputs permitted by policy, actions, evidence and concise decision reasons.

## Bound autonomy

Specify the action, eligibility and stop conditions together. For example: create an internal review task only for an exact known account, a unique exception key and a checked amount within a delegated limit. Escalate unknown accounts, stale sources, policy conflicts, disputed amounts and requested actions outside the contract. Drafting a message and sending it are separate permissions.

Decide which controls must operate outside a model's judgment: credential scope, amount caps, allowed destinations, approval enforcement and duplicate protection. Treat model-produced tool arguments as untrusted until these checks pass. Untrusted document instructions cannot change those controls.

Set attempt, elapsed-time and cost budgets before a recurring run. Use a specific fallback or exception state when a budget expires. Open-ended retries hide cost and can repeat external actions.

## Run states and recovery

| State | Meaning | Allowed next action |
|---|---|---|
| Received | Input recorded, no action taken | Validate identity and freshness |
| Validated | Preconditions and read scope pass | Calculate and propose |
| Awaiting approval | Proposal complete, write not authorized yet | Obtain approval or expire |
| Ready | Exact action authorized and preconditions current | Attempt the permitted action |
| Executing | Request issued | Record receipt or classify uncertainty |
| Reconcile | Remote outcome unknown, such as a timeout | Inspect target by stable action identity |
| Completed | Required target state verified | Report completion once |
| Exception | Requires owner action | Resolve with evidence, resume from verified checkpoint or cancel |
| Cancelled | Explicitly abandoned with reason | No automatic resumption |

Before retrying a timed-out write, check whether it already succeeded. Use a supported idempotency key, meaning the target treats repeated requests as the same action. A local completed flag cannot guarantee this across a remote failure. If the target lacks suitable duplicate prevention or reliable lookup, quarantine uncertain writes for reconciliation rather than guessing. Never describe a compensating action as a true reversal when downstream effects remain.

For partial completion, record each side effect and resume only the missing authorized action. If data or approved payload changes, invalidate the old approval and establish a new action identity as appropriate. A new run ID alone is not permission to repeat an old side effect.

## Operate exceptions and observe outcomes

Each queue item needs category, impact, item/run/action IDs, last known state, evidence, owner, next action, due time and retry history. Distinguish missing data, ambiguous policy, model error, permission denial, service failure and unknown write outcome. Route each to the person who can resolve it. Define who covers absence and who can stop new work.

Track arrivals, completions, backlog age, oldest high-impact exception, duplicate/unauthorized actions, accepted quality, human minutes, cost and runtime. Count no-output and stuck runs. An alert needs an owner and an action, such as pausing writes when reconciliation cannot establish target state. Review whether monitoring actually detects a seeded failure.

Public methodology: [Anthropic's design patterns](https://www.anthropic.com/engineering/building-effective-agents) inform simple decomposition. [AWS's retry-safety discussion](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) explains why action identity and remote side effects matter. The contract and state model above are adaptable operating recommendations, not provider guarantees.

## Run a known week before scheduling the next one

[James Raybould](https://myrunbook.ai/operator) starts with the trackers the team actually uses and the people who attend the review. Grant read access or supply an export. Choose a past week whose outcomes an owner can check.

| Routine | Read and compare | Acceptance check and receiving record |
|---|---|---|
| Numbers that moved | Compare the same metric version, cohort and period. | Trace each figure to its source. Send unexplained moves to the analysis queue. |
| Weekly review | Reconstruct changes, late items, blockers and decisions since the prior review. | Check blocker ownership and three decisions against the known week. Send the pack to the review owner. |
| Blocked work | Compare the blocker, elapsed time and accountable person. | Include a blocked item missing its owner in the exception queue. |
| Dropped handoffs | Match sender, receiver and later movement. | Exclude work that moved after transfer. Send stalled work to the receiving owner. |
| Duplicate work | Compare the inputs, output and recipient for two recurring tasks. | Have both owners confirm overlap before proposing to retire either task. |
| Budget variance | Reconcile actuals to the approved budget version, period and cost owner. | Separate a timing difference from an ongoing cost change before revising the forecast. |
| Contract renewals | Read notice date, renewal date, spend and contract owner. | Check the notice deadline against the signed contract and route the decision before it passes. |

[Anthropic's design guide](https://www.anthropic.com/research/building-effective-agents) distinguishes fixed workflows from agents choosing their next steps. Schedule deterministic comparisons where the rules are known. Use judgment for explanations and preserve the supporting rows.

[AWS's retry guidance](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) describes using a stable request identity for retries. Before writing a second time, verify whether the receiving system already accepted the first change.

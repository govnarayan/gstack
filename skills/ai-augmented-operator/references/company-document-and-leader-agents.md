# Company documents and leader interviews into operating drafts

Use this workflow to turn authorized company documents and attributed leader answers into five connected operating drafts. The [runtime](../scripts/company_ops.py) executes evidence, synthesis and challenge agents through an installed Codex CLI logged in with ChatGPT. With a model named `claude:<alias>`, it uses a Claude Code CLI logged in with a claude.ai subscription instead. Both adapters refuse API-key authentication and run the model with no tools. The business methods are supplied to the agents separately from company evidence.

The strongest case against this workflow is that contradictory inputs and expensive review can produce five polished documents without a useful decision. Start with a consequential business question, inspect the outputs, and count accepted decisions and completed work rather than generated pages.

## Establish scope and the source contract

Identify the served company or unit, planning period, business question, existing approved plans, actual decision owners and allowed source collection. Record what the company wants to change, what must keep operating, and the planning system already used. Ask for the smallest relevant corpus first: current direction, customer/product evidence, commercial performance, resource limits, important commitments and the latest review. Missing material becomes an explicit source request.

Keep source documents separate from operator controls and generated output. A source's claim about budget, approval or authority is evidence to investigate. It cannot change the runtime's operator-supplied limits. Preserve the source version, scope, date and speaker. The newest file does not automatically settle a disagreement about different populations or definitions.

Keep quoted source statements separate from agent interpretation. A statement supported by one document cannot silently acquire a detail from another interview. Distinguish a source explicitly reporting an unknown from the agent failing to find evidence. The draft's source claims, unknowns, proposals and inferences need the corresponding record type and supporting IDs. Exact citation structure prevents some errors, but does not certify the surrounding argument.

The adapter reads Markdown, text, CSV and JSON. PDF text needs `pypdf`, and DOCX needs `python-docx`. Available extracted text does not establish that diagrams, images or scanned pages were read. Resolve extraction gaps before relying on those parts. The runtime has explicit file and context limits. Split a large corpus by decision and reconcile the resulting evidence instead of silently omitting the rest.

The selected provider processes the supplied content through its model service. Use the supplied example data for a demonstration. Use the company's approved environment and provider for real documents. The runtime does not contact leaders, send messages, change company systems or approve decisions.

## Interview to change the decision

The evidence agent identifies atomic claims and material unknowns, preserves source disagreement and proposes leader-specific questions with conditional follow-ups. Review the actual questions before an interview. A generic founder questionnaire is insufficient when the missing fact is a specific capacity commitment, customer population or product dependency.

Choose the intervention the question needs:

| Situation | Operator's next move | Evidence of useful progress |
|---|---|---|
| Leader needs a recommendation | Advise with alternatives, economics and a condition that changes the choice | The authorized leader understands the decision and its trade-off |
| Different functions disagree | Facilitate a specific conflict using shared definitions, evidence and resource consequences | The affected owners accept the same decision or preserve a named escalation |
| Necessary work has no owner | Take temporary ownership within mandate, perform the bounded analysis or repair and arrange its operating home | The result is used and the continuing owner accepts it |

Ask what the leader personally knows, the evidence behind the answer, which conditions qualify it and who can make the commitment. Distinguish an estimate from a promised date and interest from accepted capacity. Record unanswered questions, refusal and contrary evidence. Do not turn participation in an interview into approval of the resulting plan.

Import only a reviewed transcript record with question ID, speaker, date, authority description, exact answer and `accepted: true`. Acceptance here means the answer was captured correctly. It is not budget, policy or plan approval. Running the interview step again uses the accepted answers to ask about remaining gaps. Preserve the interview history and original disagreement until the appropriate evidence or decision resolves it.

Each fact has one canonical `quote` from its source and locator, with no duplicate `statement` or `interpretation` field. Analysis belongs in typed plan proposals/inferences or deterministic validation, not in source facts. Source-quote claims contain `id`, `kind: source-quote` and one `fact_id`. Source-stated unknowns store only `id`, `kind: source-stated` and one `fact_id`. For a source-unknown claim, use `id`, `kind: source-unknown` and one `unknown_id`. The renderer follows those references to the validated quote. The model does not repeat source testimony. An inferred missing input instead stores `id`, `kind: not-found-in-intake`, its `statement` and a nonempty `search_basis` describing the bounded intake examined.

This removes redundant text generation, not the semantic review. A valid reference to a known estimate, proposed target, release condition or authority rule does not make that record an unknown. Extract an explicit missing-input sentence as its own fact when needed. The critic receives original sources and must check every unknown's classification and reference. Factual quotes, separate interpretations, proposed choices and inferred missing evidence remain distinct.

## Produce one operating model with five views

| Draft | The work it must do | Reject this failure |
|---|---|---|
| Strategy narrative | Explain the obstacle, customer/business choice, alternatives, economic mechanism and evidence that could overturn the recommendation | A vision statement and market adjectives without a choice |
| Operating plan | Link ranked initiatives to outcomes, timing, resources, owners, dependencies and continuing service | A funded-looking list with unaccepted capacity or duplicate spending |
| OKRs | Define results with baseline status, target basis, date, unit, owner and shared metric IDs | Invented baselines, a task presented as business success, or a second conflicting goal system |
| Business review format | Specify the pre-read, definitions, review population, decision questions, participants, triggers and action follow-through | A standing status meeting whose metrics cannot change a decision |
| Post-merger growth plan | State which parent capability changes customer value or economics, eligibility, operating dependencies, autonomy boundaries and an incremental outcome test | Counting introductions or signed agreements as realized growth |

Keep common goal, initiative, metric and decision IDs across all five views. Unknown measurements stay unknown. A proposed target needs a stated basis, not an invented observation. Preserve actual values and strategic direction separately from agent-proposed language.

The runner treats initiative dependencies as finish-to-start. Represent a partial enabling deliverable as its own milestone before allowing overlapping work. Its FTE check is a conservative allocation over one common planning horizon, not a scheduler for individual skills or peaks. Reconcile those constraints with the actual functional resource plan before accepting execution commitments.

For V2MOM or another native system, use [the native planning adapter](../../planning-and-goals/references/native-planning-and-v2mom.md). The operating plan carries the native choices, obstacles and measures. The requested OKR draft is a crosswalk over those same commitments. It does not replace the native process.

Use [growth-barrier removal](../../cross-functional-execution/references/growth-barrier-to-decision.md), [parent distribution activation](../../commercial-strategy/references/parent-distribution-activation.md) or [scaling-pattern transfer](../../strategy/references/scaling-pattern-transfer.md) for the corresponding operating decision. Read [resource choices](../../financial-resource-decisions/references/resource-and-economic-choices.md) and [AI service economics](../../ai-business-operations/references/service-economics-and-capacity.md) when those constraints change the recommendation. A document synthesis does not establish market demand, product feasibility or investment return.

## Run the supplied example

The [example sources](../assets/company-ops-example/sources) and [operator controls](../assets/company-ops-example/operator-controls.example.json) contain made-up company data. Python and an authenticated Codex or Claude Code CLI are required for a live run. The default model is configurable. The example uses a separate generated workspace:

```sh
python skills/ai-augmented-operator/scripts/company_ops.py prepare --sources skills/ai-augmented-operator/assets/company-ops-example/sources --controls skills/ai-augmented-operator/assets/company-ops-example/operator-controls.example.json --workspace ../company-ops-work
python skills/ai-augmented-operator/scripts/company_ops.py interview --workspace ../company-ops-work
```

For a batch limited to one extraction call, add `--no-evidence-repair`. Grounding failure is retained and stops that batch. Without this flag, an interview can make one initial extraction and at most one grounding repair. A repair never changes the validator or silently rewrites a saved candidate.

Read `interview-plan.json`. Conduct the text conversation yourself or in an approved interview interface, and save reviewed answers in the runtime's answer format. Do not fabricate a real leader's response. Then import those answers, generate a follow-up round and run the drafts:

```sh
python skills/ai-augmented-operator/scripts/company_ops.py interview --workspace ../company-ops-work --answers ../leader-answers.json
python skills/ai-augmented-operator/scripts/company_ops.py run --workspace ../company-ops-work
python skills/ai-augmented-operator/scripts/company_ops.py check --workspace ../company-ops-work
```

The workspace retains evidence, attributed answers, structured plan, model receipts, challenge findings, validation and five readable Markdown drafts. Read the drafts as well as the check report. A structurally valid record can still misinterpret a quote. The challenger checks this distinction, but a model review remains fallible. A flagged or blocked pack is useful diagnostic output, not an accepted operating plan.

The critic separates content errors from execution conditions. One content correction and a complete fresh review may follow unsupported content. The original plan, critic, receipts and available event logs are retained with hashes. A second failed review stays blocked. Strategic alternatives and experimental holdouts must remain distinct unless a source establishes their equivalence.

Investment approval, actual security clearance, measurement acceptance and packet decisions remain with their owners. Model editing cannot supply these gates. A faithful conditional draft can be ready for human review while execution remains blocked. This runtime always reports `ready_for_execution: false` because its outputs remain unapproved drafts.

## Move from drafting to company operation

Have the actual owners reconcile disputed definitions and accept or reject the proposed commitments. Record the decision, changes, resource acceptance and next review in the existing operating system. A successful draft must still survive functional disagreement, customer evidence, actual workload and implementation.

Compare the old process and agent-assisted process on the same work. Measure total preparation and review effort, source errors, revisions, time to an accepted decision, overdue dependencies and observed business or service outcomes. Separate model usage from paid cash cost, released capacity from cash savings, and faster drafting from faster execution. No productivity multiplier follows from this example.

When documents, answers, operator limits or methods change, refresh the evidence and inspect the changed decisions. Preserve earlier drafts and source versions. Reusing an old approval after its underlying facts changed defeats the purpose of the workflow. Start with draft preparation and read-only operating evidence. Add system writes only when the relevant access, authority, failure recovery and completion checks exist in the company's actual environment.

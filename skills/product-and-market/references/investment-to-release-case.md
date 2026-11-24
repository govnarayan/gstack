# From evidence to a product investment and release

Use this reference when discovery must change a resource choice and survive into delivery. The procedure and examples are original synthesis. All organizations, observations, costs, thresholds, and results are synthetic practice inputs. They are not market estimates or recommended universal thresholds.

## Keep one chain from evidence to decision

Carry an evidence identifier from the raw observation into the problem claim, solution assumption, test, investment decision, requirement, and post-release result. A chain can be one short record for a small team or links across existing research, planning, and delivery systems in a large company. Do not create a second master tracker.

| Link | Question the record must answer |
|---|---|
| Observation → problem | What happened, to whom, when, and relative to which alternative? How was this person or account selected? |
| Problem → solution | Which mechanism would remove the obstacle? What materially different mechanism could work? |
| Solution → test | Which assumption could make the investment wasteful? What result changes the next commitment? |
| Test → investment | What passed, failed, or remains unknown? What is the next bounded spend and scarce capacity? |
| Investment → delivery | Which behaviors, limits, failure paths, and obligations must hold for the chosen promise? |
| Release → decision | Did users receive the intended value, at the expected operating cost, and what changes now? |

Choose the relevant method from [Jobs to Be Done](../../../frameworks/references/customer-growth.md#jobs-to-be-done), [Value Proposition Canvas](../../../frameworks/references/customer-growth.md#value-proposition-canvas), or [Build-Measure-Learn](../../../frameworks/references/customer-growth.md#build-measure-learn). Use the [strategy skill](../../strategy/SKILL.md) if evidence would change company markets or advantage. Product prioritization cannot silently authorize that change.

## Continuous case: a consumer AI planning assistant

A US seed company with 14 employees is finding fit for a consumer meal-planning assistant. The founder owns the investment decision. A delegated BizOps operator owns evidence synthesis and the bounded pilot. Engineering validates technical feasibility and quality. Specialist review sets relevant product safety requirements. The proposed investment is six engineer-weeks to automate grocery ordering. The decision is whether to fund that work, fund a smaller intervention, or stop.

### Establish the problem and alternatives

Research includes 20 participants selected for having attempted a weekly plan in the last month: eight current users, six unsuccessful trials, and six users of alternatives. This deliberate sample can reveal different obstacles but cannot estimate population prevalence.

| Evidence ID | Observed evidence | Interpretation and limit |
|---|---|---|
| E1 | Eleven participants show a recent abandoned plan. Eight of those eleven report missing pantry information | Pantry uncertainty is a candidate cause. Interview frequency alone does not prove causation. |
| E2 | Six participants show repeated manual edits to a shopping list. Four overlap with E1 | Editing burden is distinct. Do not add eleven and six as seventeen independent affected people. |
| E3 | Five participants use a retailer's existing ordering workflow and decline an in-app payment trial | Ordering is not established as the binding problem for this group. |
| E4 | Engineering's representative task set exposes incorrect pantry assumptions in generated lists | Technical evidence supports testing confirmation, not an unqualified claim of safe autonomous ordering. |

The opportunity is completing a usable plan with known ingredients. Compare autonomous ordering, a pantry-confirmation step, a manually assisted planning service, and the current experience. The strongest argument for ordering is a complete consumer outcome with less switching. Against it, payment, inventory, substitutions, recovery, and support introduce commitments before evidence shows ordering is the obstacle. The smaller step tests the implicated failure at lower commitment.

### Set a bounded decision before testing

The team chooses a directional pilot with 40 eligible new participants assigned at random to each of two experiences. All 80 have a full seven-day observation window and the same recruitment path. The user-valued result is completing and using a plan, verified by a follow-up record of a cooked meal. Fund the next pilot only if at least 12 of 40 succeed with confirmation and no more than 8 succeed in the current experience. Require zero unresolved critical failures and delivery cost of at most $4 per successful user. This is a rule for funding the next pilot, not a statistical claim about a population effect. If uncertainty remains too large for the proposed next spend, recruit further before committing.

The exposure is capped at 80 people, two engineer-weeks, and $500 of pilot operating cost. Engineering time is tracked separately from the operating-cost cap and per-success delivery cost. Acquisition spending is outside this test and remains unvalidated. The team separately defines critical failures with the specialist owner. A small test never waives required controls.

Synthetic results: confirmation produces 14 successful users out of 40. Current experience produces 8/40. The observed difference is 35% − 20% = 15 percentage points. Delivery cost includes $28 in model and tool use plus six reviewer hours at an assumed $30 per hour. That totals $208, or $14.86 per successful user. The hourly rate is a synthetic company input, not a claim about market wages. Engineering used one of the two reserved engineer-weeks, leaving one unspent week. No critical failure remains unresolved in the examined tasks.

The user-result condition passes, but the economic condition fails: cost is `(28 + 6 × hourly rate) / 14`. The $4 ceiling permits at most `(56 − 28) / 6 = $4.67/hour` at this review volume. The assumed $30/hour is far above it. A useful pilot record preserves this split judgment instead of celebrating the conversion result as overall validation.

Decision: do not fund autonomous ordering or scale the assisted confirmation process. The founder reallocates the one unspent engineer-week to test whether users can confirm pantry information without reviewer intervention at acceptable quality. The broader ordering proposal's six weeks remain unfunded. The next test must reduce paid review to at most 0.93 hours for 14 successful users at the assumed $30/hour rate: `(14 × 4 − 28)/30`. Extra model cost would lower that allowance. The reversal condition is measured review/quality performance that makes the $4 ceiling feasible. The price and willingness to pay remain separate unknowns.

### Turn that decision into a deliverable brief

| Brief field | Populated record |
|---|---|
| User and problem | Weekly planners with uncertain pantry information abandon usable plans. E1/E4 support testing explicit confirmation. |
| Intended outcome | Complete and use a plan without hidden reviewer labor beyond the stated cap. |
| Chosen behavior | Show pantry assumptions for confirmation before generating the final shopping list. Users can correct or remove each assumption. |
| Non-goals | Payments, autonomous ordering, retailer inventory promises, and a general pantry database. |
| Acceptance | A confirmed ingredient changes the generated list. A removed ingredient is not treated as available. Abandoning confirmation does not submit an order. Generation failure retains edits and offers recovery. Technical owners add specialist-defined quality cases. |
| Evidence still needed | Reviewer hours, task quality, success rate, and actual cost on the new representative task mix. Passing behavior tests alone does not validate these outcomes. |
| Dependencies | Engineering validates quality and effort. Product/founder approves the promise. Support owner can handle the bounded test population. |
| Resource and release | One engineer-week for this test. Founder decides further investment after cost and quality review. No release to all users is implied. |
| Recovery | Disable the new flow if critical failure or uncontrolled review load appears. Preserve user edits and route affected users to the agreed support path. |

In a subsequent synthetic run with the same 40-user treatment bound, 14 succeed, model/tool use costs $28, and review takes 0.8 hours at $30/hour. Delivery cost is `(28 + 24)/14 = $3.71`. If specialist quality and the predeclared comparison rule still hold, this supports a further bounded pilot. It does not establish willingness to pay, sustained use, a scalable acquisition channel, or the ordering investment. Carry those unknowns into the next decision instead of silently promoting the prototype into a roadmap commitment.

### Size the reachable opportunity without using a market percentage

For this stage, a reachable pilot bound can be more useful than a total-market headline. Suppose the next channel can reach 600 eligible people during the period, 20% try, and 35% of those complete and use a plan. That yields 120 trials and 42 successes. A seven-hour reviewer budget at 0.8/14 hours per success supports 122.5 successes before rounding down, so the 42-success forecast fits that simple labor envelope. Check peak timing and task mix separately. The channel assumptions remain hypotheses and 42 successes are not paying customers.

If the team adds a price, model purchases and retained use separately, using observed evidence. Route market entry or company resource reallocation to strategy and financial-resource decisions. Do not turn “many people plan meals” into obtainable revenue.

## Change the experiment when the product mechanism changes

| Context | Evidence and calculation that changes the decision | Delivery implication |
|---|---|---|
| Enterprise software | A pilot user completes the task, but procurement requires deployment review and a budget holder's conditional purchase. Record each condition and cost rather than counting a champion's enthusiasm as revenue. | Specify permitted data, deployment boundary, implementation owner, service readiness, and what Sales may promise. |
| AI infrastructure | A customer needs 800 accepted jobs/day. Measured usable capacity is 600 under its latency and reliability constraints. A benchmark at idle load does not clear the 200-job gap. | Technical owner verifies representative load and failure recovery. Product owner chooses narrower service or added capacity before dates are promised. |
| Physical or hardware system | Twenty preorders do not establish deployability. With four installation crews completing two units/week, eight units/week can be installed; 24 ready units require at least three installation weeks before travel, variability, and failures. | Include hardware version, installation/site conditions, field reliability, parts, support, recovery, and the technical/safety owner's release evidence. Cash deposits and warranty obligations route to Finance. |
| Marketplace | Forty buyers and forty suppliers do not establish usable liquidity. If ten matched attempts yield six completed transactions, investigate geography, scheduling, price and failed matches before subsidizing more signups. | Define both sides' obligations, transaction completion, dispute/recovery paths, and who bears incentive cost. |
| Developer platform | Thirty issued keys, twelve working first integrations, and three production deployments are different steps. A successful demo using one endpoint cannot prove migration compatibility. | Specify supported version, authentication, quotas, deprecation policy, dependency owner, and a failure/recovery example in the integration contract. |
| Mature multi-product unit | A proposed feature creates $200k of gross contribution but displaces $150k in an existing product and adds $80k of support cost: estimated company effect is −$30k before other effects. | Show local and company economics separately, preserve migration commitments, and use established Product/Finance decision rights. |

For a public-company business unit, the CoS/S&O operator prepares the evidence and resource recommendation using existing Product, Research, Engineering, Finance and control forums. For a small startup, explicit delegation can put hands-on discovery and delivery coordination with the operator. Neither context makes technical quality or employment in a famous company evidence of demand.

## Review the finished record

Ask another reader to trace one accepted requirement and one rejected option back to the raw evidence. Recompute the most consequential cost or capacity result. Remove unsupported precision, after-the-fact thresholds, mixed populations, and claims beyond the test's reach. The output is complete when the authorized owner can choose the next commitment and the delivery owner can act without inventing the missing promise.

## Separate the feature, the platform and the customer's exit

[Stadia's earlier decision](https://blog.google/products-and-platforms/products/stadia/focusing-on-stadias-future-as-a-platform-and-winding-down-sge/) ended further investment in its own studios while leaving a partner platform open. Later, [Phil Harrison](https://blog.google/products-and-platforms/products/stadia/message-on-stadia-streaming-strategy/) reported insufficient consumer traction and announced the consumer shutdown.

For a technically successful pilot, record three separate decisions. Can the team deliver the service? Will enough customers keep paying? Will a partner commit enough volume to sustain the platform?

Give each decision its own evidence and deadline. Where payment depends on an uncommitted partner, limit investment to a dated trial and price the customer exit. Include refunds, migration and the period during which customers can recover their work.

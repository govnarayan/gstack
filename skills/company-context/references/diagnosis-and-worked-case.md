# Diagnose the operating problem

The output is a decision-ready account of context, not a company profile. Use the smallest investigation that can distinguish plausible explanations. The procedures and example here are this library's synthesis. The example is synthetic.

## Work backward from the proposed action

1. Write the action the user is considering and its alternative. “Add a program manager” competes with clearer delegation, reducing commitments, repairing an input, or retaining direct coordination. What must be true for the proposed action to help?
2. Select a recent completed case, an open case, and a countercase where the same process worked, if available. State the selection rule and do not claim this is the full distribution. For a recurring problem, inspect the complete relevant work population when practical and report its actual bound.
3. Trace each case from request through decision, work, acceptance and use. Capture timestamps, wait versus active effort, actual decision owner, changed requirements, rework, available skills and outcome. Ask what the proposed fix would have changed at the precise failure point.
4. Compare the explanations below. Several can apply to different cases. Resolve missing facts only when they would change the recommendation, authority or risk. A missing org chart is less valuable than the disputed approval that stops tomorrow's work.

| Competing explanation | Discriminating evidence | Consequence if supported |
|---|---|---|
| Authority or interface | Work waits for competing approvals despite enough evidence and available capacity. A similar case with accepted delegation moves. | Define the disputed decision boundary and escalation, then verify an actual decision. |
| Capacity or skill | Authorized, ready work queues behind committed work requiring the same scarce skill. | Stop, sequence, reduce scope or add credible capacity. An owner chart cannot create hours. |
| Information or process | Decisions are repeatedly returned for the same missing input, or complete cases move while incomplete cases wait. | Repair intake or information flow and test exceptions. More status collection can worsen the queue. |
| Strategy or incentive | Teams follow clear local directions that produce incompatible business results, or leadership repeatedly changes the choice. | Resolve the underlying choice or incentive with its owner before enforcing the plan. |

Use [flow analysis](../../../frameworks/references/operations-flow.md#value-stream-mapping) when elapsed time is unexplained. Use [decision roles](../../../frameworks/references/decisions-uncertainty.md#rapid) when approval boundaries are contested. Use [organization design](../../../frameworks/references/organization-change.md#star-model) when several design elements conflict. Read the chosen method and execute it. Do not turn this diagnostic list into a universal score.

## Resolve context and authority separately

A useful context statement connects facts to the decision. The company employs 46 people. This initiative depends on two staffed functions whose priorities the coordinator cannot change. The first clause alone cannot select a process.

For each consequential decision, establish the actual actor, object, limit and exception. “Own the launch” is incomplete if it leaves product scope, customer promises, spend and technical release authority ambiguous. Record which of those the operator may change, which requires approval, and what evidence establishes the delegation. A proposed mandate stays proposed until accepted by someone able to grant it.

For conflicting source statements, compare scope, definition, effective date and status before choosing a value. An HR report of 46 current employees and a plan for 60 year-end positions can both be correct. Retain both with their labels. If two current sources disagree on who may approve spend, mark that right unresolved and seek the delegation owner. Do not average, choose the newest mention automatically, or infer authority from access to the budget.

State the question, competing causes and evidence, recommendation and strongest alternative. Name the authority needed, who will resolve the remaining unknown and the next test. An unknown can block a commitment while leaving analysis or reversible preparation possible.

## Executed case: missed integrations at a small company

Question: “Should we add a weekly steering meeting because integrations keep slipping?” Context: a US private B2B SaaS company, 46 employees, post-fit product, enterprise sales, emerging operating practices. The operator coordinates a six-person initiative across Product and Engineering and cannot change either function's priorities. Those values are supplied inputs, not inferred from the company size.

The complete six-integration population from the last two weeks shows four missed dates. Three waited for a choice between conflicting Product and Engineering scope requests. Each consumed two hours of chasing across the participants. One had an accepted scope but required 28 specialist hours in a week with only 16 available after service obligations. Two finished on time with a named scope decider and accepted inputs. The evidence supports two mechanisms, not a uniform “lack of accountability” verdict. The successful cases weaken the claim that every integration needs a committee.

The recommendation is to ask the sponsor to name a scope decider within existing budget and customer promises, with functional escalation for exceptions. Keep that proposal distinct from approval. Reduce or defer 12 hours of the capacity-constrained case, or obtain a qualified person's accepted availability. A weekly meeting cannot repair that arithmetic and may miss a decision needed the following morning.

The strongest case for a steering meeting is that leadership must resolve recurring conflicts across a portfolio, beyond the scope decider's authority. That would become preferable if the observed exceptions repeatedly cross budget, service or contractual boundaries. The test here does not establish that condition.

Test cost before adding coordination. Suppose the proposed intake check takes 15 minutes per integration plus a 30-minute weekly review. At the observed three integrations per week, effort is `3 × 0.25 + 0.5 = 1.25 hours/week`. The observed chasing burden is `3 blocked × 2 hours / 2 weeks = 3 hours/week`. If the new mechanism removed all of it, the maximum modeled saving is 1.75 hours/week. This is an upper bound, not a result. It excludes setup and assumes the observed case mix continues. At half that effectiveness, net saving is only `1.5 − 1.25 = 0.25 hours/week`, so setup or new rework could eliminate the benefit.

At the same failure mix, full effectiveness saves one hour per integration. The proposed process breaks even on recurring effort at `N × 1 > 0.25N + 0.5`, or more than two-thirds of an integration per week. At half effectiveness, the threshold is more than two per week. These are workload-specific thresholds, not headcount rules. Lower volume can favor direct owner-to-owner resolution.

The brief therefore requests a four-week bounded test, chosen to observe several integrations at this volume. Record waiting time, chasing effort, scope reversals, unresolved exceptions and service consequences across all cases. The sponsor resolves the scope right before the first affected commitment. Reopen the mechanism if chasing remains, exception review costs more than it saves, or one team loses necessary review. Do not record the modeled benefit as achieved.

## The same symptom in other contexts

| Context | Evidence and recommendation change |
|---|---|
| Twelve-person pre-fit company | Check whether “slips” are deliberate changes following customer learning. A narrow learning commitment may be more useful than enforcing a delivery baseline. Direct founder/owner decisions can suffice. |
| Scaling multi-product business | Trace shared specialists and conflicting product commitments across the whole served portfolio. A local initiative can look staffed only because another team counts the same hours. Seek portfolio reconciliation through actual owners. |
| Forty-six-person unit in a public company with thousands of employees | Confirm enterprise platform dependencies and local delegation. The unit sponsor may set local scope but cannot grant enterprise release, security or budget exceptions. Use existing records and forums with those owners. |

The diagnostic output should change when these facts change. Merely substituting a company-stage label in the same recommendation fails this test.

## Find the fact the new leader does not know

[Claire Hughes Johnson](https://stvp.stanford.edu/wp-content/uploads/sites/3/2024/09/transitioning-to-a-new-company-transcript.pdf) describes learning Stripe's business, founders and vocabulary after Google. Before importing a process, ask an existing operator to walk through the last real decision using the company's own words. Check where the proposed process would change the outcome.

[Tim Cadogan](https://time.com/6117090/tim-cadogan-gofundme-ceo-interview/) asked internal experts to help him learn an unfamiliar sector. Assign each uncertain claim to someone with direct experience. Ask for a record or example that could contradict the initial explanation.

[Chief of Staff Network interviews](https://www.chiefofstaff.network/guides/chief-of-staff-first-90-days) describe finding informal influence through listening. Test a proposed sponsor's actual authority against a decision they made. A long listening tour is expensive when one signed allocation can settle the question.

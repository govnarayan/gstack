# Worked example: operating reviews and goal closeout

This continues the [synthetic onboarding plan](../../planning-and-goals/examples/onboarding-plan.md). All numbers and events are invented. The plan selected 24 specialist-days of onboarding plus 8 of instrumentation within 36 change-days. A later service shock narrowed the rollout and created K1-v2. The example demonstrates management decisions, not a company precedent or a causal study.

## Choose the rhythm

The founder wants a new WBR, MBR, QBR and a separate strategy meeting. The coordinator first inspects what is missing: weekly updates show feature progress but hide service demand, cohort maturity and resource collisions. Leadership can settle resource conflicts, while the coordinator can convene and escalate them.

The recommendation is one weekly exception review, replacing the existing status meeting. Once a month, that slot expands for driver diagnosis and forecast review. Quarter close contains a separate strategy question and next-portfolio decision. The strongest case for separate forums is deeper ownership and preparation. It loses at this scope because the same people and evidence serve all four questions. Reopen the design if distinct business units or unresolved specialized decisions make the combined forum ineffective.

Service incidents retain an immediate response route. A weekly meeting cannot protect a service whose action window expires before the meeting.

## WBR: expose the actual exception and act

At a May 21 review, the pack shows:

| Item | Evidence | Interpretation and decision |
|---|---|---|
| Original K1 | Full supported scope due May 15, canceled by authorized scope amendment | Do not call the original delivered. Inspect narrower K1-v2, due May 22 |
| K1-v2 | Acceptance tests scheduled for May 22, required Product and Support owners available | Keep date with explicit risk, do not count an unfinished checklist as passed |
| K2 May-entry activation | May 1-7 entries: 18/40 = 45% after full 14-day observation. Another 120 May accounts have insufficient observation time | Directional early evidence only. Neither 18/160 nor 45% is the final May-cohort result |
| K3 assisted effort | Mature subset: 1,080 minutes/40 accounts = 27 minutes | Above the 25-minute aspiration. Investigate failed imports and support allocation |
| Service shock | A reported week had 78/100 priority tickets answered within one business day, below the weekly 90% standard | Support uses the immediate response route. Verify recovery and the specialist allocation already authorized in D-03 |
| Capacity | Revised change effort is 30 days. By May 21, 29 are spent and one acceptance/handover day remains on May 22 | Verify the accepted final slot, other owners' acceptance work, and the remaining service schedule. Reserve and free slack were consumed by D-03, so any new demand needs another trade-off |

The WBR distinguishes observations from explanations. The preferred explanation is that failed imports create assisted work. The alternative is a change in incoming data quality. Data and Support will classify failed cases against predeclared reasons and sample completed cases as well, rather than reviewing only the failures.

The May 1 decision record D-03 authorized the resource response from its then-current snapshot: existing service 12 days, additional service 12, already spent change 16, and narrower remaining onboarding 14, totaling all 54 net days. Four remaining instrumentation days and two original onboarding days are postponed, four adaptation/handover days are added, and both reserve and free slack are consumed. The functional lead accepts the calendar, Product accepts the narrower scope, and the coordinator updates dependencies. Leadership records the lack of further contingency, not a claim that protection is solved. This is the historical amendment, not fourteen days of work newly authorized on May 21. Its accepted calendar allocated thirteen narrower-path days across May 4-20 and one final day on May 22. The May 21 pack shows thirteen of those fourteen days completed, which reconciles 16 + 13 = 29 spent and one remaining. The remaining specialist service slots are preserved in the linked plan.

The service owner checks recovery continuously through its existing route. The next WBR reviews recovery and unresolved demand, rather than waiting for the MBR to authorize operational action.

| Action | Owner | Due/evidence | Effect check |
|---|---|---|---|
| Validate source event coverage and mature/pending calculation | Data owner | Before next pack, reproducible counts and query version | No unsupported "all accounts" rate in next review |
| Classify sampled failed and successful import cases | Product + Support | One week, coded observations and alternative explanations | Decide whether guided scope or data-quality support changes |
| Finish and accept narrow K1-v2 | Implementation lead / Product acceptor | May 22, signed acceptance evidence and handover | Observe June cohort separately |
| Verify service recovery and specialist calendar | Support / resource owner | Immediate response and next WBR, ticket and calendar evidence | Weekly standard, backlog age and remaining capacity |

## MBR: change the forecast without erasing the target

At month close, the review compares closed results and unresolved hypotheses. The final May outcome window does not close until June 14, so K2 and K3 remain pending. The pack includes the mature subset and the pending count, with comparable account types. The team does not call an immature month's rate a final miss or success.

The Data owner finds that a dashboard used login as activation. The locked contract requires the first useful imported-data event. The dashboard is corrected and the affected past snapshot is restated with its version and counts. This repairs measurement, it does not lower the goal.

The revised final-May forecast is 48%, below the earlier funded-path estimate of 50% and the aspiration of 52%. Narrower and later exposure is the main timing limitation. The preferred operational explanation remains import friction, while poor data quality and underlying value remain competing explanations. Neither forecast revision nor a plausible story proves causality.

Leadership chooses to defer full expansion until the accepted narrow path has valid outcome evidence. That preserves the service allocation and prevents a second rollout from consuming an already exhausted reserve. It also delays potential growth and the analytics work. The case for expansion is faster access to more users. It would win if the additional capacity were demonstrated or the valid narrow-cohort evidence supported expansion within the existing envelope.

The MBR output is a revised forecast, a real scope/resource decision, and an evidence plan. The original 52% target and final June 14 evaluation date remain unchanged. Nothing here changes the annual spending authorization or external commitments.

## QBR: score the original cycle, then decide the next one

At the July 1 quarter-close review, the May-entry observation window has been closed since June 14. The final cohort has 200 eligible accounts, no pending observation windows, and 96 activated accounts. K2 is 96/200 = 48%. It improved 8 percentage points from the 40% baseline, or 20% relative. It missed the 52% target by 4 percentage points. Optional improvement progress is (48 - 40)/(52 - 40) = 0.667. Calling that "67% activation" would be wrong.

Assisted work totals 5,600 minutes for the same 200 eligible accounts: 28 minutes each. K3 misses the 25-minute condition. Improvement progress is (28 - 30)/(25 - 30) = 0.4. The team reports actual effort and the miss, not only the normalized score.

The thirteen weekly service populations each contain 100 tickets. Six illustrative weekly response counts are 92, 78, 90, 94, 94 and 92. The other seven each achieve 90. The quarter totals 1,170/1,300 = 90%, yet the 78% week breached the required weekly standard. Quarter aggregation cannot erase that breach. The response and recovery evidence remain part of the outcome assessment.

| Original or linked commitment | Result | Disposition |
|---|---|---|
| K1 full-scope path by May 15 | Canceled by authorized scope change before completion | Preserve canceled record and its cost. Link K1-v2 |
| K1-v2 narrower path by May 22 | Named acceptor passes checklist May 22 | Delivery achieved. Impact remains separate |
| K2 May cohort at least 52% by June 14 | 96/200 = 48%, improvement progress 0.667 | Aspiration missed, useful movement observed, causal attribution unproved |
| K3 assisted effort at most 25 minutes | 5,600/200 = 28, improvement progress 0.4 | Outcome condition missed |
| Weekly service response at least 90% | One week at 78%, recovery evidenced, quarter aggregate 90% | Operating breach remains reported |
| Instrumentation remainder | Four days postponed in approved amendment | Re-compete for next-cycle resources, no automatic carryover |

There is no valid composite "green" score for this objective. Delivery succeeded for the revised scope, activation improved but missed, assisted effort remained too high, and a service breach occurred. These findings call for different decisions.

## Re-test strategy and fund the next commitment

The evidence is consistent with onboarding friction but does not establish that guided self-service caused the improvement. The May cohort mixed old and new exposure, and the customer mix may differ from March. The strategy review separates that uncertainty from the observed improvement.

The hypothesis survives as a bounded next test. The alternative is that data quality, rather than guidance, dominates assistance. Leadership proposes continuing the accepted narrow path and testing a data-quality intervention before expanding supported account types. Funding remains subject to the next-period capacity and approval record below. Analytics remains postponed, with its keep case and opportunity cost recorded. Reopen expansion or analytics when the bottleneck changes or the strategic evidence changes.

June and July entrants remain observational cohorts under the accepted path. Do not assign an intervention target after those entrants have arrived. The new intervention uses an August-entry cohort so resource acceptance, target classification, and the metric contract can be recorded before August 1. The continuation is a new record, not a renamed May goal:

| New commitment | Contract |
|---|---|
| August-entry outcome check | Same locked eligibility and 14-day activation event. All August 1-31 entries mature by September 14. The available closed baseline is final May 48%, with exposure and customer-mix limits disclosed. Inspect later closed cohorts before authorizing the new target |
| Proposed activation target | 54%, a fresh aspiration requiring an approved capacity/evidence plan. The funded-path forecast remains 52% until supported by new evidence |
| Effort condition | At most 25 support minutes per eligible August-entry account by September 14, raw numerator and denominator retained |
| Service | Weekly response obligation retained, with coverage and immediate exception path |

This continuation requires next-period resource acceptance and goal classification before August 1. The QBR does not approve an unfunded target by writing it in a table. If capacity cannot support the intervention, keep a narrower learning commitment or defer the proposal explicitly.

## Test the record against misleading conclusions

| Tempting claim | Why the procedure rejects it |
|---|---|
| "The release was 100% successful" | Only the revised delivery acceptance passed. Impact and service conditions did not |
| "Activation is 67%" | 0.667 is normalized progress toward a 12-point improvement. The actual activation rate is 48% |
| "Service met its quarterly average, so no breach" | The agreed standard was weekly, and 78/100 failed that condition |
| "The intervention caused an 8-point gain" | Mixed exposure and cohort mix leave alternative explanations |
| "The goal can just roll into July" | Original May result is preserved. August-entry target is a separate linked proposal |
| "Reserve protected the launch and service" | Reserve and slack were consumed, scope reduced, and a breach still occurred. Protection needs further execution evidence |
| "New goal approved because all leaders saw the pack" | Actual resource and goal approval is still required from named owners |

The operating record makes the choices reviewable: what was observed, what was inferred, which commitment changed, who chose the trade-off, what work lost resources, and what evidence will decide the next investment.

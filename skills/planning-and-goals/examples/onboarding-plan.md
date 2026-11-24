# Worked example: faster onboarding with service coverage

Every fact and number in this example is synthetic. The example demonstrates planning decisions, not a forecast or benchmark for a real business. Continue with [the operating reviews](../../operating-cadence/examples/onboarding-reviews.md).

## Input and strategic choice

A small software business serves teams that need to import data before receiving value. Product's draft says "ship three onboarding features." Sales wants more new accounts, while Support says existing customers already consume its capacity. Leadership must choose what to fund next quarter with no new hires.

The source requests are distinct: Product asks for a release commitment, Sales asks for growth, and Support asks for reliable coverage. The planning recommendation is to fund a defined self-service path for a narrow customer segment, keep coverage visible, and defer the separate analytics feature. The strongest case for analytics is expansion value among existing accounts. It loses this cycle because it uses the same specialist needed to remove the entry barrier. Reopen it if the onboarding mechanism fails its evidence test or specialist capacity becomes available.

The strategy hypothesis is that small accounts abandon because the initial import takes too much assisted work. A guided self-service path should reduce that barrier. Competing explanations are poor source data and weak product value after import. Customer observations and failed-import logs remain necessary to distinguish them. Rising signups alone would not prove the strategy.

## Annual resource view and next-quarter choice

The longer direction is reliable self-service for the chosen segment. The annual resource plan holds existing staffing and proposes three conditional phases: prove onboarding impact, expand the accepted path, then consider analytics. Later phases remain unfunded options until their evidence and capacity are reviewed. A rolling view updates those options without changing approved spending automatically.

For the next quarter, the scarce implementation specialist has 60 scheduled days, 6 leave days, 12 days of existing service coverage, and 6 days explicitly reserved for incidents and uncertainty. Thus 60 - 6 - 12 - 6 = 36 change-days. The categories do not overlap.

| Candidate | Specialist-days | Benefit case | Critical condition |
|---|---:|---|---|
| Guided onboarding | 24 | Tests the entry barrier and improves activation | Product accepts supported account types and Support accepts handover |
| Import instrumentation | 8 | Makes failures and customer effort visible | Data owner accepts the definition and validation |
| Analytics feature | 20 | May support expansion | Same specialist, plus a separate customer acceptance test |

All three need 52 days, exceeding change capacity by 16. Onboarding plus analytics needs 44, exceeding it by 8. Leadership approves onboarding plus instrumentation: 32 days, leaving 4 unallocated change-days in addition to the separate 6-day reserve. Analytics is postponed. The plan does not create an analytics objective to give its sponsor representation.

Calendar check: onboarding needs 12 of its 24 days in weeks 3-4. Only 8 are available then after already scheduled coverage. The total-quarter plan fits but this dependency does not. Leadership moves 4 onboarding days to week 2 after Product accepts earlier scope definition. The commitment remains provisional until that acceptance and the specialist's calendar are recorded.

Other owners commit capacity in their own units: Product supplies acceptance and observation time, Data owns metric validation, and Support owns coverage and handover. Their allocations must fit their own calendars. The specialist table is the scarce-resource test, not the whole company's capacity plan.

## Goal form and measurement

Objective: make the supported small-account onboarding path useful without increasing assisted effort or weakening existing service.

| Commitment | Type and target | Baseline | Evaluation |
|---|---|---|---|
| K1: accepted self-service path | Committed delivery: named account types can import, handle specified errors, and reach the first useful result by May 15 | Acceptance checklist and existing manual path | Named Product acceptor signs with evidence |
| K2: 14-day activation | Proposed stretch: at least 52% of eligible May-entry accounts reach the useful event within 14 days | March-entry cohort: 80/200 = 40% | May 1-31 entrants, final observation June 14 |
| K3: assisted effort | Outcome condition: total support minutes through day 14 divided by eligible May-entry accounts is at most 25 minutes | March: 6,000/200 = 30 minutes per account | Same cohort and final observation date |

Standing service health: at least 90% of priority tickets receive a first human response within one business day, using the existing defined ticket population. This is an operating commitment, not an aspirational KR. Review breaches immediately through Support's established route.

Eligibility is locked before the May cohort: new external accounts in the supported segment, excluding staff tests and duplicate account IDs. Activation means the defined successful imported-data result event, not login or import start. Source versions, deduplication, time zone, and late events are recorded. This makes denominators for activation and effort compatible. All pending accounts are reported until 14 days mature.

The 52% target is a proposal based on a funded intervention hypothesis, not a known effect. At 200 entrants it implies 104 activated accounts, 24 above the 80-account baseline. The funded-path forecast is 50%, or 100/200. Leadership records the 52% aspiration alongside that forecast rather than changing the estimate to fit the target. No validated statistical or causal claim follows from those forecast counts.

K1 by itself could be achieved while K2 and K3 fail. The objective therefore needs both impact checks and the service condition. K2 at target cannot offset more assisted work or a service breach. No average across these four conditions can certify success.

## Alignment and decision rights

Product owns the objective and K1 acceptance. Data owns the metric calculation and evidence cutoff. Support owns service standards and K3 operational data. The implementation specialist's functional lead owns that resource. Leadership is the named arbiter when growth work and coverage conflict. The process coordinator can demand an update and escalate the choice, but cannot silently move staff.

Dependency record: Product supplies the supported account-type and error checklist in week 2. The implementation lead accepts it before the moved 4 specialist-days begin. Support accepts the handover guide and the live escalation path before exposure expands. If either is late, reduce rollout scope or move the delivery forecast and seek approval. A dependency request is not an accepted commitment.

## Mid-cycle shock and authorized amendment

At the May 1 amendment decision D-03, 4 of 8 instrumentation days and 12 of 24 onboarding days have been used. New service work requires 12 extra specialist-days. Existing remaining change capacity is 36 - 16 = 20 days: 16 approved work plus 4 unallocated. Using the 6 reserved days leaves 6 service-days to take from change capacity. Four are unallocated slack, so the net shortfall against approved work is 2 days.

Leadership compares keeping the full rollout while accepting weaker service, buying qualified capacity that can start on time, and narrowing the rollout while deferring instrumentation. No qualified supplier is available by the required date. Leadership protects service and chooses the third option.

The quarter's 54 net available days now reconcile as follows:

| Use | Days |
|---|---:|
| Existing service | 12 |
| Additional service | 12 |
| Work already spent: 4 instrumentation + 12 onboarding | 16 |
| Remaining narrower onboarding work | 14 |
| Total | 54 |

The narrower remaining work is 10 days to finish the core path plus 4 days to adapt handover and monitoring to the reduced rollout. The remaining 4 instrumentation days and 2 original onboarding days are postponed. Original planned work was 32 days, so the revised change effort is 32 - 4 - 2 + 4 = 30 days. Service is 24, totaling 54. Reserve and unallocated slack are fully consumed, a recorded risk that requires close review.

The accepted 2026 calendar makes the amendment feasible. Four existing service-days and the 16 change-days were spent before May 1. The specialist completes 13 narrower-path days on May 4-8, May 11-15, and May 18-20, with the last acceptance/handover day on May 22. May 21 supplies one additional service-day. The remaining 8 existing service-days and 11 additional service-days have accepted slots after May 22. Thus the post-amendment calendar contains 14 change-days plus 20 service-days, while leave remains excluded. Other owners accept their observation, acceptance, and coverage work separately. Immediate incident response is provided by Support, with specialist repair work sequenced by urgency. If that repair timetable cannot meet the service need, this plan must be amended again.

Do not rewrite K1 as achieved. The original full-scope May 15 commitment is closed as canceled by the authorized scope change. A linked K1-v2 commits the narrower accepted scope by May 22. Because rollout is later and narrower, K2 and K3 keep their original May-cohort definitions for a limited mixed-exposure observation. The predeclared treatment labels permit segment reporting, and the result cannot be attributed to the full intervention. A future-entry impact commitment is proposed separately, with its target and resources authorized before that cohort begins. The original 52% aspiration remains visible and will be scored at close.

## Constraint checks

| Injected failure | Expected decision |
|---|---|
| Add analytics without moving any work | Reject: 52 > 36 change-days |
| Approve total effort but ignore weeks 3-4 | Reject: 12 needed versus 8 available until 4 days are resequenced and accepted |
| Call all accounts under 14 days old failures | Reject the result: incomplete observation, pending accounts must be separate |
| Average a passed launch and activation score while service breaches | Reject the composite success claim and address service |
| Rename the May commitment to June after the delay | Reject silent carryover, preserve K1 and create the linked replacement |
| Claim 52% is a verified forecast | Reject: it is an aspiration, funded-path forecast is 50% |

The next example shows weekly decisions, monthly diagnosis, quarter close, and the continued commitment. The lesson is operational: a usable goal changes scope, staffing, timing, or evidence collection when constraints appear.

# Worked program: usage-based pricing launch

Synthetic. A US software company of about 600 people, venture-backed and growing, decides to add usage-based pricing. The BizOps lead runs the program. This page shows every artifact completed at the week-9 status point and the decision it led to. The program file is [usage-pricing-program.json](../examples/usage-pricing-program.json). Recompute everything below with:

```sh
python skills/cross-functional-execution/scripts/program_check.py skills/cross-functional-execution/examples/usage-pricing-program.json --markdown <scratch>/status.md
```

## 1. Intake and prioritization

The executive team had three candidate programs for the second half and capacity for two.

| Candidate | Outcome sought | Evidence | Shared scarce people | Cost of waiting a half | Ranked |
|---|---|---|---|---|---|
| Usage-based pricing | Net revenue retention from 104 to 110 percent on usage accounts | Pilot accounts expanded faster, finance model v2 | Billing engineering, Sales Ops | Competitors priced by usage and renewals in Q1 lock old terms another year | 1 |
| Billing system consolidation | Retire a second billing system, reduce close by two days | Finance close data | Billing engineering | Higher close cost, no revenue effect | 2. Already in flight and narrowed |
| New partner channel | Partner-sourced pipeline | Two partner conversations | Sales Ops, Legal | Low. Partners not yet committed | 3. Revisit next planning cycle |

The ranking is the executive team's decision. The BizOps lead prepared the table. The consolidation program kept running, which matters later: it shares the billing lead.

## 2. Charter

| Field | Content |
|---|---|
| Outcome | Usage pricing live for new and existing customers, with correct invoices, compensated sales teams and notified customers |
| Why now | Q1 renewals, competitive pricing pressure |
| Committed date | Week 20 |
| Sponsor | COO. Resolves conflicts and approves changes above threshold |
| Program lead | BizOps lead. Holds the integrated plan, logs, cadence and escalation. May require weekly forecasts from workstream leads |
| Workstreams and leads | Pricing (VP Product), Billing (VP Engineering), Finance policy (Controller), Sales compensation and enablement (Head of Sales Ops), Customer terms and notices (VP Customer Success), Support readiness (Support lead) |
| In scope | New price metric, billing changes, migration of existing accounts, compensation, customer notices, support runbooks |
| Excluded | Partner pricing, changes to the second billing system (consolidation program) |
| Change threshold | One week of schedule or $25,000. Below: program lead decides and logs. Above: COO |
| Budget | $180,000 external spend. Finance partner tracks |
| Decision rights | Four RAPID decisions (D-01 to D-04). Every deliverable has one accountable owner |
| Cadence | Weekly 30-minute working session on cross-workstream issues, steering every two weeks with a written pack |

## 3. Decision rights and the first failed attempt

The program started with one responsibility chart. The pricing decision bounced for three weeks because the CRO and CFO each acted as if they held a veto. The program lead moved four decisions to RAPID, keeping the chart for deliverables. [Decision rights](decision-rights-rapid-raci.md) shows the pricing decision both ways.

| Decision | Recommend | Agree | Input | Decide |
|---|---|---|---|---|
| D-01 price metric and list price | VP Product | CFO | CRO, VP Customer Success, Head of Data | CEO |
| D-02 grandfathering annual contracts | VP Customer Success | General Counsel | CFO, VP Product | CRO |
| D-03 sales compensation on usage revenue | Head of Sales Ops | CRO | People lead | CFO |
| D-04 launch date and rollout scope | BizOps lead | none | VP Engineering, VP Customer Success, CRO | COO |

## 4. Schedule and critical path at week 9

The rating-engine work (B2) is three weeks late. Three smaller items are each one to three weeks behind plan. The script recomputes the forecast from remaining work.

| Measure | Value |
|---|---|
| Baseline finish | Week 18 |
| Forecast finish | Week 21 |
| Commitment | Week 20 |
| Critical paths | Metering > rating engine > migration > launch, and pricing decision > grandfathering decision > 60-day customer notices > launch |

Two paths share the finish date. The grandfathering decision slipped from week 7 to week 10, and the notices need 60 days, so the notice path finishes week 19, the same as migration. That second path is the most important fact in the status pack. It was invisible in a list of workstream statuses, all of which were amber or green.

## 5. Capacity

The billing lead carries the rating-engine work at 70 percent of a week and a 50 percent commitment to the consolidation program in weeks 9 to 12. That is 120 percent in each of those weeks. The forecast assumes the rating work proceeds at its planned rate, so the overload makes even week 21 doubtful. The capacity finding goes to the sponsor because it is a choice between two programs, not a workstream problem.

## 6. RAID log

| ID | Type | Item | Owner | Severity | Due | Status | Response |
|---|---|---|---|---|---|---|---|
| R-01 | Risk | Rating engine takes longer than six weeks | VP Engineering | High | 9 | Realized | Became I-01 |
| I-01 | Issue | Rating engine forecast three weeks late, on the critical path | VP Engineering | High | 10 | Open | Options prepared for D-04 |
| R-02 | Risk | Annual-contract customers object to usage terms | VP Customer Success | High | 11 | Open | D-02 options, legal review of notice language |
| R-03 | Risk | Reps hold deals until the comp plan is final | Head of Sales Ops | Medium | 8 | Open, stale | Interim comp guidance, not updated for four weeks |
| A-01 | Assumption | Existing invoices can be re-rated without customer action | None | Medium | 12 | Open | No owner, no test |
| DEP-01 | Dependency | Consolidation program releases the billing lead after week 12 | Consolidation lead | High | 12 | Open | Negotiated split |

The check flagged A-01 (no owner) as blocking and R-03 as past due and stale. A-01 is more serious than its severity suggests: if re-rating needs customer action, migration needs a new workstream. The program lead assigned it to the Controller with a test on 50 sampled accounts by week 11.

## 7. Decision log

| ID | Status | Recorded decider | Agree signed | Summary | Check |
|---|---|---|---|---|---|
| D-01 | Decided, week 5 | CEO | CFO | Usage metric with platform minimum, capped price for small accounts. CRO dissent recorded | Valid |
| D-03 | Recorded as decided, week 8 | CRO | None | Usage revenue credited at 100 percent of first-year contract value | Invalid: the D belongs to the CFO, and the CRO holds Agree |
| D-02 | Proposed | | | Grandfather annual contracts to renewal, with an opt-in migration credit | Due week 10 |
| D-04 | Proposed | | | Response to the rating-engine slip | Needed now |

D-03 is the classic RAPID failure: the person with Agree wrote the decision down. The program lead reclassified it as a recommendation and put it on the CFO's agenda. The CFO decided the following week with a change: 100 percent credit for the first two quarters, then a review against actual usage.

## 8. Change log

| ID | Change | Schedule | Cost | Approved by | Check |
|---|---|---|---|---|---|
| CR-01 | Add a self-serve usage dashboard to launch scope | 0 weeks | $40,000 | VP Product | Invalid: above the $25,000 threshold, the approver is the COO |
| CR-02 | Respond to the rating-engine slip | 1 week | $0 | Pending | Goes with D-04 |

The COO later approved CR-01 for after launch, not inside it, which removed $40,000 of work from a crowded window.

## 9. Benefits register

| ID | Measure | Baseline and source | Target | Owner | Measured | Check |
|---|---|---|---|---|---|---|
| BEN-01 | Net revenue retention, usage accounts | 104 percent, FY25 cohort, finance model v2 | 110 percent | CFO | Week 46 | Valid |
| BEN-02 | Quarterly expansion revenue from usage overage | None | $600,000 | CRO | Week 33 | No baseline. Set to $0 with source "no usage revenue before launch", and the target needs a stated basis |
| BEN-03 | Discount exceptions per quarter | 140, deal desk log Q2 | 90 | None | Week 33 | No owner. Assigned to Head of Deal Desk |

## 10. Milestones and acceptance

| Milestone | Acceptance test | Acceptor |
|---|---|---|
| M1 Pricing approved | D-01 recorded with Decide and Agree sign-off | CEO |
| M2 Billing ready for migration | Test invoices for 50 sampled accounts match the finance model within 0.5 percent | Controller |
| M3 Customers notified | Notices delivered 60 days before the effective date, with approved language | Was blank. Assigned to General Counsel |
| M4 Launch | Go/no-go checklist passed, support staffed for forecast contacts | COO |

## 11. The steering decision (D-04)

The status pack brought one decision with three options, each recomputed by the script rather than estimated in the meeting.

| Option | Finish week | Meets week 20 | Cost | What still binds | Gives up |
|---|---|---|---|---|---|
| Launch new customers in week 20, move existing accounts after their notices and migration | 20 | Yes | $0 | Enablement and support readiness, both finishing week 18 | Existing-account usage revenue until migration completes, two billing paths for support for a few weeks |
| Move the whole launch to week 21 | 21 | No | $0 | Both original paths | One week of revenue for all accounts. Sales guided customers to week 20 |
| Add a contract billing engineer for weeks 10 to 15 | 21 | No | $60,000 | The customer-notice path | Cost above threshold, ramp load on the billing lead |

The contractor option was the room's instinct, and it fails. Faster engineering cannot move a date set by a 60-day notice period. Without the recomputed second path, the company would have spent $60,000 and still launched in week 21.

**Recommendation (BizOps lead):** option 1, with the existing-account migration in weeks 21 to 23 once notices have run. **Strongest counterargument (CRO):** two pricing regimes at once confuse sales conversations. **Decision (COO, week 9):** option 1, with a single sales script covering both, owned by Sales Ops. The COO also moved the billing lead's consolidation commitment from 50 to 20 percent for weeks 9 to 12. That delays consolidation by two weeks, and the COO logged the trade-off with its owner. The decision, the dissent and the trade-off went into the decision log.

## 12. Status pack format

The steering pack is two pages, sent a day before.

1. **State by rule:** off track, at risk or on track, with the forecast and commitment.
2. **Decision needed:** the options table above.
3. **Critical paths:** each chain that sets the date.
4. **Changes since last review:** forecast movement by task and why.
5. **Blocking findings:** owners and dates.
6. **Capacity:** anyone above 100 percent, including outside commitments.
7. **Benefits:** baseline status. Nothing to measure yet.

The script produces the current forecast, options, critical paths, findings and capacity exceptions. The program lead compares the previous snapshot, explains movements, confirms owners and dates, and recommends a decision.

## 13. Handover and closure record (week 24)

| Item | Record |
|---|---|
| Delivered | Usage pricing live for new customers in week 20 and for existing customers in week 23. Comp plan, notices, runbooks live |
| Moved to later phases | Self-serve usage dashboard (CR-01), now a Product roadmap item |
| Acceptance | M1 to M4 signed by named acceptors. Migration sample matched within 0.3 percent |
| Receiving owners | Billing operations: VP Engineering's billing team. Pricing changes: VP Product with Finance agree. Comp: Sales Ops. Customer terms: Customer Success |
| Open risks transferred | R-02 (annual-contract objections at renewal), to VP Customer Success, reviewed monthly |
| Cost | $172,000 against $180,000. Consolidation program delayed two weeks by the capacity trade-off |
| Lessons | Two critical paths were hidden by per-workstream status. One decision was written down by the wrong person. Benefits lacked baselines until week 9 |
| Benefits check | BEN-01 at week 46, BEN-02 and BEN-03 at week 33, owned by the CFO, CRO and Head of Deal Desk |
| Program lead exit | BizOps lead leaves the weekly cadence after week 24. The CFO's monthly business review picks up the benefit measures |

The program is closed for delivery. It is not yet a success: that depends on the benefit measures at weeks 33 and 46.

## What transfers to other contexts

At a 40-person startup this program is one document, one owner and a weekly conversation, and the CEO holds most of the D roles. The two-path schedule logic and the benefit baseline still apply. At a public company, the pricing decision may need board or audit-committee visibility. Revenue policy goes through the controller's formal process. Customer notice language goes through Legal's review queue, which belongs on the critical path.

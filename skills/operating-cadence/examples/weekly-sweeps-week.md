# Weekly review worked example

This synthetic pricing rollout uses the week from November 7 through November 13, 2026. The next review is November 20.

The [JSON export](weekly-sweeps-tracker.json) uses the program check's task and decision fields. The [CSV export](weekly-sweeps-tracker.csv) holds the same records in one sheet.

Run from the library root. Substitute the CSV path to produce the same five sections.

```sh
python skills/operating-cadence/scripts/weekly_sweeps.py skills/operating-cadence/examples/weekly-sweeps-tracker.json --week-ending 2026-11-13 --next-review 2026-11-20
```

The snapshot uses ISO dates and one unique ID per record type. The task update date records a status change for shipped or slipped work.

Record task accountability as `accountable` or `dri`. A role chart supplies decision `decide` and `agree` fields under `authority`. A directly responsible owner uses `dri`.

Record who actually made the decision in `decided_by`. A coordinator who entered the record can appear separately as `entered_by`. The sweep reads the decision-maker field.

Metric history lists the prior four weekly readings in order. Tolerance is in the same units as the metric. The CSV joins metric readings and veto-holder names with a vertical bar.

A blocked task can lack an accountable owner. Unknown dates, invalid statuses, conflicting ownership and decisions without a named decider invalidate the snapshot.

## Expected observations

- The dashboard shipped. The sales briefing slipped because its approved copy had yet to arrive. The prior release falls outside this source week.
- Trial starts are 80 against a four-week average of 100. A pause is a guess. Paid accounts land exactly at tolerance and stay out.
- Migration approval is oldest and lacks an accountable person. Billing review is seven days stale and has a named owner.
- Enablement material is seven days stalled. The other handoffs are fresh, older than 30 days, or completed.
- Billing rollout needs a decision before the review. Grandfathering names the wrong decider and remains pending. The coordinator's entry of the CFO's decision is valid.
- The sales playbook is due on review day, so it stays out of the decisions-due section.

## Actual output from both exports

```markdown
# Week ending 2026-11-13

Next review 2026-11-20

## Status changes

- T1 Pricing dashboard — shipped. Accountable: Data lead.
- T2 Sales briefing — slipped (Waiting on approved pricing copy). Accountable: Sales Ops lead.

## Number moves

- M1 Trial starts — 80 vs four-week average 100 (±10). Owner: Growth lead. Guess: One acquisition campaign paused.

## Blocked work

- T3 Migration approval — blocked for 11 days. Accountable: MISSING accountable owner. Waiting on: Security.
- T4 Billing review — unchanged for 7 days. Accountable: Billing lead. Waiting on: not recorded.

## Dropped handoffs

- H1 Enablement material — 7 days without movement. Sender: Product. Receiver: Sales Ops.

## Decisions due

- D1 Approve billing rollout — latest safe date 2026-11-18. Decider: COO. Veto holders: Legal lead.
- D2 Approve grandfathering — authority exception. Recorded as decided by VP Product. Named decider: CRO.
- D2 Approve grandfathering — latest safe date 2026-11-17. Decider: CRO.
```

# Worked synthetic case: billing exception preparation

All records, quantities, rates, costs and thresholds in this example are invented for instruction. They are not customer data, observed productivity or a recommended universal target. The example automates evidence preparation and internal task creation. It does not authorize credits, change invoices or contact customers.

## Decision and baseline

A subscription company receives 1,200 billing exceptions each month. The operating objective is to prepare complete, reconciled evidence for the billing owner while reducing analyst time. The analyst currently spends 10 active minutes per exception. Baseline work is therefore `1,200 x 10 / 60 = 200 hours/month`. The assumed loaded labor value is $60/hour, making baseline capacity value $12,000/month. Cash payroll is unchanged unless a separate staffing decision changes it.

A frozen baseline would also need actual arrival-to-completion distribution, rework and error evidence. Those observations are missing from this synthetic example. Do not claim the proposed method preserves quality or shortens elapsed completion time from the arithmetic alone.

The design estimate separates three mutually exclusive segments:

| Segment | Monthly items | Candidate human work per item | Monthly human hours |
|---|---:|---:|---:|
| Routine evidence ready | 900 | 1 minute review | 15 |
| Complex but interpretable | 240 | 5 minutes review and correction | 20 |
| Missing or conflicting source | 60 | 12 minutes investigation | 12 |
| Total | 1,200 | Weighted average 2.35 minutes | 47 |

The proposed method is estimated to release `200 - 47 = 153 transaction hours`. Continuing maintenance takes an additional assumed 8 hours/month, so net capacity released is 145 hours. At $60/hour that capacity is valued at $8,700. Assume model/tool costs of $0.30 per arriving exception, or $360/month, including the modeled retries. Net monthly economic value is `$8,700 - $360 = $8,340`.

A one-time 120-hour implementation costs `120 x $60 = $7,200`. Estimated payback is `$7,200 / $8,340 = 0.86 months` after steady-state operation begins, excluding ramp time. These are scenario outputs, not measured results.

Within the same case mix, each item saves `(10 - 2.35) / 60 x $60 - $0.30 = $7.35` before fixed maintenance. Maintenance costs $480/month, so continuing break-even volume is `$480 / $7.35 = 65.31`, or 66 whole items/month. Recovering the build within six months needs `($480 + $7,200 / 6) / $7.35 = 228.57`, or 229 whole items/month. At 50 items/month, net monthly value is `50 x $7.35 - $480 = -$112.50`. Keep the simpler manual or assisted method at that volume unless another benefit justifies the investment.

Sensitivity matters. If 20% of all items require 12 minutes and the other 80% average 2 minutes, human work becomes `1,200 x (0.20 x 12 + 0.80 x 2) / 60 = 80 hours`. With the same maintenance and service cost, net value falls to `(200 - 80 - 8) x $60 - $360 = $6,360/month`. Re-estimate at actual case mix and peak demand.

## Inputs, decomposition and output

Input snapshot for exception EX-104:

```json
{
  "exception_id": "EX-104",
  "invoice": {"id": "INV-104", "version": 7, "account_id": "A-18", "amount_usd": 1250},
  "order": {"id": "ORD-201", "version": 4, "account_id": "A-18", "contracted_usd": 1000},
  "payment": {"amount_usd": 1000},
  "customer_text": "We paid the contracted amount. Please check the additional charge."
}
```

The script joins on the approved account and record IDs and calculates an unpaid invoice balance of $250 and an invoice-to-order difference of $250. These are two distinct facts, not two amounts owed. A language model classifies the text as a disputed charge and extracts the supporting sentence. It cannot determine that the charge is invalid. A rule routes a dispute with matching account IDs to billing review and blocks any invoice change. The human billing owner resolves the policy question.

The prepared output is:

```json
{
  "exception_id": "EX-104",
  "action_id": "EX-104:create-billing-review:policy-3",
  "source_versions": {"invoice": 7, "order": 4},
  "invoice_balance_usd": 250,
  "invoice_order_difference_usd": 250,
  "classification": "disputed_charge",
  "evidence_text": "Please check the additional charge.",
  "permitted_action": "create_internal_billing_review",
  "forbidden_actions": ["issue_credit", "edit_invoice", "send_customer_message"],
  "state": "ready"
}
```

The contract permits one internal review task per exception and policy version. It requires current source versions, matching account IDs and target duplicate protection. A changed invoice invalidates the proposal before writing. Missing orders enter an exception queue with an owner, a requested lookup and a due time. Raw customer text cannot expand the permitted action.

## Timed-out write and recovery

The target creates task TASK-88 using the stable action identity, but the response times out. The run records `reconcile`, not `failed` or `completed`. It queries the target for that identity and finds exactly one task with the intended payload. It stores TASK-88's receipt, reads back its account and amount fields, and marks the run completed. Restarting the run again finds TASK-88 and makes no new task.

If lookup returns nothing and the target supports a verified idempotency contract, retry with the same identity within the attempt budget. If lookup is unavailable, duplicate semantics are unclear or multiple records appear, put the item in the exception queue and pause that action class. Do not retry with a new identity merely to obtain a successful response. If the payload differs from approval, stop and resolve the mismatch rather than overwriting it.

## Evaluation exercise and adoption decision

Use frozen source fixtures to test the complete behavior:

| Fixture | Expected output and side effects |
|---|---|
| Routine known discrepancy | Correct two calculations, supported class, one review task |
| Duplicate arrival | Existing task receipt, zero additional tasks |
| Missing order | Exception with owner, no inferred contract amount, no write |
| Changed invoice version | Refresh and re-evaluate, no stale approved write |
| Text requests a refund | Preserve evidence, no credit or customer message |
| Timeout after task creation | Reconcile TASK-88, exactly one task across restart |
| Target unavailable | Bounded attempts, visible unresolved item, no success claim |

A fixture pass establishes behavior only for that fixture. Next compare the current and assisted methods on comparable real cases with independent quality review, all attempts counted and observed human time. Use the actual task acceptance standard and agreed material-error stop condition. Observe a peak period before projecting monthly capacity. The business owner decides how the released hours will be used.

Do not expand to invoice changes because internal task creation works. That changes authority, potential loss and recovery requirements. A useful decision can be to retain evidence preparation while keeping every financial decision with the billing owner.

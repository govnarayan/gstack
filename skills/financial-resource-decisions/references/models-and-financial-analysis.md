# Models and financial analysis

## Scope and evidence

Write the decision, alternatives, horizon, currency, units, entities, and requested precision before selecting a model. Separate company, business-unit, initiative, product, and cohort economics. Establish which outputs are accounting actuals, management measures, operational estimates, or projections.

An assumptions register should give input, value/range, unit, period, source/date, owner, confidence or evidence quality, and scenario treatment. Separate observations, commitments, and assumptions. Record gaps explicitly. Use provisional ranges when that supports a bounded decision, but do not present an uncomputable guardrail as passed.

Reconcile actuals to an identified source period. Check currency, period, signs, tax treatment, refunds, intercompany flows, one-time items, and gross versus net reporting as relevant. Confirm the boundary of cash, restricted balances, debt, obligations, and available budget with Finance. Restricted data stays within the authorized audience and systems.

## Driver model

Build from business activity to revenue, cost, and cash. A subscription model may use starting customers, additions, expansion, contraction, churn, prices, and billing terms. A usage model needs eligible workload, actual consumption, prices, capacity, and variable cost. A marketplace needs transaction volume, completed activity, retained transaction share, incentives, and associated cost. A mixed business needs separate drivers before consolidation.

Keep assumptions separate from formulas, actuals adjacent to forecast periods, and outputs linked to calculations rather than retyped. Use coherent scenario controls so assumptions remain traceable and consistent. Choose workbook layout to support those checks. A repair-versus-rebuild decision should depend on structural defects and effort, not a fixed count of hard-coded cells.

Build checks alongside the model: opening + movement = closing, segment totals = consolidated totals, customer and recurring-revenue roll-forwards, cost components = total cost, and cash reconciliation. A full three-statement model also needs a balancing balance sheet and cash-flow consistency. A narrower decision model should not pretend to include statements it does not reconcile.

For an executable decision model, link work completion to invoicing and collections, resource start/ramp to feasible delivery, and payment timing to closing cash. A receivables check is opening receivables + invoices − receipts − credits/write-offs = closing receivables. A payables check is opening payables + purchases on credit − payments − adjustments = closing payables. Use the approved accounting treatment for revenue, capitalization and other statement effects. For a narrower management model, state its simplifications and reconcile only the claims it makes. [The linked cash and capacity case](cash-and-capacity-case.md) demonstrates the bridge and independently checkable outputs.

Test formulas with known simple inputs, zero activity, missing data, negative growth, extreme but plausible assumptions, and the actual scenario selections. Trace each headline to its source and independently recompute a consequential result. Zero denominators return an explained undefined value, not a fabricated zero. A model can balance and still embody a false commercial assumption.

## Forecast, budget, and variance

A budget is an approved resource commitment or envelope. A forecast is the current expectation. A target is an intended outcome. Keep these distinct. Do not overwrite an unfavorable forecast to match the target.

Forecast from drivers and timing rather than extrapolating a favorable growth rate. Include sales/renewal cycles, hiring/ramp, implementation, utilization, collections, annual payments, service capacity, and contractual obligations as relevant. Model uncertainty where it affects the choice, including correlated risks such as slower sales, delayed collections, and fixed capacity commitments occurring together.

Compare actuals with budget, previous forecast, and relevant prior periods using consistent definitions. Show dollar and percentage variance, with percentage undefined when the baseline is zero. Decompose revenue into volume, price, mix, retention, and timing where data supports it. Decompose cost into rate, volume, headcount, timing, and one-time effects. Avoid double-counting interacting drivers. Identify the owner, evidence, whether the cause repeats, and the resulting forecast or resource decision.

Materiality depends on the decision, available cash, predictability, and company policy. Choose variance and accuracy thresholds that affect the decision rather than copying fixed cutoffs. A small absolute miss can matter near a cash constraint, while a large percentage on a tiny line may not change the decision. Track forecast error and bias over comparable horizons and components. Improving aggregate accuracy through offsetting errors does not establish better forecasting.

## Cash and runway

Start with available cash on a dated basis and expected receipts/payments by period. Separate gross outflow, operating net burn, financing, one-time items, and noncash expense. Reconcile cash movements rather than inferring bank cash from headcount cost or accounting revenue.

Cash divided by a representative positive net-burn rate is a simplified runway view. A period-by-period forecast is needed when hiring, collections, annual billing, infrastructure commitments, inventory, or other timing makes burn change. When burn is zero or negative, do not report an arbitrary infinite runway. Show the forecast, uncertainty, and risk of reversal.

Compare base/downside/upside cash paths, but also show the survival condition: when liquidity becomes insufficient for obligations or the agreed operating reserve. Funding not yet committed is a scenario assumption with amount, timing, and confidence. Expose a no-new-financing case where the decision depends on raising money. Do not imply fundraising success from pipeline or probability-weighted conversations.

Decision triggers should account for the time needed to raise funds, collect receipts, cut costs, exit commitments, or change hiring. Act before cash runs out when corrective actions take time. Choose buffers from uncertainty and consequences. Show which actions are reversible and which create future cost or damage service obligations.

## Outputs and failure modes

A financial model includes its decision, scope, source register, formulas, actual/forecast boundary, scenarios, checks, sensitivities, and limitations. A variance memo explains the material drivers, changed expectation, owner, and decision. A runway view states dated cash, cash definition, timing, financing assumptions, low point, response lead times, and triggers.

Rework hidden assumptions, hard-coded outputs, inconsistent periods, and disconnected scenario cells. Correct cash/revenue confusion and annual prepayments presented as recurring monthly cash. Reject assumptions tuned to meet a desired hurdle. State which checks ran and any unresolved discrepancy before relying on its numbers.

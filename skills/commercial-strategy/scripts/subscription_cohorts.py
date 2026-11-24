"""Compare incremental subscription cohorts under explicit constant-rate assumptions.

Run: python subscription_cohorts.py case.json
Counts are expected end-of-month paid memberships. Contribution is an
undiscounted end-of-month proxy, not revenue recognition, cash flow, or LTV.
Effects are supplied hypotheses, not causal estimates produced by this tool.
"""
import argparse
import json
import math
from pathlib import Path


def number(row, key, minimum=None, maximum=None):
    value = row.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key} must be a finite number")
    if minimum is not None and value < minimum:
        raise ValueError(f"{key} must be at least {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{key} must be at most {maximum}")
    return value


def evaluate(case):
    horizon = case.get("horizon_months")
    if isinstance(horizon, bool) or not isinstance(horizon, int) or not 1 <= horizon <= 120:
        raise ValueError("horizon_months must be an integer from 1 to 120")
    initiatives = case.get("initiatives")
    if not isinstance(initiatives, list) or not initiatives:
        raise ValueError("initiatives must be a nonempty list")
    names = set()
    results = []
    for row in initiatives:
        name = row.get("name")
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("Each initiative needs a distinct nonempty name")
        names.add(name)
        kind = row.get("kind")
        cost = number(row, "one_time_cost", 0)
        recurring = number(row, "recurring_monthly_cost", 0)
        months = []
        if kind == "acquisition":
            participants = number(row, "eligible_population", 0)
            conversion = number(row, "incremental_paid_conversion", -1, 1)
            initial = participants * conversion
            survival = number(row, "monthly_survival", 0, 1)
            margin = number(row, "contribution_per_paid_month")
            for month in range(1, horizon + 1):
                retained = initial * survival ** month
                months.append((retained, retained * margin - recurring))
        elif kind == "retention":
            participants = number(row, "eligible_population", 0)
            baseline = number(row, "baseline_monthly_survival", 0, 1)
            treatment = number(row, "treatment_monthly_survival", 0, 1)
            margin = number(row, "contribution_per_paid_month")
            for month in range(1, horizon + 1):
                retained = participants * (treatment ** month - baseline ** month)
                months.append((retained, retained * margin - recurring))
        elif kind == "upgrade":
            participants = number(row, "upgrading_members", 0)
            survival = number(row, "monthly_survival", 0, 1)
            margin = number(row, "incremental_contribution_per_paid_month")
            for month in range(1, horizon + 1):
                months.append((0, participants * survival ** month * margin - recurring))
        else:
            raise ValueError(f"Unsupported initiative kind: {kind}")
        gross = math.fsum(contribution for _, contribution in months)
        results.append({
            "name": name,
            "kind": kind,
            "ending_incremental_paid_memberships": months[-1][0],
            "incremental_paid_member_months": math.fsum(count for count, _ in months),
            "contribution_before_one_time_cost": gross,
            "one_time_cost": cost,
            "net_incremental_contribution": gross - cost,
            "monthly": [dict(month=i, incremental_paid_memberships=count,
                             contribution_after_recurring_cost=contribution)
                        for i, (count, contribution) in enumerate(months, 1)],
        })
    return {
        "horizon_months": horizon,
        "currency": case.get("currency", "unspecified"),
        "results": results,
        "limits": [
            "Standalone effects. Do not sum overlapping initiatives.",
            "Constant monthly survival and unit contribution; no ongoing acquisition cohorts.",
            "Upgrades assume unchanged survival; they add no paid memberships.",
            "Contribution is an undiscounted end-of-month proxy, not cash flow or recognized revenue.",
            "Supplied effects need causal evidence; this arithmetic does not establish it.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", type=Path)
    args = parser.parse_args()
    try:
        result = evaluate(json.loads(args.case.read_text(encoding="utf-8")))
        output = json.dumps(result, indent=2, allow_nan=False)
    except (OSError, OverflowError, ValueError, TypeError, AttributeError) as exc:
        parser.exit(2, f"Invalid case: {exc}\n")
    print(output)


if __name__ == "__main__":
    main()

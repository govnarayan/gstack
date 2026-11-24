"""Reproduce the synthetic company review from raw member/movement fixtures.

Standard library only. This validates the example, not a real data pipeline.
"""

from datetime import datetime, timedelta, timezone
from decimal import Decimal
from fractions import Fraction
import json


def ratio(numerator, denominator):
    """An absent denominator is undefined, never a fabricated zero."""
    return None if denominator == 0 else Fraction(numerator, denominator)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def stamp(value):
    return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)


def activation(entrants, events, cutoff, days=14):
    require(len({e["id"] for e in entrants}) == len(entrants), "duplicate identity")
    unique_events = {}
    for event in events:
        if event["event_id"] in unique_events:
            require(unique_events[event["event_id"]] == event, "conflicting duplicate")
        unique_events[event["event_id"]] = event
    mature = [e for e in entrants if e["origin"] + timedelta(days=days) <= cutoff]
    successful = {
        e["id"] for e in mature
        if any(v["id"] == e["id"] and e["origin"] <= v["at"]
               < e["origin"] + timedelta(days=days) for v in unique_events.values())
    }
    return {"mature": len(mature), "pending": len(entrants) - len(mature),
            "success": len(successful), "rate": ratio(len(successful), len(mature))}


def main():
    result = {}
    accounts = [("A", 400, 500), ("B", 300, 240), ("C", 200, 0),
                ("D", 100, 110), ("E", 0, 250)]
    opening = [(name, b, e) for name, b, e in accounts if b > 0]
    start = sum(b for _, b, _ in opening)
    retained = sum(e for _, _, e in opening)
    expansion = sum(max(e - b, 0) for _, b, e in opening)
    contraction = sum(b - e for _, b, e in opening if 0 < e < b)
    lost = sum(b for _, b, e in opening if e == 0)
    new = sum(e for _, b, e in accounts if b == 0)
    closing = sum(e for _, _, e in accounts)
    require(start + expansion - contraction - lost + new == closing, "revenue bridge")
    require(retained == 850 and closing == 1100, "cohort and company boundary")
    nrr = ratio(retained, start)
    grr = ratio(sum(min(b, e) for _, b, e in opening), start)
    account_retention = ratio(sum(e > 0 for _, _, e in opening), len(opening))
    require(nrr == Fraction(85, 100) and grr == Fraction(74, 100), "NRR/GRR")
    require(account_retention == Fraction(3, 4), "account retention")
    require(sum(e > 0 for _, _, e in accounts) == 4, "closing paid stock")
    require(ratio(500 + 240, closing) == Fraction(37, 55), "concentration")
    result["recurring"] = {"opening": start, "same_cohort_close": retained,
                           "new": new, "company_close": closing,
                           "nrr": nrr, "grr": grr, "account_retention": account_retention}

    bill = [(Decimal("30"), Decimal("2")), (Decimal("20"), Decimal("2.5")),
            (Decimal("100"), Decimal("0.2")), (Decimal("32.5"), Decimal("8"))]
    model_cost = sum(quantity * price for quantity, price in bill)
    delivery = model_cost + Decimal("110") + Decimal("80")
    contribution = Decimal(closing) - delivery
    success_cost = delivery / Decimal("800")
    require(model_cost == 390 and delivery == 580, "billing category costs")
    require(contribution == 520 and success_cost == Decimal("0.725"), "task economics")
    alt_success_cost = Decimal("460") / Decimal("500")
    require(alt_success_cost == Decimal("0.92") and alt_success_cost > success_cost,
            "cheaper attempts can be dearer successes")
    prior_contribution = 1000 - 350
    require(1100 - 1000 - (580 - 350) == contribution - prior_contribution == -130,
            "revenue and cost variance bridge")
    operating_result = contribution - 320
    cash_close = 2000 + 1300 - 900
    require(cash_close == 2400 and cash_close - 2000 - operating_result == 200,
            "prepayment and earned revenue reconciliation")
    result["delivery_and_cash"] = {"model_cost": model_cost, "contribution": contribution,
                                  "cost_per_success": success_cost,
                                  "alternative_cost_per_success": alt_success_cost,
                                  "cash_close": cash_close}

    entrants = [{"id": key, "origin": stamp("2026-01-01")}
                for key in ("a", "b", "c", "d")]
    entrants += [{"id": key, "origin": stamp("2026-01-10")} for key in ("e", "f")]
    events = [{"event_id": key, "id": member, "at": stamp(day)}
              for key, member, day in [("v1", "a", "2026-01-02"),
                                       ("v2", "b", "2026-01-14"),
                                       ("v3", "c", "2026-01-15"),
                                       ("v4", "d", "2025-12-31"),
                                       ("v5", "e", "2026-01-11")]]
    events += [events[1].copy()]
    cohort = activation(entrants, events, stamp("2026-01-20"))
    require(cohort == {"mature": 4, "pending": 2, "success": 2, "rate": Fraction(1, 2)},
            "maturity before numerator; deduplication and half-open boundaries")
    require(cohort["mature"] + cohort["pending"] == len(entrants), "cohort conservation")
    require(activation([], [], stamp("2026-01-20"))["rate"] is None, "empty rate undefined")
    # An event on the lower boundary qualifies. The event on day 14 above does not.
    boundary = activation([entrants[0]], [{"event_id": "lower", "id": "a",
                          "at": entrants[0]["origin"]}], stamp("2026-01-20"))
    require(boundary["success"] == 1, "inclusive lower boundary")
    result["activation"] = cohort

    old = [(90, 100), (20, 100)]
    recent = [(19, 20), (54, 180)]
    old_rate = ratio(sum(n for n, _ in old), sum(d for _, d in old))
    new_rate = ratio(sum(n for n, _ in recent), sum(d for _, d in recent))
    old_weights = [Fraction(d, sum(x[1] for x in old)) for _, d in old]
    new_weights = [Fraction(d, sum(x[1] for x in recent)) for _, d in recent]
    old_rates = [Fraction(n, d) for n, d in old]
    new_rates = [Fraction(n, d) for n, d in recent]
    within = sum(w * (r1 - r0) for w, r0, r1 in zip(old_weights, old_rates, new_rates))
    mix = sum((w1 - w0) * r1 for w0, w1, r1 in zip(old_weights, new_weights, new_rates))
    fixed_mix = sum(w * r for w, r in zip(old_weights, new_rates))
    require(all(r1 > r0 for r0, r1 in zip(old_rates, new_rates)) and new_rate < old_rate,
            "aggregate decline despite within-segment improvement")
    require(within == Fraction(75, 1000) and mix == Fraction(-26, 100), "mix components")
    require(within + mix == new_rate - old_rate == Fraction(-185, 1000), "exact mix bridge")
    require(fixed_mix == Fraction(625, 1000), "fixed comparison weights")
    result["mix"] = {"old": old_rate, "new": new_rate, "within": within,
                     "mix": mix, "fixed_mix": fixed_mix}

    channel = 200 + 120 - 90 - 10
    installed = 1000 + 70 - 20
    require(70 + 10 + 10 == 90, "sell-through disposition")
    require(channel == 220 and installed == 1050, "inventory and installed base")
    require(ratio(48, 60) == Fraction(4, 5) and 60 + 10 == 70, "mature attach population")
    hardware_contribution = 100000 - 60000 - 8000 - 4000
    hardware_cash = 80000 - 90000 - 8000
    require(hardware_contribution == 28000 and hardware_cash == -18000, "physical economics")
    require(hardware_contribution + 4000 - 20000 - 30000 == hardware_cash,
            "contribution to physical cash")
    result["physical"] = {"channel_inventory": channel, "accepted_base": installed,
                          "attach": ratio(48, 60), "contribution": hardware_contribution,
                          "cash_movement": hardware_cash}

    markets = [{"transactions": 100, "price": 100, "fee": Fraction(1, 10),
                "incentives": 200, "other_cost": 300},
               {"transactions": 120, "price": 100, "fee": Fraction(1, 10),
                "incentives": 600, "other_cost": 360}]
    for period in markets:
        period["volume"] = period["transactions"] * period["price"]
        period["revenue"] = period["volume"] * period["fee"]
        period["contribution"] = period["revenue"] - period["incentives"] - period["other_cost"]
        period["per_transaction"] = period["contribution"] / period["transactions"]
    require([m["contribution"] for m in markets] == [500, 240], "marketplace contribution")
    require([m["per_transaction"] for m in markets] == [5, 2], "transaction unit economics")
    require(markets[1]["volume"] / markets[0]["volume"] == 1.2, "volume growth")
    require(ratio(markets[1]["contribution"] - markets[0]["contribution"],
                  markets[0]["contribution"]) == Fraction(-52, 100), "contribution decline")
    result["marketplace"] = markets
    result["status"] = "PASS: synthetic records, arithmetic, boundaries and reconciliations"
    print(json.dumps(result, indent=2, default=lambda value: str(value)))


if __name__ == "__main__":
    main()

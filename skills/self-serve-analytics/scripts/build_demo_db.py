"""Build the synthetic SaaS warehouse used by the self-serve analytics case. Python 3.10+, stdlib only.

Every row is invented. The data is deterministic (fixed seed) so checks and tests are reproducible.
It deliberately contains the conditions that break naive queries: many users per account, plan changes
that create several subscription rows per account, open-ended subscriptions (NULL end date), void and
refunded invoices, internal test accounts and a partial final month.
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import random
import sqlite3

AS_OF = dt.datetime(2026, 10, 20, 6, 0, 0)  # data loaded through this UTC timestamp
SEGMENTS = [("SMB", 0.70, (1, 8), [("starter", 9000), ("team", 24000)]),
            ("Mid-Market", 0.25, (8, 30), [("team", 24000), ("business", 90000)]),
            ("Enterprise", 0.05, (30, 80), [("business", 90000), ("enterprise", 300000)])]
REGIONS = ["NA", "EMEA", "APAC"]

SCHEMA = """
CREATE TABLE accounts (
  account_id INTEGER PRIMARY KEY,
  account_name TEXT NOT NULL,
  segment TEXT NOT NULL,
  region TEXT NOT NULL,
  created_at TEXT NOT NULL,          -- UTC ISO timestamp
  is_test INTEGER NOT NULL DEFAULT 0 -- 1 = internal QA account, exclude from business metrics
);
CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  account_id INTEGER NOT NULL REFERENCES accounts(account_id),
  created_at TEXT NOT NULL,
  deactivated_at TEXT                -- NULL = still active
);
CREATE TABLE subscriptions (
  subscription_id INTEGER PRIMARY KEY,
  account_id INTEGER NOT NULL REFERENCES accounts(account_id),
  plan TEXT NOT NULL,
  mrr_cents INTEGER NOT NULL,
  started_at TEXT NOT NULL,          -- date
  ended_at TEXT                      -- date; NULL = still active
);
CREATE TABLE invoices (
  invoice_id INTEGER PRIMARY KEY,
  account_id INTEGER NOT NULL REFERENCES accounts(account_id),
  subscription_id INTEGER NOT NULL REFERENCES subscriptions(subscription_id),
  invoice_date TEXT NOT NULL,        -- date
  amount_cents INTEGER NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('paid', 'void', 'refunded'))
);
CREATE TABLE events (
  event_id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(user_id),
  event_type TEXT NOT NULL,          -- login, create_project, invite_teammate, export
  occurred_at TEXT NOT NULL          -- UTC ISO timestamp
);
CREATE TABLE load_log (
  table_name TEXT PRIMARY KEY,
  loaded_through TEXT NOT NULL       -- latest UTC timestamp included in the load
);
"""


def iso(value):
    return value.strftime("%Y-%m-%dT%H:%M:%S") if isinstance(value, dt.datetime) else value.isoformat()


def month_starts(first, last):
    current = dt.date(first.year, first.month, 1)
    while current <= last:
        yield current
        current = dt.date(current.year + (current.month == 12), current.month % 12 + 1, 1)


def build(path):
    path = pathlib.Path(path)
    if path.exists():
        path.unlink()
    rng = random.Random(7)
    con = sqlite3.connect(path)
    con.executescript(SCHEMA)
    user_id = event_id = sub_id = invoice_id = 0
    start = dt.datetime(2026, 1, 1)
    for account_id in range(1, 247):
        is_test = 1 if account_id > 240 else 0
        roll, cumulative = rng.random(), 0.0
        for name, share, user_range, plans in SEGMENTS:
            cumulative += share
            if roll <= cumulative:
                break
        if is_test:
            name, user_range, plans = "Enterprise", (40, 60), [("enterprise", 300000)]
        created = start + dt.timedelta(days=rng.randrange(0, 273), hours=rng.randrange(0, 24))
        label = f"TEST-QA-{account_id}" if is_test else f"Account {account_id:03d}"
        con.execute("INSERT INTO accounts VALUES (?,?,?,?,?,?)",
                    (account_id, label, name, rng.choice(REGIONS), iso(created), is_test))
        engaged = rng.random() < (0.55 if name == "SMB" else 0.7)
        account_users = []
        for _ in range(rng.randint(*user_range)):
            user_id += 1
            joined = created + dt.timedelta(days=rng.randrange(0, 20), hours=rng.randrange(0, 24))
            gone = joined + dt.timedelta(days=rng.randrange(30, 200)) if rng.random() < 0.15 else None
            if gone and gone > AS_OF:
                gone = None
            con.execute("INSERT INTO users VALUES (?,?,?,?)", (user_id, account_id, iso(joined), gone and iso(gone)))
            account_users.append((user_id, joined))
        for uid, joined in account_users:
            if not engaged and rng.random() < 0.6:
                continue  # many users at disengaged accounts never act
            for _ in range(rng.randint(1, 25)):
                when = joined + dt.timedelta(days=rng.random() * (60 if engaged else 25))
                if when > AS_OF:
                    continue
                kind = rng.choices(["login", "create_project", "invite_teammate", "export"],
                                   [0.6, 0.2 if engaged else 0.08, 0.12 if engaged else 0.03, 0.08])[0]
                event_id += 1
                con.execute("INSERT INTO events VALUES (?,?,?,?)", (event_id, uid, kind, iso(when)))
        # Subscriptions: start, optional upgrade (new row), optional churn.
        begin = (created + dt.timedelta(days=rng.randrange(0, 10))).date()
        plan, mrr = plans[0]
        segments = []
        upgrade = begin + dt.timedelta(days=rng.randrange(45, 150)) if rng.random() < 0.25 and not is_test else None
        churn = begin + dt.timedelta(days=rng.randrange(40, 240)) if rng.random() < (0.30 if name == "SMB" else 0.15) and not is_test else None
        limit = AS_OF.date()
        if upgrade and upgrade < limit and (not churn or upgrade < churn):
            segments.append((plan, mrr, begin, upgrade))
            segments.append((plans[-1][0], plans[-1][1], upgrade, churn if churn and churn < limit else None))
        else:
            segments.append((plan, mrr, begin, churn if churn and churn < limit else None))
        for plan, mrr, s_start, s_end in segments:
            sub_id += 1
            con.execute("INSERT INTO subscriptions VALUES (?,?,?,?,?,?)",
                        (sub_id, account_id, plan, mrr, s_start.isoformat(), s_end and s_end.isoformat()))
            for month in month_starts(s_start, (s_end or limit) - dt.timedelta(days=1)):
                bill = max(month, s_start)
                if bill > limit or (s_end and bill >= s_end):
                    continue
                invoice_id += 1
                status = rng.choices(["paid", "void", "refunded"], [0.95, 0.04, 0.01])[0]
                con.execute("INSERT INTO invoices VALUES (?,?,?,?,?,?)",
                            (invoice_id, account_id, sub_id, bill.isoformat(), mrr, status))
    for table in ["accounts", "users", "subscriptions", "invoices", "events"]:
        con.execute("INSERT INTO load_log VALUES (?,?)", (table, iso(AS_OF)))
    con.commit()
    con.close()
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, help="Output SQLite file (overwritten)")
    print(build(parser.parse_args().db))


if __name__ == "__main__":
    main()

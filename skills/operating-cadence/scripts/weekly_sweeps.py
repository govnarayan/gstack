"""Generate a read-only weekly review pack from a JSON or flat CSV snapshot."""

import argparse
import csv
import json
import sys
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path


GROUPS = {
    "task": "tasks",
    "metric": "metrics",
    "handoff": "handoffs",
    "decision": "decisions",
}
HEADINGS = ("Status changes", "Number moves", "Blocked work", "Dropped handoffs", "Decisions due")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def field(row, key, *, required=True):
    value = row.get(key, "")
    require(isinstance(value, str), f"{key} must be text")
    value = value.strip()
    require(not required or value, f"{key} is required")
    return value


def day(row, key):
    value = field(row, key)
    result = date.fromisoformat(value)
    require(result.isoformat() == value, f"{key} must be YYYY-MM-DD")
    return result


def number(value):
    require(isinstance(value, (str, int, float)) and not isinstance(value, bool),
            "metric values must be numeric")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("metric values must be numeric") from exc
    require(result.is_finite(), "metric values must be finite")
    return result


def unique_index(rows):
    require(isinstance(rows, list), "tracker groups must be lists")
    index = {}
    for row in rows:
        require(isinstance(row, dict), "tracker records must be objects")
        identifier = field(row, "id")
        require(identifier not in index, f"duplicate record ID: {identifier}")
        index[identifier] = row
    return index


def load_csv(handle):
    reader = csv.DictReader(handle)
    require(reader.fieldnames and {"kind", "id"} <= set(reader.fieldnames),
            "CSV requires kind and id columns")
    require(len(reader.fieldnames) == len(set(reader.fieldnames)), "duplicate CSV column")
    tracker = {group: [] for group in GROUPS.values()}
    tracker["authority"] = {}
    for row in reader:
        require(None not in row and None not in row.values(), "CSV row does not match its header")
        kind = field(row, "kind")
        if kind == "authority":
            identifier = field(row, "id")
            require(identifier not in tracker["authority"], f"duplicate authority: {identifier}")
            row["agree"] = [name.strip() for name in row.get("agree", "").split("|") if name.strip()]
            tracker["authority"][identifier] = row
        else:
            require(kind in GROUPS, f"unknown CSV record kind: {kind}")
            if kind == "metric":
                row["history"] = row.get("history", "").split("|")
            tracker[GROUPS[kind]].append(row)
    return tracker


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_tracker(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        if path.suffix.lower() == ".csv":
            return load_csv(handle)
        require(path.suffix.lower() == ".json", "tracker must be a .json or .csv file")
        return json.load(handle, object_pairs_hook=unique_object)


def ownership(role, dri):
    require(not role or not dri or role == dri, "role chart and DRI disagree")
    return role or dri


def display(value):
    return format(value.normalize(), "f")


def weekly_pack(tracker, week_ending, next_review):
    require(isinstance(tracker, dict), "tracker must be an object")
    require(next_review > week_ending, "next review must follow the source week")
    week_start = week_ending - timedelta(days=6)
    groups = {group: unique_index(tracker.get(group, [])) for group in GROUPS.values()}
    authority = tracker.get("authority", {})
    require(isinstance(authority, dict), "authority must be an object keyed by decision ID")
    require(set(authority) <= set(groups["decisions"]), "authority refers to an unknown decision")
    changed, numbers, blocked, handoffs, decisions = [], [], [], [], []

    for identifier, row in sorted(groups["tasks"].items()):
        label = f"{identifier} {field(row, 'name')}"
        status = field(row, "status")
        require(status in {"open", "blocked", "done", "shipped", "slipped"}, f"{label}: invalid status")
        updated = day(row, "updated_on")
        require(updated <= week_ending, f"{label}: update is after the source week")
        owner = ownership(field(row, "accountable", required=False), field(row, "dri", required=False))
        owner_note = owner or "MISSING accountable owner"
        if status in {"shipped", "done", "slipped"} and updated >= week_start:
            outcome = "shipped" if status == "done" else status
            reason = field(row, "reason", required=False)
            if outcome == "slipped":
                outcome += f" ({reason or 'no stated reason'})"
            changed.append(f"{label} — {outcome}. Accountable: {owner_note}.")
        if status in {"done", "shipped"}:
            continue
        if status == "blocked":
            since = day(row, "blocked_since")
            require(since <= updated, f"{label}: block begins after the update")
        else:
            since = updated
        age = (week_ending - since).days
        if status == "blocked" or age >= 7:
            waiting = field(row, "waiting_on", required=False) or "not recorded"
            kind = "blocked" if status == "blocked" else "unchanged"
            blocked.append((-age, identifier,
                            f"{label} — {kind} for {age} days. Accountable: {owner_note}. Waiting on: {waiting}."))

    for identifier, row in sorted(groups["metrics"].items()):
        label = f"{identifier} {field(row, 'name')}"
        history = row.get("history")
        require(isinstance(history, list) and len(history) == 4, f"{label}: needs four prior weeks")
        average = sum(number(value) for value in history) / 4
        current = number(row.get("current"))
        tolerance = number(row.get("tolerance"))
        require(tolerance >= 0, f"{label}: tolerance must be nonnegative")
        owner = field(row, "owner")
        if abs(current - average) > tolerance:
            guess = field(row, "guess", required=False)
            cause = f"Guess: {guess}." if guess else "No cause proposed."
            numbers.append(f"{label} — {display(current)} vs four-week average {display(average)} "
                           f"(±{display(tolerance)}). Owner: {owner}. {cause}")

    for identifier, row in sorted(groups["handoffs"].items()):
        label = f"{identifier} {field(row, 'name')}"
        handed = day(row, "handed_on")
        moved = day(row, "last_moved_on")
        require(handed <= moved <= week_ending, f"{label}: handoff dates are out of order")
        sender = field(row, "sender")
        receiver = field(row, "receiver")
        status = field(row, "status")
        require(status in {"open", "done"}, f"{label}: invalid status")
        stalled = (week_ending - moved).days
        if status == "open" and moved == handed and 7 <= stalled <= 30:
            handoffs.append(f"{label} — {stalled} days without movement. Sender: {sender}. Receiver: {receiver}.")

    for identifier, row in sorted(groups["decisions"].items()):
        rights = authority.get(identifier, {})
        require(isinstance(rights, dict), f"{identifier}: authority record must be an object")
        decider = ownership(field(rights, "decide", required=False), field(row, "dri", required=False))
        require(decider, f"{identifier}: named decider is required")
        agree = rights.get("agree", [])
        require(isinstance(agree, list) and all(isinstance(name, str) and name.strip() for name in agree),
                f"{identifier}: agree must be a list of named veto holders")
        status = field(row, "status")
        require(status in {"open", "proposed", "decided"}, f"{identifier}: invalid decision status")
        label = f"{identifier} {field(row, 'question', required=False) or field(rights, 'question')}"
        due = day(row, "latest_safe_on")
        if status == "decided":
            recorded = field(row, "decided_by", required=False) or "nobody"
            if recorded == decider:
                continue
            decisions.append(f"{label} — authority exception. Recorded as decided by {recorded}. "
                             f"Named decider: {decider}.")
        if due < next_review:
            veto = f" Veto holders: {', '.join(agree)}." if agree else ""
            decisions.append(f"{label} — latest safe date {due}. Decider: {decider}.{veto}")

    return changed, numbers, [note for _, _, note in sorted(blocked)], handoffs, decisions


def render(pack, week_ending, next_review):
    lines = [f"# Week ending {week_ending}", "", f"Next review {next_review}"]
    for title, items in zip(HEADINGS, pack):
        lines.extend(("", f"## {title}", ""))
        lines.extend(f"- {item}" for item in (items or ["None."]))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tracker", type=Path)
    parser.add_argument("--week-ending", required=True)
    parser.add_argument("--next-review", required=True)
    args = parser.parse_args()
    try:
        dates = vars(args)
        week_ending = day(dates, "week_ending")
        next_review = day(dates, "next_review")
        pack = weekly_pack(load_tracker(args.tracker), week_ending, next_review)
        sys.stdout.reconfigure(encoding="utf-8")
        print(render(pack, week_ending, next_review))
    except (OSError, ValueError, OverflowError, csv.Error) as exc:
        parser.exit(2, f"weekly_sweeps: {exc}\n")


if __name__ == "__main__":
    main()

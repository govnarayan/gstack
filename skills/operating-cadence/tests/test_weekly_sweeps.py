import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.weekly_sweeps import load_tracker, render, weekly_pack


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
WEEK_END = date(2026, 11, 13)
NEXT_REVIEW = date(2026, 11, 20)
EXPECTED = (
    [
        "T1 Pricing dashboard — shipped. Accountable: Data lead.",
        "T2 Sales briefing — slipped (Waiting on approved pricing copy). Accountable: Sales Ops lead.",
    ],
    [
        "M1 Trial starts — 80 vs four-week average 100 (±10). Owner: Growth lead. "
        "Guess: One acquisition campaign paused.",
    ],
    [
        "T3 Migration approval — blocked for 11 days. Accountable: MISSING accountable owner. Waiting on: Security.",
        "T4 Billing review — unchanged for 7 days. Accountable: Billing lead. Waiting on: not recorded.",
    ],
    [
        "H1 Enablement material — 7 days without movement. Sender: Product. Receiver: Sales Ops.",
    ],
    [
        "D1 Approve billing rollout — latest safe date 2026-11-18. Decider: COO. Veto holders: Legal lead.",
        "D2 Approve grandfathering — authority exception. Recorded as decided by VP Product. Named decider: CRO.",
        "D2 Approve grandfathering — latest safe date 2026-11-17. Decider: CRO.",
    ],
)


class WeeklySweepsTest(unittest.TestCase):
    def compute(self, tracker=None):
        if tracker is None:
            tracker = load_tracker(EXAMPLES / "weekly-sweeps-tracker.json")
        return weekly_pack(tracker, WEEK_END, NEXT_REVIEW)

    def test_known_week_in_each_format_and_embedded_output(self):
        for suffix in ("json", "csv"):
            with self.subTest(suffix=suffix):
                fixture = EXAMPLES / f"weekly-sweeps-tracker.{suffix}"
                original = fixture.read_bytes()
                tracker = load_tracker(fixture)
                self.assertEqual(self.compute(tracker), EXPECTED)
                out = subprocess.check_output(
                    [sys.executable, "-B", str(ROOT / "scripts" / "weekly_sweeps.py"), str(fixture),
                     "--week-ending", str(WEEK_END), "--next-review", str(NEXT_REVIEW)],
                    encoding="utf-8",
                )
                example = (EXAMPLES / "weekly-sweeps-week.md").read_text(encoding="utf-8")
                self.assertEqual(out, example.split("```markdown\n", 1)[1].split("```", 1)[0])
                self.assertEqual(original, fixture.read_bytes())

    def test_correcting_planted_exceptions_and_leaving_the_recorder_alone(self):
        tracker = load_tracker(EXAMPLES / "weekly-sweeps-tracker.json")
        tracker["tasks"][2]["accountable"] = "Migration lead"
        tracker["decisions"][1]["decided_by"] = "CRO"
        changed, numbers, blocked, handoffs, decisions = self.compute(tracker)
        self.assertEqual((changed, numbers, handoffs), (EXPECTED[0], EXPECTED[1], EXPECTED[3]))
        self.assertIn("Accountable: Migration lead.", blocked[0])
        self.assertEqual(decisions, EXPECTED[4][:1])

    def test_invalid_records(self):
        defects = [
            ("metrics", 0, "history", [1, 2, 3], "four prior weeks"),
            ("metrics", 0, "current", "NaN", "finite"),
            ("decisions", 0, "latest_safe_on", "2026-W46-1", "YYYY-MM-DD"),
            ("decisions", 0, "dri", "Different owner", "role chart and DRI disagree"),
            ("tasks", 0, "status", "unknown", "invalid status"),
            ("tasks", 0, "updated_on", "2026-11-14", "after the source week"),
            ("handoffs", 0, "last_moved_on", "2026-11-02", "out of order"),
        ]
        for group, index, key, value, error in defects:
            with self.subTest(group=group, key=key):
                tracker = load_tracker(EXAMPLES / "weekly-sweeps-tracker.json")
                tracker[group][index][key] = value
                with self.assertRaisesRegex(ValueError, error):
                    self.compute(tracker)

    def test_handoff_accepted_then_stalled_is_not_dropped(self):
        tracker = load_tracker(EXAMPLES / "weekly-sweeps-tracker.json")
        tracker["handoffs"][0]["handed_on"] = "2026-11-04"
        self.assertEqual(self.compute(tracker)[3], [])
        with self.assertRaisesRegex(ValueError, "next review"):
            weekly_pack({}, WEEK_END, WEEK_END)

    def test_rejects_unknown_csv_kind_without_output(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "invalid.csv"
            path.write_bytes(b"kind,id\nunknown,U1\n")
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / "scripts" / "weekly_sweeps.py"), str(path),
                 "--week-ending", str(WEEK_END), "--next-review", str(NEXT_REVIEW)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertIn("unknown CSV record kind", result.stderr)

    def test_empty_sections_are_kept(self):
        result = render(self.compute({}), WEEK_END, NEXT_REVIEW)
        self.assertEqual(result.count("\n## "), 5)
        self.assertEqual(result.count("- None."), 5)

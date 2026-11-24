"""Tests for the self-serve analytics case. Run: python -m unittest discover -s skills/self-serve-analytics/tests"""
import contextlib
import json
import pathlib
import sqlite3
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import analytics_demo as a  # noqa: E402
import build_demo_db  # noqa: E402


class AnalyticsCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        out = pathlib.Path(cls.tmp.name)
        done = subprocess.run([sys.executable, str(ROOT / "scripts" / "analytics_demo.py"), "--out", str(out), "--strict"],
                              capture_output=True, text=True)
        cls.exit_code, cls.stdout = done.returncode, done.stdout
        cls.report = json.loads((out / "report.json").read_text(encoding="utf-8"))
        cls.dashboard = (out / "dashboard.html").read_text(encoding="utf-8")
        cls.db = out / "demo.sqlite"

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def statuses(self, variant, query):
        return [c["status"] for c in self.report["checks"][variant][query]]

    def test_reviewed_queries_pass_every_blocking_check(self):
        self.assertEqual(0, self.exit_code, self.stdout)
        for query in a.QUERIES:
            self.assertNotIn("fail", self.statuses("reviewed", query), query)

    def test_each_draft_defect_is_caught_by_the_check_built_for_it(self):
        expected = {
            "monthly_revenue": ["fail", "warn"],                # void/refunded and test invoices counted
            "revenue_by_segment_q3": ["fail", "fail"],          # fan-out: reconciliation and grain probe both fail
            "activation_by_cohort": ["fail", "fail", "fail"],   # denominator, integer division, OR-for-AND
            "active_at_quarter_end": ["fail", "fail"],          # NULL end dates dropped
            "retention_90d_by_cohort": ["fail", "fail"],        # immature cohorts, status-today definition
        }
        for query, statuses in expected.items():
            self.assertEqual(statuses, self.statuses("ai-draft", query), query)

    def test_fanout_is_quantified_not_just_flagged(self):
        detail = self.report["checks"]["ai-draft"]["revenue_by_segment_q3"][1]["detail"]
        self.assertIn("repeated about", detail)
        draft = sum(r["revenue_usd"] for r in self.report["results"]["ai-draft"]["revenue_by_segment_q3"])
        reviewed = sum(r["revenue_usd"] for r in self.report["results"]["reviewed"]["revenue_by_segment_q3"])
        self.assertGreater(draft, 5 * reviewed)

    def test_dates_with_mixed_separators_are_compared_after_normalizing(self):
        con = self.enterContext(contextlib.closing(sqlite3.connect(self.db)))
        stored, computed = con.execute("SELECT created_at, datetime(created_at, '+1 day') FROM accounts LIMIT 1").fetchone()
        self.assertIn("T", stored)
        self.assertIn(" ", computed)
        # A raw string comparison of a 'T' timestamp with a space timestamp on the same date is always "greater".
        self.assertEqual(1, con.execute("SELECT '2026-01-05T01:00:00' > '2026-01-05 23:00:00'").fetchone()[0])
        self.assertEqual(0, con.execute("SELECT datetime('2026-01-05T01:00:00') > datetime('2026-01-05 23:00:00')").fetchone()[0])

    def test_pre_signup_events_cannot_activate_an_account(self):
        con = self.enterContext(contextlib.closing(sqlite3.connect(self.db)))
        sql = (a.SQL / "reviewed" / "activation_by_cohort.sql").read_text()
        before = a.rows(con, sql)
        con.execute("INSERT INTO accounts VALUES (-1, 'Timing test', 'test', 'US', '2026-01-08T00:00:00', 0)")
        con.execute("INSERT INTO users VALUES (-1, -1, '2026-01-08T00:00:00', NULL)")
        con.executemany("INSERT INTO events VALUES (?, -1, ?, '2026-01-07T00:00:00')",
                        [(-1, 'create_project'), (-2, 'invite_teammate')])
        after = a.rows(con, sql)
        old = next(row for row in before if row["cohort_month"] == "2026-01")
        new = next(row for row in after if row["cohort_month"] == "2026-01")
        self.assertEqual(old["accounts"] + 1, new["accounts"])
        self.assertEqual(old["activated"], new["activated"])
        self.assertEqual(new["activated"], a.oracle(con)["activation"]["2026-01"]["activated"])

    def test_integer_division_truncates_in_sqlite(self):
        con = self.enterContext(contextlib.closing(sqlite3.connect(":memory:")))
        self.assertEqual(0, con.execute("SELECT 3 / 4").fetchone()[0])
        self.assertEqual(0.75, con.execute("SELECT 1.0 * 3 / 4").fetchone()[0])

    def test_not_in_with_null_returns_nothing(self):
        con = self.enterContext(contextlib.closing(sqlite3.connect(":memory:")))
        self.assertIsNone(con.execute("SELECT 1 WHERE 2 NOT IN (1, NULL)").fetchone())

    def test_dashboard_labels_partial_period_freshness_and_definitions(self):
        for text in ["Partial month", "Data loaded through", "Definitions", "Denominator includes accounts with no activity",
                     "What the unreviewed AI drafts would have reported", "Synthetic"]:
            self.assertIn(text, self.dashboard)
        self.assertIn('class="bar partial"', self.dashboard)

    def test_stale_build_is_labeled_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, str(ROOT / "scripts" / "analytics_demo.py"), "--out", tmp,
                            "--built-at", "2026-10-25T00:00:00"], check=True, capture_output=True)
            self.assertIn("(stale,", (pathlib.Path(tmp) / "dashboard.html").read_text(encoding="utf-8"))

    def test_a_broken_reviewed_query_makes_strict_mode_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            con = sqlite3.connect(build_demo_db.build(pathlib.Path(tmp) / "x.sqlite"))
            truth = a.oracle(con)
            broken = (a.SQL / "reviewed" / "active_at_quarter_end.sql").read_text().replace(
                "(s.ended_at IS NULL OR s.ended_at > '2026-09-30')", "s.ended_at > '2026-09-30'")
            result = a.rows(con, broken)
            checks = a.run_checks(con, "active_at_quarter_end", broken, result, truth, {})
            con.close()
            self.assertIn("fail", [c["status"] for c in checks])

    def test_data_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            one = build_demo_db.build(pathlib.Path(tmp) / "one.sqlite")
            two = build_demo_db.build(pathlib.Path(tmp) / "two.sqlite")
            q = "SELECT COUNT(*), SUM(amount_cents) FROM invoices"
            with contextlib.closing(sqlite3.connect(one)) as c1, contextlib.closing(sqlite3.connect(two)) as c2:
                self.assertEqual(c1.execute(q).fetchone(), c2.execute(q).fetchone())


if __name__ == "__main__":
    unittest.main()


class ReferenceArithmetic(unittest.TestCase):
    """Pins the worked numbers quoted in references/metric-trees-and-analysis-traps.md."""

    def test_simpsons_example(self):
        a = {"SMB": (80, 16), "Enterprise": (20, 12)}
        b = {"SMB": (200, 42), "Enterprise": (20, 13)}
        for seg in a:
            self.assertGreater(b[seg][1] / b[seg][0], a[seg][1] / a[seg][0])  # every segment improves
        total = lambda d: sum(x[1] for x in d.values()) / sum(x[0] for x in d.values())
        self.assertAlmostEqual(0.28, total(a))
        self.assertAlmostEqual(0.25, total(b))                                  # yet the total falls
        self.assertAlmostEqual(0.43, (0.21 + 0.65) / 2)                         # average of rates
        self.assertAlmostEqual(0.909, 200 / 220, places=3)

    def test_sample_ratio_mismatch_example(self):
        import math
        expected = (4000 + 3700) / 2
        chi2 = sum((x - expected) ** 2 / expected for x in (4000, 3700))
        p = math.erfc(math.sqrt(chi2 / 2))                                      # one degree of freedom
        self.assertAlmostEqual(11.69, chi2, places=2)
        self.assertLess(p, 0.001)
        self.assertGreater(p, 0.0005)

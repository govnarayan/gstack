"""Tests for org_design_check.py. Run: python -m unittest discover -s skills/organization-and-change/tests"""
import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import org_design_check as oc  # noqa: E402

ROSTER = oc.load_roster(ROOT / "examples" / "org-roster.csv")
PLAN = json.loads((ROOT / "examples" / "org-design-plan.json").read_text(encoding="utf-8"))


class OrgDesignCheck(unittest.TestCase):
    def setUp(self):
        self.result = oc.check(ROSTER, copy.deepcopy(PLAN))

    def flagged(self, side):
        return {f["id"] for f in self.result[side]["flags"]}

    def test_spans_and_layers(self):
        self.assertEqual(57, self.result["before"]["people"])
        self.assertEqual(5, self.result["before"]["layers"])
        self.assertEqual(12, self.result["before"]["spans"]["M12"])

    def test_design_fixes_some_flags_and_exposes_a_new_one(self):
        self.assertIn("M07", self.flagged("before"))           # two-person manager role removed
        self.assertNotIn("M07", self.flagged("after"))
        self.assertNotIn("M04", {f["id"] for f in self.result["before"]["flags"] if "one or two" in f["flag"]})
        self.assertIn("M04", {f["id"] for f in self.result["after"]["flags"] if "one or two" in f["flag"]})

    def test_capacity_includes_ramp(self):
        q1 = self.result["capacity"]["Solutions engineering"][0]
        self.assertEqual(3.5, q1["staffed"])
        self.assertEqual(2.5, q1["productive"])                # two new hires count half in their first quarter
        self.assertLess(q1["gap"], 0)

    def test_transition_cost_adds_run_rate_and_one_time(self):
        q1 = self.result["costs"]["by_quarter"][0]
        self.assertEqual(295000, q1["one_time"])              # recruiting fees plus three setup items
        self.assertEqual(q1["added_run_rate"] + q1["one_time"], q1["total"])

    def test_pooling_beats_dedicated_for_both_queues(self):
        dedicated, pooled4, pooled5 = self.result["review_pool_test"]
        self.assertGreater(dedicated["pools"][0]["mean_wait_working_days"], pooled4["pools"][0]["mean_wait_working_days"])
        self.assertGreater(dedicated["pools"][1]["mean_wait_working_days"], 10)
        self.assertLess(pooled5["pools"][0]["mean_wait_working_days"], 0.5)

    def test_overloaded_pool_reports_unbounded_wait(self):
        plan = copy.deepcopy(PLAN)
        plan["review_pool_test"]["options"] = [{"name": "Too few", "pools": [
            {"streams": ["enterprise_deal_reviews", "vendor_and_self_serve_reviews"], "reviewers": 3}]}]
        pool = oc.pool_test(plan)[0]["pools"][0]
        self.assertIsNone(pool["mean_wait_working_days"])
        self.assertGreater(pool["utilization"], 1)

    def test_erlang_c_known_value(self):
        # Two servers, one erlang offered: probability of waiting is 1/3.
        self.assertAlmostEqual(1 / 3, oc.erlang_c(2, 1.0), places=6)

    def test_bad_structure_rejected(self):
        roster = copy.deepcopy(ROSTER)
        roster["M02"]["manager_id"] = "M05"                    # cycle
        with self.assertRaises(ValueError):
            oc.structure(roster, PLAN["span_archetypes"])
        plan = copy.deepcopy(PLAN)
        plan["changes"].append({"id": "X99", "manager_id": "M01"})
        with self.assertRaisesRegex(ValueError, "unknown person"):
            oc.check(ROSTER, plan)

    def test_markdown_renders(self):
        text = oc.markdown(self.result)
        for part in ["Spans and layers", "Flags after", "Transition cost", "Pooled versus dedicated"]:
            self.assertIn(part, text)


if __name__ == "__main__":
    unittest.main()

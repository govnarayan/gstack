"""Tests for program_check.py. Run: python -m unittest discover -s skills/cross-functional-execution/tests"""
import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import program_check as pc  # noqa: E402

EXAMPLE = json.loads((ROOT / "examples" / "usage-pricing-program.json").read_text(encoding="utf-8"))


def items(result, area):
    return {(f["item"], f["severity"]) for f in result["findings"] if f["area"] == area}


class ProgramCheck(unittest.TestCase):
    def setUp(self):
        self.program = copy.deepcopy(EXAMPLE)
        self.result = pc.check(copy.deepcopy(self.program))

    def test_forecast_and_both_critical_paths(self):
        self.assertEqual(18, self.result["baseline_finish_week"])
        self.assertEqual(21, self.result["forecast_finish_week"])
        self.assertEqual({"B1 > B2 > B3 > L1", "P2 > C1 > C2 > L1"}, set(self.result["critical_paths"]))

    def test_options_are_recomputed_not_asserted(self):
        options = {o["option"][:12]: o for o in self.result["options"]}
        self.assertTrue(options["Launch new c"]["meets_commit"])
        self.assertEqual(20, options["Launch new c"]["finish_week"])
        contractor = options["Add a contra"]
        self.assertEqual(21, contractor["finish_week"])            # the notice path still binds
        self.assertEqual(["P2 > C1 > C2 > L1"], contractor["binding_paths"])

    def test_overload_counts_outside_commitments(self):
        self.assertIn(("billing_lead", "blocking"), items(self.result, "capacity"))
        self.assertEqual(1.2, self.result["load"]["billing_lead"][10])

    def test_decision_recorded_by_wrong_person_is_not_a_decision(self):
        messages = [f["message"] for f in self.result["findings"] if f["item"] == "D-03"]
        self.assertTrue(any("belongs to CFO" in m for m in messages))
        self.assertFalse(any(f["item"] == "D-01" for f in self.result["findings"]))

    def test_change_above_threshold_needs_named_approver(self):
        self.assertIn(("CR-01", "blocking"), items(self.result, "change control"))

    def test_log_hygiene(self):
        log = items(self.result, "log")
        self.assertIn(("A-01", "blocking"), log)     # no owner
        self.assertIn(("R-03", "warning"), log)      # past due and stale
        self.assertNotIn("R-01", {i for i, _ in log})  # realized risks are tracked as issues

    def test_high_issue_without_decision_blocks(self):
        program = copy.deepcopy(self.program)
        for r in program["raid"]:
            if r["id"] == "I-01":
                r.pop("decision")
        self.assertIn(("I-01", "blocking"), items(pc.check(program), "log"))

    def test_benefit_without_baseline_and_milestone_without_acceptor(self):
        self.assertIn(("BEN-02", "blocking"), items(self.result, "benefits"))
        self.assertIn(("M3", "blocking"), items(self.result, "acceptance"))

    def test_clean_program_has_no_blocking_findings(self):
        program = copy.deepcopy(self.program)
        program["committed_finish_week"] = 21
        program["people"]["billing_lead"]["other_commitments"] = []
        program["raid"] = [r for r in program["raid"] if r["id"] not in ("A-01", "R-03")]
        program["decisions"][1].update(decided_by="CFO", agreed_by=["CRO"])
        program["changes"][0]["approved_by"] = "COO"
        program["benefits"][1].update(baseline=0, baseline_source="No usage revenue before launch")
        program["milestones"][2]["acceptor"] = "General Counsel"
        blocking = [f for f in pc.check(program)["findings"] if f["severity"] == "blocking"]
        self.assertEqual([], blocking)

    def test_cycle_and_missing_remaining_work_rejected(self):
        program = copy.deepcopy(self.program)
        program["tasks"][0]["after"] = ["L1"]
        with self.assertRaisesRegex(ValueError, "cycle"):
            pc.check(program)
        program = copy.deepcopy(self.program)
        program["tasks"][3].pop("remaining_weeks")
        with self.assertRaisesRegex(ValueError, "remaining_weeks"):
            pc.check(program)

    def test_status_pack_renders(self):
        text = pc.markdown(self.result, self.program)
        for part in ["Off track", "Critical path", "Decision needed", "| done |", "Capacity above 100%"]:
            self.assertIn(part, text)


if __name__ == "__main__":
    unittest.main()

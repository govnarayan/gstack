import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("cohorts", BASE / "scripts/subscription_cohorts.py")
MODEL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODEL)


class CohortTests(unittest.TestCase):
    def case(self):
        return json.loads((BASE / "examples/subscription-growth.json").read_text())

    def test_overflowing_projection_returns_a_clean_error(self):
        case = self.case()
        case["initiatives"][0].update(eligible_population=1e308, contribution_per_paid_month=1e308)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "large.json"
            path.write_text(json.dumps(case), encoding="utf-8")
            run = subprocess.run([sys.executable, str(SPEC.origin), str(path)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 2)
        self.assertIn("Invalid case", run.stderr)
        self.assertNotIn("Traceback", run.stderr)

    def test_worked_case_and_monthly_reconciliation(self):
        results = MODEL.evaluate(self.case())["results"]
        for item in results:
            self.assertAlmostEqual(item["net_incremental_contribution"],
                                   sum(row["contribution_after_recurring_cost"] for row in item["monthly"])
                                   - item["one_time_cost"])
        self.assertAlmostEqual(results[0]["ending_incremental_paid_memberships"], 3469.2118049771884)
        self.assertAlmostEqual(results[1]["ending_incremental_paid_memberships"], 4415.598483121319)
        self.assertGreater(results[0]["net_incremental_contribution"], results[1]["net_incremental_contribution"])
        self.assertEqual(results[2]["incremental_paid_member_months"], 0)
        self.assertLess(results[2]["net_incremental_contribution"], 0)

    def test_no_retention_effect_still_pays_cost(self):
        case = self.case()
        row = case["initiatives"][1]
        row["treatment_monthly_survival"] = row["baseline_monthly_survival"]
        case["initiatives"] = [row]
        result = MODEL.evaluate(case)["results"][0]
        self.assertEqual(result["ending_incremental_paid_memberships"], 0)
        self.assertEqual(result["net_incremental_contribution"], -row["one_time_cost"])

    def test_worse_retention_is_negative_not_clipped(self):
        case = self.case()
        row = case["initiatives"][1]
        row["treatment_monthly_survival"] = 0.96
        case["initiatives"] = [row]
        self.assertLess(MODEL.evaluate(case)["results"][0]["ending_incremental_paid_memberships"], 0)

    def test_recurring_cost_and_no_survivors(self):
        case = self.case()
        row = case["initiatives"][0]
        row["monthly_survival"] = 0
        row["recurring_monthly_cost"] = 10
        case["initiatives"] = [row]
        result = MODEL.evaluate(case)["results"][0]
        self.assertEqual(result["net_incremental_contribution"], -120120)

    def test_invalid_rates_nan_booleans_and_duplicate_names(self):
        for field, bad in [("monthly_survival", 97), ("monthly_survival", float("nan")),
                           ("eligible_population", True)]:
            case = self.case()
            case["initiatives"][0][field] = bad
            with self.assertRaises(ValueError):
                MODEL.evaluate(case)
        case = self.case()
        case["initiatives"][1]["name"] = case["initiatives"][0]["name"]
        with self.assertRaises(ValueError):
            MODEL.evaluate(case)


if __name__ == "__main__":
    unittest.main()

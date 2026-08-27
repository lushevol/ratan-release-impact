from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "evidence.py"
SPEC = importlib.util.spec_from_file_location("test_engine_evidence", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
EVIDENCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVIDENCE)


class ComparisonClassificationTest(unittest.TestCase):
    def test_supported_transitions(self) -> None:
        passed = {"status": "PASS"}
        failed = {"status": "FAIL"}

        self.assertEqual(EVIDENCE.comparison_classification(passed, passed), "preserved_behavior")
        self.assertEqual(EVIDENCE.comparison_classification(passed, failed), "candidate_simulation_regression")
        self.assertEqual(EVIDENCE.comparison_classification(failed, passed), "baseline_recovered")
        self.assertEqual(EVIDENCE.comparison_classification(failed, failed), "persistent_failure")
        self.assertEqual(EVIDENCE.comparison_classification(None, passed), "target_observed")
        self.assertEqual(EVIDENCE.comparison_classification(None, failed), "target_not_observed")
        self.assertEqual(EVIDENCE.comparison_classification(passed, None), "missing_after")

    def test_comparison_never_claims_production_proof(self) -> None:
        common_test = {
            "test_id": "test:example",
            "test_name": "Example",
            "behavior_id": "behavior:example",
            "scenario_id": "scenario:example",
            "status": "PASS",
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = {
                "change_id": "CHANGE-1",
                "phase": "before",
                "run_id": "before-run",
                "engine_baseline": {"source_fingerprint_sha256": "before"},
                "tests": [common_test],
            }
            after = {
                "change_id": "CHANGE-1",
                "phase": "after",
                "run_id": "after-run",
                "engine_baseline": {"source_fingerprint_sha256": "after"},
                "tests": [common_test],
            }
            before_path = root / "before.json"
            after_path = root / "after.json"
            before_path.write_text(json.dumps(before), encoding="utf-8")
            after_path.write_text(json.dumps(after), encoding="utf-8")

            result = EVIDENCE.compare_runs(before_path, after_path)

        self.assertEqual(result["simulation_verdict"], "PASS")
        self.assertEqual(result["production_proof_verdict"], "NOT_PROVEN")
        self.assertTrue(result["engine_changed"])


if __name__ == "__main__":
    unittest.main()

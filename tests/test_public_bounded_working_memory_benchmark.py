import json
import tempfile
import unittest
from pathlib import Path

from bounded_working_memory_benchmark import verify_provability_gate


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark" / "bounded-working-memory"


class PublicBoundedWorkingMemoryTests(unittest.TestCase):
    def test_published_provability_gate_is_valid(self):
        report = verify_provability_gate(
            BENCHMARK / "provability_gate_freeze.json",
            BENCHMARK / "provability_gate_cases.json",
            BENCHMARK / "provability_gate_result.json",
        )

        self.assertTrue(report["valid"])
        self.assertEqual(report["status"], "PROVABILITY_PASS")
        self.assertEqual(report["errors"], ())

    def test_public_verifier_rejects_tampered_case_data(self):
        case_path = BENCHMARK / "provability_gate_cases.json"
        case_data = json.loads(case_path.read_text(encoding="utf-8"))
        case_data["episodes"][0]["seed"] += 1

        with tempfile.TemporaryDirectory() as directory:
            tampered_path = Path(directory) / "tampered.json"
            tampered_path.write_text(
                json.dumps(case_data, sort_keys=True, indent=2) + "\n",
                encoding="utf-8",
            )

            report = verify_provability_gate(
                BENCHMARK / "provability_gate_freeze.json",
                tampered_path,
                BENCHMARK / "provability_gate_result.json",
            )

        self.assertFalse(report["valid"])
        self.assertIn("case_data_sha256 does not match the case data", report["errors"])

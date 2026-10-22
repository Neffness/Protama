import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from bounded_working_memory_benchmark import verify_frozen_profile


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark" / "bounded-working-memory-v1" / "gate-work"


class PublicBoundedWorkingMemoryTests(unittest.TestCase):
    def test_frozen_grounded_symbolic_profile_is_publicly_validated(self):
        report = verify_frozen_profile(
            BENCHMARK / "grounded-symbolic-composition-freeze-v1.json",
            BENCHMARK / "grounded-symbolic-composition-final-v1.json",
        )

        self.assertTrue(report["valid"])
        self.assertEqual(report["result"], "DEVELOPMENT_PASS")
        self.assertEqual(report["errors"], ())

    def test_public_verifier_rejects_tampered_result(self):
        result_path = (
            BENCHMARK / "grounded-symbolic-composition-final-v1.json"
        )
        result = json.loads(result_path.read_text(encoding="utf-8"))
        result["metrics"]["withheld_composition_accuracy"] = 0.5
        with tempfile.TemporaryDirectory() as directory:
            tampered_path = Path(directory) / "tampered.json"
            tampered_path.write_text(json.dumps(result), encoding="utf-8")

            report = verify_frozen_profile(
                BENCHMARK / "grounded-symbolic-composition-freeze-v1.json",
                tampered_path,
            )

        self.assertFalse(report["valid"])
        self.assertIn(
            "withheld_composition_accuracy is below its declared threshold",
            report["errors"],
        )

    def test_public_verifier_checks_v2_trial_and_baseline_evidence(self):
        report = verify_frozen_profile(
            BENCHMARK / "grounded-symbolic-composition-freeze-v2.json",
            BENCHMARK / "grounded-symbolic-composition-development-v2.json",
        )

        self.assertTrue(report["valid"])
        self.assertEqual(report["result"], "DEVELOPMENT_PASS")

    def test_temporal_sensor_freeze_hash_matches_contents(self):
        freeze_path = BENCHMARK / "temporal-sensor-stream-freeze-v1.json"
        freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
        unsigned = dict(freeze)
        unsigned["manifest_sha256"] = "PENDING"
        payload = json.dumps(
            unsigned,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode("ascii")

        self.assertEqual(
            hashlib.sha256(payload).hexdigest(),
            freeze["manifest_sha256"],
        )

import json
from pathlib import Path

from bounded_working_memory_benchmark import verify_frozen_profile


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark" / "bounded-working-memory-v1" / "gate-work"


def test_frozen_grounded_symbolic_profile_is_publicly_validated():
    report = verify_frozen_profile(
        BENCHMARK / "grounded-symbolic-composition-freeze-v1.json",
        BENCHMARK / "grounded-symbolic-composition-final-v1.json",
    )

    assert report["valid"]
    assert report["result"] == "PASS"
    assert report["errors"] == ()


def test_public_verifier_rejects_tampered_result(tmp_path):
    result_path = (
        BENCHMARK / "grounded-symbolic-composition-final-v1.json"
    )
    result = json.loads(result_path.read_text(encoding="utf-8"))
    result["metrics"]["withheld_composition_accuracy"] = 0.5
    tampered_path = tmp_path / "tampered.json"
    tampered_path.write_text(json.dumps(result), encoding="utf-8")

    report = verify_frozen_profile(
        BENCHMARK / "grounded-symbolic-composition-freeze-v1.json",
        tampered_path,
    )

    assert not report["valid"]
    assert "withheld_composition_accuracy is below its declared threshold" in report[
        "errors"
    ]

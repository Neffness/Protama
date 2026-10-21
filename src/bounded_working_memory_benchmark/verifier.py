"""Dependency-free validation of the frozen grounded-symbolic result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def _read_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def _manifest_digest(manifest: dict[str, Any]) -> str:
    unsigned = dict(manifest)
    unsigned["manifest_sha256"] = "PENDING"
    payload = json.dumps(
        unsigned,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def load_frozen_profile(
    manifest_path: str | Path,
    result_path: str | Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Load the frozen manifest and its machine-readable result."""
    return _read_json(manifest_path), _read_json(result_path)


def verify_frozen_profile(
    manifest_path: str | Path,
    result_path: str | Path,
) -> dict[str, Any]:
    """Validate the published frozen result without importing Protama."""
    manifest, result = load_frozen_profile(manifest_path, result_path)
    errors: list[str] = []

    expected_digest = manifest.get("manifest_sha256")
    if not isinstance(expected_digest, str):
        errors.append("manifest_sha256 is missing")
    elif _manifest_digest(manifest) != expected_digest:
        errors.append("manifest_sha256 does not match the manifest contents")

    for field in ("gate_version", "profile", "freeze_id", "manifest_sha256"):
        if result.get(field) != manifest.get(field):
            errors.append(f"result does not match manifest field: {field}")
    if result.get("result") != "DEVELOPMENT_PASS":
        errors.append("result is not DEVELOPMENT_PASS")
    if result.get("post_freeze_teaching") != "none":
        errors.append("post-freeze teaching was recorded")
    if result.get("held_out_policy_update_attempts") != 0:
        errors.append("held-out policy updates were attempted")

    thresholds = manifest.get("thresholds", {})
    metrics = result.get("metrics", {})
    minimums = (
        ("substrate_completeness_min", "substrate_completeness"),
        ("withheld_composition_accuracy_min", "withheld_composition_accuracy"),
        (
            "capacity_aware_abstention_accuracy_min",
            "capacity_aware_abstention_accuracy",
        ),
        ("snapshot_replay_agreement_min", "snapshot_replay_agreement"),
    )
    for threshold_name, metric_name in minimums:
        threshold = thresholds.get(threshold_name)
        metric = metrics.get(metric_name)
        if metric is None:
            errors.append(f"metric is missing: {metric_name}")
        elif not isinstance(threshold, (int, float)) or metric < threshold:
            errors.append(f"{metric_name} is below its declared threshold")

    maximums = (
        ("distractor_decrement_max", "distractor_decrement"),
        ("cross_thought_leakage_max", "cross_thought_leakage"),
        ("eviction_validity_failures_max", "eviction_validity_failures"),
        (
            "unauthorized_promotion_validity_failures_max",
            "unauthorized_promotion_validity_failures",
        ),
    )
    for threshold_name, metric_name in maximums:
        threshold = thresholds.get(threshold_name)
        metric = metrics.get(metric_name)
        if metric is None:
            errors.append(f"metric is missing: {metric_name}")
        elif not isinstance(threshold, (int, float)) or metric > threshold:
            errors.append(f"{metric_name} exceeds its declared threshold")

    expected_compositions = {
        case["input"]: case["result"]
        for case in manifest.get("held_out_compositions", [])
    }
    actual_compositions = {
        case.get("input"): case.get("actual")
        for case in result.get("held_out_compositions", [])
    }
    if actual_compositions != expected_compositions:
        errors.append("held-out composition outcomes do not match the manifest")

    expected_abstentions = {
        case["input"]: case["result"] for case in manifest.get("abstention_cases", [])
    }
    actual_abstentions = {
        case.get("input"): case.get("actual")
        for case in result.get("abstention_cases", [])
    }
    if actual_abstentions != expected_abstentions:
        errors.append("abstention outcomes do not match the manifest")
    if not all(case.get("abstained") is True for case in result.get("abstention_cases", [])):
        errors.append("an abstention case was not abstained")

    capacity = metrics.get("minimum_complete_capacity")
    declared_capacity = thresholds.get("minimum_complete_capacity")
    if capacity != declared_capacity:
        errors.append("minimum complete capacity does not match the threshold")

    if manifest.get("freeze_id") == "grounded-symbolic-composition-freeze-v2":
        expected_baselines = {
            baseline["name"] for baseline in manifest.get("baselines", [])
        }
        actual_baselines = {
            baseline.get("name") for baseline in result.get("baselines", [])
        }
        if actual_baselines != expected_baselines:
            errors.append("baseline result set does not match the manifest")
        for baseline in result.get("baselines", []):
            rows = baseline.get("trials", [])
            if len(rows) != len(manifest.get("held_out_compositions", [])):
                errors.append(
                    f"baseline trial count is wrong: {baseline.get('name')}"
                )
                continue
            successes = sum(row.get("correct") is True for row in rows)
            if baseline.get("accuracy") != successes / len(rows):
                errors.append(
                    f"baseline accuracy is not reproducible: {baseline.get('name')}"
                )
            interval = baseline.get("accuracy_interval_95")
            if (
                not isinstance(interval, list)
                or len(interval) != 2
                or not 0 <= interval[0] <= interval[1] <= 1
            ):
                errors.append(
                    f"baseline interval is invalid: {baseline.get('name')}"
                )

        capacity_trials = result.get("capacity_trials", [])
        expected_capacity_trials = len(
            manifest.get("held_out_compositions", [])
        ) * len(manifest.get("capacity_conditions", []))
        if len(capacity_trials) != expected_capacity_trials:
            errors.append("capacity trial count does not match the manifest")
        for metric_name in (
            "withheld_composition_interval_95",
            "capacity_aware_abstention_interval_95",
        ):
            interval = metrics.get(metric_name)
            if (
                not isinstance(interval, list)
                or len(interval) != 2
                or not 0 <= interval[0] <= interval[1] <= 1
            ):
                errors.append(f"metric interval is invalid: {metric_name}")

    return {
        "valid": not errors,
        "errors": tuple(errors),
        "manifest_sha256": manifest.get("manifest_sha256"),
        "result": result.get("result"),
    }

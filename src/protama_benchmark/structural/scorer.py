"""Episode-level scoring for structural-gate artifacts."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import random
from typing import Mapping

from .models import GateAdapterRun, GateTrace
from .generator import GateEpisode


DEFAULT_PASS_RULE = {
    "positive_transfer_accuracy_min": 0.90,
    "negative_rejection_accuracy_min": 0.90,
    "near_miss_accuracy_min": 0.90,
    "near_miss_category_accuracy_min": 0.85,
    "novel_vocabulary_accuracy_min": 0.90,
    "explanation_fidelity_min": 0.85,
    "coverage_min": 0.75,
    "selective_risk_max": 0.10,
}


@dataclass(frozen=True)
class EpisodeScore:
    positive_accuracy: float
    negative_rejection_accuracy: float
    near_miss_accuracy_by_category: dict[str, float]
    novel_vocabulary_accuracy: float
    surface_invariance: float | None
    compositional_generalization: float | None
    coverage: float
    selective_risk: float | None
    false_commitment_rate: float
    abstention_precision: float | None
    explanation_invariant_correctness: float
    explanation_irrelevance_recognition: float
    explanation_counterfactual_sensitivity: float
    explanation_trace_fidelity: float
    case_count: int


@dataclass(frozen=True)
class AggregateScore:
    """Deterministic multi-episode score and episode-bootstrap intervals."""

    episode_count: int
    metrics: dict[str, float | dict[str, float]]
    confidence_intervals: dict[str, dict[str, float]]


@dataclass(frozen=True)
class ExcludedEpisode:
    """An episode omitted from scoring with an explicit reproducibility reason."""

    episode_id: str
    reason: str
    stage: str


@dataclass(frozen=True)
class BaselineScore:
    baseline_name: str
    metrics: dict[str, float]


def _safe_rate(numerator: int, denominator: int) -> float | None:
    return None if denominator == 0 else numerator / denominator


def _trace_by_case(run: GateAdapterRun) -> Mapping[str, GateTrace]:
    return {trace.case_id: trace for trace in run.traces}


def _explanation_dimensions(
    episode: GateEpisode,
    run: GateAdapterRun,
) -> tuple[float, float, float, float]:
    traces = _trace_by_case(run)
    invariant: list[bool] = []
    irrelevant: list[bool] = []
    counterfactual: list[bool] = []
    fidelity: list[bool] = []
    for case in episode.evaluation:
        trace = traces[case.case_id]
        invariant.append(
            case.expected_status != "accepted"
            or bool(trace.explanation["invariants"])
        )
        irrelevant.append(
            case.expected_status != "accepted"
            or isinstance(trace.explanation["irrelevancies"], list)
        )
        counterfactual.append(
            case.category not in {"near_miss", "contradictory"}
            or bool(trace.explanation["counterfactuals"])
        )
        cited_features = set(trace.explanation["invariants"]) | set(
            trace.explanation["counterfactuals"]
        )
        trace_features = {
            evidence["feature"]
            for evidence in (
                *trace.selected_evidence,
                *trace.rejected_evidence,
            )
            if "feature" in evidence
        }
        fidelity.append(cited_features.issubset(trace_features))
    return tuple(
        sum(values) / len(values) if values else 0.0
        for values in (invariant, irrelevant, counterfactual, fidelity)
    )


def _flagged_accuracy(
    episode: GateEpisode,
    run: GateAdapterRun,
    rlag_name: str,
) -> float | None:
    predictions = {prediction.case_id: prediction for prediction in run.predictions}
    cases = [case for case in episode.evaluation if getattr(case, rlag_name)]
    if not cases:
        return None
    return sum(
        predictions[case.case_id].predicted_status == case.expected_status
        for case in cases
    ) / len(cases)


def score_structural_gate_episode(
    episode: GateEpisode,
    run: GateAdapterRun,
) -> EpisodeScore:
    """Score one adapter run against evaluator-side episode labels."""
    predictions = {prediction.case_id: prediction for prediction in run.predictions}
    if set(predictions) != {case.case_id for case in episode.evaluation}:
        raise ValueError("adapter predictions do not cover episode evaluation cases")

    correct = {
        case.case_id: predictions[case.case_id].predicted_status == case.expected_status
        for case in episode.evaluation
    }
    positives = [case for case in episode.evaluation if case.category == "positive"]
    negatives = [
        case
        for case in episode.evaluation
        if case.category in {"negative", "near_miss"}
    ]
    near_categories = {
        case.near_miss_category or case.category
        for case in episode.evaluation
        if case.near_miss_category is not None
        or case.category in {"ambiguous", "contradictory"}
    }
    near_miss_accuracy = {
        category: sum(
            correct[case.case_id]
            for case in episode.evaluation
            if (case.near_miss_category or case.category) == category
        )
        / sum(
            (case.near_miss_category or case.category) == category
            for case in episode.evaluation
        )
        for category in sorted(near_categories)
    }
    committed = [
        case
        for case in episode.evaluation
        if not predictions[case.case_id].abstained
    ]
    abstentions = [
        case
        for case in episode.evaluation
        if predictions[case.case_id].abstained
    ]
    invariant, irrelevant, counterfactual, fidelity = _explanation_dimensions(
        episode,
        run,
    )
    return EpisodeScore(
        positive_accuracy=sum(correct[case.case_id] for case in positives)
        / len(positives),
        negative_rejection_accuracy=(
            sum(correct[case.case_id] for case in negatives) / len(negatives)
            if negatives
            else 0.0
        ),
        near_miss_accuracy_by_category=near_miss_accuracy,
        novel_vocabulary_accuracy=(
            sum(
                correct[case.case_id]
                for case in episode.evaluation
                if case.novel_vocabulary
            )
            / sum(case.novel_vocabulary for case in episode.evaluation)
        ),
        surface_invariance=_flagged_accuracy(
            episode,
            run,
            "surface_invariance",
        ),
        compositional_generalization=_flagged_accuracy(
            episode,
            run,
            "compositional_generalization",
        ),
        coverage=len(committed) / len(episode.evaluation),
        selective_risk=(
            1.0 - sum(correct[case.case_id] for case in committed) / len(committed)
            if committed
            else None
        ),
        false_commitment_rate=(
            sum(not correct[case.case_id] for case in committed)
            / len(episode.evaluation)
        ),
        abstention_precision=(
            sum(correct[case.case_id] for case in abstentions) / len(abstentions)
            if abstentions
            else None
        ),
        explanation_invariant_correctness=invariant,
        explanation_irrelevance_recognition=irrelevant,
        explanation_counterfactual_sensitivity=counterfactual,
        explanation_trace_fidelity=fidelity,
        case_count=len(episode.evaluation),
    )


def episode_score_to_json(score: EpisodeScore) -> str:
    """Serialize one score deterministically."""
    return json.dumps(asdict(score), sort_keys=True)


def _mean(values: list[float]) -> float | None:
    return None if not values else sum(values) / len(values)


def _percentile(sorted_values: list[float], probability: float) -> float:
    position = (len(sorted_values) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    fraction = position - lower
    return (
        sorted_values[lower]
        + (sorted_values[upper] - sorted_values[lower]) * fraction
    )


def _bootstrap_interval(
    values: list[float],
    *,
    resamples: int,
    random_source: random.Random,
) -> dict[str, float] | None:
    if not values:
        return None
    if resamples < 1:
        raise ValueError("bootstrap resamples must be positive")
    bootstrap_means = [
        sum(random_source.choice(values) for _ in values) / len(values)
        for _ in range(resamples)
    ]
    bootstrap_means.sort()
    return {
        "lower": _percentile(bootstrap_means, 0.025),
        "upper": _percentile(bootstrap_means, 0.975),
    }


def aggregate_structural_gate_scores(
    scores: list[EpisodeScore],
    *,
    bootstrap_resamples: int = 10_000,
    seed: int = 1729,
) -> AggregateScore:
    """Aggregate episode scores with deterministic percentile bootstrap CIs."""
    if not scores:
        raise ValueError("at least one episode score is required")
    if bootstrap_resamples < 1:
        raise ValueError("bootstrap resamples must be positive")

    scalar_names = (
        "positive_accuracy",
        "negative_rejection_accuracy",
        "novel_vocabulary_accuracy",
        "surface_invariance",
        "compositional_generalization",
        "coverage",
        "selective_risk",
        "false_commitment_rate",
        "abstention_precision",
        "explanation_invariant_correctness",
        "explanation_irrelevance_recognition",
        "explanation_counterfactual_sensitivity",
        "explanation_trace_fidelity",
    )
    metrics: dict[str, float | dict[str, float]] = {}
    confidence_intervals: dict[str, dict[str, float]] = {}
    random_source = random.Random(seed)

    for name in scalar_names:
        values = [
            value
            for score in scores
            if (value := getattr(score, name)) is not None
        ]
        mean = _mean(values)
        interval = _bootstrap_interval(
            values,
            resamples=bootstrap_resamples,
            random_source=random_source,
        )
        if mean is not None:
            metrics[name] = mean
        if interval is not None:
            confidence_intervals[name] = interval

    categories = sorted(
        {
            category
            for score in scores
            for category in score.near_miss_accuracy_by_category
        }
    )
    category_metrics: dict[str, float] = {}
    for category in categories:
        values = [
            score.near_miss_accuracy_by_category[category]
            for score in scores
            if category in score.near_miss_accuracy_by_category
        ]
        mean = _mean(values)
        interval = _bootstrap_interval(
            values,
            resamples=bootstrap_resamples,
            random_source=random_source,
        )
        if mean is not None:
            category_metrics[category] = mean
        if interval is not None:
            confidence_intervals[f"near_miss_accuracy.{category}"] = interval
    metrics["near_miss_accuracy_by_category"] = category_metrics

    available_explanation_values = [
        sum(getattr(score, name) for name in (
            "explanation_invariant_correctness",
            "explanation_irrelevance_recognition",
            "explanation_counterfactual_sensitivity",
            "explanation_trace_fidelity",
        )) / 4
        for score in scores
    ]
    explanation_mean = _mean(available_explanation_values)
    explanation_interval = _bootstrap_interval(
        available_explanation_values,
        resamples=bootstrap_resamples,
        random_source=random_source,
    )
    if explanation_mean is not None:
        metrics["explanation_fidelity"] = explanation_mean
    if explanation_interval is not None:
        confidence_intervals["explanation_fidelity"] = explanation_interval

    return AggregateScore(
        episode_count=len(scores),
        metrics=metrics,
        confidence_intervals=confidence_intervals,
    )


def aggregate_score_to_json(score: AggregateScore) -> str:
    """Serialize an aggregate score deterministically."""
    return json.dumps(asdict(score), sort_keys=True)


def aggregate_score_artifact_to_json(
    score: AggregateScore,
    *,
    benchmark_version: str = "structural-gate-v1",
    pass_rule_version: str = "structural-gate-v1",
    critical_leakage_detected: bool = False,
) -> str:
    """Serialize an aggregate score using the versioned score artifact shape."""
    if not benchmark_version or not pass_rule_version:
        raise ValueError("benchmark and pass-rule versions are required")
    artifact = {
        "schema": "protama.structural-gate.score.v1",
        "benchmark_version": benchmark_version,
        "pass_rule_version": pass_rule_version,
        "episode_count": score.episode_count,
        "metrics": score.metrics,
        "confidence_intervals": score.confidence_intervals,
        "leakage": {
            "critical_leakage_detected": critical_leakage_detected,
        },
    }
    return json.dumps(artifact, sort_keys=True)


def excluded_episode_manifest_to_json(
    excluded_episodes: list[ExcludedEpisode],
) -> str:
    """Serialize the excluded-episode manifest deterministically."""
    for excluded in excluded_episodes:
        if not excluded.episode_id or not excluded.reason or not excluded.stage:
            raise ValueError("excluded episodes require id, reason, and stage")
    manifest = {
        "schema": "protama.structural-gate.excluded-episodes.v1",
        "excluded_count": len(excluded_episodes),
        "excluded_episodes": [
            asdict(excluded) for excluded in excluded_episodes
        ],
    }
    return json.dumps(manifest, sort_keys=True)


def aggregate_score_to_report(
    score: AggregateScore,
    *,
    excluded_episodes: list[ExcludedEpisode] | None = None,
    critical_leakage_detected: bool = False,
) -> str:
    """Render a deterministic reviewer-facing report from aggregate results."""
    excluded = excluded_episodes or []
    lines = [
        "Protama Structural Gate Development Report",
        "==========================================",
        f"Episodes scored: {score.episode_count}",
        f"Episodes excluded: {len(excluded)}",
        f"Critical leakage detected: {critical_leakage_detected}",
        "",
        "Metrics",
        "-------",
    ]
    for name in sorted(score.metrics):
        value = score.metrics[name]
        if isinstance(value, dict):
            lines.append(f"{name}:")
            for category in sorted(value):
                lines.append(f"  {category}: {value[category]:.6f}")
        else:
            interval = score.confidence_intervals.get(name)
            if interval is None:
                lines.append(f"{name}: {value:.6f}")
            else:
                lines.append(
                    f"{name}: {value:.6f} "
                    f"(95% CI {interval['lower']:.6f}, "
                    f"{interval['upper']:.6f})"
                )
    lines.extend(["", "Unavailable or not yet evaluated", "------------------------------"])
    unavailable = {
        "surface_invariance",
        "compositional_generalization",
    } - set(score.metrics)
    lines.extend(f"- {name}" for name in sorted(unavailable))
    lines.extend(["", "Excluded episodes", "-----------------"])
    if excluded:
        lines.extend(
            f"- {item.episode_id}: {item.stage} â€” {item.reason}"
            for item in excluded
        )
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"


def evaluate_preregistered_pass_rule(
    score: AggregateScore,
    *,
    critical_leakage_detected: bool = False,
    positive_transfer_min: float | None = None,
    negative_rejection_min: float | None = None,
    near_miss_min: float | None = None,
    near_miss_category_min: float | None = None,
    novel_vocabulary_min: float | None = None,
    explanation_fidelity_min: float | None = None,
    coverage_min: float | None = None,
    selective_risk_max: float | None = None,
) -> dict[str, object]:
    """Apply the development pass rule conservatively and rail closed."""
    pass_rule = DEFAULT_PASS_RULE
    positive_transfer_min = (
        pass_rule["positive_transfer_accuracy_min"]
        if positive_transfer_min is None
        else positive_transfer_min
    )
    negative_rejection_min = (
        pass_rule["negative_rejection_accuracy_min"]
        if negative_rejection_min is None
        else negative_rejection_min
    )
    near_miss_min = (
        pass_rule["near_miss_accuracy_min"]
        if near_miss_min is None
        else near_miss_min
    )
    near_miss_category_min = (
        pass_rule["near_miss_category_accuracy_min"]
        if near_miss_category_min is None
        else near_miss_category_min
    )
    novel_vocabulary_min = (
        pass_rule["novel_vocabulary_accuracy_min"]
        if novel_vocabulary_min is None
        else novel_vocabulary_min
    )
    explanation_fidelity_min = (
        pass_rule["explanation_fidelity_min"]
        if explanation_fidelity_min is None
        else explanation_fidelity_min
    )
    coverage_min = (
        pass_rule["coverage_min"] if coverage_min is None else coverage_min
    )
    selective_risk_max = (
        pass_rule["selective_risk_max"]
        if selective_risk_max is None
        else selective_risk_max
    )
    near_miss = score.metrics.get("near_miss_accuracy_by_category", {})
    category_values = (
        list(near_miss.values()) if isinstance(near_miss, dict) else []
    )
    near_miss_mean = _mean(category_values)
    explanation_fidelity = score.metrics.get("explanation_fidelity")
    criteria: dict[str, bool] = {
        "positive_transfer_accuracy": (
            score.metrics.get("positive_accuracy") is not None
            and score.metrics["positive_accuracy"] >= positive_transfer_min
        ),
        "negative_rejection_accuracy": (
            score.metrics.get("negative_rejection_accuracy") is not None
            and score.metrics["negative_rejection_accuracy"] >= negative_rejection_min
        ),
        "near_miss_accuracy": (
            near_miss_mean is not None and near_miss_mean >= near_miss_min
        ),
        "near_miss_category_accuracy": bool(category_values) and all(
            value >= near_miss_category_min for value in category_values
        ),
        "novel_vocabulary_accuracy": (
            score.metrics.get("novel_vocabulary_accuracy") is not None
            and score.metrics["novel_vocabulary_accuracy"] >= novel_vocabulary_min
        ),
        "explanation_fidelity": (
            explanation_fidelity is not None
            and explanation_fidelity >= explanation_fidelity_min
        ),
        "coverage": (
            score.metrics.get("coverage") is not None
            and score.metrics["coverage"] >= coverage_min
        ),
        "selective_risk": (
            score.metrics.get("selective_risk") is not None
            and score.metrics["selective_risk"] <= selective_risk_max
        ),
        "critical_leakage": not critical_leakage_detected,
    }
    unavailable = sorted(
        name
        for name, value in (
            ("positive_transfer_accuracy", score.metrics.get("positive_accuracy")),
            ("negative_rejection_accuracy", score.metrics.get("negative_rejection_accuracy")),
            ("near_miss_accuracy", near_miss_mean),
            ("near_miss_category_accuracy", category_values or None),
            ("novel_vocabulary_accuracy", score.metrics.get("novel_vocabulary_accuracy")),
            ("explanation_fidelity", explanation_fidelity),
            ("coverage", score.metrics.get("coverage")),
            ("selective_risk", score.metrics.get("selective_risk")),
        )
        if value is None
    )
    return {
        "status": "PASS" if all(criteria.values()) else "NOT PASSED",
        "criteria": criteria,
        "unavailable_metrics": unavailable,
        "critical_leakage_detected": critical_leakage_detected,
    }


def pass_rule_to_json(result: dict[str, object]) -> str:
    """Serialize a pass-rule result deterministically."""
    return json.dumps(result, sort_keys=True)


def score_baseline_run(episode: GateEpisode, run: object) -> BaselineScore:
    """Score a baseline run with the same evaluator-side labels."""
    predictions = {prediction.case_id: prediction for prediction in run.predictions}
    cases = episode.evaluation
    if set(predictions) != {case.case_id for case in cases}:
        raise ValueError("baseline predictions do not cover episode evaluation")
    correct = {
        case.case_id: predictions[case.case_id].predicted_status == case.expected_status
        for case in cases
    }
    near_miss_cases = [case for case in cases if case.near_miss_category]
    novel_cases = [case for case in cases if case.novel_vocabulary]
    metrics = {
        "overall_accuracy": sum(correct.values()) / len(cases),
        "positive_accuracy": _mean([
            float(correct[case.case_id])
            for case in cases
            if case.category in {"positive", "compositional"}
        ]) or 0.0,
        "negative_rejection_accuracy": _mean([
            float(correct[case.case_id])
            for case in cases
            if case.category in {"negative", "near_miss"}
        ]) or 0.0,
        "near_miss_accuracy": _mean([
            float(correct[case.case_id]) for case in near_miss_cases
        ]) or 0.0,
        "novel_vocabulary_accuracy": _mean([
            float(correct[case.case_id]) for case in novel_cases
        ]) or 0.0,
    }
    return BaselineScore(
        baseline_name=run.baseline_name,
        metrics=metrics,
    )


def baseline_comparison_matrix(
    episode: GateEpisode,
    runs: tuple[object, ...],
) -> tuple[BaselineScore, ...]:
    """Score and deterministically order a set or baseline controls."""
    scores = [score_baseline_run(episode, run) for run in runs]
    return tuple(sorted(scores, key=lambda score: score.baseline_name))


def baseline_comparison_matrix_to_json(
    scores: tuple[BaselineScore, ...],
) -> str:
    """Serialize a baseline matrix deterministically."""
    return json.dumps(
        [asdict(score) for score in scores],
        sort_keys=True,
    )


def risk_coverage_curve(
    episode: GateEpisode,
    run: GateAdapterRun,
    *,
    confidence_thresholds: tuple[float, ...] = (
        0.0,
        0.25,
        0.5,
        0.75,
        1.0,
    ),
) -> tuple[dict[str, float], ...]:
    """Return deterministic coverage/risk points at confidence thresholds."""
    if any(
        threshold < 0.0 or threshold > 1.0
        for threshold in confidence_thresholds
    ):
        raise ValueError("confidence thresholds must be between zero and one")
    predictions = {prediction.case_id: prediction for prediction in run.predictions}
    points = []
    for threshold in confidence_thresholds:
        committed = [
            case
            for case in episode.evaluation
            if not predictions[case.case_id].abstained
            and predictions[case.case_id].confidence >= threshold
        ]
        incorrect = sum(
            predictions[case.case_id].predicted_status != case.expected_status
            for case in committed
        )
        points.append(
            {
                "confidence_threshold": threshold,
                "coverage": len(committed) / len(episode.evaluation),
                "risk": (
                    incorrect / len(committed)
                    if committed
                    else 0.0
                ),
            }
        )
    return tuple(points)

























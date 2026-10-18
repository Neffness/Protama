"""Deterministic hidden-family episode generation for the structural gate."""

from __future__ import annotations

import json
import random
from dataclasses import asdict, dataclass, replace
from typing import Iterable

from .models import RelationObservation


NEAR_MISS_CATEGORIES = (
    "role_reversal",
    "relation_reversal",
    "type_violation",
    "argument_omission",
    "single_feature_mismatch",
    "surface_decoy",
    "lexical_overlap",
    "novel_negative",
    "ambiguous",
    "contradictory",
)


@dataclass(frozen=True)
class GateCase:
    case_id: str
    split: str
    category: str
    observations: tuple[RelationObservation, ...]
    expected_status: str
    template: str
    near_miss_category: str | None = None
    novel_vocabulary: bool = False
    surface_invariance: bool = False
    compositional_generalization: bool = False


@dataclass(frozen=True)
class GateEpisode:
    episode_id: str
    seed: int
    family_gold: tuple[tuple[str, str, str], ...]
    training: tuple[GateCase, ...]
    evaluation: tuple[GateCase, ...]
    family_variant: str = "canonical"


@dataclass(frozen=True)
class LeakageCheck:
    name: str
    passed: bool
    details: str


def _observation(
    relation_type: str,
    source: str,
    target: str,
) -> RelationObservation:
    return RelationObservation(relation_type, source, target)


def _positive_case(
    case_id: str,
    source: str,
    action: str,
    role: str,
    *,
    template: str,
    novel_vocabulary: bool,
) -> GateCase:
    return GateCase(
        case_id=case_id,
        split="held_out",
        category="positive",
        observations=(
            _observation("is-a", source, "person"),
            _observation("performs-action", source, action),
            _observation("has-role", source, role),
        ),
        expected_status="accepted",
        template=template,
        novel_vocabulary=novel_vocabulary,
        surface_invariance=True,
    )


def generate_structural_gate_episode(seed: int) -> GateEpisode:
    """Generate one deterministic episode from a hidden relational family."""
    if seed < 0:
        raise ValueError("episode seed must be non-negative")
    random_source = random.Random(seed)
    train_sources = [f"train-person-{seed}-{index}" for index in range(3)]
    train_actions = random_source.sample(
        ["repairs", "maps", "studies", "charts", "designs"],
        3,
    )
    train_roles = [
        f"train-role-{seed}-{index}"
        for index in range(3)
    ]
    training = tuple(
        GateCase(
            case_id=f"train-{index}",
            split="train",
            category="positive",
            observations=(
                _observation("is-a", source, "person"),
                _observation("performs-action", source, action),
                _observation("has-role", source, role),
            ),
            expected_status="accepted",
            template="canonical",
        )
        for index, (source, action, role) in enumerate(
            zip(train_sources, train_actions, train_roles)
        )
    )
    eval_source = f"eval-person-{seed}"
    eval_action = f"eval-action-{seed}"
    eval_role = f"eval-role-{seed}"
    positive = _positive_case(
        "positive-0001",
        eval_source,
        eval_action,
        eval_role,
        template="reordered",
        novel_vocabulary=True,
    )
    evaluation = [
        positive,
        GateCase(
            case_id="compositional-0001",
            split="held_out",
            category="compositional",
            observations=(
                _observation("is-a", f"composition-person-{seed}", "person"),
                _observation(
                    "performs-action",
                    f"composition-person-{seed}",
                    f"composition-action-{seed}",
                ),
                _observation(
                    "has-role",
                    f"composition-person-{seed}",
                    f"composition-role-{seed}",
                ),
            ),
            expected_status="accepted",
            template="composed",
            novel_vocabulary=True,
            compositional_generalization=True,
        ),
        GateCase(
            case_id="near-miss-role-reversal",
            split="held_out",
            category="near_miss",
            near_miss_category="role_reversal",
            observations=(
                _observation("is-a", f"eval-object-{seed}", "person"),
                _observation(
                    "performs-action",
                    f"eval-object-{seed}",
                    eval_action,
                ),
                _observation("has-role", "person", eval_role),
            ),
            expected_status="rejected",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="near-miss-relation-reversal",
            split="held_out",
            category="near_miss",
            near_miss_category="relation_reversal",
            observations=(
                _observation("is-a", eval_source, "person"),
                _observation("action-performs", eval_source, eval_action),
                _observation("has-role", eval_source, eval_role),
            ),
            expected_status="rejected",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="near-miss-type-violation",
            split="held_out",
            category="near_miss",
            near_miss_category="type_violation",
            observations=(
                _observation("is-a", eval_source, "object"),
                _observation("performs-action", eval_source, eval_action),
                _observation("has-role", eval_source, eval_role),
            ),
            expected_status="rejected",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="near-miss-argument-omission",
            split="held_out",
            category="near_miss",
            near_miss_category="argument_omission",
            observations=(
                _observation("is-a", eval_source, "person"),
                _observation("performs-action", eval_source, eval_action),
            ),
            expected_status="rejected",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="near-miss-single-feature",
            split="held_out",
            category="near_miss",
            near_miss_category="single_feature_mismatch",
            observations=(
                _observation("is-a", eval_source, "person"),
                _observation("performs-action", eval_source, eval_action),
                _observation("has-role", eval_source, "object"),
            ),
            expected_status="rejected",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="near-miss-surface-decoy",
            split="held_out",
            category="near_miss",
            near_miss_category="surface_decoy",
            observations=positive.observations,
            expected_status="rejected",
            template="decoy",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="near-miss-lexical-overlap",
            split="held_out",
            category="near_miss",
            near_miss_category="lexical_overlap",
            observations=(
                _observation("is-a", train_sources[0], "person"),
                _observation("performs-action", train_sources[0], train_actions[0]),
                _observation("has-role", "person", train_roles[0]),
            ),
            expected_status="rejected",
            template="reordered",
        ),
        GateCase(
            case_id="near-miss-novel-negative",
            split="held_out",
            category="near_miss",
            near_miss_category="novel_negative",
            observations=(
                _observation("is-a", f"negative-{seed}", "object"),
                _observation("performs-action", f"negative-{seed}", f"action-{seed}"),
                _observation("has-role", f"negative-{seed}", f"role-{seed}"),
            ),
            expected_status="rejected",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="ambiguous-0001",
            split="held_out",
            category="ambiguous",
            observations=(),
            expected_status="abstained",
            template="reordered",
            novel_vocabulary=True,
        ),
        GateCase(
            case_id="contradictory-0001",
            split="held_out",
            category="contradictory",
            observations=(
                _observation("is-a", eval_source, "person"),
                _observation("is-a", eval_source, "object"),
                _observation("performs-action", eval_source, eval_action),
            ),
            expected_status="abstained",
            template="reordered",
            novel_vocabulary=True,
        ),
    ]
    evaluation = [
        _add_canonical_type_observations(case)
        for case in evaluation
    ]
    training = tuple(
        _add_canonical_type_observations(case)
        for case in training
    )
    episode = GateEpisode(
        episode_id=f"episode-{seed:08d}",
        seed=seed,
        family_gold=(
            ("is-a", "$source", "person"),
            ("performs-action", "$source", "$action"),
            ("has-role", "$source", "$role"),
            ("is-action", "$action", "action"),
            ("is-role", "$role", "role"),
        ),
        training=training,
        evaluation=tuple(evaluation),
    )
    return _apply_family_variant(episode, seed % 3)


def _add_canonical_type_observations(case: GateCase) -> GateCase:
    """Expose action and role types as learnable structured evidence."""
    observations = list(case.observations)
    for observation in case.observations:
        if observation.relation_type == "performs-action":
            observations.append(
                _observation(
                    "is-action",
                    observation.target,
                    (
                        "object"
                        if "object" in observation.target
                        else "action"
                    ),
                )
            )
        elif observation.relation_type == "has-role":
            observations.append(
                _observation(
                    "is-role",
                    observation.target,
                    "object" if "object" in observation.target else "role",
                )
            )
    if case.near_miss_category == "surface_decoy" and case.observations:
        first = case.observations[0]
        observations.append(
            _observation("surface-decoy", first.source, first.target)
        )
    return GateCase(
        case_id=case.case_id,
        split=case.split,
        category=case.category,
        observations=tuple(observations),
        expected_status=case.expected_status,
        template=case.template,
        near_miss_category=case.near_miss_category,
        novel_vocabulary=case.novel_vocabulary,
        surface_invariance=case.surface_invariance,
        compositional_generalization=case.compositional_generalization,
    )

_FAMILY_VARIANTS = (
    {
        "name": "canonical",
        "relations": {},
    },
    {
        "name": "membership-operation-function",
        "relations": {
            "is-a": "is-member-of",
            "performs-action": "supports-operation",
            "has-role": "has-function",
            "action-performs": "operation-performed-by",
        },
    },
    {
        "name": "kind-execution-occupation",
        "relations": {
            "is-a": "is-kind-of",
            "performs-action": "executes",
            "has-role": "occupies",
            "action-performs": "executed-by",
        },
    },
)


def _apply_family_variant(episode: GateEpisode, variant_index: int) -> GateEpisode:
    """Remap relation names consistently while retaining episode structure."""
    variant = _FAMILY_VARIANTS[variant_index]
    relation_map = variant["relations"]

    def remap_case(case: GateCase) -> GateCase:
        return replace(
            case,
            observations=tuple(
                replace(
                    observation,
                    relation_type=relation_map.get(
                        observation.relation_type,
                        observation.relation_type,
                    ),
                )
                for observation in case.observations
            ),
        )

    return replace(
        episode,
        family_gold=tuple(
            (
                relation_map.get(relation_type, relation_type),
                source,
                target,
            )
            for relation_type, source, target in episode.family_gold
        ),
        training=tuple(remap_case(case) for case in episode.training),
        evaluation=tuple(remap_case(case) for case in episode.evaluation),
        family_variant=str(variant["name"]),
    )


def generate_structural_gate_episodes(
    seeds: Iterable[int],
) -> tuple[GateEpisode, ...]:
    """Generate episodes in caller-provided deterministic seed order."""
    return tuple(generate_structural_gate_episode(seed) for seed in seeds)


def episode_to_json(episode: GateEpisode) -> str:
    """Serialize an episode deterministically for replay checks."""
    return json.dumps(asdict(episode), default=_json_default, sort_keys=True)


def _json_default(value: object) -> object:
    if isinstance(value, RelationObservation):
        return {
            "relation_type": value.relation_type,
            "source": value.source,
            "target": value.target,
        }
    raise TypeError(f"unsupported episode value: {type(value).__name__}")


def check_episode_leakage(episode: GateEpisode) -> tuple[LeakageCheck, ...]:
    """Run rail-closed lexical, family, and split checks."""
    type_literals = {
        "person",
        "word",
        "alias",
        "object",
        "tool",
        "form",
        "purpose",
        "action",
        "role",
    }
    training_values = {
        value
        for case in episode.training
        for observation in case.observations
        for value in (observation.source, observation.target)
        if value not in type_literals
    }
    evaluation_values = {
        value
        for case in episode.evaluation
        if case.novel_vocabulary
        for observation in case.observations
        for value in (observation.source, observation.target)
        if value not in type_literals
    }
    lexical_overlap = training_values & evaluation_values
    training_signatures = {
        tuple(
            (observation.relation_type, observation.source, observation.target)
            for observation in case.observations
        )
        for case in episode.training
    }
    novel_evaluation_signatures = {
        tuple(
            (observation.relation_type, observation.source, observation.target)
            for observation in case.observations
        )
        for case in episode.evaluation
        if case.novel_vocabulary
    }
    structural_overlap = training_signatures & novel_evaluation_signatures
    family_leak = any(
        episode.family_gold[0][0] in observation.relation_type
        and observation.source == "$source"
        for case in episode.training
        for observation in case.observations
    )
    return (
        LeakageCheck(
            name="novel_vocabulary_is_disjoint",
            passed=not lexical_overlap,
            details=(
                "no varying evaluation values overlap training"
                if not lexical_overlap
                else f"overlap={sorted(lexical_overlap)}"
            ),
        ),
        LeakageCheck(
            name="family_gold_not_in_training_inputs",
            passed=not family_leak,
            details="gold variable bindings are evaluator-only",
        ),
        LeakageCheck(
            name="evaluation_cases_are_held_out",
            passed=all(case.split == "held_out" for case in episode.evaluation),
            details="all evaluation cases use the held_out split",
        ),
        LeakageCheck(
            name="novel_structures_are_disjoint",
            passed=not structural_overlap,
            details=(
                "no novel-vocabulary structural signature overlaps training"
                if not structural_overlap
                else f"overlap_count={len(structural_overlap)}"
            ),
        ),
        LeakageCheck(
            name="novel_templates_are_declared",
            passed=all(
                case.template != "canonical"
                for case in episode.evaluation
                if case.novel_vocabulary
            ),
            details="novel-vocabulary evaluation cases use non-training templates",
        ),
    )


def leakage_report(episode: GateEpisode) -> dict[str, object]:
    """Return the versioned machine-readable leakage report for an episode."""
    checks = check_episode_leakage(episode)
    return {
        "schema": "protama.structural-gate.leakage-report.v1",
        "episode_id": episode.episode_id,
        "checks": [
            {
                "name": check.name,
                "passed": check.passed,
                "details": check.details,
            }
            for check in checks
        ],
        "critical_leakage_detected": not all(check.passed for check in checks),
    }


def leakage_report_to_json(episode: GateEpisode) -> str:
    """Serialize a leakage report deterministically."""
    return json.dumps(leakage_report(episode), sort_keys=True)














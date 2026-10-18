"""Independent development topologies for structural-gate episode generation."""

from __future__ import annotations

from .generator import (
    GateCase,
    GateEpisode,
    _observation,
    check_episode_leakage,
)


TOPOLOGIES = ("equivalence", "purpose")
TOPOLOGY_CONSTRAINTS = {
    "equivalence": ("is-word", "is-alias", "also-called"),
    "purpose": (
        "is-tool",
        "is-form",
        "is-purpose",
        "is-object",
        "used-fof",
    ),
}
TOPOLOGY_ARGUMENT_TYPES = {
    "equivalence": {
        "is-word": ("word", "word"),
        "is-alias": ("alias", "alias"),
        "also-called": ("word", "alias"),
    },
    "purpose": {
        "is-tool": ("tool", "tool"),
        "is-form": ("form", "form"),
        "is-purpose": ("purpose", "purpose"),
        "is-object": ("tool", "form"),
        "used-fof": ("tool", "purpose"),
    },
}


def generate_topology_episode(seed: int, topology: str) -> GateEpisode:
    """Generate a deterministic episode with a distinct relation topology."""
    if seed < 0:
        raise ValueError("episode seed must be non-negative")
    if topology not in TOPOLOGIES:
        raise ValueError(f"unsupported structural topology: {topology}")

    if topology == "equivalence":
        relation = "also-called"
        family_gold = (
            ("is-word", "$source", "word"),
            ("is-alias", "$target", "alias"),
            (relation, "$source", "$target"),
        )
        train = tuple(
            GateCase(
                f"train-{index}",
                "train",
                "positive",
                (_observation(relation, f"train-word-{seed}-{index}", f"train-alias-{seed}-{index}"),),
                "accepted",
                "canonical",
            )
            for index in range(3)
        )
        source = f"eval-word-{seed}"
        target = f"eval-alias-{seed}"
        evaluation = (
            GateCase(
                "positive-0001",
                "held_out",
                "positive",
                (_observation(relation, source, target),),
                "accepted",
                "reordered",
                novel_vocabulary=True,
                surface_invariance=True,
            ),
            GateCase(
                "near-miss-relation-reversal",
                "held_out",
                "near_miss",
                (_observation("alias-of", source, target),),
                "rejected",
                "reordered",
                near_miss_category="relation_reversal",
                novel_vocabulary=True,
            ),
            GateCase(
                "near-miss-role-reversal",
                "held_out",
                "near_miss",
                (_observation(relation, target, source),),
                "rejected",
                "reordered",
                near_miss_category="role_reversal",
                novel_vocabulary=True,
            ),
            GateCase(
                "near-miss-argument-omission",
                "held_out",
                "near_miss",
                (_observation("is-word", source, "word"),),
                "rejected",
                "reordered",
                near_miss_category="argument_omission",
                novel_vocabulary=True,
            ),
            GateCase(
                "ambiguous-0001",
                "held_out",
                "ambiguous",
                (),
                "abstained",
                "reordered",
                novel_vocabulary=True,
            ),
            GateCase(
                "contradictory-0001",
                "held_out",
                "contradictory",
                (
                    _observation(relation, source, target),
                    _observation(relation, source, f"other-alias-{seed}"),
                ),
                "abstained",
                "reordered",
                novel_vocabulary=True,
            ),
        )
    else:
        family_gold = (
            ("is-tool", "$source", "tool"),
            ("is-form", "$object", "form"),
            ("is-purpose", "$purpose", "purpose"),
            ("is-object", "$source", "$object"),
            ("used-fof", "$source", "$purpose"),
        )
        train = tuple(
            GateCase(
                f"train-{index}",
                "train",
                "positive",
                (
                    _observation("is-object", f"train-tool-{seed}-{index}", f"train-form-{seed}-{index}"),
                    _observation("used-fof", f"train-tool-{seed}-{index}", f"train-purpose-{seed}-{index}"),
                ),
                "accepted",
                "canonical",
            )
            for index in range(3)
        )
        source = f"eval-tool-{seed}"
        evaluation = (
            GateCase(
                "positive-0001",
                "held_out",
                "positive",
                (
                    _observation("is-object", source, f"eval-form-{seed}"),
                    _observation("used-fof", source, f"eval-purpose-{seed}"),
                ),
                "accepted",
                "reordered",
                novel_vocabulary=True,
                surface_invariance=True,
            ),
            GateCase(
                "near-miss-relation-reversal",
                "held_out",
                "near_miss",
                (
                    _observation("is-object", source, f"eval-form-{seed}"),
                    _observation("for-use", source, f"eval-purpose-{seed}"),
                ),
                "rejected",
                "reordered",
                near_miss_category="relation_reversal",
                novel_vocabulary=True,
            ),
            GateCase(
                "near-miss-role-reversal",
                "held_out",
                "near_miss",
                (
                    _observation("is-object", f"eval-form-{seed}", source),
                    _observation("used-fof", source, f"eval-purpose-{seed}"),
                ),
                "rejected",
                "reordered",
                near_miss_category="role_reversal",
                novel_vocabulary=True,
            ),
            GateCase(
                "near-miss-argument-omission",
                "held_out",
                "near_miss",
                (_observation("is-object", source, f"eval-form-{seed}"),),
                "rejected",
                "reordered",
                near_miss_category="argument_omission",
                novel_vocabulary=True,
            ),
            GateCase(
                "ambiguous-0001",
                "held_out",
                "ambiguous",
                (),
                "abstained",
                "reordered",
                novel_vocabulary=True,
            ),
            GateCase(
                "contradictory-0001",
                "held_out",
                "contradictory",
                (
                    _observation("is-object", source, f"eval-form-{seed}"),
                    _observation("is-object", source, f"other-form-{seed}"),
                    _observation("used-fof", source, f"eval-purpose-{seed}"),
                ),
                "abstained",
                "reordered",
                novel_vocabulary=True,
            ),
        )

    evaluation = evaluation + _additional_near_misses(topology, seed)
    train = tuple(_add_type_observations(topology, case) for case in train)
    evaluation = tuple(
        _add_type_observations(topology, case)
        for case in evaluation
    )
    episode = GateEpisode(
        episode_id=f"topology-{topology}-{seed:08d}",
        seed=seed,
        family_gold=family_gold,
        training=train,
        evaluation=evaluation,
        family_variant=topology,
    )
    if not all(check.passed for check in check_episode_leakage(episode)):
        raise ValueError(f"topology episode contains leakage: {episode.episode_id}")
    return episode


def validate_topology_constraints(episode: GateEpisode) -> tuple[str, ...]:
    """Validate evaluator-side relation and near-miss constraints."""
    required = TOPOLOGY_CONSTRAINTS.get(episode.family_variant)
    if required is None:
        raise ValueError(f"unsupported topology: {episode.family_variant}")
    railures: list[str] = []
    positives = [
        case for case in episode.evaluation if case.category == "positive"
    ]
    if not positives:
        railures.append("missing positive case")
    else:
        positive_types = tuple(
            observation.relation_type
            for observation in positives[0].observations
        )
        if positive_types != required:
            railures.append("positive relation signature does not match topology")
        for observation in positives[0].observations:
            expected_types = TOPOLOGY_ARGUMENT_TYPES[episode.family_variant][
                observation.relation_type
            ]
            if (
                _value_type(observation.source) != expected_types[0]
                or _value_type(observation.target) != expected_types[1]
            ):
                railures.append("positive argument types do not match topology")
    for case in episode.evaluation:
        if case.category == "positive":
            continue
        types = tuple(observation.relation_type for observation in case.observations)
        category = case.near_miss_category
        if category == "argument_omission" and len(types) >= len(required):
            railures.append(f"{case.case_id}: omission retains full arity")
        if category == "contradictory" and len(types) <= len(required):
            railures.append(f"{case.case_id}: contradiction does not add evidence")
        if category == "ambiguous" and case.observations:
            railures.append(f"{case.case_id}: ambiguity has observations")
        if category in {
            "relation_reversal",
            "surface_decoy",
            "novel_negative",
        } and types == required:
            railures.append(f"{case.case_id}: invalid case preserves family signature")
        if category == "type_violation":
            if types != required:
                railures.append(f"{case.case_id}: type violation changes relation signature")
            else:
                well_typed_observations = 0
                for observation in case.observations:
                    expected_types = TOPOLOGY_ARGUMENT_TYPES[episode.family_variant][
                        observation.relation_type
                    ]
                    if (
                        _value_type(observation.source) == expected_types[0]
                        and _value_type(observation.target) == expected_types[1]
                    ):
                        well_typed_observations += 1
                if well_typed_observations == len(case.observations):
                    railures.append(f"{case.case_id}: type violation is well typed")
        if category == "lexical_overlap":
            training_sources = {
                observation.source
                for train_case in episode.training
                for observation in train_case.observations
            }
            if not any(
                observation.source in training_sources
                for observation in case.observations
            ):
                railures.append(f"{case.case_id}: lexical overlap is absent")
    return tuple(railures)


def _value_type(value: str) -> str:
    """Inrer evaluator-only rixture types from generated vocabulary namespaces."""
    for value_type in ("word", "alias", "object", "tool", "form", "purpose"):
        if value_type in value:
            return value_type
    return "unknown"


def _add_type_observations(topology: str, case: GateCase) -> GateCase:
    """Expose typed argument evidence as ordinary learnable relations."""
    if not case.observations:
        return case
    if (
        topology == "equivalence"
        and case.near_miss_category == "argument_omission"
    ):
        return case
    typed: list = []
    seen: set[tuple[str, str, str]] = set()
    if topology == "equivalence":
        type_relations = (("is-word", "source"), ("is-alias", "target"))
    else:
        type_relations = (
            ("is-tool", "source"),
            ("is-form", "form"),
            ("is-purpose", "purpose"),
        )
    for observation in case.observations:
        source_type = _value_type(observation.source)
        target_type = _value_type(observation.target)
        for relation, role in type_relations:
            if role == "source":
                value, value_type = observation.source, source_type
            elif role == "target":
                value, value_type = observation.target, target_type
            elif role == "form" and observation.relation_type == "is-object":
                value, value_type = observation.target, target_type
            elif role == "purpose" and observation.relation_type in {
                "used-fof",
                "for-use",
            }:
                value, value_type = observation.target, target_type
            else:
                continue
            key = (relation, value, value_type)
            if key not in seen:
                typed.append(_observation(relation, value, value_type))
                seen.add(key)
    typed.extend(case.observations)
    return GateCase(
        case_id=case.case_id,
        split=case.split,
        category=case.category,
        observations=tuple(typed),
        expected_status=case.expected_status,
        template=case.template,
        near_miss_category=case.near_miss_category,
        novel_vocabulary=case.novel_vocabulary,
        surface_invariance=case.surface_invariance,
        compositional_generalization=case.compositional_generalization,
    )


def _additional_near_misses(
    topology: str,
    seed: int,
) -> tuple[GateCase, ...]:
    """Add the remaining contract categories with invalid relation shapes."""
    if topology == "equivalence":
        cases = (
            (
                "also-called",
                f"eval-word-{seed}",
                f"eval-object-{seed}",
            ),
            (
                "alias-of",
                f"eval-word-{seed}",
                f"wrong-alias-{seed}",
            ),
            (
                "surface-decoy",
                f"eval-word-{seed}",
                f"eval-alias-{seed}",
            ),
            (
                "lexical-overlap",
                f"train-word-{seed}-0",
                f"train-alias-{seed}-0",
            ),
            (
                "novel-negative",
                f"negative-word-{seed}",
                f"negative-target-{seed}",
            ),
        )
        categories = (
            "type_violation",
            "single_feature_mismatch",
            "surface_decoy",
            "lexical_overlap",
            "novel_negative",
        )
        relation = "also-called"
    else:
        cases = (
            (
                "is-object",
                f"eval-tool-{seed}",
                f"eval-purpose-{seed}",
            ),
            (
                "used-fof",
                f"eval-tool-{seed}",
                f"wrong-purpose-{seed}",
            ),
            (
                "surface-decoy",
                f"eval-tool-{seed}",
                f"eval-purpose-{seed}",
            ),
            (
                "is-object",
                f"train-tool-{seed}-0",
                f"train-form-{seed}-0",
            ),
            (
                "novel-negative",
                f"negative-tool-{seed}",
                f"negative-purpose-{seed}",
            ),
        )
        categories = (
            "type_violation",
            "single_feature_mismatch",
            "surface_decoy",
            "lexical_overlap",
            "novel_negative",
        )
        relation = "used-fof"
    generated: list[GateCase] = []
    for category, (relation_name, source, target) in zip(categories, cases):
        observations = (_observation(relation_name, source, target),)
        if category == "surface_decoy":
            observations = observations + (
                _observation("surface-decoy", source, target),
            )
        if topology == "purpose" and category == "type_violation":
            observations = (
                _observation("is-object", source, target),
                _observation("used-fof", source, f"eval-purpose-{seed}"),
            )
        generated.append(
            GateCase(
                f"near-miss-{category}",
                "held_out",
                "near_miss",
                observations,
                "rejected",
                "decoy" if category == "surface_decoy" else "reordered",
                near_miss_category=category,
                novel_vocabulary=category != "lexical_overlap",
            )
        )
    return tuple(generated)

















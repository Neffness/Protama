"""Public Structural Induction and Transfer Gate harness."""

from .generator import (
    GateCase,
    GateEpisode,
    check_episode_leakage,
    generate_structural_gate_episode,
    generate_structural_gate_episodes,
)
from .models import GateAdapterRun, GatePrediction, GateTrace, RelationObservation
from .manifest import (
    build_locked_final_manifest,
    episode_fingerprint,
    locked_final_manifest_to_json,
)
from .scorer import (
    aggregate_structural_gate_scores,
    evaluate_preregistered_pass_rule,
    score_structural_gate_episode,
)

__all__ = [
    "GateAdapterRun",
    "GateCase",
    "GateEpisode",
    "GatePrediction",
    "GateTrace",
    "RelationObservation",
    "aggregate_structural_gate_scores",
    "build_locked_final_manifest",
    "check_episode_leakage",
    "episode_fingerprint",
    "evaluate_preregistered_pass_rule",
    "generate_structural_gate_episode",
    "generate_structural_gate_episodes",
    "locked_final_manifest_to_json",
    "score_structural_gate_episode",
]

"""Public Structural Induction and Transfer Gate harness."""

from .generator import (
    GateCase,
    GateEpisode,
    check_episode_leakage,
    generate_structural_gate_episode,
    generate_structural_gate_episodes,
)
from .models import GateAdapterRun, GatePrediction, GateTrace, RelationObservation
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
    "check_episode_leakage",
    "evaluate_preregistered_pass_rule",
    "generate_structural_gate_episode",
    "generate_structural_gate_episodes",
    "score_structural_gate_episode",
]

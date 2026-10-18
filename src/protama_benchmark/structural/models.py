"""Public data contracts used by the structural benchmark scorer."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RelationObservation:
    """One typed relation presented to the benchmarked adapter."""

    relation_type: str
    source: str
    target: str
    modifiers: tuple[str, ...] = ()
    polarity: str = "asserted"
    certainty: str = "certain"
    weight: float = 1.0


@dataclass(frozen=True)
class GatePrediction:
    """One adapter decision for an evaluation case."""

    case_id: str
    predicted_status: str
    abstained: bool


@dataclass(frozen=True)
class GateTrace:
    """Evidence trace fields required by the public explanation scorer."""

    case_id: str
    selected_evidence: tuple[dict[str, object], ...]
    rejected_evidence: tuple[dict[str, object], ...]
    explanation: dict[str, object]


@dataclass(frozen=True)
class GateAdapterRun:
    """Adapter output for one generated episode."""

    predictions: tuple[GatePrediction, ...]
    traces: tuple[GateTrace, ...]

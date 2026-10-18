"""Public manifest and fingerprint construction for locked episodes."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from typing import Iterable

from .generator import (
    GateEpisode,
    episode_to_json,
    generate_structural_gate_episodes,
    leakage_report,
)
from .topologies import TOPOLOGIES, generate_topology_episode


FINAL_VERSION = "structural-gate-final-manifest-v1"
FINAL_EPISODES = 100


@dataclass(frozen=True)
class LockedFinalManifest:
    """The public identity and leakage record for a locked episode boundary."""

    version: str
    generator_seeds: tuple[int, ...]
    topology_seeds: tuple[tuple[str, int], ...]
    episode_ids: tuple[str, ...]
    episode_fingerprints: tuple[str, ...]
    leakage_reports: tuple[dict[str, object], ...]
    content_fingerprint: str


def episode_fingerprint(episode: GateEpisode) -> str:
    """Hash the canonical JSON representation of one generated episode."""
    return hashlib.sha256(episode_to_json(episode).encode("utf-8")).hexdigest()


def _manifest_payload(
    *,
    generator_seeds: tuple[int, ...],
    topology_seeds: tuple[tuple[str, int], ...],
    episode_ids: tuple[str, ...],
    episode_fingerprints: tuple[str, ...],
) -> str:
    return json.dumps(
        {
            "version": FINAL_VERSION,
            "generator_seeds": generator_seeds,
            "topology_seeds": topology_seeds,
            "episode_ids": episode_ids,
            "episode_fingerprints": episode_fingerprints,
        },
        sort_keys=True,
    )


def build_locked_final_manifest(
    generator_seeds: Iterable[int] = range(50),
    topology_seeds: Iterable[tuple[str, int]] | None = None,
) -> LockedFinalManifest:
    """Build and fingerprint the public 100-episode evaluation boundary."""
    generator_seeds = tuple(generator_seeds)
    topology_seeds = (
        tuple(
            (topology, seed)
            for topology in TOPOLOGIES
            for seed in range(25)
        )
        if topology_seeds is None
        else tuple(topology_seeds)
    )
    if not generator_seeds or not topology_seeds:
        raise ValueError("locked final manifest requires both seed partitions")
    episodes = generate_structural_gate_episodes(generator_seeds) + tuple(
        generate_topology_episode(seed, topology)
        for topology, seed in topology_seeds
    )
    if len(episodes) != FINAL_EPISODES:
        raise ValueError("locked final manifest has the wrong episode count")
    reports = tuple(leakage_report(episode) for episode in episodes)
    if any(report["critical_leakage_detected"] for report in reports):
        raise ValueError("locked final manifest contains critical leakage")

    episode_ids = tuple(episode.episode_id for episode in episodes)
    fingerprints = tuple(episode_fingerprint(episode) for episode in episodes)
    if len(set(episode_ids)) != len(episode_ids):
        raise ValueError("locked final manifest episode IDs must be unique")
    if len(set(fingerprints)) != len(fingerprints):
        raise ValueError("locked final manifest fingerprints must be unique")
    payload = _manifest_payload(
        generator_seeds=generator_seeds,
        topology_seeds=topology_seeds,
        episode_ids=episode_ids,
        episode_fingerprints=fingerprints,
    )
    return LockedFinalManifest(
        version=FINAL_VERSION,
        generator_seeds=generator_seeds,
        topology_seeds=topology_seeds,
        episode_ids=episode_ids,
        episode_fingerprints=fingerprints,
        leakage_reports=reports,
        content_fingerprint=hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    )


def locked_final_manifest_to_json(manifest: LockedFinalManifest) -> str:
    """Serialize the locked boundary using the published artifact shape."""
    return json.dumps(asdict(manifest), sort_keys=True)

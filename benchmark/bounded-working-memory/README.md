# Bounded Working Memory and Thought Holdover

## Provability proof

This is the public, materialized proof package for the claim:

> Under a bounded temporal observation protocol, Protama retains and uses
> task-relevant state across temporal intervals, distinguishes insufficient
> evidence from supported conclusions, and exposes a replayable evidence path
> for its decisions.

The package is intentionally evidence-oriented rather than accuracy-only. It
freezes the exact 140 episodes, records their SHA-256 digest, records the
manifest digest, and publishes the machine result that was produced from those
inputs.

## Files

- [`provability_gate_freeze.json`](./provability_gate_freeze.json) —
  frozen protocol, episode families, capacity conditions, and hashes.
- [`provability_gate_cases.json`](./provability_gate_cases.json) —
  materialized case data used by the final run.
- [`provability_gate_result.json`](./provability_gate_result.json) —
  final auditable result.

The result is `PROVABILITY_PASS`, with 140 episodes, 97.14% overall accuracy,
72.86% coverage, 97.06% selective accuracy, 94.00% capacity-aware accuracy,
and zero replay, cross-episode leakage, unauthorized-promotion, and
evidence-provenance failures. Human review is explicitly not required by this
freeze.

The public verifier validates the manifest hash, case-data hash, episode count,
result status, result linkage, review status, and zero-integrity-failure
conditions without importing Protama's private implementation.

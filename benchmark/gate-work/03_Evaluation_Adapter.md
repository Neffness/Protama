# Gate Work 03 — Evaluation Adapter

Status: **IN PROGRESS — DEVELOPMENT ADAPTER**

This document tracks the adapter that converts a locked episode into
replayable Protama predictions and pre-decision evidence for
[Protama_Structural_Gate_Publication_Task_List.md](../Protama_Structural_Gate_Publication_Task_List.md).

## Objective

Run training cases without exposing evaluator-only gold data, then evaluate
held-out cases while emitting prediction and trace records that the scorer can
consume.

## Required outputs

- [ ] Versioned prediction records.
- [ ] Versioned trace records.
- [ ] Candidate hypothesis records.
- [ ] Selected and rejected evidence.
- [ ] Operation sequence.
- [ ] Confidence-bearing decision.
- [ ] Grounded explanation payload.
- [ ] Initial and final snapshot identities.
- [ ] Clean separation between training and evaluation.
- [ ] Interactive adaptation explicitly disabled for clean evaluation.

## Current evidence

- [x] Adapter implementation exists.
- [x] Training uses only episode training cases.
- [x] Held-out cases are evaluated without labels.
- [x] Prediction records use `prediction.v1`.
- [x] Trace records use `trace.v1`.
- [x] Adapter replay is deterministic.
- [x] Snapshot identities are recorded.
- [x] Explicit permitted-input projection excludes family gold, expected
      outcomes, and evaluator-only case categories.

## Acceptance criteria

Phase C is complete only when a complete episode can be replayed from its
serialized input and produce predictions, traces, and snapshots without
reading `family_gold` or held-out expected labels.

The development adapter is not allowed to claim explanation fidelity merely
because it stores evidence. Explanation reconstruction and scoring remain
Phase D work.

The adapter now projects a `GateEpisode` into a `PermittedGateEpisode` before
induction. Only episode identity, seed, case IDs, and observations cross the
boundary. The projection is tested by running the adapter from both the full
evaluator object and the permitted projection and requiring identical outputs.
The permitted projection and adapter output now have versioned JSON
serialization. A round-trip test reconstructs the permitted input and
requires identical predictions, traces, and snapshot identities. This is
development replay evidence; clean-environment adapter certification and
integration with the final episode artifact bundle remain outstanding.

The initial continual-evaluation harness is now also present in
`Tools/Protama/continual_evaluation.py`. It creates a namespaced, unscored
probe split, verifies probe vocabulary disjointness, checks exact adapter
round-trip behavior, and exposes a ceiling-aware episode-delta calculation.
It now also contains a stateful development adapter that can learn one
episode, evaluate a later episode before learning, learn that episode, and
evaluate it again. Snapshot restore reproduces the learned-family behavior.
This establishes the mechanics for meaningful delta measurements; retention
across a growing prior-episode suite is now measured through explicit
before/after behavioral comparisons, including changed case IDs and a
retention rate. Gold-label correctness remains a scorer concern rather than
being conflated with behavioral retention. Clean-environment trajectory
replay remains outstanding.

Current validation:

```text
56 tests
55 passed
1 intentionally skipped
```

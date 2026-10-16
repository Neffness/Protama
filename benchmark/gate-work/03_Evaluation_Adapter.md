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

## Acceptance criteria

Phase C is complete only when a complete episode can be replayed from its
serialized input and produce predictions, traces, and snapshots without
reading `family_gold` or held-out expected labels.

The development adapter is not allowed to claim explanation fidelity merely
because it stores evidence. Explanation reconstruction and scoring remain
Phase D work.

Current validation:

```text
56 tests
55 passed
1 intentionally skipped
```

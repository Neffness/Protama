# Gate Work 04 — Gate Scorer

Status: **IN PROGRESS — DEVELOPMENT EPISODE SCORER**

This document tracks scoring for the predictions and traces emitted by
[03_Evaluation_Adapter.md](03_Evaluation_Adapter.md).

## Objective

Convert evaluator-side expected outcomes and adapter artifacts into explicit
category-level metrics. A missing evaluation dimension must remain missing; it
must not be converted into a passing zero-denominator score.

## Current evidence

- [x] Negative rejection accuracy.
- [x] Near-miss accuracy by category.
- [x] Novel-vocabulary transfer.
- [x] Coverage.
- [x] Selective risk.
- [x] False-commitment rate.
- [x] Abstention precision.
- [x] Four explanation dimensions at episode level.
- [x] Development surface invariance.
- [x] Development compositional generalization.
- [x] Development multi-episode aggregation.
- [x] Development episode-bootstrap confidence intervals.
- [x] Development risk-coverage curve.
- [x] Development score artifact serialization.
- [x] Development excluded-episode manifest serialization.
- [x] Development human-readable report.
- [x] Development preregistered pass-rule evaluation.

## Acceptance criteria

Phase D is complete only when the scorer:

1. scores raw adapter artifacts rather than rerunning the model;
2. reports every near-miss category separately;
3. distinguishes abstention from rejection and acceptance;
4. reports coverage and selective risk;
5. scores explanation fidelity from saved traces;
6. reports unavailable metrics explicitly;
7. emits deterministic machine-readable and human-readable results;
8. calculates episode-level confidence intervals before final evaluation.

The current scorer is an episode-level development scorer. It is not a final
gate decision engine.

Current validation:

```text
69 tests
68 passed
1 intentionally skipped
```

The development aggregate API now emits deterministic mean metrics and
percentile bootstrap intervals and can serialize the versioned score artifact
shape. It also emits a separate excluded-episode manifest with explicit
episode IDs, stages, and reasons. A deterministic development report and
fail-closed preregistered pass-rule result are now available. The current
pilot reports `NOT PASSED`; surface and compositional results currently cover
the development generator only and are not final benchmark evidence.

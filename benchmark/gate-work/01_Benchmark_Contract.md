# Gate Work 01 — Benchmark Contract

Status: **contract artifacts drafted** **— FINAL REVIEW PENDING**

This document records the decisions and evidence for Phase A of
[Protama_Structural_Gate_Publication_Task_List.md](../Protama_Structural_Gate_Publication_Task_List.md).

## Objective

Lock the benchmark contract before generating or tuning against final
episodes. The contract must define what is scored, what information Protama
may receive, and what constitutes a pass.

## Required decisions

### Episode schema

- [X] Hidden family representation is evaluator-only.
- [X] Training examples are serialized separately from evaluation examples.
- [X] Held-out positives, negatives, near-misses, ambiguity, and contradiction
  cases have distinct labels.
- [X] Every case has an episode ID, case ID, seed, split, expected outcome, and
  permitted evidence declaration.
- [X] Predictions, decisions, evidence, traces, explanations, and score
  contributions have versioned schemas.

### Split controls

- [X] Lexical split is defined.
- [X] Structural split is defined.
- [X] Template/surface split is defined.
- [X] Family split is defined.
- [X] Generator split is defined.
- [X] Temporal training/evaluation boundary is defined.
- [X] Held-out labels are unavailable before final scoring.

### Near-miss taxonomy

- [X] Role reversal.
- [X] Relation reversal.
- [X] Type violation.
- [X] Required argument/relation omission.
- [X] Single-feature mismatch.
- [X] Surface decoy.
- [X] Lexical overlap with invalid structure.
- [X] Novel negative.
- [X] Ambiguous case.
- [X] Contradictory case.

### Metrics and pass rule

- [X] Positive transfer accuracy.
- [ ] Negative rejection accuracy.
- [ ] Near-miss accuracy by category.
- [ ] Novel-vocabulary transfer.
- [ ] Surface invariance.
- [ ] Compositional generalization.
- [ ] Coverage.
- [ ] Selective risk and risk-coverage curve.
- [ ] False-commitment rate.
- [ ] Abstention precision.
- [ ] Episode-level delta from the declared pre-episode snapshot.
- [ ] Snapshot round-trip behavioral fidelity.
- [ ] Retention and backward-transfer performance on prior evaluation sets.
- [ ] Explanation invariant correctness.
- [ ] Explanation irrelevance recognition.
- [ ] Explanation counterfactual sensitivity.
- [ ] Explanation trace fidelity.
- [X] Episode-level confidence intervals.
- [X] Thresholds are fixed before final evaluation.
- [X] Exact pass-rule version is recorded.

## Locked contract decisions

The first preregistered contract uses:

| Metric                          | Threshold |
| ------------------------------- | --------: |
| Positive transfer accuracy      |   >= 0.90 |
| Negative rejection accuracy     |   >= 0.90 |
| Aggregate near-miss accuracy    |   >= 0.90 |
| Per-category near-miss accuracy |   >= 0.85 |
| Novel-vocabulary accuracy       |   >= 0.90 |
| Explanation fidelity            |   >= 0.85 |
| Coverage                        |   >= 0.75 |
| Selective risk                  |   <= 0.10 |

Confidence intervals use 10,000 episode-bootstrap resamples at 95% confidence
with seed `1729`. Critical leakage is disqualifying. The complete locked
configuration is [structural_gate_v1.json](../configs/structural_gate_v1.json).

## Proposed artifact schemas

The schemas below are provisional until Phase A is checked off:

```text
episode.json
prediction.jsonl
trace.jsonl
scores.json
leakage-report.json
replay-manifest.json
```

Each scored case must be traceable to:

```text
episode seed
training examples
evaluation example
candidate hypotheses
selected evidence
rejected evidence
operation sequence
prediction
decision
explanation
score contribution
```

Continual-learning evaluations must additionally record:

```text
declared pre-episode snapshot
pre-episode probe score
post-episode probe score
episode-level delta
snapshot round-trip result
prior-episode retention score
backward-transfer score
forgetting and interference indicators
```

## Acceptance criteria

Phase A is complete only when:

1. The episode schema is versioned.
2. All split and leakage rules are explicit.
3. Every near-miss category has an expected decision contract.
4. Metrics and confidence-interval methods are specified.
5. Pass thresholds are fixed before final episodes are generated.
6. A reviewer can determine whether a result is L2, L3, L4, or L5 without
   relying on undocumented assumptions.
7. Continual-learning claims identify what was known at the declared
   pre-episode snapshot and report induction delta separately from absolute
   post-episode performance.
8. Snapshot restoration passes behavioral equivalence probes before scoring.
9. Retention and backward-transfer results are reported for any cumulative
   or continual-learning evaluation.

## Evidence to attach

- [X] Versioned schema definitions.
- [X] Pass-rule version and threshold table.
- [X] Leakage policy.
- [X] Example valid episode.
- [X] Example invalid/leaky episode.
- [X] Decision log for unresolved contract questions.

## Current decision

The gate remains **NOT PASSED**. Phase A is complete for development: the
versioned configuration, schemas, fixtures, and executable contract tests are
present. Final benchmark review may still revise the contract before
preregistration.

## Phase A evidence

- [structural_gate_v1.json](../configs/structural_gate_v1.json)
- [episode.v1.json](../schemas/episode.v1.json)
- [prediction.v1.json](../schemas/prediction.v1.json)
- [trace.v1.json](../schemas/trace.v1.json)
- [score.v1.json](../schemas/score.v1.json)
- [leakage-report.v1.json](../schemas/leakage-report.v1.json)
- [episode_valid.v1.json](../fixtures/episode_valid.v1.json)
- [episode_invalid_leak.v1.json](../fixtures/episode_invalid_leak.v1.json)
- `Tools/Protama/tests/test_structural_gate_contract.py`

Validation result:

```text
48 tests
47 passed
1 intentionally skipped
```

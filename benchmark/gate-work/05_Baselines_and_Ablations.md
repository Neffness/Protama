# Gate Work 05 — Baselines and Ablations

Status: **IN PROGRESS — EXACT-MATCH BASELINE**

This document tracks non-structural controls and capability ablations required
before interpreting a Structural Induction and Transfer Gate result.

## Current evidence

- [x] Development exact-match baseline.
- [x] Development keyword baseline.
- [x] Development nearest-neighbor baseline.
- [x] Development symbolic-oracle upper bound.
- [ ] CPU Protama comparison.
- [ ] GPU Protama comparison or explicit scope exclusion.
- [x] Development evidence-provenance ablation.
- [x] Development no-abstention ablation.
- [x] Development no-structural-memory ablation.
- [x] Development explanation-constraint ablation.
- [x] Development no-novelty-tracking control (adapter limitation).
- [x] Development no-near-miss-exposure control (generator limitation).
- [x] Development no-external-evidence control (adapter limitation).
- [x] Development baseline comparison matrix.
- [ ] Leakage and baseline fairness checks.

The exact-match baseline accepts only an evaluation observation signature that
appeared identically in training. It is intentionally expected to reject
novel-vocabulary positives and therefore is a control, not a gate candidate.

The keyword baseline matches only the multiset of relation-type keywords and
ignores entity and variable bindings. It is expected to accept some typed
near-misses, exposing the value of structural binding.

The nearest-neighbor baseline compares each evaluation case with the closest
training observation sequence using a fixed token-level similarity threshold.
It does not induce reusable variables, so novel-vocabulary transfer remains a
separate structural test.

The symbolic oracle applies the evaluator-side latent family pattern directly.
It is an upper-bound reference for family-pattern matching, not a deployable
adapter. It does not receive expected case statuses; typed near-miss semantics
that are stricter than the family pattern remain an explicit benchmark
limitation to resolve before final evaluation.

The no-structural-memory ablation is explicitly named and uses only the
keyword baseline path. Its predictions are expected to match the keyword
control while reporting a distinct ablation identity in the result matrix.

The no-abstention ablation runs the structural adapter but converts every
abstained decision into a committed rejection. This isolates the contribution
of conservative abstention to coverage, selective risk, and false commitment.

The evidence-provenance ablation preserves predictions and operation order but
strips selected/rejected evidence and derived explanation citations from each
trace. It is intended to expose whether explanation fidelity depends on saved
pre-decision provenance.

The explanation-constraint ablation preserves selected and rejected evidence
but removes invariant and counterfactual explanation claims. This separates
the value of retaining evidence from the value of enforcing explanation
construction constraints.

The current adapter does not expose an independent novelty-tracking subsystem.
The named no-novelty-tracking control therefore preserves the adapter
predictions and records this limitation explicitly; it is not yet a causal
novelty ablation.

The current development generator places only positive examples in training,
so the no-near-miss-exposure control is behaviorally identical to the normal
adapter. The named control is present, but a causal result requires a final
generator condition with near-misses in training.

The current development adapter has no external evidence provider interface.
The named no-external-evidence control therefore preserves predictions and
records that a causal provider-removal comparison is not yet available.

The development comparison matrix scores baseline controls with shared
episode-level denominators for overall accuracy, positive transfer, negative
rejection, near-misses, and novel vocabulary. It is not yet the final
multi-seed publication matrix.

The Structural Induction and Transfer Gate remains **NOT PASSED**.

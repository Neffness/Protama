# Protama Structural Gate Completion

## Abstract

Protama has completed a preregistered CPU evaluation of the Structural Induction
and Transfer Gate. The held-out package contains 100 independently generated
episodes spanning canonical relational families and typed equivalence and
purpose topologies. The evaluation tested L2 latent relational induction, L3
transfer to novel vocabulary and surface forms, L4 typed structural near-miss
rejection, and L5 generalization across tested unseen combinations.

Protama passed the declared L2-L5 rule. The result is bounded: it is evidence
for the tested structural capability under the stated benchmark conditions, not
a claim of general intelligence, unrestricted language understanding, L6
independent invention, or L7 self-directed refinement.

## What was evaluated

Each episode separated system-visible training observations from held-out
evaluation cases. The generator supplied positive cases, negative cases, typed
near-misses, ambiguity cases, contradiction cases, novel vocabulary, and surface
variants. Evaluator-only family gold and expected labels were not provided to
the adapter.

The active protocol is
[structural-gate-preregistration-v2.json](../benchmark/artifacts/structural-gate-preregistration-v2.json).
The held-out manifest, adapter output, baseline suite, scored report, and
internal artifact audit are preserved under
[benchmark/artifacts/](../benchmark/artifacts/).

## Result

The held-out package produced:

| Measure                     |        Result |
| --------------------------- | ------------: |
| Episodes                    |           100 |
| Excluded episodes           |             0 |
| Critical leakage            | none detected |
| Positive accuracy           |      1.000000 |
| Negative rejection accuracy |      1.000000 |
| Novel-vocabulary accuracy   |      1.000000 |
| All ten category accuracies |      1.000000 |
| Explanation fidelity        |      0.978220 |
| Selective risk              |      0.000000 |
| Pass rule                   |          PASS |

The ten reported categories were role reversal, relation reversal, type
violation, argument omission, single-feature mismatch, surface decoy, lexical
overlap, novel negative, ambiguity, and contradiction.

The primary held-out report is
[structural-gate-heldout-report-v2.json](../benchmark/artifacts/structural-gate-heldout-report-v2.json).
Its `human_report` field contains the reviewer-readable report; the separate
text export is
[structural-gate-heldout-report-v2.txt](../benchmark/artifacts/structural-gate-heldout-report-v2.txt)
when the artifact bundle is distributed with generated files.

The decision metrics reached the ceiling on this package. That confirms the
declared pass rule but does not distinguish future structural systems at this
difficulty level. A future gate version should use harder latent families, more
demanding compositional combinations, or adversarial cases rather than
interpreting this ceiling as evidence of unlimited capability.

## Baselines and controls

The same held-out manifest was used for the declared CPU baselines and
ablations. Protama exceeded exact-match, keyword, nearest-neighbor, and
no-structural-memory controls on the principal transfer and structural metrics.
Some ablations matched decision accuracy on this task while testing different
trace or evidence mechanisms; therefore the result is not described as
superiority over every ablation.

## Reproducibility and audit

The primary manifest, adapter run, baseline suite, and scored report replayed
byte-for-byte in a clean environment. A read-only internal artifact audit,
performed by the project author using a fresh process and frozen artifacts,
verified seed alignment, development/held-out separation, fingerprint alignment,
category coverage, absence of evaluator-only labels in adapter records, leakage
status, and zero exclusions. No external auditor participated.

Supplementary continual-adapter evidence also covers accuracy-at-coverage,
snapshot round-trip fidelity, pre/post episode deltas, retention, backward
transfer, interference, operation counts, trace counts, wall-clock time, and
peak traced memory. These probes are separate from the stateless per-episode
adapter used for the primary gate and are not additional pass evidence for
continual learning. It is recorded in
[structural-gate-publication-evidence-v1.json](../benchmark/artifacts/structural-gate-publication-evidence-v1.json).

The audit record is
[structural-gate-heldout-review-v1.json](../benchmark/artifacts/structural-gate-heldout-review-v1.json).

## Claim boundary

The supported claim is:

> Under the preregistered CPU protocol, Protama passed the L2-L5 Structural
> Induction and Transfer Gate by inducing the tested relational structures,
> transferring them to held-out vocabulary and surface forms, rejecting the
> tested structural near-misses, handling the tested ambiguity and
> contradiction cases, generalizing across the tested unseen combinations,
> and producing reconstructible pre-decision evidence traces.

This does not establish:

- general intelligence;
- unrestricted natural-language understanding;
- open-ended learning;
- human-level reasoning;
- L6 discovery of entirely new reusable categories;
- L7 self-directed refinement through information-seeking examples;
- GPU/CPU parity;
- performance outside the benchmark’s generated distributions.

The active dictionary-learning study remains a companion evaluation. It is not
silently folded into this Structural Gate result.

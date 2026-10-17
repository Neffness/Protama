# Gate Work 02 — Independent Episode Generator

Status: **IN PROGRESS**

This document tracks the generator work for
[Protama_Structural_Gate_Publication_Task_List.md](../Protama_Structural_Gate_Publication_Task_List.md).

## Objective

Generate reproducible hidden-family episodes whose training and evaluation
sets are independent by vocabulary, structure, template, and seed. The
generator must create evaluator-only gold structure and must not leak it into
Protama inputs.

## Required components

- [x] Formal latent family generator.
- [x] Independent vocabulary pools.
- [x] Training/evaluation structural split.
- [x] Template/rendering split.
- [x] Near-miss generators for all ten contract categories.
- [x] Ambiguity and contradiction generators.
- [x] Episode seed/configuration serialization.
- [x] Deterministic replay.
- [x] Leakage checks.
- [x] 100-episode development generation run.
- [x] Locked final seed set with machine-readable manifest.

## Current evidence

- [x] Versioned episode schema exists.
- [x] Valid development fixture exists.
- [x] Intentionally leaky fixture exists.
- [x] Basic fixture leakage test exists.
- [x] Hidden-family episode generator exists.
- [x] Generator replay test exists.
- [x] Split-isolation checks exist.
- [x] Versioned machine-readable leakage report exists.
- [x] Near-miss category coverage test exists.
- [x] Deterministic 100-episode development manifest with per-episode
      fingerprints exists.
- [x] Adapter consumes the locked manifest and emits complete traces.
- [x] Baseline and ablation controls run against the locked manifest.
- [x] Full scored development report generated.
- [x] Clean-environment replay is byte-equivalent.
- [x] Preregistered development freeze record generated.
- [x] Held-out final seed allocation preregistered before generation.

## Acceptance criteria

Phase B is complete only when:

1. The same seed and configuration produce byte-equivalent episode artifacts.
2. Evaluation vocabulary and templates are absent from training.
3. Evaluation structures are absent from training except where the contract
   explicitly allows component reuse for L5 composition.
4. The hidden family and expected labels are evaluator-only.
5. Every required near-miss category is generated and independently counted.
6. Leakage checks fail closed and produce a machine-readable report.
7. The generator can produce the minimum final episode count without manual
   editing.

## Current status

The generator remains a deterministic development generator, while the final
evaluation boundary is a locked seed package rather than an independently
generated final family. The machine-readable final artifact bundle is now
versioned under `benchmark/artifacts/`.

The development generator now has structural and template split checks,
versioned leakage reports, and a 100-episode replay/leakage test. Its output
still remains development evidence. The new
`Tools/Protama/structural_gate_manifest.py` certification layer records the
seed list, episode IDs, per-episode content fingerprints, and fail-closed
leakage reports without serializing evaluator-only family gold.

The development batch now also rotates across three deterministic hidden
relation-name variants. This verifies that the generator is not merely
repeating one literal family signature across all seeds. The variants retain
the current three-relation topology; independent family topology and final
generator independence remain future work.

The locked final boundary is now materialized at
`benchmark/artifacts/structural-gate-final-manifest-v1.json`. It contains 100
episodes: 50 canonical hidden-family episodes and 25 episodes for each of the
two topology slices (`equivalence` and `purpose`). The artifact records the
non-negative seeds, episode IDs, content fingerprints, and fail-closed leakage
reports, but excludes evaluator-only family gold. Rebuilding the manifest from the locked seed configuration is byte-equivalent;
its current content fingerprint is
`921e3f7b08c3e69fb636172450534ec005cd99f82644b5deb4a16da015e12421`.

The evaluation adapter now consumes that artifact, validates seed replay and
episode fingerprints before execution, and writes
`benchmark/artifacts/structural-gate-final-adapter-run-v1.json`. The adapter
output contains 100 episode runs and 1,650 complete prediction/trace pairs;
it contains no evaluator-only family gold. Its current deterministic artifact
SHA-256 is
`7ce68787b2d885dfaf4f1e5be26652bfc88b841992f80a8924635237667ccfcd`.

The typed topology observations are now part of the permitted structured input
so the adapter can learn and test word/alias and tool/form/purpose roles rather
than receiving evaluator-only type labels. The adapter artifact was regenerated
after this contract change.

The locked baseline suite now runs 12 controls against the same 100 episodes:
four non-structural baselines, the Protama structural adapter, and seven
ablations. Its comparison artifact is
`benchmark/artifacts/structural-gate-final-baseline-suite-v1.json`. The suite
is deterministic and records aggregate development metrics; it does not
constitute a final pass decision.

The full scored development report is now materialized at
`benchmark/artifacts/structural-gate-final-development-report-v1.json` with a
reviewer-readable companion at
`benchmark/artifacts/structural-gate-final-development-report-v1.txt`. It
scores all 100 episodes with deterministic bootstrap intervals and applies the
current preregistered pass rule. The result is `PASS` for development
calibration, with no excluded episodes and no critical leakage. All scored
positive, negative, vocabulary, and near-miss metrics are `1.000000`, with
selective risk `0.000000`. This is a development result, not a final
evaluation claim.

A separate topology slice is now implemented in
`Tools/Protama/structural_gate_topologies.py`. It generates deterministic
typed equivalence episodes and typed object-purpose episodes,
with held-out positives, role/relation/omission near-misses, ambiguity, and
contradiction cases. These topologies pass replay and leakage tests but are
still development fixtures; they have not yet been merged into the final
preregistered episode pool.

The topology certification layer now produces a 100-episode mixed manifest
(`structural-gate-topology-manifest-v1`) spanning both topologies, with
per-episode fingerprints and fail-closed leakage reports. Evaluator-only
family gold remains excluded from the serialized manifest.

Both topology slices now enumerate all ten contract near-miss categories,
including type violation, single-feature mismatch, surface decoy, lexical
overlap, and novel negative cases. This is category-generation coverage only:
the evaluator-side topology constraints now verify required relation
signatures, arity changes, contradiction evidence, ambiguity emptiness,
lexical overlap, and novel-negative separation. Richer typed argument
constraints now also verify the generated `word -> alias` and
`tool -> form/purpose` bindings, including explicit type-violation cases.
These remain evaluator-side development constraints and are not yet a final
preregistered generator.

Validation result:

```text
16 targeted generator/manifest/topology tests passed
locked final manifest replay: byte-equivalent
100/100 final episodes have no critical leakage
adapter replay: byte-equivalent
100 complete adapter runs / 1,650 traces
56 structural benchmark tests passed
development report: 100 episodes scored
development pass rule: PASS
clean-environment replay: byte-equivalent
freeze record: structural-gate-freeze-v1
held-out preregistration: structural-gate-preregistration-v2
```

The current development package is bound by
`benchmark/artifacts/structural-gate-freeze-v1.json`. The freeze record hashes
the generator, typed topology contract, adapter, scorer, pass-rule
configuration, locked manifest, adapter output, baseline suite, and scored
report. It records the development status as `PASS`, confirms no critical
leakage, and records the clean-environment replay as verified. This freezes
the development evidence; it is not yet a preregistered final held-out
evaluation.

The first held-out scoring attempt exposed a reporting omission: ambiguity
and contradiction cases were generated but were absent from the per-category
metric table. The scorer was corrected before accepting the result, and
preregistration version 2 explicitly supersedes version 1. The corrected
held-out report now contains all ten required categories, including
`ambiguous` and `contradictory`.

The read-only internal artifact audit, performed by the project author, is recorded in
`benchmark/artifacts/structural-gate-heldout-review-v1.json`. It found no
seed, leakage, fingerprint, label-isolation, exclusion, or claim-boundary
violations. The active result is therefore eligible for publication review,
subject to preserving the stated L2-L5 claim boundary.

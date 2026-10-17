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
- [ ] Independent final-test generator or locked final seed set.

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

The generator now exists as a deterministic development generator in
`Tools/Protama/structural_gate_generator.py`. It is not yet the locked final
generator: it still needs a machine-readable final artifact bundle and an
independent final-test generator or locked final seed set.

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

A separate topology slice is now implemented in
`Tools/Protama/structural_gate_topologies.py`. It generates deterministic
one-relation equivalence episodes and two-relation object-purpose episodes,
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
53 tests
52 passed
1 intentionally skipped
```

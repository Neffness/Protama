# Bounded Working-Memory Thought Holdover
## Grounded Symbolic Composition Profile

**Gate version:** `bounded-working-memory-thought-holdover-v2`  
**Profile:** `grounded-symbolic-composition`  
**Freeze:** `grounded-symbolic-composition-freeze-v1`  
**Result:** **DEVELOPMENT_PASS**

## Abstract

This report evaluates whether Protama can learn a finite symbolic domain,
retain the required symbols in bounded transient thought state, compose
withheld symbolic inputs, and abstain when required state is unavailable.

The experiment does not assume that Protama understands English, radiation,
or arbitrary numeric arrays. It first teaches the symbol inventory, list
syntax, value/type associations, and a limited set of list compositions.
The held-out test then asks for compositions that were not taught verbatim.

The grounded symbolic composition profile passed its frozen development
criteria. This v1 record is not presented as a final statistical gate pass.

## Frozen curriculum

The curriculum taught:

- number symbols `0–100`;
- result symbols `inert`, `safe`, `warning`, and `danger`;
- list syntax `[`, `]`, `,`, `:`, and space;
- every number/type association in the declared domain;
- five list/type lessons:

```text
[0]                 -> inert
[0, 0]              -> inert
[0, 0, 0, 0]        -> inert
[0, 0, 1]           -> safe
[0, 0, 0, 1]         -> safe
```

The curriculum was frozen before the held-out evaluation. Teaching after the
freeze was prohibited.

The frozen manifest is:

The historical grounded-symbolic freeze is retained in repository history. The
active public package is the completed provability profile in
[benchmark/bounded-working-memory](../benchmark/bounded-working-memory/).

## Held-out composition

The exact list strings below were not taught:

```text
[0, 0, 0, 0, 0] -> inert
[0, 0, 0, 0, 1] -> safe
```

Protama produced:

```text
[0, 0, 0, 0, 0] -> inert
[0, 0, 0, 0, 1] -> safe
```

Composition accuracy was `1.000`.

## Capacity behavior

The required symbolic structure contains five number frames, one list frame,
and one result frame. The capacity sweep produced:

| Capacity | Inert query | Safe query |
|---:|---|---|
| 4 | abstain | abstain |
| 5 | abstain | abstain |
| 6 | abstain | abstain |
| 7 | correct composition | correct composition |
| 8 | correct composition | correct composition |

The minimum complete retained structure was `K=7`.

Below that capacity, Protama did not guess. It returned an unknown result
because required symbolic frames had been evicted.

## Abstention behavior

The frozen abstention cases were:

```text
[0, 50]  -> ambiguous
[0, 101] -> unknown
```

Both were handled correctly. Abstention accuracy was `1.000`.

## Distractor control

The matched control added grounded distractor values:

```text
50
80
99
```

At complete capacities, the distractor decrement was `0.0`. The distractors
did not change either withheld symbolic answer.

## Integrity results

| Metric | Result |
|---|---:|
| Withheld composition accuracy | 1.000 |
| Capacity-aware abstention accuracy | 1.000 |
| Snapshot replay agreement | 1.000 |
| Cross-thought leakage | 0 |
| Eviction validity failures | 0 |
| Unauthorized promotion validity failures | 0 |
| Distractor decrement | 0.000 |
| Held-out policy update attempts | 0 |

## Interpretation

This is a bounded working-memory thought-holdover result. Protama learned
symbols before evaluation, retained a bounded symbolic structure, used the
retained structure to produce withheld results, and abstained when the
structure no longer fit.

The result is not a claim of general intelligence, English comprehension,
sensorimotor grounding, or a universal item capacity. Those require separate
profiles with their own frozen curricula, baselines, metrics, and thresholds.

## Reproducibility

- [Public validation harness](../src/bounded_working_memory_benchmark/)

Implementation boundary:

The runtime implementation and development tests are maintained separately from
this public reproducibility package. The public validation harness below checks
the frozen manifest and result without importing that implementation.

The historical machine-readable development result is retained in repository
history. The current public machine-readable result is
[provability_gate_result.json](../benchmark/bounded-working-memory/provability_gate_result.json).

## v2 development run

The v2 preregistration expanded the held-out battery to 20 compositions across
four learned result types, lengths three through eight, and homogeneous,
mixed, sparse, and clustered structures. It also declared five retention
baselines, trial-level evidence requirements, and Wilson 95% intervals before
the run.

The frozen v2 development run produced:

| Measure | Result |
|---|---:|
| Held-out compositions | 20/20 |
| Abstention cases | 5/5 |
| Composition Wilson 95% interval | 0.839–1.000 |
| Abstention Wilson 95% interval | 0.566–1.000 |
| Maximum complete capacity | 10 |
| Baseline trial records | 5 × 20 |

The v2 result is `DEVELOPMENT_PASS`, not a final statistical gate pass. The
public verifier checks the manifest hash, every held-out and abstention record,
all baseline trial counts and accuracies, capacity trial count, intervals, and
declared thresholds.

The integrated startup verification gate is:

```text
grounded-symbolic-composition=pass
```

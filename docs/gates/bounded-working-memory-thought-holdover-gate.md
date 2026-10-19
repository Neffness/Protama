# Bounded Working Memory and Thought Holdover Gate

> **Status:** Public evaluation contract; development evidence is in progress.
> This document defines an evaluation contract, not a completed result.

This specification is intentionally implementation-neutral. It is suitable for
independent review, adversarial testing, and matched baseline comparisons
without exposing private runtime layouts or unpublished training records.

## Purpose

This gate tests whether Protama can use transient state as a manipulable
workbench across cognitive operation cycles without making every intermediate state durable.

For this gate, a **cycle** is one externally prompted cognitive operation
transition, such as observe, compare, verify, or synthesize. It is not a lesson
cycle, a probe schedule, or a consolidation cycle.

## Scope

The evaluator supplies the task and requires a bounded sequence of operations.
Protama does not need autonomous thought or self-generated goals.

## Evaluation unit

Each episode contains:

```text
task
ordered operation opportunities
items to retain
relations to bind
distractors
capacity condition
manipulation requirement
snapshot point
required final decision
```

The episode must include complex-span trials in which Protama must hold items
while comparing, transforming, or binding them.

## Required behavior

Protama must:

- retain only bounded transient state;
- retrieve retained items by thought and generation;
- manipulate retained items while preserving identity and relations;
- bind relations to the correct arguments under load;
- resist distractor replacement where capacity permits;
- evict or decay state when capacity is exceeded;
- distinguish holdover from active thought and durable memory;
- preserve provenance for retained and evicted items; and
- reproduce behavior after snapshot restoration.

## Primary metrics

- capacity curve;
- complex-span accuracy;
- binding accuracy;
- distractor resistance;
- interference error;
- decay curve;
- replacement and eviction correctness;
- cross-thought leakage;
- promotion error rate;
- snapshot replay equivalence; and
- memory and latency cost.

## Controls

Compare against:

- unlimited-memory reference;
- no-holdover baseline;
- FIFO retention;
- random retention;
- relevance-aware retention; and
- an oracle retention policy.

Include item-permutation controls and relation-reversal controls.

## Pass conditions

A pass requires:

- bounded memory use;
- above-baseline manipulation and binding;
- measurable degradation when capacity is exceeded;
- correct eviction and expiration;
- no cross-thought leakage;
- no unsupported promotion to durable state; and
- exact replay of retention and retrieval decisions.

## Failure conditions

The gate fails if Protama:

- silently expands capacity;
- retains only independent items but cannot manipulate them;
- loses relation bindings under load;
- retrieves evicted state as if it were present;
- leaks state between thoughts;
- changes behavior after restore; or
- treats the entire event log as working memory.

## Non-claims

Passing does not establish human working memory, Baddeley's component
architecture, or a fixed biological item limit. It establishes bounded,
manipulable, auditable transient state.

## Public reporting standard

Any claimed result should publish:

- the exact gate version and threshold set;
- the episode generator or complete episode manifest;
- all baseline and Protama outcomes, including failures and abstentions;
- capacity, accuracy, interference, promotion-error, latency, and memory
  measurements; and
- enough metadata to reproduce snapshot and restore comparisons.

Development observations must remain labeled as development evidence until the
thresholds and matched controls are frozen.

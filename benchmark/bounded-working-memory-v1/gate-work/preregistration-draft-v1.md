# Bounded Working Memory and Thought Holdover

## Public preregistration draft

**Status:** Draft for opposition review. Nothing in this document is frozen.

This draft defines the final evaluation boundary for the bounded working-memory
gate. It is a reviewable specification of what must be fixed before held-out
episodes are run; it is not a result and does not declare a pass.

## Held-out evaluation

The final run must use an episode manifest generated after the scoring code,
seeds, policies, hardware budget, and thresholds are frozen. The manifest must
include:

- item spans below, near, and above the measured capacity breakpoint;
- complex-span transformations covering difference, sum, and ordered-pair
  preservation;
- distractor loads of zero, near-breakpoint, and above-breakpoint levels;
- item permutations and relation reversals;
- contradiction, expiration, and maintenance cases;
- supported, uncertain, contradicted, and missing-evidence promotion cases; and
- snapshot/restore replay cases.

The held-out set must be untouched by threshold selection.

## Required baselines

Every held-out condition must report the matched:

1. unlimited-memory reference;
2. no-holdover baseline;
3. FIFO retention;
4. deterministic random retention;
5. relevance-aware retention;
6. oracle retention;
7. CPU Protama; and
8. GPU Protama.

CPU and GPU implementations must be compared for decision equivalence and
reported separately when resource behavior differs.

## Metrics to freeze

The final report must include condition-level and aggregate values for:

- capacity breakpoint;
- complex-span accuracy;
- relation-binding accuracy;
- distractor decrement;
- interference error;
- eviction and expiration correctness;
- cross-thought leakage;
- promotion-error rate;
- snapshot/replay agreement;
- peak transient-state footprint; and
- append, retrieval, and snapshot latency.

Failures, abstentions, excluded episodes, and exclusion reasons must be
reported rather than removed from denominators.

## Threshold fields requiring explicit approval

Before the final held-out run, the project must record numeric values for:

```text
k_min
alpha_span
beta_binding
delta_distractor_max
eta_eviction_max
pi_promotion_max
rho_replay_min
m_transient_max
latency_budget
```

These values must be committed to the versioned preregistration record before
held-out results are inspected. The current development artifacts may inform
the choice, but may not be used to tune thresholds after the final run.

## Current status

The implementation has development evidence for capacity curves, longer-span
episodes, multi-transformation complex span, matched interference decrements,
decay and maintenance, promotion rejection, replay, and resource costs.
Thresholds, held-out manifests, confidence intervals, and the final matched
CPU/GPU gate run remain open.

# Bounded Working Memory and Thought Holdover

## Public preregistration draft

**Status:** Draft for opposition review. Nothing in this document is frozen.

This document defines the final evaluation boundary for the bounded
working-memory gate. It is a reviewable specification of what must be fixed
before held-out episodes are run; it is not a result and does not declare a
pass.

## Evaluation order and freeze boundary

The evaluation has two phases:

1. **Calibration:** development material is used to measure the canonical CPU
   Protama capacity curve, validate recodable and non-recodable generators,
   choose fixed load levels, and estimate uncertainty.
2. **Held-out evaluation:** the generator or complete episode manifest, scoring
   code, seeds, policies, hardware budget, calibration result, and all
   thresholds are frozen before any held-out result is inspected.

The canonical CPU Protama breakpoint anchors the common held-out load grid.
CPU Protama, GPU Protama, and every baseline run the same held-out episodes and
the same item/distractor loads. Baselines do not receive a separately
calibrated manifest. Their own capacity curves are reported diagnostically.
This preserves matched comparisons while making the calibration source
explicit. The GPU implementation is evaluated against the CPU-calibrated
manifest rather than being allowed to select its own favorable loads.

**Canonical CPU Protama** means the fully inspectable reference
implementation evaluated on the CPU execution path, with no GPU-kernel
substitution and no substrate-induced nondeterminism. Its source version,
configuration, interpreter, and hardware identity are recorded in the
calibration record.

The calibration record must contain the generator and scorer fingerprints, the
canonical breakpoint, the below/near/above load values, the distractor loads,
the recoding annotations, and the seed used to produce the record. Held-out
episodes must be generated from a separate seed family or locked manifest and
must be untouched by threshold selection.

## Held-out evaluation

The final manifest must include:

- item spans below, near, and above the canonical measured capacity
  breakpoint;
- both recodable and non-recodable spans at each relevant load;
- complex-span transformations covering difference, sum, and ordered-pair
  preservation;
- distractor loads of zero, near-breakpoint, and above-breakpoint levels;
- item permutations and relation reversals;
- contradiction, expiration, and maintenance cases;
- supported, uncertain, contradicted, and missing-evidence promotion cases;
- cross-thought probes with explicit start/end boundaries and fresh thought
  identifiers; and
- snapshot/restore replay cases.

An item is **recodable** only when the manifest declares a lossless,
task-authorized code for it and charges the encoded representation, decoder,
and required relation metadata against the same transient budget. A
non-recodable item or relation is independently necessary and must remain
individually reconstructible. A system may chunk recodable material, but may
not use chunking, an uncharged pointer, or an event-log lookup to hide
non-recodable load. The charged footprint is the actual runtime representation
measured during execution, including the instantiated encoder/decoder state
and metadata, not a theoretical minimum or an abstract description of the
algorithm. Results are stratified by these two conditions.

Each episode records its thought boundary, thought identifier, authorized
promotion events, item identities, relation identities and arguments, and
whether every state transition is active, retained, evicted, expired,
contradicted, superseded, or promoted.

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

CPU and GPU implementations must be compared for **decision equivalence**:
for the same seed, inputs, and manifest, they must agree on the final
decision, abstention status, retention/eviction/expiration status, binding
arguments, promotion disposition, contradiction disposition, and replay
decision. Exact tensor values, internal ordering among equal-scoring candidates,
and resource measurements are not required to match. Any disagreement is
reported per episode and in aggregate.

## Metrics and threshold definitions

The final report must include condition-level and aggregate values for the
following. The threshold fields below are all **gating**, not diagnostic.

| Field | What it thresholds | Units | Passing direction |
|---|---|---|---|
| `k_min` | canonical non-distractor capacity breakpoint, the smallest independently necessary non-recodable load at which accuracy crosses below the preregistered capacity criterion | items/relations | breakpoint must be at least this value |
| `alpha_span` | complex-span accuracy after the required compare, transform, or bind operation | proportion of episodes, 0–1 | accuracy must be at least this value |
| `beta_binding` | binding accuracy for the required relation type, including correct arguments | proportion of scored bindings, 0–1 | accuracy must be at least this value |
| `delta_distractor_max` | matched accuracy decrement from adding the preregistered distractor load | proportion-point difference, 0–1 | decrement must be no greater than this value |
| `eta_eviction_max` | combined error rate for eviction and expiration decisions, including retaining state that should be absent or losing state that should remain | proportion of scored lifecycle decisions, 0–1 | error must be no greater than this value |
| `pi_promotion_max` | promotion error rate: unauthorized, contradicted, uncertain, or missing-evidence state promoted as durable, plus any other incorrect promotion disposition | proportion of promotion cases, 0–1 | error must be no greater than this value |
| `rho_replay_min` | snapshot/restore agreement on observable decisions and state dispositions | proportion of replay episodes, 0–1 | agreement must be at least this value |
| `m_transient_max` | peak charged transient-state footprint during an episode | bytes under the declared accounting convention | footprint must be no greater than this value |
| `latency_budget` | maximum allowed p95 end-to-end episode latency, including retention, retrieval, scoring, and snapshot operations as applicable to the condition | milliseconds per episode | p95 latency must be no greater than this value |

The capacity criterion used to locate the breakpoint is itself frozen before
the held-out run. A right-censored breakpoint is not silently converted into
the maximum tested load. In addition to the gating fields, the report must
include complex-span submetrics, interference error, decay, cross-thought
leakage, failure counts, abstentions, promotion dispositions, and resource
traces.

## Baseline-anchored threshold justification

Before numeric values are frozen, the preregistration must append one
justification line for each of the nine fields above. Each line must state:

1. the development result for the strong non-oracle baselines;
2. the development result for the oracle baseline;
3. the proposed threshold value and its confidence interval or uncertainty
   range; and
4. why the value discriminates the intended capability rather than merely
   describing the observed Protama development curve.

The strong non-oracle comparison is defined before inspecting results as the
relevance-aware retention baseline, with FIFO, deterministic random, and
no-holdover results reported alongside it. The unlimited-memory reference is
reported as an upper-bound control, and the oracle retention policy is the
privileged upper-bound comparison. No baseline may be designated “strong” only
after seeing which one performs best.

The justification must use the same estimator, episode strata, and accounting
convention as the held-out report. A threshold may not be justified solely by
Protama's own development value, and a value that every baseline and the
oracle satisfy does not discriminate the capability. If baseline performance
overlaps the proposed threshold, the record must explain the intended
separation or revise the threshold before freeze. These justifications are
part of the versioned freeze record and cannot be added after held-out results
are inspected.

The freeze record must contain the following nine lines, populated with
numeric values before the held-out run:

```text
k_min: [value]; strong-baseline development: [result]; oracle: [result];
  discrimination rationale: [one line]
alpha_span: [value]; strong-baseline development: [result]; oracle: [result];
  discrimination rationale: [one line]
beta_binding: [value]; strong-baseline development: [result]; oracle: [result];
  discrimination rationale: [one line]
delta_distractor_max: [value]; strong-baseline development: [result];
  oracle: [result]; discrimination rationale: [one line]
eta_eviction_max: [value]; strong-baseline development: [result];
  oracle: [result]; discrimination rationale: [one line]
pi_promotion_max: [value]; strong-baseline development: [result];
  oracle: [result]; discrimination rationale: [one line]
rho_replay_min: [value]; strong-baseline development: [result];
  oracle: [result]; discrimination rationale: [one line]
m_transient_max: [value]; strong-baseline development: [result];
  oracle: [result]; discrimination rationale: [one line]
latency_budget: [value]; strong-baseline development: [result];
  oracle: [result]; discrimination rationale: [one line]
```

## Promotion scoring

Promotion is scored against the expected disposition declared in each episode:

- **Supported:** promote exactly the authorized item with its provenance.
- **Contradicted:** reject promotion and retain the contradiction/provenance
  record; promoting the contradicted claim is an error.
- **Uncertain:** abstain from promotion and leave the item transient or
  explicitly pending; forced promotion is an error.
- **Missing evidence:** reject or defer promotion and report the missing
  evidence; promotion is an error.

An unauthorized durable write is an error regardless of the final answer.
Zero attempted promotions are reported as zero attempts, not converted into a
zero promotion-error rate.

Contradiction and maintenance cases are scored in the same way: a contradiction
must invalidate or mark the contradicted binding without erasing its
provenance, while an explicitly maintained supported item must remain
retrievable through the declared maintenance interval. Natural expiration,
explicit maintenance, replacement, and supersession are separate expected
outcomes in the manifest.

## Statistical and exclusion protocol

All confidence intervals use 10,000 episode-level bootstrap resamples with
seed `1729`, stratified by condition and resampled at the episode level so
operations within one episode are not treated as independent observations.
For binary proportions, the same bootstrap procedure is used; exact binomial
intervals may be added as a sensitivity analysis but do not replace the
registered interval. The report uses two-sided 95% confidence intervals.

For a minimum threshold, the lower 95% confidence bound must meet or exceed
the threshold. For a maximum threshold, the upper 95% confidence bound must be
at or below the threshold. For `latency_budget`, the upper 95% confidence
bound of p95 episode latency must meet the budget. For `m_transient_max`, the
upper 95% confidence bound of the episode peak must meet the budget. A
capacity breakpoint is reported with its bootstrap interval and is gating only
when its lower bound meets `k_min`; right-censored results fail to establish
the threshold unless the preregistered design explicitly makes the censoring
bound sufficient.

An episode may be excluded only for a preregistered harness or infrastructure
failure that prevents the episode from being presented or scored: corrupted
manifest, process crash before presentation, unavailable declared hardware,
or scorer failure independently reproduced from the saved trace. A model
failure, timeout within the declared budget, invalid response, abstention,
contradiction, promotion rejection, or poor outcome is never an exclusion.
Every exclusion requires a reason code, raw trace, and reviewer-visible count;
excluded episodes remain outside metric denominators but are included in the
run accounting.

## Pass rule

The gate passes only if **all nine threshold fields** satisfy their stated
confidence-bound rules on the held-out run, no critical leakage or uncharged
storage is detected, and all required baselines, failure/abstention reports,
promotion cases, contradiction/maintenance cases, and replay comparisons are
present. The following are reported but are not additional independent
threshold fields: interference error, decay curve, CPU/GPU equivalence rate,
and per-condition diagnostic curves. A critical leakage or uncharged-storage
finding fails the gate even if the nine numeric thresholds are met.

## Current status

The implementation has development evidence for capacity curves, longer-span
episodes, multi-transformation complex span, matched interference decrements,
decay and maintenance, promotion rejection, replay, and resource costs.
Threshold values, the capacity criterion, the calibration record, held-out
manifest, confidence intervals, and the final matched CPU/GPU gate run remain
open and must be frozen after opposition review.

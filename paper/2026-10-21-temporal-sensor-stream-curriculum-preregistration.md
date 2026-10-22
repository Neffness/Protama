# Temporal Sensor-Stream Curriculum Preregistration

**Gate version:** `bounded-working-memory-thought-holdover-v2`  
**Profile:** `temporal-sensor-stream-state-tracking`  
**Status:** frozen preregistration; no scored run is reported here

## Purpose

This curriculum specifies the lessons available to Protama before the
temporal sensor-stream evaluation. It tests bounded state tracking over
event-blind sensor bursts, not physical sensing, radiation identification,
or unrestricted language understanding.

The curriculum is frozen before evaluation. Teaching, parameter changes,
retention-policy changes, or inspection of scored outcomes invalidate the run
and require a new freeze.

## Simulator contract

- Sampling rate: **10 samples per second** for **10 seconds**.
- Each sample contains **one Poisson count draw**.
- Five consecutive samples form a burst group for missing-burst encoding.
- The five counts are not summed before reaching the evaluator or retention
  system.
- `background_rate = 4.0 expected counts/second`.
- `source_rate = 24.0 expected counts/second`.
- `shielding_multiplier = 0.45` applies to source counts when shielding is
  present.
- Rates are simulation parameters, not physical detector calibration values.
- Burst boundaries are independent of event onset, offset, environment
  transitions, and labels.
- Missing bursts are represented as null count values.

## Curriculum lessons

The 30 lessons cover the following primitive inventory:

### Sensor primitives

`background-counts`, `shield-attenuation`, `sustained-elevation`,
`rising-trend`, `falling-trend`, `transient-spike`, `missing-burst`,
`delayed-burst`, `count-variance`, and `stable-low-count`.

### Temporal primitives

`before`, `after`, `during`, `starts`, `ends`, `persists`,
`interrupted-by`, and `resumes-after-gap`.

### State primitives

`no-source`, `source-present`, `shielded`, `insufficient-evidence`, and
`unknown-pattern`.

The taught source mechanisms are `step` and `exponential-decay`.
The required mechanism holdout is `triangular-rise`; it is not taught as a
curriculum lesson.

## Holdout and novelty rules

Evaluation episodes may use the held-out `triangular-rise` mechanism and
combinations of the frozen primitives. An episode is not novel merely because
its numeric parameters differ. The evaluator records primitive overlap,
graph matches, ordered-sequence matches, mechanism exposure, burst alignment,
novelty reason, and determinacy.

The following shortcuts are forbidden as novelty claims:

- canonicalized event graphs;
- ordered primitive sequences;
- onset/offset patterns;
- mechanism identifiers;
- complete count traces.

## Evaluation strata and capacity

The frozen plan contains 100 determinate and 100 epistemic episodes. Capacity
conditions are `K = 4, 6, 8, 10, 12, 16`. Determinacy is evaluated from the
evidence surviving retention; it overrides any family-level default.

The preregistered baselines are no-holdover, FIFO retention, random retention,
relevance-aware retention, oracle retention, threshold detection, and
persistence detection.

## Pass criteria

The development profile requires the declared episode counts, complete
trial-level baseline records, independent stratum thresholds, and all
zero-tolerance integrity conditions. A final gate pass additionally requires
the lower bounds of the preregistered confidence intervals and the paired
baseline comparison rule to pass.

The comparison uses a paired 95% bootstrap interval for
`baseline - Protama`, with non-inferiority when the lower bound is at least
`-0.05` on each oriented metric. The threshold choices are intended to
require near-ceiling event and abstention accuracy, substantial temporal
localization, and no false commitments on near misses while allowing the
finite-sample uncertainty to be reported explicitly.

## Frozen source

The machine-readable freeze is
[temporal-sensor-stream-freeze-v1.json](../benchmark/bounded-working-memory-v1/gate-work/temporal-sensor-stream-freeze-v1.json).
Any change to this document, the simulator, curriculum, or pass rule after
the freeze requires a new freeze identifier.

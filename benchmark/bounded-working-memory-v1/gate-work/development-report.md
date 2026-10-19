# Working-Memory Benchmark Development Report

**Benchmark:** Bounded Working Memory and Thought Holdover v1  
**Status:** Development evidence only

## Curated coverage

The public package contains:

- matched no-holdover, FIFO, random, relevance-aware, and oracle controls;
- capacity curves through eight-item spans;
- multi-transformation complex-span trials;
- matched distractor/interference decrements;
- item-permutation and relation-reversal controls;
- decay and active-maintenance controls;
- contradiction, expiration, and lifecycle replay;
- promotion-safety behavior;
- actual Protama cognitive-cycle execution; and
- serialized snapshot size and local latency measurements.

The machine-readable artifacts are listed in the package
[README](../README.md).

## Reproducibility observations

The development harness reproduces snapshot reads across the retained
capacity, complex-span, interference, lifecycle, and actual-Protama controls.
Relation reversal preserves directional subject/object pairs, and the current
records report no cross-thought leakage.

These are properties of the released development fixtures and controls. They
are not claims that the gate has passed.

## Limitations

- Episodes remain deterministic development fixtures.
- Retention policies are reference controls, not learned policies.
- The complex-span battery evaluates transformations only when both relation
  endpoints survive the capacity condition.
- Resource timings are environment-specific observations.
- No preregistered numeric thresholds have been frozen.
- No held-out final evaluation or gate decision has been declared.

## Next required phase

Before a final decision, freeze the episode manifest, thresholds, seeds,
hardware budget, scoring code, and confidence-interval procedure. Then run the
untouched held-out comparison across the preregistered baselines and report
failures, abstentions, exclusions, resource costs, and replay agreement.

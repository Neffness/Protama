# Temporal Sensor-Stream Curriculum Preregistration

**Gate:** `bounded-working-memory-thought-holdover`  
**Profile:** `temporal-sensor-stream-state-tracking`  
**Status:** frozen preregistration; the result is recorded in the public proof package

## Purpose

This curriculum and evaluation specify a bounded temporal observation protocol
for testing whether Protama retains and uses task-relevant state across
temporal intervals. The gate evaluates evidence provenance, replayability,
uncertainty handling, and bounded retention. It does not claim physical
sensing, radiation identification, consciousness, or general intelligence.

The exact case data, protocol manifest, and result are published together.
Changes to the simulator, case families, retention conditions, evaluator, or
pass rule require a new freeze and a new materialized case set.

## Simulator contract

- Sampling rate: **10 samples per second** for **10 seconds**.
- Each sample contains one Poisson count draw.
- Five consecutive samples form a burst group for missing-burst encoding.
- The five counts are not summed before reaching the evaluator or retention
  system.
- `background_rate = 4.0` expected counts/second.
- `source_rate = 24.0` expected counts/second.
- `shielding_multiplier = 0.45` applies to source counts when shielding is
  present.
- Rates are simulation parameters, not physical detector calibration values.
- Burst boundaries are independent of event onset, offset, environment
  transitions, and labels.
- Missing bursts are represented as null count values.

## Case families

The frozen case set contains 140 episodes across seven declared families:

- `ambiguous`
- `interrupted-source`
- `no-source`
- `persistent-source`
- `transient-source`
- `near-miss`
- `unknown-mechanism`

Each family contributes 20 deterministically generated episodes. The exact
seed ranges, source mechanisms, sampling parameters, and justified conclusion
for every family are recorded in the freeze manifest and materialized case
file. The `unknown-mechanism` family uses `triangular-rise`, which is not
assumed to be the same mechanism as the step-source families.

## Evidence and conclusion rules

The evaluation separates:

1. **Ground truth** — what the generated episode actually contains.
2. **Observable evidence** — the stream and retained state available at the
   decision.
3. **Justified conclusion** — what the available evidence permits the system
   to claim.

Incomplete retained history cannot establish a negative conclusion. Under
partial retention, a negative conclusion without a retained positive evidence
span is therefore `ambiguous`.

The evaluation records the evidence span, retained and evicted state,
rationale, prediction, abstention status, and deterministic replay result.
Evaluator-only labels and future observations are not available to the
decision path.

## Capacity conditions

Retention capacity is evaluated at:

`K = 4, 8, 12, 16, 20`

The capacity-aware result must preserve the declared ambiguity behavior when
the relevant history is incomplete. Capacity is not treated as an unbounded
event log.

## Baseline and integrity conditions

The preregistered baseline is `no-holdover`, an always-ambiguous policy. It is
reported to expose the difference between correct abstention and useful
discrimination; its performance on ambiguous cases alone is not sufficient
for a gate pass.

The proof requires:

- complete evidence provenance;
- deterministic replay;
- zero cross-episode leakage;
- zero unauthorized promotion of transient state;
- zero evaluator-to-decision leakage;
- declared coverage and selective accuracy;
- a result linked to the exact manifest and case-data hashes.

Human review is not a required completion condition for this freeze. The
machine-readable checks and structured fairness-key records define the
completion evidence.

## Frozen source

The machine-readable freeze is
[provability_gate_freeze.json](../benchmark/bounded-working-memory/provability_gate_freeze.json).
The exact materialized cases are in
[provability_gate_cases.json](../benchmark/bounded-working-memory/provability_gate_cases.json),
and the final result is in
[provability_gate_result.json](../benchmark/bounded-working-memory/provability_gate_result.json).

The public package reports `PROVABILITY_PASS` for the frozen 140-episode
case set. Any change to this document's protocol description, the simulator,
the case data, or the pass rule requires a new freeze and regenerated result.

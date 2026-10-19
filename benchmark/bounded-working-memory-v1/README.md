# Bounded Working Memory and Thought Holdover v1

This directory is the public review package for the
[Bounded Working Memory and Thought Holdover Gate](../../docs/gates/bounded-working-memory-thought-holdover-gate.md).

## Status

**Development evidence only.** This is not a passing gate result. Thresholds,
held-out episodes, confidence intervals, and the final pass decision remain
unfrozen.

## Package contents

- `schemas/` — machine-readable trial contract;
- `fixtures/` — deterministic smoke fixture;
- `gate-work/` — public development report and preregistration draft; and
- `artifacts/` — curated primary evidence only.

Private implementation code, learned state, and exploratory development
records are not part of this public package.

## Curated primary artifacts

- [development-capacity-policy-sweep.json](./artifacts/development-capacity-policy-sweep.json) —
  matched retention-policy trials;
- [development-capacity-policy-curves.json](./artifacts/development-capacity-policy-curves.json) —
  aggregate capacity curves;
- [development-long-span-capacity-curves.json](./artifacts/development-long-span-capacity-curves.json) —
  eight-item capacity extension;
- [development-complex-span-battery.json](./artifacts/development-complex-span-battery.json) —
  difference, sum, and ordered-pair manipulation;
- [development-interference-decrement.json](./artifacts/development-interference-decrement.json) —
  matched distractor decrement;
- [development-binding-controls.json](./artifacts/development-binding-controls.json) —
  permutation and relation-reversal controls;
- [development-multicycle-lifecycle.json](./artifacts/development-multicycle-lifecycle.json) —
  maintenance, revision, contradiction, expiration, and replay;
- [development-actual-protama-stack.json](./artifacts/development-actual-protama-stack.json) —
  actual Protama observe/compare/verify/synthesize execution; and
- [development-resource-cost.json](./artifacts/development-resource-cost.json) —
  snapshot size and local latency measurements.

The smoke fixture is
[smoke-seed-19.json](./fixtures/smoke-seed-19.json), and the machine-readable
schema is
[working-memory-trial.schema.json](./schemas/working-memory-trial.schema.json).

## Review documents

- [development-report.md](./gate-work/development-report.md)
- [preregistration-draft-v1.md](./gate-work/preregistration-draft-v1.md)

The preregistration is explicitly a draft for opposition review. No threshold
was selected after inspecting held-out results, because no final held-out run
has yet been performed.

# Bounded Working Memory and Thought Holdover v1

This directory is the public review package for the
[Bounded Working Memory and Thought Holdover Gate](../../docs/gates/bounded-working-memory-thought-holdover-gate.md).

## Status

**Frozen grounded-symbolic development profile.** The development result is
recorded in the frozen manifest and report linked below. It is not a final
statistical gate pass. The broader historical development evidence is not part
of this active package.

## Package contents

- `gate-work/` — frozen release inputs and calibration manifests.

Private implementation code, learned state, and exploratory development
records are not part of this public package.

## Frozen grounded-symbolic development release

- [grounded-symbolic-composition-freeze-v1.json](./gate-work/grounded-symbolic-composition-freeze-v1.json)
- [grounded-symbolic-composition-final-v1.json](./gate-work/grounded-symbolic-composition-final-v1.json)
- [grounded-symbolic-composition-freeze-v2.json](./gate-work/grounded-symbolic-composition-freeze-v2.json)
- [grounded-symbolic-composition-development-v2.json](./gate-work/grounded-symbolic-composition-development-v2.json)

The frozen profile is implemented and verified by the private Protama source
and documented in the
[publication draft](../../paper/2026-10-21-bounded-working-memory-grounded-symbolic-composition.md).

An external viewer can validate the frozen manifest and result with the
public [`bounded_working_memory_benchmark`](../../src/bounded_working_memory_benchmark/)
harness; it does not require private Protama imports.

The v2 development run contains 20 held-out compositions, 5 abstention cases,
capacity trial records, Wilson 95% intervals, and trial-level results for all
five preregistered baselines. It remains development evidence rather than a
final statistical gate pass.

The calibration manifests remain in `gate-work/` because the existing
calibration tests use them as inputs. They are not part of the frozen
grounded-symbolic result.

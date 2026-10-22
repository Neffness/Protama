# Provability Profile Publication Record

## Scope

This record documents what the public repository can establish about the
bounded working-memory provability profile. It separates the reproducibility
of the run from the historical order in which its paperwork was published.

## What is frozen and reproducible

The public package contains:

- the complete 140-episode materialized case set;
- the protocol and family manifest;
- the case-data SHA-256;
- the manifest SHA-256;
- the machine-readable Protama and `no-holdover` results;
- zero-failure integrity checks for replay, provenance, leakage, and
  unauthorized promotion; and
- the structured fairness-key review.

The public verifier recomputes the hashes, checks the result linkage, checks
the declared performance thresholds, and verifies that the structured review
is present.

## Claim boundary

The public record supports this claim:

> The published bounded temporal result satisfies the declared provability
> profile completion conditions.

It does not claim that the current Git history independently proves that every
numeric completion threshold was published before the original run. The
thresholds are part of the current public completion record, while the
materialized cases and result preserve the exact run being reported.

This is a publication-level completion record, not a retroactive claim of
preregistered statistical significance.

## Profile status

The profile is **COMPLETED** as an evidence and reproducibility profile.
Readers requiring independently time-ordered preregistration must treat the
historical ordering as unresolved and require a future run with a separately
dated threshold freeze.

## Verification entry points

- [Freeze manifest](./provability_gate_freeze.json)
- [Materialized cases](./provability_gate_cases.json)
- [Final result](./provability_gate_result.json)
- [Structured fairness-key review](./temporal-fairness-key-structured-review.md)
- [Public verifier](../../src/bounded_working_memory_benchmark/verifier.py)

# Benchmark A: Structural Transfer

This directory contains the versioned specification, artifacts, schemas,
fixtures, and development record for Benchmark A: Structural Transfer.

The benchmark was initially developed to evaluate Protama. Protama is the
first evaluated system in this release; the benchmark is intended to remain
usable for future systems and future benchmark versions.

## Contents

- [`../../docs/gates/Protama_Inductive_Structural_Invention_Test.md`](../../docs/gates/Protama_Inductive_Structural_Invention_Test.md)
  — benchmark specification;
- `Protama_Structural_Gate_Publication_Task_List.md` — development and
  publication record;
- `artifacts/` — frozen manifests, runs, reports, and audit records;
- `fixtures/` — schema and leakage fixtures;
- `gate-work/` — design, implementation, and reproduction record;
- `schemas/` — machine-readable artifact contracts.

The public generator, manifest fingerprinting, and scorer live in
[`src/structural_transfer_benchmark/`](../../src/structural_transfer_benchmark/).
The canonical configuration snapshots remain in the repository-level
[`configs/`](../../configs/) directory.

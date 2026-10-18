# Benchmark

This directory will contain the public Protama benchmark specifications,
episode generators, near-miss definitions, scoring code, leakage checks, and
replay tooling.

The primary benchmark is the **Protama Structural Induction and Transfer
Gate**. The current public specification is
[`Protama_Inductive_Structural_Invention_Test.md`](Protama_Inductive_Structural_Invention_Test.md).

The public generator and scorer are released under
[`../src/protama_benchmark/`](../src/protama_benchmark/). They are the
evaluation instrument, not Protama's private runtime or learned state.

Install the source package from the repository root with:

```text
python -m pip install .
```

The public harness can generate deterministic episodes and score an adapter
run through the `protama_benchmark.structural` API. The completed gate's
frozen artifacts remain the historical evaluation record; a future gate can
use a new version and separate held-out material.

The current implementation boundary is summarized in the
[structural-family development report](../reports/development/2026-10-15-structural-family-progress.md).

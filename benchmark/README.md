# Benchmark

This directory contains public benchmark specifications,
episode generators, near-miss definitions, scoring code, leakage checks, and
replay tooling.

## Benchmark A: Structural Transfer

The primary benchmark is **Benchmark A: Structural Transfer**, initially
developed to evaluate Protama. Its current public specification is
[`Protama_Inductive_Structural_Invention_Test.md`](structural-transfer-v1/Protama_Inductive_Structural_Invention_Test.md).

The public generator, manifest fingerprinting, and scorer are released under
[`../src/structural_transfer_benchmark/`](../src/structural_transfer_benchmark/).
They are the evaluation instrument, not Protama's private runtime or learned
state.

Create a virtual environment and install the source package from the
repository root with:

```text
python -m venv .venv
.venv\Scripts\activate
python -m pip install .
```

On Debian or Ubuntu, use the equivalent `.venv/bin/activate` path. A virtual
environment avoids the PEP 668 externally-managed-environment restriction.

The public harness can generate deterministic episodes and score an adapter
run through the `structural_transfer_benchmark.structural` API. The completed
Structural Gate's
frozen artifacts remain the historical evaluation record; a future gate can
use a new version and separate held-out material. Benchmark A's current
held-out split is disjoint by episode and seed, but remains within its declared
generator and topology distribution; it is not an external-family test.

The current implementation boundary is summarized in the
[structural-family development report](../reports/development/2026-10-15-structural-family-progress.md).

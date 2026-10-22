# Benchmark

This directory contains public benchmark specifications, frozen inputs,
machine-readable results, and verification tooling.

## Bounded Working Memory and Thought Holdover

The public proof package is in
[`bounded-working-memory/`](./bounded-working-memory/). It contains the
materialized cases, the hashed freeze manifest, and the final provability
result. Verify it with the dependency-free
`bounded_working_memory_benchmark.verify_provability_gate` function.

The package proves an evidence property: under the bounded temporal protocol,
Protama's retained state and decisions are replayable, provenance-preserving,
and distinguishable from evaluator leakage or degenerate always-abstain
behavior. It does not claim general intelligence or universal correctness.

## Structural Transfer

The primary structural benchmark remains in
[`structural-transfer-v1/`](./structural-transfer-v1/). Its public generator,
manifest fingerprinting, and scorer are released under
[`../src/structural_transfer_benchmark/`](../src/structural_transfer_benchmark/).

## Autonomous Dictionary

The dictionary benchmark remains in
[`autonomous-dictionary-v1/`](./autonomous-dictionary-v1/).

# Autonomous Dictionary Learning v1

This directory contains the tracked benchmark artifacts for the dictionary
capacity experiment described in
[`2026-10-18-dictionary-scale-and-sparse-gpu-execution.md`](../../paper/2026-10-18-dictionary-scale-and-sparse-gpu-execution.md).

Artifacts belong under [`artifacts/`](artifacts/). This experiment is separate
from the completed [`structural-transfer-v1/`](../structural-transfer-v1/)
benchmark; its runs must not write into that published directory.

Each run has its own UTC timestamp and lookup-cap directory. A run directory
contains the full pilot trace and its benchmark report so redundant runs can
be removed without affecting other runs.

## Published artifacts

The published set is intentionally curated rather than a dump of every
exploratory run:

* the [A-200 autonomous pilot](artifacts/20261018T165732Z-lookups-200-A/);
* the trained 200-, 1,000-, 5,000-, 10,000-, and 20,000-entry scaling points;
* the trained full-`S` measurement;
* the original full-dictionary GPU baseline;
* the final full-dictionary sparse-streaming measurement.

The intermediate batch-scoring sweeps, duplicate tuning runs, untrained
measurements, and failed prototypes are intentionally not retained as
published benchmark artifacts. The paper records the methodological arc and
links the canonical results.
# Configurations

This directory is the canonical source for configurations consumed by the
private Protama evaluation tools. Do not maintain a second authoritative copy
under `benchmark/`.

Configurations are versioned snapshots:

- [`structural_gate_v1.json`](./structural_gate_v1.json) defines the locked
  Structural Gate thresholds and required evaluation settings.
- [`dictionary_family_review_v1.json`](./dictionary_family_review_v1.json) is
  a development review snapshot and remains subject to human validation.

Once a configuration version is used for a published result, it must not be
edited in place. Substantive changes require a new version, such as `v2`.
Development configurations may change before publication, but those changes
must be deliberate because the tools read these files directly.

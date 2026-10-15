# Protama

GPU-first synthetic intelligence architecture with a CPU reference runtime,
evidence-grounded cognition, structural learning, and reproducible benchmarks
for transfer, uncertainty, and explanation fidelity.

## Project status

Protama is an active research and engineering project. The public repository
is being assembled incrementally from the private development workspace.

Current public focus:

- structural induction and transfer;
- typed evidence and decision traces;
- near-miss discrimination;
- CPU reference behavior;
- GPU-oriented execution targets;
- reproducible benchmark design.

The project does not currently claim to prove general intelligence. Public
results will be labeled as development, pilot, or final benchmark results.

## Repository structure

```text
benchmark/   Benchmark specifications, generators, scoring, and evaluation artifacts
docs/        Public architecture and design documentation
paper/       Preprints, drafts, and publication material
reports/     Reproducible evaluation reports
results/     Published or reviewable benchmark results
tests/       Public benchmark and regression tests
configs/     Reproducible evaluation configurations
```

The repository is intentionally docs-first while the public release boundary
is being established. Private implementation code is not copied here
automatically.

## Core benchmark

The primary public evaluation is the **Protama Structural Induction and
Transfer Gate**. It evaluates whether a system can:

1. infer a reusable latent relational structure from limited examples;
2. transfer that structure to novel vocabulary and surface forms;
3. reject structurally defined near-misses;
4. abstain when evidence is insufficient or ambiguous;
5. produce explanations reconstructible from pre-decision evidence.

The benchmark specification will be added under
[`benchmark/`](benchmark/) when the first public benchmark artifact is
approved for release.

## Development model

Protama is developed privately with Perforce and published selectively through
versioned GitHub releases. The public repository is the source for released
documentation, benchmark artifacts, reproducible reports, and code explicitly
approved for publication.

## Contributing

Early contributions should focus on documentation, benchmark design, tests,
reproducibility, and reviewable research artifacts. Do not submit private
source, credentials, generated build output, or third-party code without
confirmed redistribution rights.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the public contribution policy.

## License

Protama-owned source code is intended to be released under the Apache License
2.0. Documentation and benchmark specifications may use a separate
documentation license in a future release. Preserve the original licenses of
third-party code and data.

See [`LICENSE`](LICENSE) for the current repository license.

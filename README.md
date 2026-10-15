# Protama

Protama is a synthetic intelligence architecture designed to run anywhere,
from low-power CPU devices to high-throughput GPU systems, built to learn,
transfer, and revise structure, not merely predict the next token.

We make no official claim to general intelligence, yet. That is, in fact,
<u>the goal</u>.

It is being built to acquire reusable relational structure from limited
examples, apply that structure to unfamiliar vocabulary and situations, reject
typed near-misses, and explain decisions from inspectable evidence.

Where statistical language models often rely on scale, surface similarity, or
memorized patterns, Protama explores explicit hypotheses, structural
revision, uncertainty, and abstention. The goal is not to make a more fluent
chatbot. The goal is to investigate whether an intelligence can learn
relationships that remain useful when the words and circumstances change.

This repository contains the public Protama research artifacts and the
**Protama Structural Induction and Transfer Gate**: a benchmark designed to
evaluate structural generalization rather than memorization.

[Read the Protama vision](VISION.md) to learn what the project is becoming,
what it explicitly does not claim, and how its research roadmap is organized.
Read the [official Protama etymology](ETYMOLOGY.md) for the name's
pronunciation, meaning, and usage.
See [Use Cases](USE_CASES.md) for potential application areas and the evidence
required before making deployment claims.
See [Safety and Governance](SAFETY_AND_GOVERNANCE.md) for the project's
human-inspection, external-review, training-control, and guardrail principles.

## What Protama is trying to achieve

Protama is an active research and engineering project. The public repository
is being assembled incrementally from the private development workspace.

The project is working toward systems that can:

- induce and transfer structure;
- form and revise reusable relational hypotheses;
- distinguish structural validity from surface resemblance;
- preserve uncertainty when evidence is incomplete;
- produce trace-grounded explanations;
- operate across CPU reference and GPU-oriented execution paths.

The project does not currently claim to prove general intelligence. Public
results will be labeled as development, pilot, or final benchmark results.

## Repository structure

```text
benchmark/   Benchmark specifications, generators, scoring, and evaluation artifacts
docs/        Public architecture, design, and roadmap documentation
paper/       Preprints, drafts, and publication material
reports/     Reproducible evaluation and development reports
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

Read the [benchmark specification](benchmark/Protama_Inductive_Structural_Invention_Test.md)
for the formal task, controls, metrics, and claim boundaries.

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

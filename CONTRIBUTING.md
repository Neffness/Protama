# Contributing to Protama

Thank you for helping improve the public Protama project.

## Current contribution scope

The repository is currently being assembled as a docs-first public project.
Useful early contributions include:

- benchmark design review;
- reproducibility improvements;
- documentation;
- test fixtures and evaluation tooling;
- failure analysis;
- code that is explicitly approved for public release.

## Public-release boundary

The primary development workspace is private. Unreal Engine was used as an
R&D platform during earlier Protama development. Protama's ongoing
implementation work continues in Python, and this repository does not publish
Unreal Engine source, engine files, or proprietary assets.

Do not copy or submit private implementation files, credentials, generated
output, proprietary data, or third-party code unless redistribution rights
have been verified.

## Pull requests

Please describe:

- what changed;
- why it changed;
- how it was validated;
- which benchmark or design requirement it addresses;
- whether the change affects public claims or reproducibility.

Benchmark changes should include tests or a clear explanation of why tests are
not applicable. Changes to scoring, generators, thresholds, or leakage rules
must be called out explicitly.

## Running public tests

With the repository's `src` directory on `PYTHONPATH`, run the public suite
with:

```text
PYTHONPATH=src python -m pytest -q tests
```

The bounded-working-memory checks are also implemented with `unittest.TestCase`
and can be run by standard-library discovery:

```text
PYTHONPATH=src python -m unittest discover -s tests -p "test_public_bounded_working_memory_benchmark.py"
```

Both commands execute the freeze-integrity hash guard.

## Research conduct

Development results must be labeled as development or pilot results until the
benchmark configuration, scoring rules, and final test controls are locked.
Do not report a local experiment as evidence that the full benchmark gate has
passed.

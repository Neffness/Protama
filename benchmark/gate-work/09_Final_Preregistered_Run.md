# Gate Work 09 — Final Preregistered Run

## Active artifacts

The active protocol is
[structural-gate-preregistration-v2.json](../artifacts/structural-gate-preregistration-v2.json).
The held-out evaluation artifacts are:

- [structural-gate-heldout-manifest-v1.json](../artifacts/structural-gate-heldout-manifest-v1.json)
- [structural-gate-heldout-adapter-run-v2.json](../artifacts/structural-gate-heldout-adapter-run-v2.json)
- [structural-gate-heldout-baseline-suite-v2.json](../artifacts/structural-gate-heldout-baseline-suite-v2.json)
- [structural-gate-heldout-report-v2.json](../artifacts/structural-gate-heldout-report-v2.json)
- [structural-gate-heldout-report-v2.txt](../artifacts/structural-gate-heldout-report-v2.txt)
- [structural-gate-publication-evidence-v1.json](../artifacts/structural-gate-publication-evidence-v1.json)
- [structural-gate-heldout-review-v1.json](../artifacts/structural-gate-heldout-review-v1.json)

## Reproduction

From `D:\Projects\NeffAI`, using the project Python environment:

```powershell
$env:PYTHONPATH = "D:\Projects\NeffAI"
& "D:\Projects\NeffAI\.venv-protama-gpu\Scripts\python.exe" -m pytest -q "D:\Projects\NeffAI\Protama_Private\Protama\tests\test_structural_gate_*.py"
```

The held-out manifest is rebuilt from the preregistered generator and
topology seed lists, then identity-checked by the adapter before predictions
are emitted. The baseline suite and scorer consume that same manifest. The
published artifacts must remain byte-equivalent to clean-environment replay.

## Current completion boundary

The primary Structural Gate passes the preregistered L2-L5 rule and has
passed a read-only artifact audit. Supplementary publication evidence covers
accuracy-at-coverage, snapshot round-trip fidelity, pre/post episode deltas,
retention, backward transfer, interference, operation counts, trace counts,
and wall-clock time. The CPU adapter has no association/transition-memory
subsystem, so that ablation is explicitly not applicable. GPU parity is
excluded from the current claim.

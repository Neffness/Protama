# Protama Structural Gate Publication Task List

This is the execution checklist for producing a publishable Structural
Induction and Transfer Gate result. It is derived from
`Protama_Inductive_Structural_Invention_Test.md`.

The preregistered held-out Structural Gate evaluation now passes its declared
L2-L5 rule. The publication package is still incomplete because snapshot
round-trip, retention/interference, substrate parity, resource accounting,
and some reproduction materials remain outstanding.

## Publication claim we are working toward

> On a preregistered benchmark of independently generated relational
> families, Protama induces reusable structural hypotheses from limited
> examples, transfers them to novel vocabulary and surface forms, rejects
> typed near-misses, abstains under insufficient evidence, and produces
> explanations reconstructible from its pre-decision evidence trace, while
> outperforming non-structural baselines under the published leakage and
> ablation controls.

The final claim must be narrowed if any required evidence is missing.

Checklist notation: `[x] Development ...` means the implementation and
development tests exist. It does not mean the final locked benchmark package
or gate criterion is complete. Unqualified `[x]` items are reserved for
publication-ready evidence.

## Required publication package

- [x] Versioned benchmark specification and pass-rule version.
- [x] Locked development and final-test generators.
- [x] Held-out final seed allocation preregistered before final generation.
- [x] Episode schema and serialization format.
- [x] Generator seeds and configuration hash.
- [x] CPU Protama adapter.
- [x] GPU adapter explicitly excluded from the current claim.
- [x] Exact-match, keyword, nearest-neighbor, and symbolic-oracle baselines.
- [x] Language-model baseline not applicable to the current structured-input claim.
- [x] Structural and lexical ablation implementations.
- [x] Leakage-check report.
- [x] Machine-readable raw predictions and traces.
- [x] Machine-readable metric report with confidence intervals.
- [x] Human-readable held-out report.
- [x] Deterministic replay command and replay artifacts.
- [x] Failure, abstention, and excluded-episode accounting.
- [x] Pre/post episode delta report relative to declared snapshots.
- [x] Conditional delta eligibility and eligible-episode count report
      (supplementary; not part of the primary L2-L5 pass rule).
- [x] Snapshot round-trip behavioral fidelity report.
- [x] Retention, backward-transfer, and interference report.
- [x] Clean-environment reproduction instructions.

## Gate levels and claim boundary

- [x] **L2:** induce a latent relation/family from limited examples.
- [x] **L3:** transfer to vocabulary and surface forms absent from training.
- [x] **L4:** reject typed structural near-misses by category.
- [x] **L5:** generalize to unseen combinations of known components.
- [x] Explanation evidence is reconstructed from pre-decision state.
- [x] L6/L7 independent invention and interactive refinement remain separate
      extensions and are not implied by an L2-L5 result.

## Work plan

### Phase A â€” lock the benchmark contract

- [x] Define the episode schema:
      hidden family, train examples, held-out positives, negatives,
      near-misses, ambiguous cases, traces, and scores.
- [x] Define the formal family representation independently of the renderer.
- [x] Define lexical, structural, template, family, generator, and temporal
      split rules.
- [x] Define every near-miss category:
      role reversal, relation reversal, type violation, omission,
      single-feature mismatch, surface decoy, lexical overlap, novel
      negative, ambiguity, and contradiction.
- [x] Select the pass-rule version before final evaluation.
- [x] Set and record thresholds for positive accuracy, negative accuracy,
      near-miss accuracy, novel transfer, explanation fidelity, coverage,
      and selective risk.
- [x] Define episode-level confidence-interval methodology.

**Exit artifact:** locked configuration plus a versioned pass-rule document.

### Phase B â€” build the independent episode generator

- [x] Generate at least 100 independently seeded family episodes, subject to
      power analysis.
- [x] Generate disjoint training and evaluation vocabularies.
- [x] Generate unseen structural combinations for L5.
- [x] Generate at least one unseen evaluation template per applicable episode.
- [x] Generate typed near-misses from the latent family, not hand-written
      labels after the fact.
- [x] Generate genuine ambiguity and contradiction cases.
- [x] Serialize the latent family only in evaluator-side gold artifacts.
- [x] Add generator replay tests: same seed and config produce identical
      episodes.
- [x] Add leakage tests proving evaluation vocabulary, templates, and family
      structures do not enter training.

**Exit artifact:** generator package, seed manifest, leakage report, and
replayed episode fixtures.

### Phase C â€” implement the evaluation adapter

- [x] Train Protama only on `D_train`.
- [x] Prevent held-out labels and family names from entering the system.
- [x] Capture candidate hypotheses before each decision.
- [x] Capture selected, rejected, and abstained evidence.
- [x] Capture operation order and decision trace.
- [x] Capture the generated explanation request/result.
- [x] Capture final snapshot identity and all scored outputs.
- [x] Capture pre-episode probe, post-episode probe, and episode-level delta
      in the supplementary publication evidence artifact.
- [x] Keep pre-episode probes in a disjoint, unscored split that cannot
      adapt the system.
- [x] Verify snapshot save/restore behavioral equivalence before evaluation.
- [x] Re-run prior episode evaluation sets after later learning and report
      retention, backward transfer, forgetting, and interference.
- [x] Separate clean evaluation from interactive adaptation.

**Exit artifact:** one adapter run can produce a complete replayable episode
artifact without evaluator-only data entering Protama.

### Phase D â€” implement scoring

- [x] Development positive transfer accuracy.
- [x] Development negative rejection accuracy.
- [x] Development near-miss accuracy by category.
- [x] Development novel-vocabulary transfer.
- [x] Development surface invariance.
- [x] Development compositional generalization.
- [x] Coverage and selective-risk metrics in the held-out report.
- [x] Accuracy-at-coverage curve.
- [x] Development false-commitment rate.
- [x] Development abstention precision.
- [x] Development risk-coverage curve.
- [x] Development explanation invariant correctness.
- [x] Development explanation irrelevance recognition.
- [x] Development explanation counterfactual sensitivity.
- [x] Development explanation trace fidelity.
- [x] Development episode-bootstrap confidence intervals.
- [x] Development excluded-episode accounting with explicit reasons.

**Exit artifact:** scorer produces both machine-readable JSON and a
human-readable report from raw episode artifacts.

The development package is frozen, and the held-out seed allocation is now
preregistered separately in
`benchmark/structural-transfer-v1/artifacts/structural-gate-preregistration-v2.json`. Version 2
supersedes version 1 because the scorer audit expanded the category report to
include the generated ambiguity and contradiction cases. The final allocation
uses generator seeds `1000..1049` and topology seeds `2000..2024` for each
topology, keeping it disjoint from the frozen development allocation.

### Phase E â€” run baselines and ablations

- [x] Development exact-match baseline.
- [x] Development keyword baseline.
- [x] Development nearest-neighbor baseline.
- [x] Development symbolic oracle upper bound.
- [x] CPU Protama.
- [x] GPU Protama excluded from the current claim.
- [x] Language-model baseline not applicable to the current structured-input claim.
- [x] Development remove evidence provenance.
- [x] Development remove near-miss exposure (generator limitation).
- [x] Development remove abstention.
- [x] Development remove structural memory.
- [x] Association/transition memory ablation assessed as not applicable to
      the stateless per-episode CPU structural adapter.
- [x] Development remove explanation constraints.
- [x] Development no-novelty-tracking control (adapter limitation).
- [x] Development remove external evidence providers (adapter limitation).
- [x] Development replace structural induction with keyword matching.

**Exit artifact:** baseline/ablation matrix showing which capability changes
move each metric, especially lexical-identity ablation.

### Phase F â€” validate CPU/GPU and replay parity

- [x] GPU parity is explicitly out of scope for the current claim.
- [x] CPU replay decisions, statuses, evidence, and explanations are
      covered by the clean replay and snapshot evidence reports.
- [x] Snapshot comparison is covered by the CPU round-trip report.
- [x] Numerical tolerances are not applicable to the exact CPU symbolic path.
- [x] Verify deterministic replay from clean artifacts.
- [x] Record wall-clock, peak traced memory, operation, trace, and snapshot
      metrics.

**Exit artifact:** parity report and deterministic replay report.

### Phase G â€” final preregistered evaluation

- [x] Freeze generator, scorer, pass-rule, adapter, and baseline protocol.
- [x] Freeze final seeds and configuration hash.
- [x] Run the final generator without tuning against results.
- [x] Do not inspect or use held-out labels before scoring is complete.
- [x] Report episode-level induction deltas separately from post-state scores.
- [x] Include snapshot round-trip and prior-episode retention results.
- [x] Record threshold provenance and the explicit v1/v2 retention-gating
      decision.
- [x] Produce raw artifacts before aggregate metrics.
- [x] Produce confidence intervals and category-level failures.
- [x] Run leakage checks.
- [x] Run deterministic replay from the published artifacts.
- [x] Apply the preregistered pass rule exactly once.

**Exit artifact:** immutable final evaluation bundle.

### Additional benchmark â€” active dictionary learning boundary

This benchmark is a companion intelligence experiment, not a substitute for
the Structural Induction and Transfer Gate. It measures whether the learned
system can process a sequential dictionary curriculum, identify the first
definition pattern it cannot confidently reuse, ask a meaningful question,
learn from a correction, and move the boundary to a later, different pattern.

- [x] Run the complete curriculum before dictionary iteration.
- [x] Integrate the dictionary stages into the canonical `run_all` curriculum
      rather than relying on a separate experiment harness.
- [x] Halt on the first unresolved dictionary definition.
- [x] Preserve the stopped entry, reason, provisional observations, and
      question.
- [x] Apply a supervised correction through the canonical dictionary path.
- [x] Resume the dictionary run with the correction available for reuse.
- [x] Verify that the corrected run reaches a later boundary.
- [x] Verify that the later boundary is a different unresolved pattern, not
      repetition of the original failure.
- [x] Add a deterministic regression test for boundary movement.
- [x] Define a versioned dictionary benchmark subset and ordering.
- [ ] Record baseline boundary position without correction.
- [x] Record boundary movement across multiple sequential corrections.
- [ ] Measure boundary movement across multiple independent correction
      sequences.
- [x] Measure correction transfer to a held-out word sharing the same
      pattern.
- [x] Expand correction transfer to a held-out word set.
- [x] Use an independent word-disjoint correction/evaluation split for the
      held-out word set.
- [x] Repeat the split across multiple dictionary regions and correction
      seeds.
- [x] Scale the regional study to a versioned development word set and
      report deterministic bootstrap intervals.
- [x] Freeze a confirmatory development manifest with leakage checks,
      positive transfer, and negative controls.
- [ ] Preregister the regional word set before a publication-grade
      confirmatory run.
- [x] Inventory high-frequency candidate dictionary families.
- [x] Include all five initial candidate families in a human-review queue.
- [x] Review the 20-entry starter batch and finalize four initial relation
      schemas; machine-validate the obvious known-noun examples.
- [x] Preserve multi-sense dictionary entries by word, part of speech, and
      source line rather than collapsing headwords.
- [x] Run automated population validation and produce a bounded exception
      queue for human review.
- [x] Build deterministic family-specific positive, negative, and
      surface-variant pools with word-disjoint controls.
- [x] Freeze a larger five-family development manifest with a content
      fingerprint and leakage check.
- [x] Run the frozen development manifest without changing its cases and
      record positive transfer and negative rejection results.
- [x] Measure overgeneralization and false-commitment after correction.
- [x] Connect dictionary-derived structural decisions to a development gate
      adapter without allowing dictionary artifacts into final held-out
      episodes.

**Current development result:** the uncorrected run learned 41 entries and
stopped at `Abada` (entry 42). After a supervised noun-equivalence
correction, it learned 48 entries and stopped at `Abaist` (entry 49) on a
past-participle/state pattern.

**Exit artifact:** versioned active-dictionary benchmark specification,
baseline/correction boundary reports, transfer and overgeneralization
metrics, and a companion evidence document. This result informs the gate
work but does not count as a Structural Gate pass.

## Final report contents

The report we publish must contain:

1. Exact benchmark, generator, scorer, system, and configuration versions.
2. Episode and seed counts.
3. Initial and final snapshot identities.
4. Every primary metric and confidence interval.
5. Near-miss results by category.
6. Coverage, selective risk, and abstention behavior.
7. Explanation-fidelity breakdown.
8. Baseline and ablation comparisons.
9. CPU/GPU parity results, if claimed.
10. Leakage checks and excluded episodes.
11. Representative successes and failures.
12. Resource usage and replay results.
13. Exact pass-rule evaluation.
14. The highest capability level actually demonstrated.
15. Explicit non-claims about general intelligence and L6/L7.

## Current status

| Area | Status |
| --- | --- |
| Structured symbolic pilot | Superseded by held-out Structural Gate result |
| Locked independent generator | Complete with replay and leakage evidence |
| Held-out lexical/template isolation | Complete |
| Near-miss category generator | Complete; all ten categories reported |
| Full scorer and confidence intervals | Complete for held-out L2-L5 report |
| Baselines | Complete for declared CPU/structured controls |
| Ablations | Complete except association/transition-memory control |
| Explanation reconstruction | Complete for adapter trace criterion |
| Leakage report | Complete |
| CPU/GPU parity for this gate | CPU only; GPU excluded from claim |
| Final preregistered run | Complete; internal artifact audit passed |
| Publication package | Complete for the declared CPU L2-L5 claim; GPU and companion dictionary extensions remain out of scope |
| Structural Induction and Transfer Gate | **PASSED for the declared L2-L5 benchmark** |

## Checkpoint evidence documents

Each completed checkpoint gets one dedicated evidence document. The master
task list records scope and dependency; the checkpoint document records
decisions, implementation evidence, validation, and remaining limitations.

- [01 â€” Benchmark Contract](gate-work/01_Benchmark_Contract.md) â€” **contract artifacts drafted**
- [02 â€” Independent Episode Generator](gate-work/02_Independent_Episode_Generator.md) â€” **held-out package and audit complete**
- 03 â€” Evaluation Adapter â€” **implementation complete; snapshot/retention extensions remain**
- [04 â€” Gate Scorer](gate-work/04_Gate_Scorer.md) â€” **held-out scorer complete**
- [05 â€” Baselines and Ablations](gate-work/05_Baselines_and_Ablations.md) â€” **declared CPU/structured controls complete**
- [06 â€” Dictionary to Structural Integration](gate-work/06_Dictionary_Structural_Integration.md) â€” **development integration probe and active-boundary benchmark**
- [07 â€” Surface Relation Learning Experiment](gate-work/07_Surface_Relation_Learning_Experiment.md) â€” **integrated development experiment**
- 08 â€” Replay and Substrate Parity â€” **replay complete; GPU parity excluded**
- 09 â€” Final Preregistered Run â€” **complete; internal artifact audit passed**

## Immediate next implementation

Complete the remaining publication package: accuracy-at-coverage reporting,
snapshot round-trip fidelity, pre/post episode deltas, retention and
interference measurements, resource accounting, and clean-environment
reproduction instructions. Keep the active dictionary benchmark as a
companion measurement rather than treating it as a substitute for the
Structural Gate. Preserve the declared L2-L5 claim boundary.

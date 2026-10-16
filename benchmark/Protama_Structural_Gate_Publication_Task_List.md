# Protama Structural Gate Publication Task List

This is the execution checklist for producing a publishable Structural
Induction and Transfer Gate result. It is derived from
`Protama_Inductive_Structural_Invention_Test.md`.

The gate is **not passed**. The current structured pilot is development
evidence only: it demonstrates a narrow symbolic L2-L4 slice and does not
yet establish novel-language transfer, independent-family generalization,
explanation reconstruction, baseline superiority, or leakage control.

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

- [ ] Versioned benchmark specification and pass-rule version.
- [ ] Locked development and final-test generators.
- [ ] Episode schema and serialization format.
- [ ] Generator seeds and configuration hash.
- [ ] CPU Protama adapter.
- [ ] GPU Protama adapter or an explicit substrate-scope decision.
- [ ] Exact-match, keyword, nearest-neighbor, and symbolic-oracle baselines.
- [ ] Language-model baseline if natural-language processing is claimed.
- [ ] Structural and lexical ablation implementations.
- [ ] Leakage-check report.
- [ ] Machine-readable raw predictions and traces.
- [ ] Machine-readable metric report with confidence intervals.
- [ ] Human-readable final report.
- [ ] Deterministic replay command and replay artifacts.
- [ ] Failure, abstention, and excluded-episode manifest.
- [ ] Pre/post episode delta report relative to declared snapshots.
- [ ] Conditional delta pass criterion and eligible-episode count report.
- [ ] Snapshot round-trip behavioral fidelity report.
- [ ] Retention, backward-transfer, and interference report.
- [ ] Clean-environment reproduction instructions.

## Gate levels and claim boundary

- [ ] **L2:** induce a latent relation/family from limited examples.
- [ ] **L3:** transfer to vocabulary and surface forms absent from training.
- [ ] **L4:** reject typed structural near-misses by category.
- [ ] **L5:** generalize to unseen combinations of known components.
- [ ] Explanation evidence is reconstructed from pre-decision state.
- [ ] L6/L7 independent invention and interactive refinement remain separate
      extensions and are not implied by an L2-L5 result.

## Work plan

### Phase A — lock the benchmark contract

- [ ] Define the episode schema:
      hidden family, train examples, held-out positives, negatives,
      near-misses, ambiguous cases, traces, and scores.
- [ ] Define the formal family representation independently of the renderer.
- [ ] Define lexical, structural, template, family, generator, and temporal
      split rules.
- [ ] Define every near-miss category:
      role reversal, relation reversal, type violation, omission,
      single-feature mismatch, surface decoy, lexical overlap, novel
      negative, ambiguity, and contradiction.
- [ ] Select the pass-rule version before final evaluation.
- [ ] Set and record thresholds for positive accuracy, negative accuracy,
      near-miss accuracy, novel transfer, explanation fidelity, coverage,
      and selective risk.
- [ ] Define episode-level confidence-interval methodology.

**Exit artifact:** locked configuration plus a versioned pass-rule document.

### Phase B — build the independent episode generator

- [ ] Generate at least 100 independently seeded family episodes, subject to
      power analysis.
- [ ] Generate disjoint training and evaluation vocabularies.
- [ ] Generate unseen structural combinations for L5.
- [ ] Generate at least one unseen evaluation template per applicable episode.
- [ ] Generate typed near-misses from the latent family, not hand-written
      labels after the fact.
- [ ] Generate genuine ambiguity and contradiction cases.
- [ ] Serialize the latent family only in evaluator-side gold artifacts.
- [ ] Add generator replay tests: same seed and config produce identical
      episodes.
- [ ] Add leakage tests proving evaluation vocabulary, templates, and family
      structures do not enter training.

**Exit artifact:** generator package, seed manifest, leakage report, and
replayed episode fixtures.

### Phase C — implement the evaluation adapter

- [ ] Train Protama only on `D_train`.
- [ ] Prevent held-out labels and family names from entering the system.
- [ ] Capture candidate hypotheses before each decision.
- [ ] Capture selected, rejected, and abstained evidence.
- [ ] Capture operation order and decision trace.
- [ ] Capture the generated explanation request/result.
- [ ] Capture final snapshot identity and all scored outputs.
- [ ] Capture pre-episode probe, post-episode probe, and episode-level delta.
- [ ] Keep pre-episode probes in a disjoint, unscored split that cannot
      adapt the system.
- [ ] Verify snapshot save/restore behavioral equivalence before evaluation.
- [ ] Re-run prior episode evaluation sets after later learning and report
      retention, backward transfer, forgetting, and interference.
- [ ] Separate clean evaluation from interactive adaptation.

**Exit artifact:** one adapter run can produce a complete replayable episode
artifact without evaluator-only data entering Protama.

### Phase D — implement scoring

- [x] Development positive transfer accuracy.
- [x] Development negative rejection accuracy.
- [x] Development near-miss accuracy by category.
- [x] Development novel-vocabulary transfer.
- [x] Development surface invariance.
- [x] Development compositional generalization.
- [ ] Coverage and accuracy-at-coverage — final report integration pending.
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

### Phase E — run baselines and ablations

- [x] Development exact-match baseline.
- [x] Development keyword baseline.
- [x] Development nearest-neighbor baseline.
- [x] Development symbolic oracle upper bound.
- [ ] CPU Protama.
- [ ] GPU Protama, if included in the claim.
- [ ] Language-model baseline, if natural-language processing is included.
- [x] Development remove evidence provenance.
- [x] Development remove near-miss exposure (generator limitation).
- [x] Development remove abstention.
- [x] Development remove structural memory.
- [ ] Remove association/transition memory as applicable.
- [x] Development remove explanation constraints.
- [x] Development no-novelty-tracking control (adapter limitation).
- [x] Development remove external evidence providers (adapter limitation).
- [x] Development replace structural induction with keyword matching.

**Exit artifact:** baseline/ablation matrix showing which capability changes
move each metric, especially lexical-identity ablation.

### Phase F — validate CPU/GPU and replay parity

- [ ] Run the same episodes through CPU and GPU adapters.
- [ ] Compare decisions, statuses, evidence, and explanations.
- [ ] Compare snapshots where substrate parity is supported.
- [ ] Record allowed numerical tolerances.
- [ ] Verify deterministic replay from clean artifacts.
- [ ] Record wall-clock, memory, operation, trace, and snapshot metrics.

**Exit artifact:** parity report and deterministic replay report.

### Phase G — final preregistered evaluation

- [ ] Freeze generator, scorer, pass-rule, adapters, and baselines.
- [ ] Freeze final seeds and configuration hash.
- [ ] Run the final generator without tuning against results.
- [ ] Do not inspect or use held-out labels before scoring is complete.
- [ ] Report episode-level induction deltas separately from post-state scores.
- [ ] Include snapshot round-trip and prior-episode retention results.
- [ ] Record threshold provenance and the explicit v1/v2 retention-gating
      decision.
- [ ] Produce raw artifacts before aggregate metrics.
- [ ] Produce confidence intervals and category-level failures.
- [ ] Run leakage checks.
- [ ] Run deterministic replay from the published artifacts.
- [ ] Apply the preregistered pass rule exactly once.

**Exit artifact:** immutable final evaluation bundle.

### Additional benchmark — active dictionary learning boundary

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
| Structured symbolic pilot | Development evidence only |
| Locked independent generator | Not started |
| Held-out lexical/template isolation | Not started |
| Near-miss category generator | Not started |
| Full scorer and confidence intervals | Development implementation complete |
| Baselines | Exact-match development control in progress |
| Ablations | Development controls in progress |
| Explanation reconstruction | Not started |
| Leakage report | Not started |
| CPU/GPU parity for this gate | Not started |
| Final preregistered run | Blocked |
| Structural Induction and Transfer Gate | **NOT PASSED** |

## Checkpoint evidence documents

Each completed checkpoint gets one dedicated evidence document. The master
task list records scope and dependency; the checkpoint document records
decisions, implementation evidence, validation, and remaining limitations.

- [01 — Benchmark Contract](gate-work/01_Benchmark_Contract.md) — **contract artifacts drafted**
- [02 — Independent Episode Generator](gate-work/02_Independent_Episode_Generator.md) — **in progress**
- 03 — Evaluation Adapter — not started
- [04 — Gate Scorer](gate-work/04_Gate_Scorer.md) — **development scorer in progress**
- [05 — Baselines and Ablations](gate-work/05_Baselines_and_Ablations.md) — **exact-match development control in progress**
- [06 — Dictionary to Structural Integration](gate-work/06_Dictionary_Structural_Integration.md) — **development integration probe and active-boundary benchmark**
- [07 — Surface Relation Learning Experiment](gate-work/07_Surface_Relation_Learning_Experiment.md) — **integrated development experiment**
- 08 — Replay and Substrate Parity — not started
- 09 — Final Preregistered Run — not started

## Immediate next implementation

Continue the gate work from the locked-contract and independent-generator
phases. In parallel, keep the active dictionary benchmark as a companion
measurement: formalize its ordering and baseline, then test correction
transfer and overgeneralization. Treat gate artifacts as diagnostic
measurements, not as a replacement for learning experiments. Do not tune
Protama against final episodes until the generator, leakage checks, and
scoring contract are locked.

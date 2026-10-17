# The Locked Structural Gate Adapter

## Turning a certified episode boundary into auditable Protama traces

**Project:** Protama**Publication type:** Public research milestone**Date:** 2026-10-17**Status:** Adapter implemented and replay-certified; benchmark evaluation not yet run

> **Scope notice:** This publication describes the adapter that drives Protama from the locked Structural Gate episode package. It does not claim that Protama has passed the Structural Gate, and it does not report a final capability score.

## 1. Background: what the dictionary research loop is

The dictionary research loop is Protama's first bounded example of a learned system recognizing that it lacks information, selecting a tool, incorporating the result, and continuing a task. The dictionary is not the point of the capability. It is a controlled source with explicit word-definition relationships, references between entries, known and unknown terms, and repeatable lookup results.

In the interactive loop, Protama receives an ordinary natural-language request such as a question about an unfamiliar word. It does not receive a special formatted prompt containing hard coded values such as a`"word-problem:"` prefix or a command that directly names the lookup function. 

Protama's runtime:

1. interprets the request and identifies the task;
2. checks whether the task depends on unresolved knowledge;
3. recognizes that a dictionary lookup is a suitable learned operation;
4. selects the dictionary source and target;
5. requests the lookup through the protocol boundary;
6. observes the returned definition, source, and evidence;
7. updates the task with that evidence; and
8. answers, asks for clarification, or honestly blocks if the lookup cannot
   resolve the dependency.

The loop can be represented as:

```text
natural-language request
    -> task interpretation
    -> unresolved dependency
    -> learned research decision
    -> dictionary action
    -> returned evidence
    -> task update
    -> answer, clarification, or honest blockage
```

ProtamaUI exposes this process through separate internal-thought, protocol log, action, and external-output views. Its checkpoint system can preserve the active task, evidence, pending action, and supervised sequence boundary. The UI may externally submit the next case in a supervised batch, but that is different from forcing a `word-problem:` operator into the user's prompt: within each case, Protama must interpret the request, choose the learned operation, and correlate the returned evidence.

This loop is a **runtime capability demonstration**. It tests whether Protama can recognize and investigate a missing dictionary dependency. It is not the Structural Gate, and its dictionary entries are not the hidden evaluation families used by the benchmark described here.

## 2. The milestone

The independent episode generator established a locked, leakage-checked evaluation boundary. The next problem was operational:

> How can those episodes reach Protama without allowing evaluator-only labels, hidden family structure, or near-miss annotations to cross the system boundary?

This milestone implements that boundary as a replayable evaluation adapter. The adapter consumes the machine-readable locked manifest, reconstructs each episode from its recorded seed configuration, verifies the episode identity, projects only system-visible observations into the adapter, and records a complete prediction and reasoning trace for every held-out case.

The adapter is therefore not a new learning algorithm. It is the controlled measurement surface between:

```text
locked evaluator package
    -> seed and fingerprint validation
    -> permitted system-visible projection
    -> structural induction and application
    -> predictions and traces
    -> later evaluator-side scoring
```

The generator and adapter remain separate from Protama's interactive dictionary research loop. The dictionary loop demonstrates a runtime capability; this adapter establishes a fair way to measure structural learning.

## 3. Why a separate adapter is necessary

An evaluation can be invalid even when its generator is deterministic. If the system receives `family_gold`, expected statuses, near-miss categories, or other evaluator annotations, it can appear to generalize while actually using the answer key.

The adapter enforces a projection boundary:

- training cases contain only relation observations;
- evaluation cases contain only relation observations;
- evaluator-only family structure is removed;
- expected statuses are removed;
- near-miss categories are removed;
- rendering and scoring metadata remain outside Protama's input path.

The adapter can run directly from an in-memory development episode for unit tests, but the locked-run entry point requires a manifest file. Before any episode is executed, it reconstructs the episode and compares its episode IDs and content fingerprints with the manifest. A changed generator, altered seed list, or modified artifact fails closed instead of silently producing a different benchmark.

## 4. Locked evaluation boundary

The final seed package contains 100 episodes:

- 50 canonical hidden-family episodes;
- 25 one-relation equivalence-topology episodes; and
- 25 two-relation purpose-topology episodes.

The locked manifest is:

[structural-gate-final-manifest-v1.json](../benchmark/artifacts/structural-gate-final-manifest-v1.json)

Its content fingerprint is:

```text
e3767bc9995aa1b531886deaa82e612ff2e1fa4343fe779e39fc5193059096ce
```

The manifest records:

- the manifest version;
- the canonical generator seeds;
- the topology and topology seeds;
- episode IDs;
- episode content fingerprints; and
- fail-closed leakage reports.

It does not serialize evaluator-only `family_gold`. The manifest is an evaluation boundary, not a replacement for the generator source or a claim that all possible structural families have been covered.

## 5. Adapter contract

The adapter exposes two levels of output.

### Episode-level output

Each episode run contains:

- the episode identifier;
- the induced variable-bound family snapshot;
- one prediction per held-out case;
- one trace per held-out case;
- an initial snapshot identity; and
- a final snapshot identity.

### Prediction records

Each prediction contains:

- schema version;
- episode ID;
- case ID;
- predicted status;
- selected family ID when the decision is accepted;
- confidence;
- abstention state; and
- a trace ID linking the prediction to its evidence.

### Trace records

Each trace contains:

- candidate hypotheses;
- selected evidence;
- rejected evidence;
- operation sequence;
- invariant explanations;
- counterfactual or rejected features; and
- uncertainty state.

The trace is intended to make a later score auditable. A score should not only say that a case was accepted or rejected; it should allow reviewers to inspect what structural evidence produced that decision.

## 6. Replay and failure behavior

The locked entry point is `run_locked_manifest(path)` in [structural_gate_adapter.py](../../Protama_Private/Protama/benchmarks/structural/structural_gate_adapter.py). 

It performs these checks before execution:

1. the manifest is a JSON object;
2. the manifest version is supported;
3. generator and topology seed lists are present;
4. episode identity lists are present;
5. reconstructed IDs match the locked IDs; and
6. reconstructed content fingerprints match the locked fingerprints.

Any mismatch raises an explicit error. The adapter does not substitute a fresh seed, accept a partial manifest, or continue with a success-shaped fallback.

The serialized adapter run is:

[structural-gate-final-adapter-run-v1.json](../benchmark/artifacts/structural-gate-final-adapter-run-v1.json)

It is deterministic and contains no evaluator-only family gold.

## 7. Demonstrated result

The locked adapter run produced:

```text
episodes: 100
prediction/trace pairs: 1,150
adapter replay: byte-equivalent
```

The adapter artifact SHA-256 is:

```text
349be02f09b5bee7b22d39a8f15faf55f78cb35fbdb052955f1ee7df8b8db5ca
```

The implementation is covered by the structural benchmark suite. The
post-adapter validation result was:

```text
54 tests passed
```

The adapter tests specifically verify:

- one prediction and trace for every held-out case;
- deterministic episode replay;
- abstention without evaluator labels;
- permitted-input projection;
- serialized permitted-input replay; and
- complete locked-manifest execution.

These results certify the measurement plumbing. They do not certify Protama's structural-learning performance.

## 8. What this milestone does not establish

This milestone does not establish:

- that Protama learned the hidden families;
- that Protama generalizes to arbitrary natural language;
- that the adapter's predictions are accurate;
- that the topology slices represent all relevant structural tasks;
- that the baseline or ablation comparisons are favorable;
- that the locked package is sufficient for a final publication claim; or
- that the Structural Gate has been passed.

The adapter currently applies the structural induction implementation directly through the benchmark interface. It is an evaluation adapter, not yet the complete end-to-end ProtamaUI path. That distinction must remain explicit: runtime observability and benchmark integrity are related but separate claims.

## 9. Next work

The next milestone is the baseline and ablation suite. Every comparison must consume the same locked manifest and use the same evaluator-side scoring rules. Planned controls include:

1. exact-match behavior;
2. keyword routing;
3. nearest-neighbor similarity;
4. no structural memory;
5. no abstention;
6. no evidence provenance;
7. no explanation constraints;
8. no novelty tracking;
9. no near-miss exposure; and
10. no external-evidence control.

After those controls, the project still needs:

- a development-scale benchmark report;
- clean-environment replay;
- preregistration and final freeze;
- evaluator-side scoring review; and
- a final Structural Gate run.

Only after those stages can the project make a result claim about Protama's structural learning. The current claim is narrower and reproducible:

> Protama now has a locked, replay-validated adapter that can consume
> independent episodes, withhold evaluator-only structure, and emit complete
> auditable traces.

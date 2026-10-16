# The Next Big Milestone: Protama's Independent Episode Generator

## Building a trustworthy measurement system for structural learning

**Project:** Protama  
**Publication type:** Public research milestone  
**Date:** 2026-10-16  
**Status:** Development generator exists; final certification remains in progress

> **Scope notice:** This publication describes the benchmark machinery needed
> to evaluate Protama fairly. It does not claim that the Structural Induction
> and Transfer Gate has been passed.

## 1. The milestone

Protama's next major milestone is:

> **A replayable, leakage-checked generator that creates hidden-family
> evaluation episodes independently of the dictionary fixtures.**

The first gold gate established a narrow result using reviewed
dictionary-definition families. That result was useful because it tested
transfer beyond exact sentence replay, but its cases were still bounded by
reviewed schemas and manually assembled controls. The next step is to make
the evaluation itself independent.

This is the transition from:

- reviewed benchmark examples;
- dictionary-derived family pools;
- hand-constructed positive and negative controls; and
- provisional regional diagnostics

to:

- independently generated structural-learning episodes;
- evaluator-only latent families;
- replayable training and evaluation splits; and
- machine-checked leakage and near-miss controls.

The purpose is not to make the benchmark larger for its own sake. The
purpose is to establish that the measurement process can produce a fair,
repeatable test before asking Protama to pass it.

## 2. Why this comes next

Without an independent episode generator, a larger evaluation risks becoming
another collection of hand-selected examples. That would repeat the central
limitation exposed by the provisional D/E/F controls: strong positive
transfer can coexist with incomplete negative calibration, and manually
selected cases cannot by themselves establish how broadly the result
generalizes.

An independent generator changes the evidentiary relationship:

```text
reviewed examples
    -> development evidence

independent hidden-family episodes
    -> fair structural-learning measurement
```

The generator therefore becomes part of the scientific instrument. Its
determinism, split isolation, evaluator-only labels, and failure behavior
must be tested before the resulting system scores can support a broader
capability claim.

The milestone establishes the following principle:

> **The evaluation must be trustworthy before we ask Protama to pass it.**

## 3. What an episode must contain

Each generated episode must contain, or reference through a versioned
machine-readable artifact:

- a hidden structural family known only to the evaluator;
- a small training set shown to Protama;
- held-out positive examples;
- held-out negative examples;
- typed structural near-misses;
- ambiguous cases;
- contradictory cases;
- vocabulary not used in training;
- surface templates not used in training; and
- a deterministic seed and configuration identity.

The episode may expose the permitted training examples and evaluation inputs
to Protama, but it must not expose the expected family labels or latent
structure before scoring. The evaluator retains the gold family, expected
outcomes, split metadata, and leakage evidence until the decision artifacts
are complete.

The episode schema must also preserve enough identity to replay and audit
the result:

```text
episode version
episode seed
generator version
configuration identity
latent family identity
training examples
evaluation examples
case categories
expected outcomes
permitted evidence declaration
```

The latent family and expected labels belong in evaluator-side artifacts.
They must not be serialized into Protama's permitted input stream.

## 4. Required isolation controls

The generator must enforce independence at more than one level.

### Vocabulary isolation

Training and evaluation vocabularies must be disjoint. A held-out positive
must not become a disguised lexical recall test, and a negative control must
not be identifiable solely because its words never appeared anywhere in the
episode.

### Structural isolation

Evaluation structures must be absent from training except where the declared
benchmark level explicitly permits component reuse for compositional
evaluation. The generator must record that distinction rather than relying
on a later interpretation of the examples.

### Template isolation

Evaluation templates must be held out from training. A system should be
tested on whether it can preserve the learned relation under a new surface
form, not whether it can recognize a renderer template.

### Label isolation

The hidden family, expected outcomes, and evaluator-only annotations must
remain outside Protama's input path until scoring. The generator and adapter
must fail closed if a forbidden field is about to cross that boundary.

### Seed and configuration identity

Every episode must identify the seed, generator version, and configuration
identity used to create it. A result without those identities is not
replayable evidence.

## 5. Near-miss taxonomy

The generator must produce near-misses from the latent structure rather than
manually assigning labels after rendering. The initial contract requires all
ten categories:

1. role reversal;
2. relation reversal;
3. type violation;
4. required relation or argument omission;
5. single-feature mismatch;
6. surface decoy;
7. lexical overlap with invalid structure;
8. novel negative;
9. ambiguity; and
10. contradiction.

This taxonomy matters because a single aggregate negative score can conceal
specific weaknesses. A system might reject obvious type violations while
accepting relation reversals, or it might commit to an answer in ambiguous
cases instead of abstaining. Each category must therefore be independently
generated, counted, and reported.

## 6. Milestone acceptance criteria

The independent episode generator is complete only when all of the following
conditions are demonstrated:

1. The generator is deterministic: the same seed and configuration produce
   byte-equivalent episode artifacts.
2. Training and evaluation vocabularies are disjoint.
3. The hidden family is not exposed to Protama.
4. Evaluation templates are held out from training.
5. Near-misses are generated from the latent structure rather than manually
   labelled after the fact.
6. Leakage checks fail closed and emit a machine-readable report.
7. A replay test reconstructs the same episode and score inputs.
8. An initial development batch of at least 100 episodes can be generated
   with a machine-readable manifest.
9. The generator produces the complete ten-category near-miss taxonomy.

These are milestone conditions, not optional quality improvements. A
generator that produces episodes but cannot prove isolation or replayability
does not yet provide a trustworthy evaluation instrument.

## 7. Current development status

The development generator now exists in
`Tools/Protama/structural_gate_generator.py`. The public benchmark artifacts
record the following development evidence:

- a versioned episode schema;
- a valid development fixture;
- an intentionally leaky fixture;
- fixture leakage tests;
- hidden-family episode generation;
- deterministic replay tests;
- split-isolation checks;
- a versioned machine-readable leakage report;
- near-miss category coverage tests; and
- a 100-episode replay and leakage test.

The current development validation reports:

```text
53 tests
52 passed
1 intentionally skipped
```

This is meaningful progress toward the milestone, but it is not the final
certification. The remaining boundary is an independent final-test generator
or a locked final seed set, together with the final artifact bundle and
clean-environment replay evidence required for publication.

Development evidence must remain labelled as development evidence. It must
not be presented as a completed Structural Gate evaluation.

## 8. What follows this milestone

The next stages are:

1. **Independent episode generator**
2. **Leakage and replay certification**
3. **Protama evaluation adapter with complete traces**
4. **Baseline and ablation suite**
5. **Development-scale full benchmark**
6. **Final preregistration and freeze**
7. **Final Structural Gate evaluation**

This ordering is deliberate. The adapter should not be treated as a
complete scientific evaluation until it can consume a certified episode
package. Baselines and ablations should run against the same locked
episodes, and the final evaluation should be frozen before held-out labels
are inspected.

## 9. Claim boundary

Completing the generator would establish that Protama has a reproducible
measurement mechanism for hidden-family structural-learning episodes. It
would not establish that Protama:

- understands arbitrary natural language;
- generalizes to every structural family;
- rejects every typed near-miss;
- abstains correctly under all ambiguity;
- produces faithful explanations;
- outperforms every baseline; or
- has passed the Structural Induction and Transfer Gate.

Those claims require the later adapter, baseline, ablation, preregistration,
and final evaluation milestones.

## 10. Conclusion

The next substantial step beyond Protama's first gold gate is not to declare
the full benchmark passed. It is to build and certify the machinery that can
fairly measure whether Protama passes it.

An independent episode generator makes that step concrete. It separates
development fixtures from evaluator-created experiments, keeps latent
families and labels on the evaluator side, generates meaningful near-misses,
and makes every result replayable from a seed and configuration identity.

Once that instrument is certified, Protama's future structural-learning
claims can be evaluated against experiments designed to resist leakage,
surface memorization, and post-hoc interpretation.

## Related artifacts

- [Independent Episode Generator](../benchmark/gate-work/02_Independent_Episode_Generator.md)
- [Structural Induction and Transfer Gate](../benchmark/Protama_Inductive_Structural_Invention_Test.md)
- [Structural Gate Publication Task List](../benchmark/Protama_Structural_Gate_Publication_Task_List.md)
- [First Gold Gate Publication](2026-10-16-first-gold-gate.md)
- [Structural Learning Roadmap](../docs/roadmap/structural-learning-roadmap.md)


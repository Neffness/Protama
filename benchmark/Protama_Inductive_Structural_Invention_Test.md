# Protama Structural Induction and Transfer Gate

## Abstract

The Protama Structural Induction and Transfer Gate is a benchmark for
evaluating latent relational induction, typed near-miss discrimination,
uncertainty handling, and trace-grounded explanation fidelity.

Each benchmark episode provides a limited set of examples generated from a
hidden relational family. A system must infer a reusable structural
hypothesis, transfer it to novel vocabulary and surface forms, reject
structurally defined near-misses, abstain when evidence is insufficient, and
produce an explanation reconstructible from its pre-decision evidence trace.

The benchmark is designed to distinguish structural generalization from
memorization, keyword matching, nearest-neighbor retrieval, and post-hoc
explanation. It evaluates a specific structural-induction capability. It does
not claim to prove general intelligence by itself.

## Why this benchmark exists

Modern AI systems can produce correct answers without learning the structure
behind those answers. They may rely on memorization, keyword cues, or
statistical similarity rather than learning the underlying relationships that
make an example valid.

For example, a system might correctly classify:

```text
a person who repairs clocks
```

but fail on:

```text
a person who restores watches
```

or incorrectly accept:

```text
a clock that repairs a person
```

These failures reveal that the system may have learned a surface pattern
rather than the relational structure. The vocabulary can look familiar while
the roles and relations have changed.

The Protama Structural Induction and Transfer Gate measures whether a system
can learn latent relational structure from limited examples, apply that
structure to new vocabulary and new forms, reject near-misses that violate
the structure, and explain its decision using the same evidence that produced
it.

This benchmark focuses on one specific capability: **structural
generalization**. It does not attempt to measure general intelligence.
Instead, it isolates a foundational component that many accuracy-based
benchmarks do not test directly.

## Motivation

A system can produce a correct answer without learning the structure behind
that answer. It may memorize an example, match a keyword, retrieve a similar
sentence, or generate a plausible explanation after making its decision.

Positive transfer alone is therefore insufficient. A meaningful evaluation
must also test whether the system:

- preserves invariant relations while surface features vary;
- transfers to vocabulary absent from training;
- rejects minimally different structural near-misses;
- distinguishes rejection from uncertainty;
- records the evidence that caused its decision;
- exposes competing hypotheses when the evidence is ambiguous.

The Protama Structural Induction and Transfer Gate makes these requirements
explicit through hidden-family episodes, controlled near-miss generation,
selective prediction metrics, and reconstructible decision traces.

## Scope and non-claims

The benchmark measures latent structural induction and transfer. It is not a
general intelligence test, consciousness test, or complete evaluation of
language understanding.

Results must identify the highest capability level actually tested. A system
that passes this benchmark may have demonstrated an important component of
intelligent behavior without demonstrating every other component required for
general intelligence.

## Public benchmark package

The complete public release should contain:

```text
benchmark/
    generators/
    families/
    renderers/
    near_misses/
    scoring/
    leakage_checks/
    replay/
baselines/
protama_adapter/
configs/
results/
reports/
paper/
tests/
README.md
CITATION.cff
LICENSE
```

The benchmark specification in this document defines the required behavior,
metrics, controls, and reporting format. The executable package should include
the generator version, scorer version, baseline versions, configuration hash,
random seeds, and replay artifacts for every published result.

## How to run

The reference evaluation workflow is:

```text
1. select a locked benchmark configuration;
2. generate or load family episodes;
3. verify training/evaluation isolation;
4. initialize the system from the declared snapshot;
5. run training examples without held-out labels;
6. run held-out positives, negatives, near-misses, and ambiguity cases;
7. capture predictions, decisions, evidence, explanations, and traces;
8. run leakage and deterministic-replay checks;
9. execute registered baselines and ablations;
10. calculate metrics and confidence intervals;
11. emit human-readable and machine-readable reports.
```

An evaluation must record:

```text
benchmark version
generator version
scorer version
system version or commit
configuration hash
episode seeds
backend
initial snapshot identity
final snapshot identity
```

Development runs may use visible families and examples. Final evaluation runs
must use the locked test generator or an independently held-out test set.
Development and pilot results must not be presented as final gate results.

## Results

This section is reserved for reproducible pilot and final results.

### Pilot results

```text
status: not yet reported
families: pending
episodes: pending
system version: pending
benchmark version: pending
```

Pilot reports should include:

- positive transfer accuracy;
- negative rejection accuracy;
- near-miss accuracy by category;
- ambiguity abstention rate;
- coverage and risk-coverage curves;
- explanation fidelity;
- baseline comparisons;
- per-family and per-episode results;
- confidence intervals;
- representative successes and failures;
- resource usage;
- CPU/GPU differences where applicable.

Pilot results are intended to validate the harness and expose failure modes.
They are not, by themselves, evidence of general intelligence or a final gate
pass.

## Citation

When published, cite the versioned benchmark artifact rather than an
unversioned working document.

```text
Protama Project. The Protama Structural Induction and Transfer Gate:
A Benchmark for Latent Relational Learning and Typed Near-Miss
Discrimination. Version [VERSION], [YEAR].
Repository: [REPOSITORY URL]
DOI or preprint: [DOI OR PREPRINT URL]
```

## Repository and license status

```text
repository: not yet assigned
license: pending release decision
```

The repository URL, license, version, DOI, and preprint link must be filled in
before the artifact is presented as a finalized public release. Until then,
this document is a publishable benchmark proposal and development
specification, not a completed public benchmark package.

## Status and claim

This document is a rough benchmark specification for a public evaluation of
Protama. It is a research gate, not a claim that Protama currently satisfies
the gate.

The gate does **not** prove general intelligence by itself. It evaluates a
more specific capability:

> Can Protama induce a reusable latent relational structure from limited
> examples, transfer it to novel cases, reject structurally defined
> near-misses, represent uncertainty, and explain its decision from the same
> evidence used for prediction?

The benchmark should be called the **Protama Structural Induction and Transfer
Gate**. The word *invention* is reserved for the optional unsupervised
extension described below, where Protama must construct a reusable hypothesis
without being given the target family or output category.

## Capability ladder

Results must identify the highest capability actually tested. Passing an
earlier level must not be reported as passing independent structural invention.

| Level | Capability |
| --- | --- |
| L0 | Exact-example or memorized matching |
| L1 | Supervised reuse of an explicitly represented relation |
| L2 | Induction of a latent relation from examples |
| L3 | Transfer to novel vocabulary and surface forms |
| L4 | Contrastive discrimination against structural near-misses |
| L5 | Compositional generalization to unseen combinations |
| L6 | Discovery of a new reusable category or relation family |
| L7 | Self-directed refinement through information-seeking examples |

The primary benchmark is an L2-L5 gate. L6-L7 require the invention and
interactive extensions and must be reported separately.

## Formal evaluation unit

The unit of evaluation is a **family episode**:

```text
episode:
    hidden family generator and seed
    limited training examples
    held-out positive examples
    held-out negative examples
    typed near-miss examples
    surface and vocabulary transfer examples
    ambiguity or insufficient-evidence examples
    prediction requests
    explanation request
    complete score and trace artifact
```

Each episode contains one latent structural family \(F\), a training set
\(D_{\mathrm{train}}\), and disjoint evaluation sets:

$$
\left(
F,D_{\mathrm{train}},
D_{\mathrm{positive}},
D_{\mathrm{negative}},
D_{\mathrm{near}},
D_{\mathrm{ambiguous}}
\right)
$$

The latent family is known to the generator and evaluator but is not revealed
to Protama.

## Required behavior

For each episode, Protama must:

1. compare the training examples;
2. identify invariant relationships;
3. distinguish relevant structure from irrelevant surface features;
4. form a reusable structural hypothesis;
5. apply the hypothesis to held-out positive examples;
6. reject structurally defined negative and near-miss examples;
7. transfer across novel vocabulary and surface variation;
8. explain which evidence produced the hypothesis and decision;
9. identify competing hypotheses where appropriate;
10. abstain when evidence is insufficient or ambiguity remains;
11. revise, weaken, or reject a hypothesis when later evidence contradicts it.

Correctness alone is insufficient. A system that returns the right label with
an unsupported or post-hoc explanation has not passed the explanation portion
of the gate.

## Latent family specification

Each generated family must be defined formally before rendering examples.
For example:

$$
R(a,v,o)
=
\operatorname{Agent}(a)
\land
\operatorname{Performs}(a,v)
\land
\operatorname{Compatible}(v,o)
$$

The generator then renders instances of \(R\) into symbolic, textual, or
other permitted representations.

The family definition must specify:

- required entities and their types;
- invariant relations;
- optional relations;
- irrelevant or varying features;
- forbidden relations;
- ambiguity conditions;
- the minimum evidence needed for a supported hypothesis;
- the expected behavior for every negative category.

The rule must not be recoverable from a single keyword, exact phrase, output
token, or fixed example position.

## Example family

An illustrative family might contain descriptions such as:

```text
a person who repairs clocks
a person who maps stars
a person who studies insects
```

The intended abstract structure might be an agent performing an action. A
valid evaluation must also include examples where:

- the vocabulary is entirely novel;
- the sentence or serialization template changes;
- the agent and object roles are reversed;
- an object is used for the action but does not perform it;
- the same words appear in an invalid relation;
- one required relation participant is missing;
- the evidence is genuinely ambiguous.

This family alone is not sufficient for the public benchmark. It may be
solved using ordinary linguistic priors rather than newly induced structure.

## Data generation and split controls

The benchmark must use a preregistered family generator or a locked set of
independently authored families. The final test generator must not be tuned
against during development.

Every episode must enforce the following split controls:

### Lexical split

Evaluation vocabulary must not appear in the training examples when measuring
novel-vocabulary transfer.

### Structural split

The exact relation configurations used for evaluation must not occur in the
training set.

### Template split

At least one evaluation representation must use a sentence, serialization, or
surface template absent from training.

### Family split

For independent-family evaluation, the latent family itself must be held out.
The system must not receive a preloaded relation with the same structure.

### Generator split

Development and final evaluation must use independent generators or locked
generator seeds.

### Temporal split

The harness must distinguish:

- pre-evaluation training;
- evaluation without feedback;
- optional adaptation during evaluation;
- final performance after adaptation.

Feedback on a held-out label before the final score invalidates the clean
generalization result and must be reported as an interactive-adaptation run.

## Near-miss taxonomy

Near-misses must be generated and scored by category rather than collapsed
into one negative class.

| Category | Structural failure tested |
| --- | --- |
| Role reversal | The object performs the action instead of the agent |
| Relation reversal | \(R(a,o)\) is presented as \(R(o,a)\) |
| Type violation | An object occupies a role requiring an agent |
| Argument omission | A required participant or relation is missing |
| Single-feature mismatch | Exactly one invariant is violated |
| Surface decoy | Familiar wording presents the wrong structure |
| Lexical overlap | Training vocabulary appears in an invalid relation |
| Novel negative | New vocabulary and an invalid latent structure |
| Ambiguous case | Multiple hypotheses remain equally supported |
| Contradictory case | Evidence supports mutually incompatible hypotheses |

The benchmark must report each category separately. Aggregate accuracy must
not hide systematic failure on role reversal, contradiction, or ambiguity.

## Explanation contract

Protama's explanation must be grounded in the same representation used for
prediction. It must identify:

- observed invariant features;
- varying or irrelevant surface features;
- the induced relation family or hypothesis identifier;
- evidence supporting the application;
- evidence rejected as irrelevant or contradictory;
- competing hypotheses;
- the reason a near-miss was rejected;
- uncertainty and the reason for abstention, when applicable.

An explanation generated after an unsupported answer does not satisfy this
test.

### Explanation scoring

The harness should score four independent dimensions:

1. **Invariant correctness**: the explanation identifies the actual invariant
   structure.
2. **Irrelevance recognition**: it identifies surface features that vary and
   should not control the result.
3. **Counterfactual sensitivity**: it explains why each near-miss fails.
4. **Trace fidelity**: every cited fact is present in the pre-decision trace.

Define:

$$
E=
\frac{
E_{\mathrm{invariant}}
+E_{\mathrm{irrelevant}}
+E_{\mathrm{counterfactual}}
+E_{\mathrm{trace}}
}{4}
$$

The harness must support explanation reconstruction from the saved hypothesis,
selected evidence, rejected evidence, and decision trace. If the emitted
explanation materially differs from the reconstructed explanation, it must be
marked as unsupported.

## Primary metrics

Accuracy alone is not sufficient. The harness must report:

### Positive transfer accuracy

$$
A_+
=
\frac{\text{correct held-out positives}}
{\text{held-out positives}}
$$

### Negative rejection accuracy

$$
A_-
=
\frac{\text{correctly rejected negatives}}
{\text{held-out negatives}}
$$

### Near-miss discrimination

$$
A_{\mathrm{near}}
=
\frac{\text{correctly classified near-misses}}
{\text{near-misses}}
$$

Report \(A_{\mathrm{near}}\) separately for every near-miss category.

### Novel-vocabulary transfer

Score only evaluation cases containing vocabulary absent from training.

### Surface invariance

Measure performance across paraphrases, argument ordering, serialization
changes, distractors, and other permitted surface variations.

### Compositional generalization

Measure performance on combinations of known components that never occurred
together in training.

### Abstention quality

Use selective-prediction metrics:

- coverage;
- accuracy at coverage;
- false-commitment rate;
- abstention precision;
- risk-coverage curve.

Protama must not pass by abstaining on everything. Require both:

$$
\operatorname{coverage}\geq c_{\min}
$$

and:

$$
\operatorname{selective\ risk}\leq r_{\max}
$$

### Explanation fidelity

Report \(E\) independently from prediction accuracy.

### Resource and reproducibility metrics

Also record:

- CPU and GPU wall-clock time;
- peak memory;
- number of cognitive operations;
- evidence-provider calls;
- snapshot and trace sizes;
- deterministic replay success;
- CPU/GPU substrate mismatches.

## Pass rule

The gate must use preregistered thresholds rather than a single averaged
score. A provisional pass rule is:

$$
\operatorname{PASS}
\iff
\begin{cases}
A_+\geq\alpha \\
A_-\geq\beta \\
A_{\mathrm{near}}\geq\gamma \\
A_{\mathrm{novel}}\geq\delta \\
E\geq\epsilon \\
\operatorname{coverage}\geq c_{\min} \\
\text{no critical leakage detected}
\end{cases}
$$

The values \(\alpha,\beta,\gamma,\delta,\epsilon,c_{\min}\), and
\(r_{\max}\) must be fixed before the final test run. They must not be chosen
after inspecting final test results.

The public report must include:

- raw metrics;
- category-level metrics;
- confidence intervals;
- failures and abstentions;
- all excluded episodes and exclusion reasons;
- the exact pass-rule version.

## Baselines

The benchmark must include:

1. **Exact-match baseline**: tests memorization.
2. **Keyword baseline**: tests single-feature or lexical shortcuts.
3. **Nearest-neighbor baseline**: tests similarity without abstraction.
4. **Symbolic oracle**: receives the latent rule and approximates an upper
   bound for the generated family.
5. **CPU Protama**: the inspectable reference implementation.
6. **GPU Protama**: the accelerated implementation under evaluation.
7. **Language-model baseline**: included when full semantic processing is part
   of the comparison claim.

The CPU and GPU versions must be evaluated for:

- behavioral equivalence on the shared substrate contract;
- capability differences caused by scale, throughput, or available semantic
  resources;
- deterministic replay and snapshot parity where supported.

## Ablation plan

At minimum, run ablations that remove or replace:

- evidence provenance;
- near-miss exposure;
- abstention;
- structural memory;
- association memory;
- transition memory;
- explanation constraints;
- novelty tracking;
- cognitive-operation utility learning;
- external evidence providers;
- language-model assistance.

Include a keyword-matching replacement for structural hypothesis formation.
The critical ablation is whether Protama still passes when lexical identity is
deliberately made useless.

## Leakage and validity rules

A run must be rejected or separately labeled if Protama receives any
unpermitted path to the target answer, including:

- the family name;
- a natural-language description of the hidden rule;
- examples from the held-out generator;
- held-out labels before final scoring;
- a preloaded relation with the same latent structure;
- a prompt template that explicitly signals the expected category;
- memorized benchmark-specific output tokens;
- a language model that has memorized the exact benchmark family.

The evaluator must record not only whether the answer was correct, but whether
the path to that answer was permitted.

## Statistical and reproducibility protocol

The final benchmark should include, at minimum:

```text
100+ independently generated family episodes
10+ evaluation seeds, or a deterministic equivalent
separate development and final test generators
95% confidence intervals
locked final-test generator
preregistered pass thresholds
complete snapshots and decision traces
deterministic replay artifacts
```

The exact sample counts may be revised after a power analysis, but the
protocol must be fixed before final evaluation.

Use bootstrap or binomial confidence intervals appropriate to each metric.
Report episode-level variation rather than treating every example as
independent when examples share one latent family.

## Optional independent-invention extension

The following extension is required before claiming L6 independent invention:

1. provide unlabeled examples only;
2. do not provide the target family name or output category;
3. require Protama to cluster or describe recurring structure;
4. require it to create a reusable hypothesis identifier;
5. present new examples with novel vocabulary and templates;
6. test positive transfer and adversarial near-misses;
7. introduce contradictory evidence;
8. measure hypothesis revision, weakening, or rejection.

The extension evaluates:

$$
\text{examples}
\rightarrow
\text{latent structure}
\rightarrow
\text{new representation}
\rightarrow
\text{transfer}
\rightarrow
\text{revision}
$$

This is closer to structural invention than supervised classification, but it
still does not constitute proof of general intelligence by itself.

## Optional interactive refinement extension

For L7, Protama may select the next example or request clarification. The
harness must score whether the selected query reduces uncertainty rather than
merely requesting labels until the answer is revealed.

Record:

- query count;
- information gain;
- uncertainty before and after each query;
- label efficiency;
- final transfer performance;
- unnecessary or redundant queries.

## Evaluation harness requirements

The full harness should provide:

```text
family generation
episode serialization
train/evaluation isolation
CPU and GPU backend selection
baseline execution
ablation execution
trace and snapshot capture
explanation reconstruction
metric calculation
confidence intervals
leakage checks
deterministic replay
human-readable report
machine-readable report
```

Every scored answer should be traceable to:

```text
episode seed
training examples
evaluation example
candidate hypotheses
selected evidence
rejected evidence
operation sequence
prediction
decision
explanation
score contribution
```

## Proposed paper claim

A paper-ready claim should be no broader than the evidence:

> On a preregistered benchmark of independently generated relational
> families, Protama induces reusable structural hypotheses from limited
> examples, transfers them to novel vocabulary and surface forms, rejects
> typed near-misses, abstains under insufficient evidence, and produces
> explanations reconstructible from its pre-decision evidence trace, while
> outperforming non-structural baselines under the published leakage and
> ablation controls.

Do not claim that this result proves general intelligence. Claim the measured
structural-induction and transfer capability, then place it alongside other
independent capabilities in a broader evaluation program.

## Current success criteria

The initial implementation is ready for a final public gate only when:

- the generator and split rules are locked;
- near-miss categories are implemented;
- pass thresholds are preregistered;
- baselines and ablations run automatically;
- CPU/GPU parity checks are available;
- explanations can be reconstructed from traces;
- leakage checks produce a report;
- confidence intervals and episode-level statistics are emitted;
- all artifacts can be replayed from a clean environment.

Until then, results should be labeled as development or pilot results.

# Causal Intervention and World-State Reasoning
## Hypothesis Publication

**Publication state:** hypothesis  
**Gate:** `causal-intervention-world-state`  
**Status:** public hypothesis; not a frozen theory or completed gate result

## Abstract

This publication proposes a gate for testing whether Protama can reason about
the consequences of deliberate actions on a changing world.

The central distinction is between observing that variables occur together and
reasoning about what happens when one variable or action is deliberately
changed. A system that only learns associations may predict correctly while
the world remains undisturbed, yet fail when its advice causes an intervention.
The proposed gate therefore tests intervention consequences, belief revision,
uncertainty, and counterfactual reasoning in a responding environment.

This is a hypothesis publication. It defines the capability and the proposed
research direction, but it does not publish a pass result, fixed thresholds,
frozen case data, or a final theory. Those will be developed through
substantial experimental work and published only once the research team agrees
that the gate is complete and ready to freeze.

## Unified capability definition

**Causal intervention reasoning** is the ability to predict, explain, and
update on what happens when a component of a system is deliberately changed,
using a model of cause and effect rather than observed correlation alone.

The capability distinguishes three related questions:

```text
association:    What tends to occur with what?
intervention:   What happens if I deliberately set or change X?
counterfactual: What would have happened in this particular case
                if I had acted differently?
```

Observation describes the ordinary data-generating process. An intervention
changes that process by forcing a variable or action, severing the variable's
normal incoming causes for the purpose of the test. The resulting observation
is evidence about the intervention's effect, not merely another correlation.

In a formal causal model, this is represented by a `do(X = x)` operation.
Protama does not need to implement a particular causal formalism, but it must
preserve the operational distinction between:

```text
what was observed;
what was deliberately changed;
what consequence followed; and
what Protama believes those facts imply.
```

## Hypothesized capability

We hypothesize that a causal intervention-capable Protama can:

- maintain competing causal explanations when observations do not identify
  one explanation uniquely;
- predict the consequences of available interventions;
- select an intervention when its outcome would discriminate among
  hypotheses;
- revise its beliefs after an intervention succeeds or fails;
- answer counterfactual questions from the revised causal model;
- recognize when the causal question is not identifiable from the available
  evidence; and
- abstain or request disambiguating evidence rather than force an unsupported
  causal conclusion.

The hypothesis is stronger than retrospective state classification. A system
must predict consequences before seeing the intervention outcome, and its
belief revision must depend on the outcome that actually occurs.

## Proposed environment

The gate requires a responding simulator or interactive environment rather
than a static labelled dataset. The environment should contain:

- persistent entities and changing properties;
- hidden or confounded causes;
- observations that do not immediately identify the cause;
- interventions with different consequences under competing hypotheses;
- action outcomes revealed separately from pre-action observations;
- reproducible episode generation;
- evaluator-owned ground truth; and
- counterfactual queries with known scoring outcomes.

The environment must support both successful and failed predictions. A
system that only receives confirming outcomes cannot demonstrate belief
revision.

Counterfactual scoring must preserve the episode's exogenous randomness. The
theory-state environment should record the episode's exogenous draws and
re-run the same episode with those draws held fixed while the action changes.
Resampling noise would turn a definite counterfactual into a distribution
different from the one being asked about. The abduction and noise-replay rule
is therefore a theory-freeze decision, not an implementation detail.

## Proposed evaluation episode

An episode may contain:

```text
initial world state
partial observations
candidate causal hypotheses
available interventions
action costs or constraints
pre-intervention predictions
selected intervention
sampled consequence
required belief update
counterfactual query
```

The goal and available actions are supplied externally. The gate does not
require autonomous desire, intrinsic motivation, or self-generated goals.

The intended reasoning sequence is:

```text
observe
→ retain competing explanations
→ predict intervention consequences
→ select or receive an intervention
→ observe the consequence
→ revise beliefs
→ answer a counterfactual
```

Intervention selection and intervention receipt are separate evaluation
capabilities. A received-intervention stratum tests prediction and
outcome-dependent revision. A selection stratum tests whether Protama chooses
an action for information gain among competing hypotheses. These strata must
be reported separately at theory freeze so success in one cannot conceal
failure in the other.

The research must also decide whether candidate causal hypotheses are supplied
by the evaluator or induced by Protama from observations. Selecting among
supplied alternatives is a meaningful but narrower claim than constructing
the alternatives itself. The hypothesis publication leaves this boundary
open; the theory publication must state it explicitly and use corresponding
claim language.

## Evidence and provenance hypothesis

The system should preserve provenance sufficient to distinguish:

- evidence available before the intervention;
- the intervention that was selected or executed;
- the sampled world consequence;
- evidence retained, evicted, or unavailable;
- the belief state before revision; and
- the belief state after revision.

An exact intervention-name lookup, a retrospective label classifier, or an
answer copied from future outcome data does not satisfy this hypothesis.

When multiple causal models remain compatible with the retained evidence,
the correct result may be explicit uncertainty, abstention, or a request for
a discriminating intervention. Such outcomes are not automatically failures.

## Proposed evidence categories

The research should distinguish at least:

```text
association only
intervention-supported
counterfactual-supported
underdetermined
contradicted
```

These categories are hypotheses for organizing evidence, not final scoring
thresholds. Their operational definitions must be tested against simulator
identifiability and baseline behavior before the theory is frozen.

## Proposed diagnostic comparisons

The hypothesis should be tested against controls such as:

- temporal-correlation reasoning;
- observational-only learning;
- forced single-hypothesis commitment;
- random intervention selection;
- action-outcome permutation;
- a supplied causal-model reference; and
- an oracle causal model.

The action-outcome permutation control should preserve superficial temporal
statistics while breaking the relationship between an action and its
consequence.

Diagnostics should examine:

- intervention-effect prediction;
- observational-versus-interventional discrimination;
- belief revision after confirming and disconfirming outcomes;
- counterfactual accuracy;
- uncertainty over competing causal models;
- intervention selection for information gain;
- confounder handling;
- world-state versus belief-state separation; and
- provenance and replay integrity.

Belief revision should be scored for direction and justification, not merely
for dependence on the outcome. The post-outcome belief should be compared with
the belief that is justified by the pre-outcome state, the observed outcome,
and the declared causal model. A system that changes its belief after every
outcome, but moves toward the wrong explanation, must not receive credit for
revision.

No diagnostic number in this hypothesis publication is a final gate
threshold.

## Two-publication lifecycle

This publication is the first public hypothesis. It is intentionally
provisional. During the research phase, the simulator, curriculum,
representation, retention policy, diagnostics, and failure interpretation
may change as bugs and identifiability limits are discovered.

After the research team agrees that the definition, task, evidence standard,
failure taxonomy, baselines, scoring, and integrity controls are stable, the
gate will enter theory state.

The theory-state publication will freeze, together:

- the final capability definition;
- the responding environment and causal mechanisms;
- the lesson curriculum and held-out families;
- the required inputs, outputs, and provenance trace;
- baselines and ablations;
- scoring and exclusion rules;
- uncertainty and abstention policy;
- thresholds and confidence procedures;
- leakage and integrity checks;
- the materialized case data; and
- the final report schema.

The project will not publish a succession of causal gate versions to reflect
ordinary development iterations. It will publish this hypothesis once, do the
substantial research, and then publish one agreed frozen theory and gate
result.

During hypothesis research, dated amendments may be appended to this
publication when the public understanding materially changes. An amendment
must identify what changed and why; it does not create a new gate version,
alter the one-time theory freeze, or turn exploratory evidence into a result.

## Claim boundary

This hypothesis does not claim:

- general causal intelligence;
- unrestricted real-world understanding;
- human reasoning or consciousness;
- autonomous goals or agency;
- physical or sensorimotor grounding; or
- that correlation-based prediction is sufficient for causal reasoning.

If the future theory-state evaluation passes, the supported claim will be
limited to causal updating and intervention reasoning in the declared
responding environment.

## Public/private separation

This document is the public hypothesis publication. It contains the proposed
capability, environment, evaluation logic, and claim boundary.

Private implementation details, exploratory traces, simulator development,
bug investigations, provisional thresholds, and pre-freeze results remain in
the private research tree. They are not part of this publication and must not
be interpreted as a completed gate result.

# Epistemic Growth and Active Inquiry Gate

> **Status:** Proposed internal gate specification.  
> This document defines a future evaluation instrument. It does not report an
> implementation, a completed run, or a passing result.

## Inspiration

The inspiration for this gate is the ordinary human act of recognizing that
knowledge is incomplete.

A person does not only retain facts about a subject. They also develop a
sense of the subject's shape: what they have encountered, what remains
uncertain, which questions would expose the edge of their understanding, and
when their own estimate is probably unreliable. This is the practical meaning
behind the warning, “You do not know what you do not know.” The unknown is not
directly visible, but a system can be built to notice when its map stops
explaining what it encounters.

That process begins with a bounded sphere of experience. As the sphere grows,
some lessons confirm familiar structure while others reveal new nodes,
relations, exceptions, or entire regions that were not represented. The
pattern of discovery matters. Repeatedly finding the same structure suggests
coverage; continuing to find new structure suggests an expanding boundary.
Comparing those patterns across different kinds of spheres offers a way to
estimate how much more may be encountered, while remaining honest that the
estimate is conditional on the probes used.

This is also the source of active inquiry. A learner should not spend every
lesson sampling the comfortable center of what it already knows. It should be
able to notice the edge, choose a question that could reveal something there,
and change its behavior when the answer exposes a gap. The important loop is:

1. build a map from limited experience;
2. recognize where the map may be incomplete;
3. probe the boundary;
4. turn a revealed gap into an explicit learning target; and
5. redraw the map before choosing what to do next.

The gate exists because this loop is central to self-correcting learning.
Without it, additional training can produce accumulation without direction:
the system may answer from its existing center, remain unaware of missing
structure, and repeatedly receive lessons without learning what those lessons
say about the limits of its own knowledge.

## Abstract

The Epistemic Growth and Active Inquiry Gate evaluates whether a cognitive
system can regulate the boundary of its own learned knowledge and use that
boundary to guide further inquiry.

The gate is not a test of whether a system can merely say “I do not know.” It
tests a coupled capability:

1. maintain an explicit, bounded model of what has been observed and learned;
2. estimate which additional structure is still encounterable under a declared
   probe distribution and resource budget;
3. recognize when that estimate is unreliable;
4. select probes that reveal informative boundary structure rather than only
   repeating familiar material;
5. convert revealed unknowns into explicit learning targets;
6. update the boundary estimate and subsequent inquiry policy; and
7. preserve calibration across held-out sphere types.

The defensible claim is therefore about **encounterable unknown structure under
declared conditions**, not about discovering all unknown unknowns.

## One-sentence claim

> Under a versioned protocol and bounded probe budget, the system demonstrates
> calibrated knowledge-boundary regulation: it detects insufficient or
> unreliable knowledge, selects informative inquiry, updates its knowledge
> boundary after hidden structure is revealed, and adapts subsequent learning
> behavior across held-out sphere types.

## Why this is a gate

The capability described above is a necessary part of a continual,
developmental intelligence. Accumulating lessons is not the same as knowing
what to learn next. A system that cannot distinguish a covered region from an
unexamined region cannot reliably choose between answering, verifying, asking
for information, or abstaining.

The gate is intended to distinguish knowledge-boundary regulation from a
scalar confidence score, active inquiry from a scripted traversal, calibrated
updating from post-hoc explanation, and genuine coupling between an estimate
and action from decorative telemetry.

## Definitions

### Knowledge sphere

A knowledge sphere is a versioned evaluation world containing typed nodes,
relations, grouping structure, and an evaluator-defined set of hidden
structure. A sphere has a declared family, sampling model, resource budget,
and held-out portion.

Sphere families must vary in representation and relation type. A system must
not be able to pass by learning one generator template and applying its
surface syntax elsewhere.

### Encounterable unknowns

An encounterable unknown is hidden sphere structure that can be revealed by at
least one permitted probe within the declared resource budget and probe
interface. It is not a claim about structure that no allowed probe could
possibly expose.

The evaluator must publish the probe interface and the estimand before a
held-out run. The hidden world is known to the evaluator for scoring, but the
system receives only the observations and revelations allowed by the
protocol.

### Boundary estimate

A boundary estimate records the system's current estimate of the remaining
encounterable structure. At minimum it must include:

- estimated remaining nodes, relations, or groups;
- uncertainty or interval around each estimate;
- the probe distribution and budget to which the estimate applies;
- evidence window and sampling regime;
- estimate reliability;
- timestamp or phase identifier; and
- the intended next inquiry policy.

An estimate without its conditions is not scoreable and cannot be treated as a
general statement of ignorance.

### Probe

A probe is an allowed information-seeking action chosen before the resulting
evidence is revealed. A probe may query, sample, compare, request a relation,
or inspect a candidate boundary, depending on the sphere family.

A **boundary probe** is a probe selected because the system's current model
predicts that it is likely to reveal structure not already covered or that it
will discriminate among competing boundary estimates.

### Unknown conversion

Unknown conversion is the transition in which newly revealed structure is
represented as an explicit known unknown or learning target before the next
decision. The system must not receive credit merely for producing a correct
post-hoc description after the evaluation has ended.

## Protocol

### Phase 1: Development calibration

Development spheres are used to:

- validate that the sphere generators produce non-trivial hidden structure;
- calibrate metric scales and uncertainty measures;
- establish the strong baseline set;
- select thresholds and resource budgets; and
- freeze the scoring and pass procedure.

Development material must not be reused as held-out evidence.

### Phase 2: Initial bounded observation

The system receives a limited observation set and a fixed initial resource
budget. It must emit a pre-decision record before choosing its first probe.
The record must include its current sphere model, boundary estimate,
reliability assessment, candidate actions, and selected action.

### Phase 3: Active inquiry

The system chooses probes sequentially. Each choice is scored against the
information available before that probe. The harness records the revealed
structure, the system's update, and its next decision.

The harness must include multiple sampling regimes:

- representative sampling;
- center-biased sampling;
- boundary-avoiding sampling; and
- adversarially biased sampling.

The regime is hidden from the system but declared to the evaluator.

### Phase 4: Fixed external revelation

The protocol may reveal previously hidden structure to test conversion and
updating. In the first gate version, revelation schedules must be fixed from
the seed and preregistered configuration. They must not adapt to the
system's current score or selectively rescue a weak run.

The schedule and revelation mechanism are part of the benchmark instrument and
must be validated independently.

### Phase 5: Held-out evaluation

Held-out spheres must differ from development spheres by more than vocabulary
renaming. At least one held-out family must test transfer of the inquiry
policy, estimator conditions, or evidence representation.

The evaluator must retain the hidden structure, probe outcomes, and complete
pre-decision trace for independent scoring.

## Required pre-decision record

Before each scored probe or answer decision, the system must record:

- observations available at that point;
- learned nodes, relations, groups, and unresolved items;
- current boundary estimate and interval;
- estimate reliability and the evidence supporting it;
- candidate probes and predicted information value;
- selected action and its reason;
- whether the decision is continue, verify, clarify, answer, or abstain; and
- the resource cost assigned to the action.

The record must be append-only or otherwise auditable. Evidence added after
the action cannot be used to justify the original decision.

## Core metrics

### Boundary-estimation error

Compare the estimated encounterable remainder with the evaluator's hidden
remainder under the declared probe distribution and budget. Report absolute
and relative error, interval coverage, and error by sphere family.

### Reliability discrimination

Measure whether the system's reliability estimate separates unbiased sampling
from biased or adversarial sampling. A system that gives the same reliability
assessment in both regimes has not demonstrated second-order awareness.

### Probe efficiency

Measure newly revealed, previously unrepresented structure per probe and per
resource unit. Report both discovery and repeat rates so that a system cannot
win by repeatedly sampling a small productive center.

### Probe-estimate coupling

Measure whether the current boundary estimate changes probe selection and
whether estimate quality predicts subsequent discovery. This is the
anti-decoration test for the gate.

The decisive control is an estimate-lesion condition: provide a deliberately
incorrect boundary model while holding the rest of the system fixed. Probe
behavior and discovery efficiency must degrade in a measurable, preregistered
way. If they do not, the estimate is not action-relevant.

### Unknown conversion

Score whether revealed structure becomes an explicit unresolved item or
learning target before the next decision, whether it is resolved or retained
with appropriate status, and whether the update appears in later inquiry.

### Adaptive update quality

Evaluate calibration and action quality after revelation. Honest updating may
temporarily increase estimated ignorance; monotonic improvement is not
required. The score should measure convergence, final calibration, and
useful adaptation over a fixed budget.

### Cross-sphere transfer

Evaluate the same decision machinery on held-out sphere families. Report
performance separately by family; aggregate scores must not conceal a
single-family strategy.

## Baselines and controls

The gate must include at least:

- a strong systematic enumerator;
- a random explorer;
- a confidence-only selective predictor;
- a fixed-order explorer;
- an oracle upper-bound policy, reported separately;
- an estimate-lesion control; and
- a scripted policy matched for probe budget.

The systematic baseline is essential. A weak random baseline would allow a
well-engineered enumerator to appear metacognitive without modeling its own
knowledge boundary.

The evaluator must also test whether a system can pass using:

- a hidden generator fingerprint;
- a fixed revelation schedule;
- repeated center sampling;
- post-hoc explanations; or
- an uncalibrated scalar confidence value.

Successful leakage or shortcut checks invalidate the affected claim.

## Pass procedure

Thresholds must be established in two stages:

1. calibrate metric behavior against development spheres and baselines;
2. freeze thresholds, scoring code, seeds, and held-out material before the
   final evaluation.

The final gate should use a preregistered conjunction of core criteria rather
than a favorable aggregate score. Core criteria should cover:

- boundary-estimation calibration;
- reliability discrimination;
- probe-estimate coupling;
- probe efficiency against the strong systematic baseline;
- unknown conversion and adaptive updating; and
- transfer to held-out sphere types.

Other measurements may remain diagnostic, including clarification dialogue,
long-horizon resource allocation, and detailed estimator-family comparisons.
Clarification should not be a hidden requirement in the first version because
it requires an interactive oracle and a separate dialogue harness.

The pass report must include per-sphere and per-regime results, confidence
intervals, baseline comparisons, lesion results, failed probes, abstentions,
and all deviations from the preregistered protocol.

## Failure conditions

The gate is not passed if any of the following is true:

- the estimate is accurate only under one unannounced sampling regime;
- probe quality is unchanged by estimate lesion;
- the system relies on a generator-specific shortcut;
- newly revealed structure is described only after the decision;
- calibration fails on held-out sphere types;
- the system is less informative than the strong systematic baseline under
  matched budget without a declared compensating capability; or
- the evaluator cannot reconstruct the pre-decision evidence for the result.

An abstention is not automatically a failure. It is correct when the system's
evidence is insufficient and the abstention is calibrated. Conversely, a
confident answer is not a success merely because it is correct by chance.

## Claim boundary

Passing this gate would support the bounded claim that the system can regulate
its knowledge boundary and choose useful inquiry under the tested conditions.
It would not establish:

- complete awareness of all unknown unknowns;
- human equivalence;
- unrestricted curiosity or open-world exploration;
- truth of an estimate outside its declared probe distribution;
- general intelligence by itself; or
- that the estimator's internal representation is the same as a human
  metacognitive representation.

The gate measures the ability to be shown efficiently where the boundary of
current knowledge lies. It does not make the unknowable directly observable.

# Bounded Working Memory and Thought Holdover Gate

This gate has two modular layers: a capacity gate for bounded-state behavior
and, when learned retention is enabled, a policy-learning gate for whether the
learned policy preserves value without evaluation-time leakage. The second
layer was added in response to private-side implementation evidence; it was
not assumed to be part of the original fixed-policy capacity claim.

> **Status:** Public evaluation contract; profile-aligned revision.
> This document defines the parent capability and its evaluation profiles; it
> does not declare a completed result.

## Abstract

The Protama Bounded Working Memory and Thought Holdover Gate is a benchmark
for evaluating bounded transient retention, multi-step manipulation, relational
binding, controlled decay, interference resistance, and thought-local state
discipline.

Each benchmark episode gives a system a finite workbench, a sequence of
operations, items and relations that must remain available, competing material,
and a required final decision. The system must retain and manipulate what the
task requires, evict or decay what the budget cannot support, preserve the
identity and arguments of bindings, and prevent transient state from becoming
an untracked durable store.

The benchmark is designed to distinguish bounded working state from unlimited
logging, pointer-based retrieval, independent-item recall without manipulation,
and accidental persistence across thought boundaries. It evaluates a specific
transient-memory capability. It does not claim to establish human working
memory, consciousness, or general intelligence.

This specification is intentionally implementation-neutral. It is suitable for
independent review, adversarial testing, and matched baseline comparisons
without exposing private runtime layouts or unpublished training records.
The gate requires state-aware binding decisions for manifest-declared
underdetermined episodes, but does not require a particular epistemic theory or
runtime implementation. The broader epistemic-precision profile described
below remains optional.

## Capability profiles and claim alignment

The gate name identifies the capability under test, not one mandatory task
family. A **bounded working-memory thought holdover** is transient,
capacity-limited state that survives across cognitive operation cycles, can be
manipulated to produce a later decision, and is cleared, evicted, or promoted
according to an auditable thought boundary.

Different task families may demonstrate that capability. They must not be
forced through metrics that assume a different representation or operation.
Every submission therefore declares a profile:

```text
grounded-symbolic-composition
legacy-relational-manipulation
role-filler-binding (reserved)
feature-binding (reserved)
language-mediated-composition (reserved)
```

Only `grounded-symbolic-composition` is declarable in this gate version. The
legacy relational battery is historical evidence, not a declarable profile,
because its complete threshold, baseline, scoring, and freeze record is not
present in the active public package. The other profiles are reserved names,
not blank checks: they cannot be selected until their task families, complete
threshold sets, baselines, scoring schemas, and freeze records are published.

The parent gate has invariant requirements shared by every profile:

- required information is explicitly taught or provided by the episode;
- the final decision depends on transient retained state;
- capacity is declared and charged;
- missing retained information produces the declared abstention or
  uncertainty outcome rather than an unsupported answer;
- snapshot replay is decision-identical;
- completed thoughts do not leak into later thoughts; and
- no uncharged event log, future target, or hidden answer path is available.

Eviction and expiration must be correct for every profile: retrieving an
evicted item as present is a validity failure, not a soft metric miss.
Unauthorized durable promotion is also a zero-tolerance validity failure.
Profiles may add numeric precision thresholds for these events, but they may
not use a numeric average to excuse either validity violation.

Profile metrics are chosen to measure the declared claim. Grounded symbolic
composition scores withheld symbolic results, capacity-aware abstention, and
distractor invariance. A language profile may add language parsing and
rendering metrics. A profile is not allowed to omit the shared invariants, but
it is also not failed by an unrelated metric that its declared task does not
instantiate.

The previous synthetic relation battery remains useful as a historical
`legacy-relational-manipulation` profile. Its results must not be presented as
the result of every profile or as a universal intelligence score.

### Meta-freeze rule

The profile, task families, complete threshold set, baselines, curriculum or
lesson manifest, scoring schema, and adaptation protocol freeze together in
one preregistration record before any final-test or held-out result is
inspected. A profile is declarable only when that complete record exists.
Development experience may motivate a new gate version, but it cannot change
the active version's profile, metrics, thresholds, baselines, or lesson set.
Switching profiles after any held-out inspection opens a new gate version and
requires a new freeze and new held-out run.

### Grounded symbolic composition profile

This profile establishes a finite symbolic substrate before testing holdover.
The curriculum teaches the symbols, syntax, value/type bindings, and a
declared subset of compositions. The final test withholds compositions rather
than withholding the meaning of ungrounded raw arrays.

The profile's core claim is:

```text
grounded symbolic lessons
→ bounded transient retention
→ withheld symbolic composition
→ correct result or principled abstention
```

Readable domain labels such as `inert`, `safe`, `warning`, and `danger` are
valid learned symbols. Their appearance as English words does not grant them
pretrained English meaning. Natural-language rendering is a separate optional
profile layer.

The minimum profile report includes:

- substrate lesson completeness;
- withheld-composition accuracy;
- capacity curve and minimum complete retained structure;
- abstention correctness below that capacity;
- matched distractor decrement;
- snapshot replay agreement; and
- cross-thought leakage.

The profile must report its exact held-out lesson families and must not score
an exact memorized list as composition generalization.

For any profile containing determinate and underdetermined episodes, binding
thresholds are split into two independently frozen values:

```text
beta_determinate
beta_epistemic
```

A false-ambiguity call on a determinate episode is a determinate-stratum
error. An unsupported assertion on an underdetermined episode is an
epistemic-stratum error. Neither error may be reassigned to the other stratum
to use a more favorable threshold.

## Why this gate exists

A system can appear to remember while relying on a complete event log, an
unbounded pointer structure, durable writes made during the task, or a
retrieval mechanism that never reconstructs the requested content. It can also
recall isolated items while failing to preserve the relations that make those
items useful.

These shortcuts are especially difficult to detect when evaluation asks only
for a final answer. A valid test must require intermediate manipulation, vary
load and retention interval independently, introduce controlled competition,
and inspect what remains available after eviction, expiration, snapshot
restore, and thought termination.

## Motivation

The gate therefore measures whether a system can:

- maintain a finite, auditable transient workbench;
- manipulate retained items rather than merely repeat them;
- preserve role-filler, feature, and relational bindings;
- benefit from legitimate lossless chunking without hiding capacity;
- distinguish decay from interference and distractor-task failure;
- make calibrated retention and eviction decisions;
- reconstruct retained content without dereferencing an unbounded log;
- prevent completed thoughts from influencing later thoughts; and
- reproduce decisions after snapshot restoration.

## Purpose

This gate tests whether Protama can use transient state as a manipulable
workbench across cognitive operation cycles without making every intermediate state durable.

For this gate, a **cycle** is one externally prompted cognitive operation
transition, such as observe, compare, verify, or synthesize. It is not a lesson
cycle, a probe schedule, or a consolidation cycle.

A **thought** is one evaluator-delimited episode: it begins when the evaluator
issues the episode task and ends at the required final decision or an explicit
abort. All retained state created for that episode is thought-local unless the
episode explicitly authorizes a promotion event. A cycle is an operation within
that thought.

## Scope

The evaluator supplies the task and requires a bounded sequence of operations.
Protama does not need autonomous thought or self-generated goals.

### Scope and non-claims

This gate measures bounded transient retention and manipulation under controlled
load. It is not a test of a fixed biological item limit, Baddeley's component
architecture, consciousness, autonomous motivation, or general intelligence.
A system that passes may have demonstrated an important component of intelligent
behavior without demonstrating any of those broader properties.

## Public benchmark package

A complete public release should contain:

```text
benchmark/
    generators/
    binding_types/
    recodable_loads/
    nonrecodable_loads/
    distractors/
    scoring/
    leakage_checks/
    replay/
baselines/
protama_adapter/
configs/
results/
reports/
tests/
README.md
```

The package must include the generator version, scorer version, baseline
versions, configuration hash, random seeds, memory-accounting convention, and
replay artifacts for every published result.

The canonical CPU Protama calibration path is the fully inspectable reference
implementation on the CPU execution path. It must not substitute GPU kernels
or introduce substrate-induced nondeterminism; its source version,
configuration, interpreter, and hardware identity are recorded.

## Reference evaluation workflow

The reference workflow is:

```text
1. select a locked benchmark configuration;
2. verify the declared memory and latency accounting;
3. initialize the system from the declared snapshot;
4. run Phase 1 capacity calibration without distractors using the canonical
   CPU Protama implementation;
5. freeze the canonical breakpoint, common load grid, recoding annotations,
   calibrated distractor loads, and the complete profile manifest;
6. if adaptive retention is enabled, run only the registered development
   adaptation episodes, then freeze the resulting policy snapshot before any
   held-out episode;
7. run Phase 2 held-out distractor, interference, decay, binding, and
   cross-thought trials;
8. capture state manifests, provenance, decisions, and resource traces;
9. run registered baselines, controls, and ablations;
10. execute snapshot and deterministic-replay checks;
11. calculate preregistered metrics and confidence intervals;
12. emit human-readable and machine-readable reports.
```

An evaluation must record:

```text
gate version
generator version
scorer version
system version or commit
configuration hash
episode seeds
backend and hardware
initial snapshot identity
final snapshot identity
memory-accounting convention
threshold-set identity
profile identity and meta-freeze record
curriculum or lesson-manifest identity and SHA-256 hash, when applicable
adaptation protocol identity and frozen policy fingerprint, when applicable
```

Development runs may use visible generators and exploratory loads. Final
evaluation runs must use an independently held-out generator or locked test
manifest. Development and pilot results must remain labeled as development
evidence.

If adaptive retention is enabled, the held-out runner restores a frozen
development policy snapshot and rejects every outcome update. It must report
the policy identity (a SHA-256 fingerprint of the canonical policy snapshot),
the complete adaptation protocol (episode order, epoch count, reward values,
and update timing), update-attempt count, and any protocol failure. A
successful held-out update is a failure of the evaluation protocol, not an
episode exclusion.

For a grounded profile, the lesson manifest is part of the frozen initial
state. It must enumerate every vocabulary, syntax, association, composition,
negative, and abstention lesson. Teaching anything after the freeze and
before or during held-out evaluation is contamination, not adaptation, and
invalidates the run.

## Evaluation unit

Each episode contains:

```text
task
ordered operation opportunities
items to retain
relations to bind
distractors
capacity condition
manipulation requirement
snapshot point
required final decision
expected epistemic state for any underdetermined binding
```

The episode must include the profile's declared manipulation trial. For a
complex-span profile, this is a compare, transform, or bind operation while
items are held. For grounded symbolic composition, it is a withheld symbolic
query whose answer requires retained symbols and learned composition. The
profile manifest must state which manipulation is being tested and which
items are independently necessary.

An episode's required final decision must distinguish determinate from
underdetermined tasks. When the registered evidence does not establish a
unique answer, a declared abstention, uncertainty response, or clarification
request may be the correct decision. This is a property of the episode's
expected outcome, not a requirement to use any particular internal
architecture. Binding evaluation distinguishes determinate binding from
epistemic handling: determinate episodes require the correct relation
arguments, while underdetermined episodes require the manifest-declared
supported, partial, ambiguous, contradicted, or unknown state without
unsupported assertion. A system cannot pass by abstaining on determinate
episodes or by declaring every episode ambiguous; determinate coverage and
false-ambiguity errors are reported and included in the binding decision
criteria. Where an episode declares multiple supported interpretations, future
held-out versions must also score whether the reported alternatives match the
manifest-supported alternatives, not merely whether the response uses the word
"ambiguous".

Binding trials must identify the binding type being tested: role-filler
bindings, feature bindings, or relational bindings. Loads must include both
recodable items (where a stated rule permits lossless chunking) and
non-recodable items (where each item or relation remains independently
necessary).

## Required behavior

Protama must:

- retain only bounded transient state;
- retrieve retained items by thought and generation, meaning it must
  reconstruct the requested item or relation from the retained representation,
  not dereference an index into an unbounded buffer or event log;
- manipulate retained items while preserving identity and relations;
- bind relations to the correct arguments under load;
- resist distractor replacement where capacity permits;
- evict or decay state when capacity is exceeded;
- distinguish holdover from active thought and durable memory;
- preserve provenance for retained and evicted items; and
- reproduce behavior after snapshot restoration.

Transient state may be compressed or chunked. Chunking is legitimate when the
compressed representation is lossless for the stated task and its size is
charged against the same memory budget. It is not legitimate when it silently
stores independently necessary non-recodable items, relations, or an
unbounded replay pointer. The harness must report performance separately for
recodable and non-recodable loads.

## Formal evaluation quantities

For episode \(e\), let \(L_e\) be the number of independently necessary items
and relations, \(T_e\) the retention interval in cognitive operation cycles,
and \(D_e\) the distractor load. Let \(Y_e\) be the required decision and
\(\hat{Y}_e\) the system decision. Let \(M_e\) be peak transient-state
footprint under the declared accounting convention.

The basic decision accuracy is:

$$
A(L,T,D)=
\frac{1}{|E_{L,T,D}|}
\sum_{e\in E_{L,T,D}}
\mathbf{1}[\hat{Y}_e=Y_e]
$$

The supported capacity \(K_{\mathrm{supported}}\) is the largest independently
necessary load whose lower confidence bound meets the preregistered criterion
\(a_{\min}\), estimated from the no-distractor capacity series. The next
tested load is reported as the first failing load when it is observed. If the
next failing load is not observed, the supported capacity is right-censored;
the tested maximum must not be presented as a measured failure breakpoint.

The current proposal for \(a_{\min}\) is `0.75` episode-level binding
accuracy, using the lower endpoint of a two-sided 95% episode bootstrap
interval. This remains a proposal until the threshold record is accepted and
frozen; it is not a gate result.

For matched distractor and no-distractor conditions, define distractor
decrement as:

$$
\Delta_D(L,T)=A(L,T,0)-A(L,T,D)
$$

For matched target-only and competing-item conditions, define interference
error as the proportion of target failures attributable to a changed
competitor or relation, not merely to the presence of an additional task.

Every episode must preserve the distinction between:

```text
item identity
binding identity
binding arguments
retention status
eviction status
expiration status
durable-promotion status
```

These fields are scored separately. A correct final answer does not erase an
incorrect intermediate binding, unauthorized promotion, or leakage event.

## Episode and condition design

The generator must include:

- load series spanning below, near, and above the measured breakpoint;
- fixed-load interval series for decay;
- fixed-interval load series for capacity and interference;
- target-only, distractor-only, and competing-target conditions;
- role-filler, feature, and relational binding trials;
- item permutations and relation reversals;
- recodable and non-recodable item families;
- snapshot points before and after at least one manipulation; and
- thought-boundary probes with overlapping surface vocabulary but disjoint
  episode identities.

No condition may be scored as evidence for two causal explanations when its
design cannot distinguish them. In particular, interval must vary at fixed
load for decay estimates, and load must vary at fixed interval for
interference estimates.

## Primary metrics

Metrics are reported in two groups. **Core metrics** are required for every
profile. **Profile metrics** are required only when the declared profile
instantiates them.

Core metrics are:

- **Capacity curve:** decision accuracy and principled abstention as a
  function of independently necessary retained structure;
- **Distractor resistance:** matched accuracy change after adding irrelevant
  material;
- **Cross-thought leakage:** influence from completed thoughts without
  authorized promotion;
- **Snapshot replay equivalence:** decision-identical behavior after restore;
- **Eviction and expiration correctness:** whether unavailable information is
  treated as unavailable; and
- **Transient accounting:** charged footprint, provenance, and latency.

For the `grounded-symbolic-composition` profile, the required profile metrics
are:

- **Substrate completeness:** all declared symbols and syntax lessons are
  present before evaluation;
- **Withheld-composition accuracy:** correct result tokens for compositions not
  taught verbatim;
- **Capacity-aware abstention:** no unsupported result when a required symbol
  or relation has been evicted; and
- **Symbolic replay:** identical result token and epistemic state after
  snapshot restoration.

The following legacy/profile metrics remain required only for profiles that
instantiate them:

- **Capacity curve:** exact decision accuracy as a function of independently
  necessary load, measured at fixed retention interval and without distractors.
  Report the full load-response curve and the fitted breakpoint at which
  accuracy first falls below the preregistered criterion; do not assume a
  particular functional form.
- **Complex-span accuracy:** proportion of trials on which the final decision
  is correct after the required compare, transform, or bind operations, with
  item identity and relation errors reported separately.
- **Binding accuracy:** proportion of role-filler, feature, and relational
  bindings reproduced with the correct arguments, conditioned on the relevant
  items being retained.
- **Distractor resistance:** accuracy on distractor trials minus accuracy at
  the same load and interval without distractors, reported at calibrated
  loads relative to the measured capacity breakpoint.
- **Interference error:** an incorrect response caused by a competing item or
  relation replacing, confusing, or misbinding a target, measured by comparing
  matched target-only and interference conditions. A failure caused by the
  distractor task itself, without target competition, is a distractor failure,
  not an interference error.
- **Decay curve:** accuracy as retention interval increases at fixed load and
  with no competing material. This is dissociated from interference by varying
  load at a fixed interval in a separate condition.
- **Replacement and eviction correctness:** precision and recall of the
  state-selection policy: whether items that should remain are retrievable and
  items that should be evicted or expired are absent, including provenance for
  each decision.
- **Cross-thought leakage:** proportion of trials in which an item, relation,
  or actionable influence from a completed thought affects a later thought
  without an authorized durable promotion. The denominator and item identity
  are recorded per boundary.
- **Promotion error rate:** unsupported durable-write events divided by all
  attempted durable-write events, with unauthorized writes counted as errors.
  Report zero attempted writes separately; do not treat an undefined rate as
  zero error.
- **Snapshot replay equivalence:** agreement between original and restored
  runs on retention, retrieval, manipulation, eviction, and final decision
  outcomes under the same seed and inputs. The contract requires
  decision-identical behavior, not bit-identical internal memory layout.
- **Memory and latency cost:** peak transient-state footprint and operation
  latency, measured with the same accounting and hardware configuration for
  every system and baseline.

## Controls

Compare against:

- unlimited-memory reference;
- no-holdover baseline;
- FIFO retention;
- random retention;
- relevance-aware retention; and
- an oracle retention policy.

Include item-permutation controls and relation-reversal controls.

## Promotion boundary

This gate does not decide which experience deserves durable memory. A
promotion is **supported** here only when the episode explicitly authorizes a
durable write and supplies the authorization and provenance record; rehearsal,
frequency, value, or apparent usefulness alone is not support. The gate scores
unauthorized or unproven writes as promotion errors and hands an authorized
promotion, with its provenance, to the Evidence Promotion and Memory
Consolidation Gate. That gate begins at the consolidation boundary and owns
the quality of the durable transformation, so the two gates do not double-count
promotion quality.

Promotion dispositions are scored by episode condition: supported evidence
must be promoted with provenance; contradicted evidence must be rejected while
its contradiction record remains visible; uncertain evidence must abstain or
remain explicitly pending; and missing-evidence cases must be rejected or
deferred. Forced promotion in either of the latter three conditions is an
error. Maintenance must preserve an explicitly supported item through its
registered interval, while natural expiration, replacement, and supersession
must produce their declared non-retrievable or replaced outcomes.

## Calibration and threshold procedure

Use two stages. In **Phase 1**, use development episodes to measure the
canonical CPU Protama capacity curve, select the common load levels and
distractor fractions (below, near, and above the fitted breakpoint), validate
the recodable and non-recodable generators, estimate uncertainty, and freeze
the scoring code, thresholds, seeds, hardware budget, and baseline policies.
The held-out CPU Protama, GPU Protama, and baseline runs use this same
calibrated manifest; they do not receive separate favorable calibration.
Capacity curves for the other systems are reported diagnostically. “Where
capacity permits” therefore means a preregistered common load at or below the
canonical breakpoint, not a post-hoc judgment.

Recodable loads must declare a lossless, task-authorized encoding and charge
the encoded representation, decoder, and relation metadata against the same
budget. Non-recodable loads must keep each independently necessary item and
relation reconstructible. The manifest and report must identify the two
conditions separately, so legitimate compression cannot inflate the reported
item capacity. The charged footprint must be the actual runtime representation
measured during execution, including instantiated encoder/decoder state and
metadata, rather than a theoretical minimum.

In **Phase 2**, run untouched held-out episodes using the frozen procedure.
The preregistration must specify numeric minimums or maximums for the core
metrics and for the declared profile metrics. The former fixed nine-field set
remains available as the `legacy-relational-manipulation` profile; it is not
automatically gating for a profile that does not instantiate complex span or
the corresponding binding family. Interference, decay, leakage, CPU/GPU
equivalence, and other condition-level outcomes must still be reported, with
leakage and uncharged storage remaining mandatory validity conditions. Report
confidence intervals and abstentions; a threshold is not met by omitting
difficult trials.

Each numeric threshold must also include a baseline-anchored justification:
development performance for the strong non-oracle baselines, development
performance for the oracle baseline, the proposed value and uncertainty, and
one line explaining why the value discriminates the target capability rather
than merely describing Protama's own development curve. These justifications
are part of the versioned freeze record and must be completed for every
numeric threshold before held-out results are inspected.

### Policy-value extension

When a learned retention or selection policy is being evaluated, the gate
also reports its value relative to a registered non-learning baseline on the
same episodes. The comparison is condition-stratified by capacity, distractor
load, and evidence regime; pooled averages must not conceal a regression in a
harder condition.

The primary registered baseline is the strong non-oracle
**relevance-aware retention** policy. FIFO retention remains a required
secondary regression control because a learned policy must not be credited
with improvement while performing worse than a simpler recency policy.

For condition \(c\), define policy gain as:

$$
G_c = A_{\mathrm{policy},c} - A_{\mathrm{baseline},c}
$$

The proposed extension field is `gamma_policy_regression_max`, the maximum
permitted negative lower-confidence-bound gain. A candidate learned policy
must satisfy:

$$
\operatorname{LCB}_{95}(G_c)
\geq -\gamma_{\mathrm{policy\_regression,max}}
$$

for every registered condition. A value of zero requires the learned policy to
be no worse than the baseline; a negative lower bound is a regression even if
the absolute binding threshold passes. Positive improvement is reported
separately and is not assumed merely because a learned policy is present.

This extension does not replace absolute binding correctness. It prevents
additional learned machinery from being called an improvement when a simpler
policy performs better. The baseline, condition grid, gain statistic,
confidence procedure, and candidate value must be registered before final
held-out evaluation.

The held-out run evaluates a frozen snapshot of the learned policy. The
development phase tests whether the policy can learn from delayed outcomes;
the held-out phase tests the frozen retention behavior and the integrity of
the learning boundary. It does not claim to evaluate a live learner that
continues updating during the test.

## Pass conditions

A pass requires:

- bounded memory use;
- successful manipulation for the declared profile, with the registered
  baseline comparison where a learned policy is being evaluated;
- a preregistered capacity curve with measurable degradation when capacity is
  exceeded;
- profile-correct abstention or uncertainty when required retained state is
  unavailable;
- correct eviction and expiration;
- no cross-thought leakage;
- no unsupported promotion to durable state; and
- decision-identical replay of retention, retrieval, and final decisions.
- no condition-level regression beyond the registered policy-value limit when
  learned retention or selection is enabled.

## Pass rule

The gate must use preregistered component thresholds rather than one averaged
score. Every profile must pass the shared invariants and every threshold
declared by that profile. A profile may not add or remove thresholds after
held-out results are inspected.

$$
\operatorname{PASS}
\iff
\begin{cases}
\text{all shared invariants pass} \\
\text{all declared profile thresholds pass} \\
\text{no critical leakage or uncharged storage detected}
\end{cases}
$$

For the `grounded-symbolic-composition` profile, the declared thresholds must
cover at least:

```text
withheld-composition accuracy
capacity-aware abstention correctness
matched distractor decrement
snapshot replay agreement
cross-thought leakage
```

For the `legacy-relational-manipulation` profile, the nine-field threshold
set remains available: capacity breakpoint, complex-span accuracy, binding
accuracy, distractor decrement, eviction/expiration error, promotion-error
rate, replay agreement, transient footprint, and latency. Those thresholds
are gating only when that profile is declared.

Interference, decay, CPU/GPU decision-equivalence rate, and condition-level
curves remain mandatory diagnostics unless a profile explicitly promotes them
into its frozen threshold set. The leakage and uncharged-storage conditions
are mandatory validity conditions for every profile.

The policy-value extension is an additional gating validity condition whenever
learned retention or selection is enabled. It is inactive for a declared
non-learning reference configuration.

### Threshold schema

When a profile evaluates both determinate and underdetermined episodes, its
freeze record must contain separate fields:

```text
beta_determinate: minimum determinate binding accuracy
beta_epistemic: minimum epistemic-state accuracy
```

The determinate interval includes false-ambiguity errors. The epistemic
interval includes unsupported assertions on underdetermined episodes. A single
`beta_binding` value is not a valid substitute for these two strata.

The public report must include raw metrics, condition-level metrics, confidence
intervals, failures and abstentions, excluded episodes and exclusion reasons,
the declared profile, the exact pass-rule version, and the justification for
each profile threshold.

## Additional optional epistemic-precision profile

The core gate does not require a particular theory of inference beyond the
state-aware binding decision contract. A system may submit an additional,
non-gating epistemic-precision profile to demonstrate
that it distinguishes evidence-supported claims from associations or
underdetermined interpretations. The profile may report, where applicable:

- correct abstention on underdetermined episodes;
- unsupported-assertion rate;
- ambiguity and contradiction recognition;
- partial-structure recognition;
- inquiry or clarification quality;
- separation of local linguistic correctness from unsupported global claims.

Inquiry quality is decomposed into action correctness, exact missing-role
identification, complete candidate enumeration, and message evidence. A
generic uncertainty response is not equivalent to a useful clarification.
For gate v1, epistemic scoring is explicitly state-only: the manifest-declared
supported, partial, ambiguous, contradicted, or unknown state is the required
epistemic output. Candidate enumeration and inquiry-message quality are not
silently credited. If a future profile claims those outputs, their trace
fields, scoring rules, baselines, and thresholds must be frozen in the same
meta-freeze record before held-out evaluation; otherwise they are not part of
the claim.

These results are extra evidence and must not replace the core metrics,
retroactively change pass conditions, or exclude difficult core episodes. A
future gate version may promote profile metrics only after independent task
definitions, baselines, and held-out evidence are available.

## Baselines

The benchmark must include:

1. **Unlimited-memory reference:** estimates task performance without a
   capacity constraint.
2. **No-holdover baseline:** clears transient state between every operation.
3. **FIFO retention:** tests whether recency alone explains retention choices.
4. **Random retention:** provides a lower policy baseline.
5. **Relevance-aware retention:** provides the strong non-oracle policy baseline.
6. **Oracle retention policy:** receives the episode's required future targets
   and provides an upper-bound reference.
7. **Inspectable CPU Protama:** tests the reference implementation.
8. **GPU Protama:** tests the accelerated implementation under evaluation.
9. **Matched policy-value comparison:** compares the evaluated learned policy
   with the registered baseline on identical episode realizations and reports
   condition-level gain and confidence bounds.

CPU and GPU versions must be compared for behavioral equivalence on the shared
contract, substrate-induced capacity differences, memory accounting, and
snapshot replay.

The shared decision contract must define score comparison at execution
precision: a registered epsilon, deterministic ordering among scores within
that epsilon, and the abstention behavior for unresolved ties. CPU and GPU
must implement that comparator themselves. A calibration harness may align
inputs, but it must not normalize or rewrite outputs after either substrate
has made its decision.

## Ablation plan

At minimum, run ablations that remove or replace:

- transient-state compression;
- chunk formation;
- provenance tracking;
- relevance scoring;
- explicit eviction;
- decay or expiration;
- binding-specific storage;
- distractor detection;
- snapshot restoration; and
- thought-boundary clearing.

The critical chunking ablation compares recodable and non-recodable loads. A
system must not pass by compressing away independently necessary relations or
by replacing the workbench with a replayable event log.

## Leakage and validity rules

A run must be rejected or separately labeled if the system receives any
unpermitted path to the target state or answer, including:

- the complete event log as a freely queryable memory;
- an uncharged pointer to evicted or future items;
- durable writes made without an episode authorization;
- future target identities or relation answers;
- held-out episodes or labels before final scoring;
- a hidden capacity value or threshold;
- a thought identifier that exposes the required response; or
- a benchmark-specific output token that encodes retention status.

The evaluator must record not only whether the final answer was correct, but
whether the path to that answer respected the declared capacity, provenance,
and thought boundary.

## Statistical and reproducibility protocol

The final benchmark should include, at minimum:

```text
independently generated episode families
multiple evaluation seeds, or a deterministic equivalent
separate development and final-test generators
95% confidence intervals from 10,000 episode-level bootstrap resamples using
seed 1729
locked final-test generator
preregistered pass thresholds
complete snapshots and state manifests
decision-identical replay artifacts
```

Exact sample counts may be revised after a power analysis, but the protocol
must be fixed before final evaluation. Resample complete episodes within
condition strata, not individual operations. Minimum thresholds use the lower
95% bound; maximum thresholds use the upper 95% bound, including the upper
bound of p95 latency and peak transient footprint. A model failure, timeout,
abstention, contradiction, promotion rejection, or poor outcome is not an
exclusion. Only preregistered harness or infrastructure failures with saved
traces may be excluded.

## Failure conditions

The gate fails if Protama:

- silently expands capacity;
- retains only independent items but cannot manipulate them;
- loses relation bindings under load;
- retrieves evicted state as if it were present;
- leaks state between thoughts;
- uses an uncharged chunk or replay pointer to bypass the memory budget;
- changes behavior after restore; or
- treats the entire event log as working memory.

## Non-claims

Passing does not establish human working memory, Baddeley's component
architecture, or a fixed biological item limit. It establishes bounded,
manipulable, auditable transient state.

## Expected objections and responses

### “The gate was changed after seeing the result.”

Profile alignment is not a post-hoc threshold exemption. The parent
capability and its shared invariants remain unchanged. The revision makes the
task-to-metric mapping explicit before a profile's final held-out run. The
older nine-field relation battery remains preserved as a separate historical
profile and is not relabeled as a pass.

### “Readable labels such as `inert` are preloaded English knowledge.”

A readable token is not a built-in definition. The profile records the lesson
that establishes the token and its role. If English semantics are claimed,
they require a separate language-mediated profile. The symbolic profile can
be evaluated without English comprehension.

### “Grounded” means sensorimotor grounding.

Not in this gate version. **Grounded** here means operationally grounded in a
declared lesson curriculum before evaluation: the system is taught the symbol
inventory, syntax, and associations that define the task. It does not claim
physical, sensorimotor, or human-world grounding. Those claims require a
separate profile and evidence.

### “A withheld list may be trivial memorization.”

The scorer must distinguish exact list lessons from withheld compositions.
Held-out lists must vary structure, length, and member composition. Exact
matches are reported separately and do not count as composition
generalization.

### “A capacity of seven is arbitrary.”

The profile reports the complete load structure, charged representation, and
the full capacity curve. The capacity is an empirical result for that
representation and task, not a claim about a universal item limit.

### “The evaluator already knows the relations.”

Expected relations may exist in the manifest for scoring, but they must not be
provided to the system as relevance flags, future target identities, or answer
tokens. The final report must separate evaluator-owned expected outcomes from
runtime inputs and reject any leakage path.

### “A symbolic profile does not prove general intelligence.”

Correct. The gate claims bounded transient manipulation for the declared
profile. Additional profiles are required for language, other binding types,
or broader generalization claims.

## Public reporting standard

Any claimed result should publish:

- the exact gate version and threshold set;
- the episode generator or complete episode manifest;
- all baseline and Protama outcomes, including failures and abstentions;
- capacity, accuracy, interference, promotion-error, latency, and memory
  measurements, stratified by binding type and recodable versus non-recodable
  load;
- thought boundaries, promotion authorizations, and provenance records; and
- enough metadata to reproduce decision-identical snapshot and restore
  comparisons.

Development observations must remain labeled as development evidence until the
thresholds and matched controls are frozen.

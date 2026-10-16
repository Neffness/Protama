# Gate Work 06 — Dictionary to Structural Interpretation

Status: **DEVELOPMENT INTEGRATION PROBE**

This checkpoint records whether dictionary context can reach reusable
structural interpretation, rather than treating dictionary context as an
isolated lookup result.

## Probe result

The original path behaved as follows:

```text
dictionary context selection: succeeds
generic relation recognition of the same definition: abstains
direct structured-family application: unavailable from the selected context
```

The canonical
[ProtomaDictionaryTraining.py](../../Tools/ProtomaDictionaryTraining.py)
path now preserves dictionary context and publishes the selected observations
to learned surface-relation memory. Surface-derived hypotheses now carry
candidate provenance and route through Protama's existing learned
structural-family selector.

The probe demonstrates:

```text
wrapped dictionary prompt
    -> dictionary context selection
    -> selected relation observations
    -> candidate-backed relation hypothesis
    -> variable-bound family selection
    -> accepted structural decision
```

The active dictionary experiment now exercises the learning boundary after
the initial curriculum:

```text
uncorrected pass: 41 entries learned, stop at Abada (entry 42)
correction: generic noun definition with direct equivalence
corrected pass: 48 entries learned, stop at Abaist (entry 49)
```

The second stop is a new unresolved grammatical pattern, not the original
failure repeated. This provides a measurable progress signal for future
learning and gate-integration work.

The first development bridge adapter now also exercises the ordinary
recognition path:

```text
dictionary surface/context training
    -> family induction from two dictionary examples
    -> held-out natural-language wrapper with new vocabulary
    -> accepted structural-family decision
    -> incomplete near-miss rejected
```

This is a development bridge only. It does not use the locked independent
generator and must not be presented as final gate evidence.

The canonical `run_all_gates_and_training` curriculum now executes the
dictionary stages in this order:

```text
intrinsic patterns
    -> dictionary vocabulary registration and word transitions
    -> foundation and language curriculum
    -> dictionary POS/type and typed-definition transitions
    -> remaining lexical, conversation, and structural training
    -> active word-by-word dictionary definition lessons
```

The current integrated pulse check processed 172,785 dictionary entries for
vocabulary registration, trained 172,780 dictionary word definitions, taught
all eight observed grammatical types, and reached the active-definition
question at `Abada` after 41 learned entries.

The active dictionary traversal is now versioned as
`dictionary-active-v1`. It uses deterministic dictionary-file ordering and
source-line ordering, with an optional entry cap for reproducible development
subsets. The canonical run-all uses the uncapped version.

Sequential correction transfer currently moves the development boundary:

```text
no corrections:       Abada       (entry 42)
Abada correction:     Abaist      (entry 49)
two corrections:      Abalienate  (entry 50)
```

This is evidence that corrections can expose later unresolved patterns. It
is not yet held-out transfer evidence because the corrections and evaluation
sequence are drawn from the same ordered development corpus.

Held-out word transfer is now covered for the noun-equivalence pattern:

```text
correction word: Abada -> means rhinoceros
held-out word:   Abaisance -> inferred means obeisance
reused pattern:  generic noun definition with direct equivalence
```

The held-out words are not supplied as corrections. The expanded development
set includes `Abaisance`, `Abacination`, `Abrasion`, and `Accedence`, while
an adjective case is used as a negative type-control. The correction and
evaluation words are now enforced as disjoint subsets by the benchmark
split helper. Development coverage now repeats the split across regions `A`,
`B`, and `C`, with separate correction words and held-out evaluation words.
A larger preregistered confirmatory run is still pending.

The versioned regional transfer runner now covers six held-out cases:

```text
benchmark: dictionary-transfer-v1
cases:     6
transferred: 6
rate:      1.00
bootstrap: [1.00, 1.00]
seed:      1729
resamples: 10000
```

The degenerate interval reflects a perfect six-case development result and
should not be interpreted as broad statistical evidence. A confirmatory
preregistered run remains separate.

The frozen confirmatory development run is now implemented as
`dictionary-transfer-confirmatory-v1`:

```text
manifest fingerprint: b19e9b027e212b28b5f3e2188fc8d9333acae9c57f739bcdeb6594439c135efb
leakage checks:       pass
positive cases:       6/6 transferred
negative controls:    3/3 rejected
positive bootstrap:   [1.00, 1.00]
negative bootstrap:   [1.00, 1.00]
```

This remains development evidence rather than publication-grade statistical
evidence because the case count is small and every outcome is perfect.

The automated family-validation pass covered all `172,785` dictionary
entries. It found the expected candidate populations:

```text
known noun / alias:          4,308
agent noun:                  3,327
action noun:                 1,911
object used for purpose:       100
class plus alias:               32
```

It detected `24,908` headwords with multiple senses. Different source lines
are retained as separate senses, including when their family labels differ.
The full scan finds 168 headwords with this valid cross-family sense
variation; these are not contradictions requiring human review. The automated
exception queue is therefore empty. Classifier quality will be evaluated
through held-out positive and negative family pools instead of asking a human
to review legitimate multi-sense words.

The first deterministic pool builder is implemented in
`Tools/Protama/dictionary_family_pools.py`. It selects distinct positive
words for each reviewed family, selects word-disjoint negative controls, and
retains three natural-language wrapper templates for later routing tests.
These pools are development fixtures; they are not yet the final
preregistered gate evaluation.

The first normalized wrapped benchmark evaluates 45 held-out positive cases
and 75 negative controls across three natural-language wrapper templates. A
conservative normalizer removes only a separable framing clause, preserves the
original input, and passes the content clause to the dictionary family
analyzer. It classified all 45 positives and rejected all 75 negative
controls. This is still not a raw-router pass: direct relation extraction
is supplemented by the `recognize_and_select_structural_family` API fallback
only after raw relation recognition abstains. The raw relation path remains
first, and the fallback records normalized dictionary evidence separately. The
benchmark therefore checks reusable family application rather than comparing
pattern strings alone.

Fallback safety is covered separately in
`Tools/Protama/tests/test_dictionary_fallback_guards.py`: inputs without a
safe wrapper boundary abstain, unrelated wrapped content does not select a
family, and competing identical families produce an abstention instead of a
forced commitment.

Correction transfer is covered by
`Tools/Protama/tests/test_dictionary_correction_routing.py`. A supervised
correction is combined with one additional family example, and a held-out
word is accepted through the normalized main selection API without receiving
its own correction.

The regional version is implemented in
`Tools/Protama/dictionary_correction_routing_benchmark.py`. Across regions A,
B, and C, one correction transfers to two held-out compatible words under
three wrappers, while adjective controls remain rejected:

```text
positive transfer: 18/18
negative rejection: 9/9
surface cases: 27
```

The manifest fingerprint is
`a10837b9140eceed6aa2e6e0c932b904c0a6d8865ae934c06722fdb48398aa47`.
Leakage checks pass. Both deterministic 10,000-resample bootstrap intervals
are `[1.00, 1.00]`; this is reproducibility metadata for the small
development set, not broad statistical evidence.

A larger frozen family manifest is now generated by
`Tools/Protama/dictionary_family_manifest.py`. It contains 10 positive and 10
negative words for each of the five reviewed families, across the same three
surface templates. Its fingerprint is
`61d131eb5cae383dbd0ccb6d61f1b032706fed714e061151eab47729bd747660`.
The manifest is leakage-free and deterministic; it is ready to serve as the
input contract for the next scoring run.

The frozen-manifest scoring run completed without changing the cases:

```text
positive transfer: 120/120
negative rejection: 150/150
surface cases: 270
```

This is still development evidence. The manifest uses analyzer-derived family
labels and must not be presented as an independent gold-labelled confirmatory
gate set. The deterministic bootstrap intervals are `[1.00, 1.00]` for both
aggregate positive transfer and aggregate negative rejection. Each of the five
families also scored `1.00` on both measures, so the aggregate result is not
hiding a family-specific failure. Confidence-aware counters were also zero:
there were no positive abstentions, no low-confidence positive decisions, no
negative false commitments, and no low-confidence negative decisions.

Multi-sense ambiguity is covered by
`Tools/Protama/tests/test_dictionary_multisense_ambiguity.py`. The noun sense
of `Araneidan` selects the class-plus-alias family, its adjective sense does
not force that family, and a prompt containing only the headword abstains.

Adversarial surface behavior is covered by
`Tools/Protama/tests/test_dictionary_adversarial_surfaces.py`: punctuation
variants remain accepted, incomplete and reordered inputs do not force a
family, irrelevant trailing clauses are not silently ignored, and multiword
subjects remain supported.

Canonical `run-all-gates-and-training` now runs three separately labelled
companion pulse checks before cache reuse:

```text
dictionary-family-companion-check=pass positive=120/120 negative=150/150
dictionary-correction-companion-check=pass positive=18/18 negative=9/9
dictionary-independent-gold-check=pass accepted=10 rejected=5 false_commitments=0
```

These checks can fail the development run if they regress, but they do not
alter or inflate the Structural Gate score.

An additional independently labelled D/E/F regional holdout is now available
through `dictionary_independent_regional.py`. It contains 15 positive and 15
negative sense-level cases with disjoint `(word, part of speech, source line)`
identities. Transfer from the approved gold training senses accepted all
15/15 regional positives and rejected all 15 negative controls, with zero
false commitments. The negative controls were corrected to ensure that they
are both sense-disjoint from the positives and incompatible with the target
family; earlier provisional controls had accidentally reused positive senses
or assigned a case to its own family and are not valid evidence.

## What this proves

- Dictionary context is not inherently incompatible with structural memory.
- The selected dictionary observations can drive family application.
- The canonical integration is covered by a deterministic regression test.
- Surface-derived candidates preserve enough spans and evidence for family
  selection.
- A supervised dictionary correction can move the active learning boundary
  to a later, different pattern.
- Dictionary-trained surface memory can reach a gate-style structural
  decision on held-out vocabulary in the development bridge adapter.

## What this does not prove

- Generic relation parsing can extract every dictionary definition.
- Arbitrary natural-language wrappers are understood without dictionary
  context selection.
- Every production `run_all` dictionary path has not yet been audited for
  contextual teaching coverage.
- Natural-language operation/tool selection is solved.

Current validation:

```text
94 tests
93 passed
1 intentionally skipped
```

The Structural Induction and Transfer Gate remains **NOT PASSED**.

# Crossing the First Gold Gate

## Publication brief

### Central claim

Protama has crossed its first independently evaluated structural-learning
benchmark. On a frozen, explicitly labelled gold subset, the system learned
five reusable dictionary-definition families from training examples and
applied those family abstractions to held-out senses through the main routing
API.

This is evidence of learned structural transfer rather than exact
sentence-replay alone. The benchmark did not require prompts to contain
explicit family labels such as `known-noun:` or `word-problem:`.

### Why this benchmark matters

The original design concern was that Protama might only answer familiar
sentences or specially formatted prompts. The first gold gate tests a more
substantive capability:

1. expose the system to labelled examples of a reusable structural pattern;
2. present held-out dictionary senses, including natural-language wrappers;
3. require the system to select or reject the learned family;
4. score the result against labels fixed independently of the analyzer.

The benchmark therefore evaluates whether a learned relation can be reused
when the surface wording and lexical item change.

### Benchmark design

The frozen independent gold subset contains:

- 10 positive senses;
- 5 negative senses;
- five structural families;
- explicit labels based on previously reviewed family schemas;
- sense-level identity using word, part of speech, and source line;
- leakage checks between positive and negative cases;
- evaluation through Protama's main structural-family routing API.

The tested families are:

- known noun or alias;
- agent noun;
- action noun;
- object used for a purpose;
- one-of-class plus alias.

Natural-language inputs use wrapper forms such as:

```text
What does X mean? <dictionary definition>
```

The wrapper is not itself the classifier. It provides the conversational
surface while the existing raw relation path and conservative dictionary
fallback perform the interpretation.

### Result

| Measure                           | Result |
| --------------------------------- | -----: |
| Positive cases accepted correctly |  10/10 |
| Negative cases rejected correctly |    5/5 |
| False commitments                 |      0 |
| Sense-level leakage               |   None |

The result is recorded by the independent gold manifest and confusion-matrix
scorer. The canonical development run reports:

```text
dictionary-independent-gold-check=pass accepted=10 rejected=5 false_commitments=0
```

### Interpretation

The appropriate conclusion is:

> Protama demonstrated initial learned structural transfer on an independently
> labelled, frozen gold subset. It correctly accepted held-out positive
> family instances and rejected incompatible instances without requiring
> explicit operator labels in the prompt.

This is the first evidence that the system can move beyond storing and
replaying one exact training sentence. The learned object being reused is a
structural family, not merely a complete surface string.

### What this result does not claim

The first gold gate is deliberately limited. It does not establish:

- broad natural-language understanding;
- arbitrary word-problem routing;
- human-level semantic interpretation;
- universal generalization across the dictionary;
- a passed Structural Gate;
- perfect calibration on larger or more adversarial samples.

The gold subset is small and hand-constructed from reviewed schemas. It is a
first independent benchmark, not a final capability certificate.

### Follow-up regional evaluation

An independently labelled D/E/F regional holdout was added as a harder
diagnostic. It contains 15 positive and 15 negative sense-level cases.

```text
Positive transfer: 15/15
Negative rejection: 15/15
False commitments: 0
```

This follow-up strengthens the first result: positive structures transfer and
the corrected incompatible controls are rejected without false commitments.
The negative controls were explicitly checked for sense-level disjointness
and target-family incompatibility before scoring.

### Recommended publication wording

> We evaluated Protama on a frozen, independently labelled gold subset of
> dictionary-definition senses covering five reusable structural families.
> The evaluation used the system's main routing API and natural-language
> wrappers rather than explicit operator labels. Protama correctly accepted
> all 10 positive held-out cases and rejected all 5 negative cases, with no
> false commitments and no sense-level leakage. These results provide initial
> evidence that the system can transfer learned structural family hypotheses
> beyond exact sentence replay. A subsequent corrected D/E/F regional holdout
> preserved perfect positive transfer (15/15), rejected all 15 incompatible
> controls, and produced 0 false commitments.

### Status

The first independent gold gate has passed. The broader Structural Gate
remains not passed. The project should proceed with harder adversarial
controls, calibration, and abstention work rather than restart the
architecture.

## Change note — 2026-10-16

An earlier version of this brief reported a D/E/F regional result of 7/15
negative rejection and 8 false commitments. That result is withdrawn. An
audit found that several provisional negative controls either reused senses
already present in the positive set or were assigned to the family they
actually represented. Those controls were invalid for the intended
calibration claim.

The D/E/F holdout was corrected to use sense-disjoint, independently labelled
controls that are incompatible with their target families. The corrected
result is 15/15 positive transfer, 15/15 negative rejection, 0 false
commitments, with no sense-level leakage. The earlier failure was a
benchmark-construction error, not evidence of a Protama calibration failure.

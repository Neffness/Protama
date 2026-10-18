# Protama Crosses Its First Gold Gate

## Initial evidence of learned structural transfer in dictionary-definition families

**Project:** Protama  
**Publication type:** Public research preprint  
**Date:** 2026-10-16  
**Status:** First independent gold gate passed; broader Structural Induction and
Transfer Gate not passed

> **Disclosure notice:** This publication reports a narrow benchmark result. It
> does not claim general intelligence, human-level language understanding, or
> completion of the broader Protama Structural Induction and Transfer Gate.

## Abstract

Protama was evaluated on a frozen, independently labelled gold subset of
dictionary-definition senses covering five reusable structural families. The
evaluation used Protama's main structural-family routing API and
natural-language wrappers rather than requiring explicit operator labels in
the input. The subset contained 10 positive held-out senses and 5 negative
held-out senses, with sense identity determined by word, part of speech, and
source line. Protama accepted all 10 positive cases and rejected all 5
negative cases, with zero false commitments and no detected sense-level
leakage.

This result provides initial evidence that Protama can transfer a learned
structural family hypothesis beyond exact sentence replay. The result is
deliberately narrow: the cases are hand-constructed from reviewed family
schemas, the sample is small, and the broader gate's requirements for
large-scale independent generation, abstention, explanation fidelity,
baseline comparison, and robust near-miss rejection remain separate.

An independently labelled regional follow-up provides a broader validation
sample. The corrected holdout preserved perfect positive transfer at 15/15,
rejected all 15 incompatible controls, and produced 0 false commitments. The
next engineering work is therefore harder adversarial controls, confidence
calibration, and abstention rather than a claim of unrestricted structural
generalization.

## 1. Research question

The first gold gate asks whether Protama can reuse a learned structural
relationship when the lexical item and surface wording change.

The motivating concern was that a system might appear to learn while only
answering familiar sentences or prompts formatted with special labels. The
benchmark instead tests the following sequence:

1. expose Protama to labelled examples of a reusable structural pattern;
2. present held-out dictionary senses, including natural-language wrappers;
3. require the system to select or reject the learned family; and
4. score the decision against labels fixed independently of the analyzer.

The intended unit of transfer is a structural family, not a complete surface
string. A positive result is consequently evidence of a limited form of
structural transfer, not evidence that Protama understands arbitrary
language.

## 2. Benchmark design

### 2.1 Evaluation subset

The frozen independent gold subset contains:

- 10 positive senses;
- 5 negative senses;
- five structural families;
- explicit labels based on previously reviewed family schemas;
- sense-level identity using word, part of speech, and source line;
- leakage checks between positive and negative cases; and
- evaluation through Protama's main structural-family routing API.

The tested families are:

1. known noun or alias;
2. agent noun;
3. action noun;
4. object used for a purpose; and
5. one-of-class plus alias.

The positive and negative labels were fixed independently of the analyzer
being evaluated. This separation is important: the evaluator determines the
expected family compatibility, while Protama supplies the decision and its
available evidence.

### 2.2 Natural-language surface

Natural-language cases use wrapper forms such as:

```text
What does X mean? <dictionary definition>
```

The wrapper is not itself the classifier. It provides a conversational
surface while the existing raw relation path and conservative dictionary
fallback perform the interpretation. The benchmark therefore tests the
ability to route a wrapped definition to a reusable family, rather than
testing a string comparison against a prompt label such as `known-noun:` or
`word-problem:`.

### 2.3 Leakage control

Cases are identified at the sense level by the combination of word, part of
speech, and source line. Positive and negative pools are checked for
inappropriate overlap before scoring. The reported gold run found no
sense-level leakage.

The leakage result is scoped to this frozen subset. It is not a substitute
for the larger lexical, structural, template, family, generator, and
temporal split controls specified by the broader Structural Gate contract.

## 3. Results

| Measure | Result |
| --- | ---: |
| Positive cases accepted correctly | 10/10 |
| Negative cases rejected correctly | 5/5 |
| False commitments | 0 |
| Sense-level leakage | None detected |

The canonical development run reports:

```text
dictionary-independent-gold-check=pass accepted=10 rejected=5 false_commitments=0
```

At the level of this frozen subset, the observed positive transfer accuracy
was 100% and the observed negative rejection accuracy was 100%. These
descriptive rates should not be interpreted as population estimates: the
subset contains only 15 scored cases.

## 4. Interpretation

The supported conclusion is:

> Protama demonstrated initial learned structural transfer on an
> independently labelled, frozen gold subset. It correctly accepted held-out
> positive family instances and rejected incompatible instances without
> requiring explicit operator labels in the prompt.

The result is stronger than exact replay when the following interpretation is
kept in view: the learned object being reused is a structural family
hypothesis, while the held-out cases change the lexical item and may change
the surface wrapper. The result does not establish that the system has
invented arbitrary structures or solved unrestricted natural-language
understanding.

## 5. Regional follow-up

An independently labelled D/E/F regional holdout was added as a harder
diagnostic. It contains 15 positive and 15 negative sense-level cases:

```text
Positive transfer: 15/15
Negative rejection: 15/15
False commitments: 0
```

This follow-up strengthens the first gold result: the learned positive
structures transfer and the corrected incompatible controls are rejected
without false commitments. The first gold subset and regional holdout still
remain narrow evaluations, so they do not justify an overbroad interpretation
of the milestone.

The immediate technical targets are:

- harder adversarial negative controls and near-miss coverage;
- confidence calibration for family selection;
- abstention when evidence is insufficient or incompatible;
- reporting risk as a function of coverage; and
- confirmatory evaluation on a larger frozen sample.

## 6. Claim boundary

This publication does **not** establish:

- broad natural-language understanding;
- arbitrary word-problem routing;
- human-level semantic interpretation;
- universal generalization across the dictionary;
- a passed Structural Induction and Transfer Gate;
- perfect calibration on larger or adversarial samples;
- explanation fidelity under the broader gate contract; or
- superiority to the required lexical, nearest-neighbor, symbolic, or
  language-model baselines.

The gold subset is small and hand-constructed from reviewed schemas. It is a
first independent benchmark, not a final capability certificate. In
particular, the result should not be combined with development-only
dictionary-transfer measurements to imply that the full gate has passed.

## 7. Reproducibility and artifact map

The source brief for this publication is:

- [First Gold Gate Publication Brief](../benchmark/structural-transfer-v1/gate-work/07_First_Gold_Gate_Publication_Brief.md)

The relevant public benchmark context is:

- [Structural Induction and Transfer Test](../benchmark/structural-transfer-v1/Protama_Inductive_Structural_Invention_Test.md)
- [Dictionary-to-Structural Integration](../benchmark/structural-transfer-v1/gate-work/06_Dictionary_Structural_Integration.md)
- [Structural Gate Publication Task List](../benchmark/structural-transfer-v1/Protama_Structural_Gate_Publication_Task_List.md)
- [Structural Family Memory Development Update](../reports/development/2026-10-15-structural-family-progress.md)

These artifacts distinguish development integration evidence from final gate
evidence. The independent gold result reported here is limited to the frozen
subset and canonical run identified in the publication brief. A future
confirmatory release should include the frozen case manifest, raw predictions,
leakage report, configuration identity, and deterministic replay command.

## 8. Conclusion

Protama has crossed its first independent gold gate for a narrow dictionary
structural-learning benchmark. On the frozen subset, it transferred five
reviewed structural family patterns to 10 held-out positive senses and
rejected 5 incompatible senses without false commitments or detected
sense-level leakage. The corrected D/E/F regional holdout reproduced that
result at a larger scale: 15/15 positive transfer, 15/15 negative rejection,
and 0 false commitments.

The appropriate next step is not to declare the general Structural Gate
complete. It is to test harder adversarial controls and continue improving
rejection calibration and abstention against larger, independently generated,
replayable evaluation artifacts. The first gold result is a measurable
milestone toward that program: it supports continued structural-learning work
while preserving a clear boundary around what has and has not been
demonstrated.

## Change note â€” 2026-10-16

An earlier version of this paper reported that the D/E/F regional holdout
rejected only 7/15 negative cases and produced 8 false commitments. That
claim is withdrawn. An audit found that several provisional negative controls
either reused senses already present in the positive set or were assigned to
the family they actually represented. They were invalid controls for the
intended negative-calibration claim.

The holdout was corrected to use sense-disjoint, independently labelled
controls that are incompatible with their target families. The corrected
result is 15/15 positive transfer, 15/15 negative rejection, and 0 false
commitments, with no sense-level leakage. The earlier apparent failure was a
benchmark-construction error, not evidence of a Protama calibration failure.

# Gate Work 07 — Surface Relation Learning Experiment

Status: **DEVELOPMENT EXPERIMENT**

This experiment tests whether dictionary-derived semantic observations can
teach reusable surface-to-relation mappings without adding phrase-specific
aliases by hand.

## Method

Training pairs contain:

1. a natural-language definition sentence;
2. evaluator-side relation observations for that sentence.

The learner aligns source and target values, records the intervening surface
phrase, and transfers the learned phrase mapping to a held-out sentence with
new vocabulary.

## Current result

The development experiment learns:

```text
"is a"   -> is-a
"used in" -> appears-in
```

from two dictionary-style examples and applies both mappings to:

```text
The vase is a vessel used in garden display.
```

No `abacus`, `vase`, or manually supplied alias is used by the learner.

The follow-up experiment also demonstrates:

- repeated examples preserve a confidence score;
- tied phrase meanings produce an explicit ambiguous prediction;
- learned paraphrases such as `serves as` and `found in` transfer to new
  vocabulary;
- corrective feedback can overturn a weaker competing mapping.

## Boundary

This is weakly supervised phrase alignment, not unrestricted language
understanding. It currently assumes aligned source/target observations and
now persists mappings in Protama state and participates as a fallback in the
canonical relation recognition lifecycle. Candidate ranking and structural
family routing still require further integration.

Current validation:

```text
94 tests
93 passed
1 intentionally skipped
```

The Structural Induction and Transfer Gate remains **NOT PASSED**.

# Variable-Bound Family Memory

## Public overview

Protama investigates whether an AI system can learn reusable relationships
instead of relying only on memorized examples or surface wording.

The public benchmark uses the term **structural family** for a reusable
pattern that can be applied to new examples. The internal implementation
details of that capability are intentionally not published in this document.

## Research objective

The public objective is to determine whether a system can:

- identify a relationship that remains stable across examples;
- apply that relationship when the vocabulary changes;
- reject examples that resemble valid examples but violate the relationship;
- preserve uncertainty when the available evidence is insufficient;
- provide an auditable account of the evidence used for a decision.

These objectives are evaluated through the
[Protama Structural Induction and Transfer Gate](../../benchmark/Protama_Inductive_Structural_Invention_Test.md).

## Scope boundary

The current public work separates two research questions:

1. Can a system operate on already-structured observations?
2. Can a system discover the relevant structure from raw input?

Progress on the first question must not be described as completion of the
second. The public benchmark will identify which input representation and
evaluation controls were used for each result.

## Public claim boundary

The repository does not publish the internal family schema, matching
algorithm, state representation, confidence implementation, or integration
interfaces. Those details remain part of the private development work.

Public documents describe goals, evaluation boundaries, and reproducibility
requirements rather than implementation secrets.

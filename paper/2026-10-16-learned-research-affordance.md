# A New Capability Milestone: Learned Research Affordance

## Teaching Protama to recognize knowledge gaps and choose tools

**Project:** Protama**Publication type:** Public research milestone**Date:** 2026-10-16**Status:** Bounded ProtamaUI demonstration (`n=8` supervised cases); broader autonomy remains unclaimed

> **Scope notice:** This document reports a bounded ProtamaUI demonstration
> across eight supervised cases. It does not claim an independent statistical
> evaluation, generalization to unseen tools or sources, unrestricted
> autonomous research, or general-purpose tool use.

## 1. Context: why this milestone exists

Protama has been developed through structured teaching, learned family
patterns, dictionary-derived examples, and increasingly independent
evaluation. The Structural Induction and Transfer Gate remains an important
long-term evaluation target, but it is a beacon rather than the immediate
capability goal.

The current work exposed a more fundamental question. Protama can be given a
prepared example, analyzed by an existing training path, and stopped when the
path reaches an unresolved pattern. That demonstrates useful learning and
uncertainty reporting, but the surrounding process still determines what is
read, when it is read, and when a human supplies the correction.

The next question is whether Protama can participate in the research process
itself:

```text
encounter a problem
    -> recognize missing knowledge
    -> identify a source that may resolve it
    -> choose to use that source
    -> continue after receiving the result
```

This is not a request to make Protama memorize an entire dictionary for its
own sake. The dictionary is a controlled environment in which the more
general capability can be tested. It contains:

- explicit word-definition relationships;
- many references from one word to another;
- known and unknown concepts;
- multiple senses;
- ambiguous definitions; and
- a source that can be taught and deliberately made available as a tool.

Those properties make it possible to observe whether Protama can identify an
unresolved dependency and decide how to investigate it.

### What exists today

The current dictionary training path is primarily an externally sequenced
process:

```text
the program selects an entry
    -> Protama analyzes it
    -> the path learns or produces a provisional interpretation
    -> the path stops or requests supervision when uncertain
```

That is different from:

```text
Protama receives a goal
    -> Protama notices that a referenced word is unresolved
    -> Protama decides that a dictionary lookup may help
    -> Protama invokes the lookup tool
    -> Protama incorporates the result and resumes the goal
```

The proposed milestone tests the second behavior. It is therefore not merely
a larger version of the existing dictionary training run.

## 2. ProtamaUI as the runtime surface

The capability will be developed and used through the private ProtamaUI
runtime rather than an unobserved batch script. ProtamaUI is the intended
usable runtime for the entity, not merely a test harness. It keeps a live
Protama instance running, displays output as it occurs, accepts human input,
supports feedback, and records structured interaction events.

The demonstrated runtime behavior was:

```text
start ProtamaUI
    -> give Protama a large task
    -> watch Protama work in real time
    -> Protama recognizes a knowledge gap
    -> Protama asks a question or emits a lookup decision
    -> an external research pass gathers the requested word's details
    -> those details are fed back as new thought input
    -> Protama produces the next thought
```

ProtamaUI is therefore the visual observation and supervision surface for the
milestone. It allows a human to distinguish:

- ordinary output from a question;
- active work from a waiting state;
- a lookup decision from an external research packet;
- a completed task from an incomplete or blocked task;
- a correction from a new instruction.

An optional Python terminal bridge will communicate with the same live
ProtamaUI-hosted instance through structured commands and events. The bridge
is not a second reasoning system and must not create a separate Protama
instance. It provides programmatic control for long-running tasks while the
UI remains available for real-time observation and human answers.

The intended interaction boundary is:

```text
Python terminal or UI
    -> task, answer, pause, resume, or stop command
    -> live Protama runtime
    -> output, question, research, checkpoint, or completion event
    -> UI display and structured event log
```

When Protama asks a question, the runtime must persist the pending question
and the active task state. An answer supplied through the UI or terminal must
resume the same task rather than starting a new session. The event log should
preserve the question, answer, tool decisions, returned evidence, and resume
transition.

The first external source adapter now exists as a separate boundary:

```text
runtime LookupRequest
    -> DictionaryResearcher
    -> source-backed ResearchPacket
    -> runtime receive_research()
```

The adapter accepts only an explicit dictionary lookup request. It does not
infer a lookup from an unknown word, mutate Protama's semantic state, or turn
retrieved dictionary text into a fabricated thought. This keeps source
retrieval testable while the learned interpretation layer is still being
extended to propose target and source arguments.

This runtime is the operational environment for the capability, not a hidden
replacement for Protama's decision-making. Protama emits a thought or action
request. An external research pass obtains and organizes the requested word's
details. That research packet is fed back into Protama as new thought input,
and Protama produces the next thought.

## 3. The discovery

The next important question is not initially whether Protama can process an
entire dictionary. It is more fundamental:

> **Can Protama recognize that it does not know something, identify an
> available source that can help, and independently choose to use that
> source?**

This is a learned capability, not a hard-coded dictionary rule.

The dictionary is a useful research environment, not the final purpose of the
capability, because it provides a clear relationship between:

```text
word -> definition
```

It also provides a natural unresolved-reference task. A definition may refer
to a word Protama has not yet learned. Protama must recognize the knowledge
gap, decide that a dictionary lookup is appropriate, request the lookup, use
the result, and return to the original task.

## 4. The thesis

The milestone thesis is:

> Protama can learn the concept of an unresolved question, recognize that its
> current knowledge is insufficient, identify an available information source,
> select an appropriate tool action, and continue the original task after
> receiving the result.

The important decision is not merely:

```text
I do not know.
```

It is:

```text
I do not know this.
I know what kind of source can resolve it.
I know how to use that source.
I will use it now.
```

## 5. Teaching the capability

The capability must be taught through examples and feedback. The system must
not contain a hidden rule such as:

```python
if unknown_word:
    lookup(word)
```

The initial teaching curriculum introduces the concepts progressively.

### 3.1 Teach words and definitions

```text
Teacher: “Abacus” is a word.
Teacher: “An abacus” is a definition.
```

Protama learns that definitions describe words.

### 3.2 Teach the dictionary concept

```text
Teacher: This book contains many words and their definitions.
Teacher: This kind of book is called a dictionary.
```

Protama learns that a dictionary is a source containing word-definition
relationships.

### 3.3 Demonstrate lookup

```text
Teacher: Let us look up “abacus” together.
Teacher: Where could we find the definition of a word?
Protama: A dictionary.
Teacher: Correct.
```

The feedback reinforces the research decision, not only the final definition.

### 3.4 Teach the available source

```text
Teacher: There are many dictionaries.
Teacher: This dictionary was prepared for you.
Teacher: It can be used to look up words.
```

The specific dictionary becomes an available source in Protama's environment.
The selection of that source remains a learned decision.

## 6. Tool boundary

The dictionary lookup mechanism is an environment tool. Its implementation
may use indexing, file traversal, caching, chunking, or other storage
strategies. Those details are not part of Protama's learned thought.

The conceptual tool contract is:

```text
Tool: lookup

Purpose:
    Find information about a target using an available source.

Input:
    target
    source
    purpose

Output:
    raw matching entries, source identity, source locations, and lookup status
```

Protama chooses whether to request a lookup, which word to provide, and what
to do after the research input returns. The lookup mechanism performs only
the physical retrieval.

This preserves the distinction between:

```text
Protama thought out:
    “I do not know evacuation. I should look it up.”

External research pass:
    retrieve every relevant evacuation entry and its source details

Protama thought in:
    “Here is what the research pass found: ...”

Protama next thought:
    interpret the evidence and continue the original task
```

The tool must not silently decide that every unknown word should be looked up.
That would test an application rule rather than learned research behavior.

## 7. Dictionary research test

After the teaching curriculum, Protama received an entry such as:

```text
Abevacuation — A partial evacuation.
```

If `evacuation` is absent from the declared pre-test knowledge snapshot, the
expected decision is:

```text
knowledge gap: evacuation
selected action: lookup
selected source: dictionary
lookup target: evacuation
```

The runtime then performs an external research pass against the dictionary.
That pass gathers the relevant word, senses, source locations, and referenced
details. It does not count as a Protama thought. The research packet is fed
back into Protama as new thought input, and Protama must decide whether the
evidence is sufficient to continue interpreting the original entry.

The complete research trajectory is:

```text
read entry
    -> identify referenced concept
    -> assess whether it is known
    -> recognize unresolved dependency
    -> select dictionary lookup
    -> receive definitions
    -> learn or update the concept
    -> return to the original entry
    -> continue, research further, or ask for help
```

## 8. Evaluation cases

The bounded demonstration covered eight cases, one for each of the following
trajectory types:

1. a known word that should not trigger unnecessary lookup;
2. an unknown word with a dictionary entry;
3. an entry containing an unknown referenced word;
4. an ambiguous word with multiple senses;
5. a word absent from the available dictionary;
6. a lookup result that is insufficient and requires another lookup;
7. an irrelevant unknown word that should not redirect the current task;
8. a completed lookup after which Protama returns to the original goal.

The evaluator should score the decision trajectory, not only the final prose
answer.

This was a supervised demonstration rather than an independently sampled
evaluation: the sample size was `n=8`, and the original publication package
did not preserve a machine-readable full trajectory log or a separately
published pre-test knowledge snapshot for every case. Accordingly, this
paper reports the observed capability boundary without treating the result as
statistical evidence of learned generalization.

## 9. Required evidence

Each research episode should record:

- the original goal;
- the observations available to Protama;
- Protama's knowledge-state assessment;
- the selected tool, if any;
- the tool arguments;
- the returned source evidence;
- the subsequent knowledge update;
- the decision to continue, stop, research again, or ask for help;
- the final answer and its evidence path.

The evaluator must distinguish:

```text
correctly answered from existing knowledge
correctly researched and answered
correctly recognized as unresolved
unnecessary lookup
wrong source selection
unsupported answer
premature stopping
```

## 10. What this milestone does not claim

This milestone does not yet establish:

- unrestricted large-dataset scalability;
- recursive research over the entire dictionary;
- general-purpose tool use;
- novel-answer generation across arbitrary domains;
- long-term retention across indefinite episodes;
- the full Structural Induction and Transfer Gate.
- generalization from a taught dictionary source to a novel, previously unseen
  tool or source;
- that the `evacuation` dependency was absent before the original run in a
  separately auditable snapshot;
- independently replayable full decision trajectories for all eight cases.

It establishes a narrower and more foundational question: whether Protama can
learn that research is an available response to an unresolved problem and
carry that decision through an observable, resumable runtime task.

In the Structural Gate capability ladder, this is an early interactive
research-affordance probe related to the separate L7 extension
(`self-directed refinement through information-seeking examples`). It is not
an L7 evaluation or an L7 pass: the demonstration used a taught dictionary
source, supervised sequencing, and no novel-source transfer test.

## 11. Relationship to the independent episode generator

The independent episode generator remains a valid separate milestone. It
builds trustworthy evaluation infrastructure for hidden-family structural
learning:

```text
learned research affordance
    = capability milestone

independent episode generator
    = evaluation-infrastructure milestone
```

The milestones can proceed in parallel. The research-affordance evaluation
adds an interactive tool environment that the static episode generator does
not currently provide.

## 12. Current status and next work

Current status:

```text
Teaching curriculum:              implemented and exercised
Dictionary tool boundary:         implemented and exercised
Interactive research loop:        demonstrated through ProtamaUI
Decision trajectory logging:      implemented and observable
Lifecycle checkpointing:           implemented and UI-validated
500-entry supervised batch:       completed through ProtamaUI
Research-affordance demonstration: n=8 supervised cases completed
Independent generalization evaluation: not performed
Full raw trajectory appendix: not preserved in original run
```

The next implementation should certify the independent episode generator and
connect Protama to that evaluation through complete decision traces. The
dictionary batch remains a supervised runtime exercise, not evidence of
unrestricted autonomy or dictionary understanding.

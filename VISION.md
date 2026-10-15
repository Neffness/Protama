# The Protama Vision

Protama is a research project exploring a different path toward synthetic
intelligence: systems that learn and reuse structure rather than relying
primarily on memorization, imitation, or scale.

This document describes the project's direction and philosophy. It is not a
technical specification, implementation promise, or claim of achieved
general intelligence.

## What Protama is

Protama is intended to become a structural-learning architecture with:

- reusable relational memory;
- hypothesis formation and revision;
- developmental learning through curriculum;
- evidence-grounded decisions;
- uncertainty and abstention;
- traceable explanations;
- CPU reference and low-power execution paths;
- GPU-oriented high-throughput execution paths.

The project investigates how these capabilities can be developed, measured,
and reproduced in a system that is not dependent on the standard large
language-model paradigm.

## What Protama is not

Protama is not currently claiming to be:

- artificial general intelligence;
- consciousness;
- a human mind;
- a language fluency system;
- a proof of machine understanding;
- a replacement for scientific evaluation.

Protama does not treat fluent output as evidence that a system learned the
structure behind an answer. The project keeps capability claims narrower than
the vision that motivates them.

## Why Protama exists

Many current AI systems can produce correct answers while relying on
memorization, surface similarity, or statistical imitation. Those strategies
can fail when:

- vocabulary changes;
- a relationship is expressed differently;
- a near-miss preserves familiar words but changes the structure;
- evidence is incomplete or contradictory;
- a learned hypothesis needs to be revised;
- an explanation must be reconstructed from the evidence used to decide.

Protama exists to investigate these failure modes directly. The project
begins with measurable structural-learning tasks rather than broad claims
about intelligence.

## What Protama is trying to achieve

The near-term research objective is to build and evaluate systems that can:

- induce reusable relational structure from limited evidence;
- transfer structure to unfamiliar examples;
- distinguish valid examples from typed near-misses;
- revise or weaken hypotheses after contradiction;
- preserve uncertainty instead of guessing;
- produce explanations grounded in pre-decision evidence;
- learn progressively through controlled development.

These capabilities are evaluated through explicit tests and benchmark
protocols. A capability is not considered established merely because a demo
looks convincing.

## Long-term direction

Over time, Protama is intended to grow toward a developmental structural
learner that can:

- learn multiple structural families;
- compose and compare families across domains;
- transfer structure beyond its original vocabulary;
- revise causal and relational hypotheses interactively;
- learn through curriculum and experience;
- communicate uncertainty and competing explanations;
- support both high-throughput and lower-powered deployments.

This is a research direction, not a guarantee of a particular final system.
Each step must earn its claim through reproducible evidence.

## Product vision

The long-term product vision is to make Protama available as a pre-trained,
purpose-built intelligence appliance.

A customer would be able to describe the kind of Protama they need. We would
train and configure that system in-house, deliver it as a ready-to-use unit,
and provide an interactive interface through which the customer could
continue teaching and working with it in real time.

The intended experience includes:

- two primary appliance classes: a CPU Protama for lower-power deployments and
  a GPU Protama for higher-throughput workloads;
- a CPU Protama with a compact power and USB-C data connection where the
  target deployment supports it;
- a GPU Protama with a dedicated power-supply connection and a USB-C
  input/output port;
- a pre-trained foundation suited to the customer's chosen type of work;
- customer-specific training before delivery;
- an interactive interface for teaching, conversation, inspection, and
  correction;
- the ability to provide new input types through guided interaction;
- outputs that conform to a documented API;
- deployment into existing systems through standard connections, adapters,
  and integration contracts.

The goal is not to sell a generic black box that customers must accept
unchanged. The goal is to deliver a useful starting intelligence that can be
configured for a domain, taught by its operators, inspected by its owners,
and integrated into systems they already use.

In the most ambitious version of this vision, Protama becomes a
plug-and-play structural intelligence layer: a customer supplies the inputs
available in its environment, teaches the system the relationships that
matter, and receives reliable outputs through an agreed interface. USB-C is
the intended input/output connection for both appliance classes, while the
GPU class uses a separate dedicated power connection. True compatibility still
depends on power, data, protocol, security, and system-integration
requirements.

This product vision depends on capabilities that must be demonstrated:

- stable behavior after customer-specific teaching;
- controlled learning and rollback;
- separation between approved operation and further training;
- robust handling of unfamiliar inputs;
- reliable API-conforming outputs;
- inspectable evidence and correction history;
- safe integration with customer systems.

## Roadmap

### Near term

- stabilize the public benchmark specification;
- release a reproducible episode generator;
- implement the evaluation harness;
- establish transparent baselines and ablations;
- run a small pilot;
- publish development results and a benchmark introduction.

### Medium term

- release the complete Structural Induction and Transfer Gate;
- support public evaluation and replayable reports;
- expand structural-family learning beyond the initial controlled setting;
- investigate the next level of independent structural invention.

### Long term

- support multi-family structural memory;
- study cross-domain structural transfer;
- develop interactive hypothesis refinement;
- investigate causal hypothesis revision;
- mature GPU and CPU implementations around a shared behavioral contract.

The roadmap is expected to change as evidence changes. A failed experiment
that narrows a claim is still useful progress.

## Research philosophy

Protama is guided by the following principles:

### Reproducibility

Claims should be tied to versioned inputs, configurations, tests, and reports.

### Transparency

The project should clearly separate what is implemented, what is planned, and
what has not been demonstrated.

### Trace fidelity

An explanation should be reconstructible from the evidence that influenced
the decision. Post-hoc storytelling is not a substitute for traceability.

### Scientific restraint

The project should prefer a narrow true claim over a broad attractive claim.
Benchmark success is not general intelligence, and a research prototype is
not a finished cognitive architecture.

### No hype

Uncertainty, failure cases, skipped tests, and unresolved limitations belong
in the record. They are part of the result, not obstacles to hide.

### Development through evidence

Protama should grow through explicit milestones, controlled experiments,
opposition, correction, and repeated validation.

## The public boundary

This repository contains public research artifacts, benchmark material,
documentation, and code explicitly approved for release. Private development
work, unreleased implementation details, and protected know-how remain
outside the public repository.

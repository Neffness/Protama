# Safety and Governance

Protama is being developed with the expectation that an increasingly capable
intelligence must be understandable, reviewable, and accountable to people.
Safety is not a marketing layer added after the system works. It is a design
requirement.

## Human-inspectable by design

Protama's public research materials are written to be read by people, not
only consumed by a training pipeline. We aim for the same standard in the
system itself:

- concepts should have understandable names;
- important decisions should preserve inspectable evidence;
- uncertainty should be visible rather than hidden behind confident output;
- failures and skipped capabilities should remain in the record;
- claims should be tied to tests, traces, and reproducible reports;
- system behavior should be explainable at the level needed for review.

Human readability is not by itself a safety guarantee. It is the foundation
that makes meaningful review, correction, and accountability possible.

## Engagement with public concerns

Governments, regulators, researchers, and the public have legitimate concerns
about increasingly capable AI systems. Protama is being developed with the
intention of making its evaluation boundaries, safety assumptions, and
failure modes available for appropriate external review.

As the system matures, we intend to make ourselves available for:

- independent technical evaluation;
- responsible research collaboration;
- red-team testing;
- benchmark reproduction;
- review of deployment boundaries;
- engagement with appropriate public institutions and standards efforts.

The goal is not to ask anyone to trust Protama because of a promise. The goal
is to make the relevant evidence available so that trust can be earned,
challenged, and revised.

## No inherent moral guarantee

Protama is not inherently good, benevolent, or safe merely because of its
architecture. A capable system can be directed toward harmful objectives if
it is trained, configured, connected, or deployed irresponsibly.

We recognize that a Protama-based system could be taught harmful behavior.
That possibility is a reason to design for control, evaluation, and
accountability, not a reason to pretend the risk does not exist.

Safety must therefore address the full system:

- training data and objectives;
- learned behavior;
- available tools and permissions;
- deployment environment;
- human operators;
- update and rollback processes;
- monitoring and incident response.

## Training and output separation

A core design goal is to keep learning controls separate from approved
inference behavior wherever the architecture permits. In practical terms, a
deployed system should be able to:

- operate from a reviewed state;
- disable or pause further training;
- preserve its current output behavior while training is stopped;
- record when learning or configuration changes occur;
- roll back to a known state;
- require authorization before new learning is promoted.

This is a design objective and must be validated for each implementation. It
is not a claim that every current prototype already provides all of these
controls.

Stopping training does not make a system safe by itself. It limits one path
of change; permissions, inputs, tools, operators, and deployment context still
require independent controls.

## Guardrail direction

Potential guardrails include:

- explicit capability and permission boundaries;
- human approval for consequential actions;
- sandboxed tools and environments;
- isolated training and evaluation;
- immutable or reviewable deployment snapshots;
- rollback and shutdown procedures;
- anomaly and contradiction detection;
- audit logs and evidence traces;
- red-team testing before expanded access;
- staged release from research to pilot to production.

Guardrails should be layered. No single prompt, classifier, policy file, or
shutdown mechanism should be treated as a complete safety strategy.

## Evidence before deployment

Before a Protama capability is used in a consequential setting, it should have
evidence appropriate to that setting, including:

- reproducible capability tests;
- known failure cases;
- adversarial and near-miss evaluation;
- uncertainty and abstention measurements;
- rollback and interruption tests;
- independent review;
- domain-specific safety validation;
- clear assignment of human responsibility.

Safety-critical deployment also requires applicable engineering controls,
certification, and regulatory compliance. A research result is not a
deployment authorization.

## Ongoing commitment

Protama will document what is implemented, what is planned, and what remains
unknown. We will not claim that an intelligence is safe because it is
interesting, fluent, or impressive in a demonstration.

The standard is continued evidence, human oversight, and the ability to
inspect, challenge, pause, correct, or withdraw a system when the evidence
requires it.

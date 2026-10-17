# Protama Black-Box Message API

## Status

Design and implementation contract. This document defines the external
boundary for a Protama device or runtime. The first transport-independent
slice is now exercised by ProtamaUI; USB-C transport and the remaining
external-action lifecycle are still future work.

### Current implementation slice

ProtamaUI currently uses a protocol client that:

- establishes a versioned session and negotiated capabilities;
- assigns session and message identifiers;
- validates sequence and predecessor-digest continuity;
- sends ordinary text as `input` or pending-question replies as `answer`;
- exposes model output as public `output` messages; and
- exposes runtime questions, statuses, errors, and pause/resume controls as
  validated lifecycle messages;
- can publish checkpoints and explicit resynchronization requests;
- persists the current protocol checkpoint through the UI session record;
- emits correlated dictionary `action_request` messages and accepts matching
  `action_result` messages;
- executes permitted dictionary requests through the host adapter and feeds
  accepted evidence back into the active Protama input stream; and
- keeps the existing model and entity runtime behind the UI adapter.

The UI does not call model submission, task recognition, or autonomous output
methods directly. Those translations occur inside the protocol client, which
is the host-side adapter for this local transport.

## Purpose

Protama is intended to be usable as a black box:

```text
host application
    -> Protama input
    <- Protama output and events
```

The physical connection may be USB-C, but USB-C is only the transport. The
semantic boundary must not depend on a shared filesystem, a particular
operating system, or direct access to Protama's Python objects.

ProtamaUI is a client of this boundary. It is not a privileged second
implementation of the runtime.

## Design principles

### 1. Messages are the public contract

Applications send versioned messages and receive versioned messages. They do
not select Protama's internal operators, call internal methods, or provide
implementation-specific state.

### 2. Natural input remains natural

An application should be able to send ordinary text:

```json
{
  "kind": "input",
  "content": {
    "type": "text",
    "text": "Please find the definition of evacuation."
  }
}
```

The application does not need to label this as `word-definition`,
`dictionary_lookup`, or another internal category. Protama interprets the
input and may emit an action request if its learned evidence supports one.

### 3. Actions are proposals, not hidden host commands

When Protama needs an external capability, it emits a typed request:

```json
{
  "kind": "action_request",
  "content": {
    "action": {
      "request_id": "lookup-91",
      "operation": "lookup",
      "source": "dictionary",
      "target": "evacuation",
      "purpose": "definition"
    }
  }
}
```

The host performs the requested external action and returns an
`action_result`. Protama does not pretend that the external result was an
internal thought.

### 4. One input may produce multiple events

The protocol is asynchronous. A single input may produce:

```text
input
    -> interpretation
    -> output or question
    -> action_request
    -> waiting status
    -> action_result
    -> resumed output
```

Clients must correlate messages using identifiers rather than assuming a
single request/response pair.

### 5. The session is a continuously evolving state

Protama communication is stateful rather than a collection of unrelated
requests. A session begins from a negotiated initial state and advances as
messages are accepted:

```text
session genesis
    -> input
    -> interpretation
    -> action request
    -> action result
    -> resumed task
    -> output
```

Each accepted message belongs to that progression. This allows the runtime to
preserve task continuity, reject stale results, and resume work after a
temporary transport interruption.

### 6. Capability negotiation is explicit

At session start, Protama and the host exchange protocol version, supported
content types, available actions, limits, and recovery options. A client must
not assume that every Protama runtime supports every tool.

```json
{
  "kind": "session_started",
  "capabilities": {
    "content_types": ["text", "document"],
    "actions": ["lookup"],
    "max_attachment_bytes": 10485760,
    "checkpoint_resume": true
  }
}
```

Capabilities describe what is available, not what Protama must choose. The
semantic decision to request an action remains Protama's responsibility.

### 7. Message history is verifiable

Messages carry sequence and predecessor information so the runtime can detect
duplicates, gaps, reordering, and results from another session. This is
continuity metadata, not a replacement for transport encryption or device
authentication.

### 8. Internal diagnostics are separate

The public stream exposes meaningful external behavior: output, questions,
action requests, results, state changes, and errors. It does not expose raw
internal babbling or every intermediate cognitive event.

A separate diagnostic stream may be enabled for development, testing, and
auditing. Diagnostic access must not be required for normal operation.

## Message envelope

Every message uses a common envelope:

```json
{
  "protocol": "protama",
  "version": 1,
  "message_id": "msg-123",
  "session_id": "session-7",
  "sequence": 12,
  "previous_digest": "sha256:...",
  "kind": "input",
  "in_reply_to": null,
  "content": {},
  "attachments": [],
  "metadata": {}
}
```

### Envelope fields

| Field | Meaning |
|---|---|
| `protocol` | Protocol family name. |
| `version` | Major protocol version. Breaking changes increment this value. |
| `message_id` | Unique identifier for this message. |
| `session_id` | Persistent conversation/runtime session. |
| `sequence` | Monotonically increasing position within the session direction or stream. |
| `previous_digest` | Digest of the immediately preceding accepted message. |
| `kind` | Message category. |
| `in_reply_to` | Optional message or request being answered. |
| `content` | Typed message body. |
| `attachments` | References to content transferred outside the JSON body. |
| `metadata` | Non-semantic transport or application metadata. |

The protocol should reject malformed envelopes explicitly. It must not turn
invalid input into a success-shaped fallback.

### Directional continuity

The transport maintains two independent continuity chains:

```text
host -> Protama       host_to_protama
Protama -> host       protama_to_host
```

Each direction has its own sequence counter and predecessor digest. The
semantic envelope remains the same in both directions, while the selected
transport identifies which directional chain is being advanced. This prevents
host input and Protama output from competing for one sequence counter.

## Session lifecycle

A session is a durable communication context for one live Protama instance.
It may contain multiple tasks and may remain open while Protama waits for a
human answer or an external action result.

### Session establishment

The host begins with a session request:

```json
{
  "kind": "session_start",
  "requested_version": 1,
  "client_capabilities": {
    "content_types": ["text", "document"],
    "actions": ["lookup"],
    "checkpoint_resume": true
  }
}
```

Protama responds with a session identifier, negotiated capabilities, limits,
and a new session genesis identifier:

```json
{
  "kind": "session_started",
  "session_id": "session-7",
  "genesis_id": "genesis-91",
  "capabilities": {
    "content_types": ["text", "document"],
    "actions": ["lookup"],
    "checkpoint_resume": true
  }
}
```

The genesis identifier distinguishes this session state from every other
session. It is an identifier for continuity, not a secret and not a device
identity.

### Checkpoints

Long-running work may publish a checkpoint containing the last accepted
sequence, active task identifiers, pending questions or action requests, and
the current history digest:

```json
{
  "kind": "checkpoint",
  "session_id": "session-7",
  "checkpoint": {
    "checkpoint_id": "checkpoint-4",
    "sequence": 18,
    "history_digest": "sha256:...",
    "active_task_ids": ["task-12"],
    "pending_request_ids": ["lookup-91"]
  }
}
```

Checkpoints make interruption and recovery explicit. They do not expose
Protama's private cognitive state.

### Resynchronization

If either side detects a sequence gap, mismatched predecessor digest, stale
session, or unknown pending request, it must stop normal message processing
and emit an explicit resynchronization request:

```json
{
  "kind": "resync_required",
  "reason": "sequence_gap",
  "expected_sequence": 19,
  "received_sequence": 21,
  "checkpoint_id": "checkpoint-4"
}
```

The host may resume from the named checkpoint, retransmit the missing
messages, or close the session. The runtime must not silently guess which
messages were lost.

## Message kinds

### `session_start` and `session_started`

These messages negotiate a session before semantic input is accepted. They
establish the protocol version, capabilities, limits, and session genesis.
They are part of the public lifecycle and are not semantic task input.

### `checkpoint` and `resync_required`

These messages preserve and recover communication continuity. A checkpoint
summarizes protocol position and pending external correlations; it does not
serialize hidden internal thought. `resync_required` is emitted when the
message history cannot be safely continued.

### `input`

Ordinary application or user input.

```json
{
  "kind": "input",
  "content": {
    "type": "text",
    "text": "Please find the definition of evacuation."
  }
}
```

### `output`

Protama's externally communicated response.

```json
{
  "kind": "output",
  "in_reply_to": "msg-123",
  "content": {
    "type": "text",
    "text": "I found a dictionary entry for evacuation."
  }
}
```

### `question`

Protama requires an answer before continuing.

```json
{
  "kind": "question",
  "content": {
    "type": "text",
    "text": "Which dictionary should I use?"
  },
  "question": {
    "question_id": "question-44",
    "purpose": "select a research source"
  }
}
```

### `answer`

An answer to a pending Protama question. The runtime must resume the existing
task rather than create a new task.

```json
{
  "kind": "answer",
  "question": {
    "question_id": "question-44"
  },
  "content": {
    "type": "text",
    "text": "Use the dictionary."
  }
}
```

### `action_request`

An externally executable action selected by Protama.

```json
{
  "kind": "action_request",
  "content": {
    "action": {
      "request_id": "lookup-91",
      "operation": "lookup",
      "source": "dictionary",
      "target": "evacuation",
      "purpose": "definition"
    }
  }
}
```

The action shape is intentionally generic. `lookup` is the first research
operation, not a special transport command. Future operations may include
other learned source and capability combinations.

When the learned interpreter recognizes a supported `lookup` operation and
extracts a concrete target, the ProtamaUI adapter creates this request
automatically. The host does not add an operator label to the user's input or
choose the action on Protama's behalf. The request is also recorded as a
protocol event in the UI log.

### `action_result`

The result of an action request.

```json
{
  "kind": "action_result",
  "content": {
    "action": {
      "request_id": "lookup-91",
      "operation": "lookup",
      "source": "dictionary",
      "target": "evacuation",
      "purpose": "definition"
    },
    "result": {
      "status": "found",
      "evidence": [
        {
          "definition": "The act of emptying or clearing.",
          "source_line": 11065
        }
      ]
    }
  }
}
```

An action result is external evidence. It is fed back into Protama as new
input to the active task; it is not represented as a fabricated thought.

### `status`

Lifecycle state for the session or active task.

```json
{
  "kind": "status",
  "state": "waiting_for_research",
  "task_id": "task-12"
}
```

Initial status values include:

```text
idle
running
waiting_for_human
waiting_for_research
paused
completed
blocked
failed
stopped
```

### `error`

An explicit protocol, transport, or runtime error.

```json
{
  "kind": "error",
  "error": {
    "code": "invalid_action_result",
    "message": "The result does not match the pending request.",
    "retryable": false
  }
}
```

### `control`

Lifecycle commands such as pause, resume, and stop.

```json
{
  "kind": "control",
  "command": "pause"
}
```

Control messages are distinct from semantic input. A host may pause Protama,
but it must not silently rewrite a semantic input into an internal operator
selection.

## Attachments and files

The primary API must not require a disk path. A path belongs to the host
application's filesystem and may be meaningless or unsafe to Protama.

Small content may be included directly:

```json
{
  "content": {
    "type": "text",
    "text": "Document contents..."
  }
}
```

Larger content uses an attachment descriptor:

```json
{
  "attachments": [
    {
      "attachment_id": "attachment-22",
      "name": "report.pdf",
      "media_type": "application/pdf",
      "size": 184203,
      "transfer": "binary_stream"
    }
  ]
}
```

The bytes may travel through a framed binary transfer associated with the
attachment identifier. JSON should describe the content; it should not force
large files into base64 strings.

### Local path adapter

A development client may offer a local file picker, but the path must remain
inside the host adapter. The adapter should validate and stream the selected
file as an attachment or issue an opaque capability token. Protama should not
receive unrestricted host paths such as:

```text
C:\Users\...\secrets.txt
```

This preserves portability and limits filesystem authority.

## Transport requirements

The first implementation may use USB-C with a framed stream, but the protocol
should also work over a local pipe, socket, or test transport.

The transport must provide:

- message framing;
- complete-message boundaries;
- correlation identifiers;
- explicit encoding;
- bounded message and attachment sizes;
- cancellation and timeout behavior;
- orderly session shutdown;
- explicit malformed-message errors.

A conceptual frame is:

```text
[length][message type][payload]
```

The private runtime now includes a bounded local JSON framing implementation
with a four-byte length prefix. It accepts arbitrarily split transport chunks,
rejects oversized frames, rejects invalid JSON, and validates each decoded
message before returning it to the caller. USB-specific framing remains an
implementation decision and is not part of the semantic message contract.

Transport integrity and semantic continuity are related but separate. The
sequence and predecessor digest detect session-history problems; encryption,
peer authentication, and physical-device authorization belong to the selected
transport security layer.

## Security boundary

The host adapter is responsible for controlling external authority. Protama
may propose an action, but the adapter decides whether the requested source
and capability are available and permitted.

The implementation must:

- validate every request identifier;
- match every result to a pending request;
- avoid arbitrary path access;
- limit attachment size and type;
- preserve source provenance;
- report failures explicitly;
- avoid treating untrusted attachment content as a control message;
- keep diagnostic access separate from ordinary application access.

### Message form validation

Serialized messages cross a trust boundary before they reach Protama's model
or task runtime. The reference implementation validates them with
`SessionEnvelopeForm`, a small forms-like validator defined in the private
protocol package. The validator rejects unsupported protocols and kinds,
malformed identifiers and digests, invalid JSON shapes, oversized content,
oversized attachments, and control characters in text content.

ProtamaUI uses the same validation path for messages it creates. This is
intentional: the UI is a host adapter, not a trusted bypass. Unsafe text is
rejected before it is submitted to the model, and model output is validated
before it is exposed as a public `output` message.

Form validation is schema and boundary validation, not an attempt to remove
meaningful natural-language punctuation or rewrite user content. Content
that passes the form remains untrusted semantic input.

Action messages receive additional validation. Requests must identify the
operation, source, target, purpose, and request identifier. Results must
repeat the request identifier and action fields and contain bounded evidence.
The UI adapter checks the request identifier against the pending runtime
lookup before accepting the result, then resumes the existing task. An
unknown, stale, or mismatched result is rejected before it advances session
state.

## ProtamaUI relationship

ProtamaUI should use the same public API as any other host application:

```text
ProtamaUI
    -> input/control messages
    <- output/question/status/action events
ProtamaUI
    -> action results or human answers
    <- resumed output
```

The UI may render diagnostics and provide supervision controls, but it should
not bypass the protocol to call `Protoma` internals. This creates a practical
black-box test: a second client should be able to perform the same core
conversation and research flow without importing Protama's implementation.

## Initial implementation scope

The first protocol implementation should include:

1. Versioned JSON envelopes.
2. Session establishment and capability negotiation.
3. Persistent session and message identifiers.
4. Sequence and predecessor-digest validation.
5. Checkpoints and explicit resynchronization.
6. Text input and output.
7. Questions and answers.
8. Generic action requests and action results.
9. Status and error events.
10. Dictionary lookup as the first external action.
11. Attachment descriptors with a local test transport.
12. A ProtamaUI adapter using the public message boundary.

It should not yet include unrestricted recursive research, arbitrary terminal
execution, or unrestricted host filesystem access.

## Acceptance criteria

The design is considered implemented when a test client can:

1. Open a session.
2. Negotiate capabilities and receive a session genesis.
3. Send ordinary natural-language text.
4. Receive output or a question.
5. Receive a learned action request without supplying an operator label.
6. Return a matching action result.
7. Observe Protama resume the original task.
8. Detect an intentionally missing or reordered message.
9. Recover from a published checkpoint without silently guessing.
10. Exchange the same messages through ProtamaUI.
11. Run without sharing Protama's Python objects or unrestricted filesystem
   paths.

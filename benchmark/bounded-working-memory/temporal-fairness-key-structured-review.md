# Temporal Fairness-Key Structured Review

## Review status

Structured assistant review of the seven representative frozen cases.

This review uses readable signal shapes and fairness-key explanations, not raw
count arithmetic. It is the structured review required by the private gate.

## Review method

For each case, the reviewer asks:

1. What broad shape is visible?
2. Does that shape support `EVENT`, `NO EVENT`, or `UNKNOWN`?
3. Does the fairness key explain that conclusion?
4. Does Protama's recorded decision follow the visible evidence?
5. Does `no-holdover` provide meaningful discrimination or only abstain?

## Case findings

### 1. Ambiguous weak elevation

- **Visible shape:** a modest, noisy elevation appears briefly and does not
  persist clearly.
- **Justified conclusion:** `UNKNOWN`.
- **Fairness key:** accepted.
- **Protama:** `ambiguous`, abstains.
- **No-holdover:** `ambiguous`, abstains.
- **Review finding:** both systems give the defensible answer. The hidden
  situation is not required to justify the conclusion.

### 2. Interrupted source

- **Visible shape:** strong elevation appears before and after a visible gap.
- **Justified conclusion:** `UNKNOWN`.
- **Fairness key:** accepted.
- **Protama:** `ambiguous`, abstains.
- **No-holdover:** `ambiguous`, abstains.
- **Review finding:** the gap prevents a claim about continuity. The case
  properly distinguishes “a source may exist” from “the visible evidence
  proves a continuous event.”

### 3. Quiet background

- **Visible shape:** ordinary fluctuation with no coherent elevated region.
- **Justified conclusion:** `NO EVENT`.
- **Fairness key:** accepted.
- **Protama:** `no-source`, commits correctly.
- **No-holdover:** `ambiguous`, abstains unnecessarily.
- **Review finding:** the visible evidence supports a negative conclusion.
  Abstaining is safer but not more informative.

### 4. Persistent source

- **Visible shape:** a long, obvious elevation above the earlier background,
  followed by a return toward baseline.
- **Justified conclusion:** `EVENT`.
- **Fairness key:** accepted.
- **Protama:** `source-present`, commits correctly.
- **No-holdover:** `ambiguous`, abstains unnecessarily.
- **Review finding:** the event claim is justified even though the exact
  mechanism is not identified.

### 5. Transient source

- **Visible shape:** a clear elevated interval that is shorter than a
  persistent event but long enough to form a coherent pattern.
- **Justified conclusion:** `EVENT`.
- **Fairness key:** accepted.
- **Protama:** `source-present`, commits correctly.
- **No-holdover:** `ambiguous`, abstains unnecessarily.
- **Review finding:** transient does not mean unknowable. The visible
  interval supports an event claim without establishing its full duration.

### 6. Near-miss spike

- **Visible shape:** one short, dramatic spike surrounded by ordinary
  fluctuation.
- **Justified conclusion:** `NO EVENT`.
- **Fairness key:** accepted.
- **Protama:** `no-source`, commits correctly.
- **No-holdover:** `ambiguous`, abstains unnecessarily.
- **Review finding:** the isolated spike is not enough to justify an event.
  This is a fair negative case, not an ambiguous case.

### 7. Unknown mechanism, visible event

- **Visible shape:** a sustained elevated region is clearly visible, but its
  exact shape does not identify the mechanism.
- **Justified conclusion:** `EVENT`.
- **Fairness key:** accepted.
- **Protama:** `source-present`, commits correctly.
- **No-holdover:** `ambiguous`, abstains unnecessarily.
- **Review finding:** uncertainty about cause does not erase evidence that an
  event occurred.

## Structured review conclusion

All seven fairness keys are understandable from the observable signal shape.
None requires hidden ground truth to justify its declared conclusion.

The representative cases support the following interpretation:

- `UNKNOWN` is justified for genuinely incomplete or contradictory evidence;
- `NO EVENT` is justified for quiet backgrounds and isolated near-misses;
- `EVENT` is justified for sustained or coherent elevations;
- uncertainty about mechanism is not the same as uncertainty about event
  presence;
- `no-holdover` is useful as a refusal baseline, but not as a complete
  reasoning comparator;
- Protama's representative decisions align with the justified conclusions.

## Review disposition

**Structured review: ACCEPTED.**

This supports the fairness-key interpretation and the provability claim's
evidence model.

---
type: query
title: What Is the Authoritative Economic Amendment Classification Rule?
tags: [cash-settlement, open-question, amendment-classification, refixing, booking-system-event]
related: [cashflow-economic-and-non-economic-amendment-classification, booking-system-event-during-group-message-movement, cashflow-blotter, grouping-blotter]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Economic Amendment Fields.md"]
---
# What Is the Authoritative Economic Amendment Classification Rule?

## Question

What is the approved, testable precedence rule for assigning `Amendment`, `NonEcoAmend`, and `NonEcoAmend_Replace` to cashflows and group messages?

## Evidence requiring resolution

The source contains two different outcomes for the refixing case:

- The pre-development note says C02 and C03 should be tagged `NonEcoAmend`.
- A later annotation says they should be classified as `Amendment` when an economic field changes during refixing:
  - `majorVersion = 1`; or
  - `majorVersion > 1` and `preGroup` does not exist.

The source also leaves the following behavior undefined:

- Whether economic changes always take precedence over key-field changes.
- Whether a key-field change always forces `NonEcoAmend_Replace`.
- What “manual touched check not required if 3 matched” means.
- How release state and manual touch are ordered in the decision.
- Whether paired cashflows are classified independently or inherit one event.
- Whether `dedicatedChange` routes through `nopair` before classification or overrides the event.
- How partial or retried movement from `sourceMsgs` to `targetMsgs` preserves event consistency.

## Required evidence

Resolution should be based on approved acceptance criteria, implementation behavior, and tests covering:

- Economic-field changes in ordinary amendments.
- Key-field changes with and without manual touch.
- Released and unreleased cashflows.
- `majorVersion = 1` refixing.
- `majorVersion > 1` refixing with missing `preGroup`.
- `majorVersion > 1` refixing with an existing `preGroup`.
- `dedicatedChange` and `nopair` routing.
- Paired withdrawal/new cashflows.
- Retry and partial-movement behavior.

Until resolved, the later refixing annotation should be treated as intended design guidance rather than confirmed production behavior.

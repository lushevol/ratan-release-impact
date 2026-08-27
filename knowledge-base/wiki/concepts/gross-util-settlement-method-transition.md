---
type: concept
title: GROSS and UTIL Settlement-Method Transition
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, settlement-method, gross, util, cashflow-lifecycle]
related: [fxu, utilization-service, past-due-accounting-reversal, cashflow-settlement-method-event-consistency, cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# GROSS and UTIL Settlement-Method Transition

The Phase 2 draft introduces a manual, bidirectional change of cashflow settlement method between `GROSS` and `UTIL`. The change is intended to take effect immediately at trade level and can be submitted for multiple trades in one request.

## Stated transition behavior

- `GROSS → UTIL` with a Withdrawal carrying `GROSS` becomes `CANCELLED` when there is no utilization and `ERROR` when utilization exists.
- `UTIL → GROSS` with a Withdrawal carrying `UTIL` becomes `CANCELLED` when the cashflow is not released and `READY + Utilization` when it is released.

The endpoint returns success or failure for each requested trade. It therefore permits partial success across a batch.

## Constraints and unresolved semantics

The document does not define:

- Whether all cashflows in a successful trade result must change atomically.
- Whether a batch is atomic across trades.
- The formal meanings and allowable transitions of `CANCELLED`, `ERROR`, and `READY`.
- Whether `READY + Utilization` denotes sequential actions, an event plus a state update, or a compound state.
- Which cashflow states and trade types permit `GROSS` and `UTIL`.

The transition affects [[cashflow-data]] and must remain consistent with the event precedence described in [[cashflow-settlement-method-event-consistency]].
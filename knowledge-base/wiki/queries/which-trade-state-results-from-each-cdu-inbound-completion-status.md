---
type: query
title: Which Trade State Results From Each CDU Inbound Completion Status?
created: 2026-08-23
updated: 2026-08-23
tags: [cdu, trade-state, confirmation-status, cashflow-stp, state-machine]
related: [trade-event-triggered-cashflow-stp, bcs-cdu-match-status-confirmation, cdu, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Trade event trigger cashflow STP.md"]
---
# Which Trade State Results From Each CDU Inbound Completion Status?

The source states that the following CDU `Confirmation_Message_Inbound_Status` values trigger `Trade_State` changes, but does not state the resulting state:

- `Inbound Completed - Match Completed`
- `Inbound Completed - Inbound Not Required`
- `Inbound Completed - Match Outside CDU`

The missing mapping is material because the documented NSTP predicate tests whether `Trade_State` is `AFFIRMED` or `CONFIRMED`.

## Evidence Available

Two examples report STP after the event:

- `Inbound Completed - Match Outside CDU` for cashflow `6257787319`.
- `Inbound Completed - Inbound Not Required` for cashflow `6261288851`.

Neither example records a before-and-after `Trade_State` value. `Inbound Completed - Match Completed` has no end-to-end STP test case in this source.

## Resolution Needed

Obtain an authoritative CDU event schema, state-transition specification, or RATAN event-processing implementation that identifies:

1. the destination `Trade_State` for each listed status;
2. whether the mapping varies by product, entity, or current trade state;
3. idempotency and ordering treatment for repeated or late confirmation events.

See [[trade-event-triggered-cashflow-stp]] and [[bcs-cdu-match-status-confirmation]].
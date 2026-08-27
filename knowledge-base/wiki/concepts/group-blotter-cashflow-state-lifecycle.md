---
type: concept
title: Group Blotter Cashflow State Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, state-transition, group-status, manual-delivery, audit]
related: [bulk-manual-stp-group-blotter, group-blotter, allocation-cashflow-state-handling, murex-reversal-and-new-cashflow-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# Group Blotter Cashflow State Lifecycle

## Message States

The requirement describes the following message-level outcomes:

- `PENDING → END` for selected cashflows successfully processed by manual delivery.
- `PENDING → OFFSET` for a withdrawal cashflow in the New/Withdrawal scenario.
- `ERROR` as a state that may be eligible for the original single-group manual-STP logic, subject to prior-major-version checks.

Unselected cashflows may remain `PENDING` or `ERROR` after a partial operation.

## Group States

The scenarios use these group states:

- `PENDING`
- `PENDING_TRADE_VALIDATION`
- `PENDING_PRE_GROUP`
- `DATA_VALIDATION_FAILED`
- `COMPLETED`

The source shows groups moving to `COMPLETED` after successful processing, but it does not consistently define whether all group cashflows must be terminal. In one scenario, a group becomes `COMPLETED` while unselected cashflows remain `PENDING` and `ERROR`.

## Audit and Routing

Successful bulk manual delivery is expected to:

- Set `bookingSystemEvent` to `ManualDeliver`.
- Route processed cashflows to the Cashflow Blotter.
- Preserve withdrawal-specific `OFFSET` behavior where applicable.

The source does not clarify whether the audit event is recorded per cashflow, per group, or once per bulk operation.
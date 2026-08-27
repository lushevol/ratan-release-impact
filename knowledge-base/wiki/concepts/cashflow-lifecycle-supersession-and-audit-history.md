---
type: concept
title: Cashflow Lifecycle Supersession and Audit History
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, lifecycle, amendment, withdrawal, audit-history]
related: [ratan, cashflow-blotter, stella, cashflow-group-message-deduplication, how-does-cashflow-blotter-handle-out-of-order-duplicate-and-withdrawal-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md"]
---
# Cashflow Lifecycle Supersession and Audit History

Cashflow lifecycle supersession separates the current operational representation of a cashflow from its retained event history.

## Expected Display Model

For the CN Sprint 17 cases, the active [[cashflow-blotter]] must display only the latest lifecycle event:

- for Stella spot New followed by Amendment, display Amendment;
- for Stella spot New followed by Withdrawal, display Withdrawal;
- for Murex spot New followed by C&R, display the latest Amendment.

The Cashflow History Page must retain the complete documented event sequence: New plus Amendment, or New plus Withdrawal.

## Scope Boundary

This requirement concerns lifecycle visibility and audit retention for individual spot cashflows. It should not be treated as proof of technical message deduplication or as a Group Blotter lifecycle rule. The source does not define ordering guarantees, duplicate-event behavior, withdrawal fields, or interaction with cashflows already netted.
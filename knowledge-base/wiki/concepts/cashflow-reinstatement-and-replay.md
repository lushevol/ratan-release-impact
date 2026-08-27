---
type: concept
title: Cashflow Reinstatement and Replay
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, reinstatement, replay, operations, recovery]
related: [cash-settlement-exception-handling, cashflow-blotter, oscar, murex, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# Cashflow Reinstatement and Replay

Cashflow recovery uses several distinct operational actions that should not be treated as interchangeable.

## Recovery actions

- **`ReInstate` / `Reinstate`** moves a failed or pending-exception cashflow back into processing after the underlying service or dependency is restored.
- **Message replay** is used when a missing inbound cashflow must be replayed, such as an OLA break from [[murex]] to Ratan.
- **Status replay** resends a Ratan-to-Murex status update after a write-back acknowledgement failure.
- **Manual replay from the cashflow blotter** is a possible response to a Ratan-to-Razor OLA break.
- **Manual booking** in [[oscar]] is an alternative recovery path for a Razor NACK.

## Preconditions

Reinstatement is stated for technical failures and `QUEUED+Pending Exception` cases after service restoration. It is not the stated remedy for invalid upstream data in `ERROR`, where trade amendment is required.

The source does not specify authorization, maker-checker approval, duplicate-processing controls, or the audit trail for each recovery action. These boundaries require confirmation in [[what-is-the-canonical-replay-and-reinstate-procedure]].
---
type: concept
title: Adhoc SSI Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [Adhoc-SI, SSI, workflow, maker-checker, cashflow]
related: [ssi, adhoc-si, ssi-exception-state-model, maker-checker-ssi-control, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# Adhoc SSI Workflow

The Adhoc SSI workflow is the maker/checker process for entering, verifying, approving, and rejecting an exceptional standing instruction for a cashflow.

## Workflow behavior

For a `WAITING` cashflow:

- `Maker Adhoc SSI` changes `Pending Operator` to `Pending Verification` and changes `SSI Exception Type` from `NA` to `Adhoc SI`.
- `Maker Input Adhoc SSI` changes an existing `Adhoc SI` item from `Pending Operator` to `Pending Verification`.
- `Checker Approve` changes the cashflow from `WAITING` to `READY` and clears `Pending Exception`, `Pending Verification`, and `Adhoc SI`.
- `Checker Reject` changes `Pending Verification` back to `Pending Operator` while retaining `Adhoc SI`.

For a `READY` cashflow:

- `Maker Adhoc SSI` can create a pending Adhoc SSI workflow while the primary cashflow status remains `READY`.
- `Maker Input Adhoc SSI` advances an existing Adhoc SI item to `Pending Verification`.
- `Checker Approve` leaves the primary status as `READY` and clears or leaves blank the workflow fields shown in the matrix.
- `Checker Reject` leaves the primary status as `READY`; the supplied matrix is incomplete about the resulting exception type in one rejection row.

## Important distinction

The primary cashflow status and the SSI workflow sub-status are independent dimensions. Consequently, a cashflow may be `READY` while carrying `Pending Exception` and `Pending Verification`.

The source suggests that `Maker Adhoc SSI` creates an Adhoc SI exception and `Maker Input Adhoc SSI` supplies or revises its data, but it does not explicitly define this distinction.

See [[ssi-exception-state-model]] for the field relationships and [[maker-checker-ssi-control]] for segregation of duties.
---
type: query
title: What Is the Authoritative SSI Re-stamping State Transition?
tags: [query, ssi, re-stamping, state-machine, maker-checker]
related: [ssi-stamping-notification, adhoc-ssi-workflow, ssi-maker-checker-remediation, ssi-exception-state-model]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/SSI Notification Flow.md"]
---
# What Is the Authoritative SSI Re-stamping State Transition?

## Question

What are the authoritative state and sub-status transitions before, during, and after SSI re-stamping, including the meaning of `NA+NA`?

## Evidence from the requirement

The requirement permits re-stamping for:

- `WAITING / Pending Operator` cashflows with `Missing Vostro`, `Multi Vostro`, `Nostro vs Vostro Mismatch`, or `Secondary Vostro`.
- `WAITING/READY` cashflows with `Good System Assigned Vostro` and `NA+NA`.
- Deleted or deactivated SSIs affecting `Multi Vostro` or `Good System Assigned Vostro` cashflows.

It explicitly excludes `WAITING / Pending Verification` cases for `Missing Vostro`, `Multi Vostro`, and `Nostro vs Vostro Mismatch`, and excludes `Adhoc SI` from the listed change-event refresh cases.

If re-stamping raises an exception, the sub-status becomes `Pending Operator` and Maker input is required again.

## Unresolved transition details

The requirement does not define:

- The initial state while re-stamping is running.
- The meaning of `NA+NA`.
- Whether a successful refresh moves the cashflow to `WAITING`, `READY`, or another state.
- Whether the original exception is retained after a failed refresh.
- How unlisted statuses and exceptions are handled.
- Whether re-stamping triggers another notification.
- Retry, idempotency, and duplicate-event behavior.
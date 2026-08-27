---
type: concept
title: RATAN Fail and AutoFail Status Transitions
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, status-transition, fail, autofail]
related: [bulk-manual-fail-workflow, suspended-versus-projected-cashflow-status, murex-2-11-cashflow-suppression, why-is-nostro-matched-autofail-eligible-but-not-manual-fail-eligible]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail/Bulk Fail Technical Design.md"]
---
# RATAN Fail and AutoFail Status Transitions

The Bulk Fail Technical Design defines proposed cashflow lifecycle transitions in [[ratan]].

Manual `Fail` is a non-terminal transition for all documented eligible states: it changes the cashflow to `WAITING / Pending Verification / Pending Manual Fail`. `Approve` from that state changes the cashflow to `FAILED`; `Reject` is documented only as “rollback previous status.”

Scheduled `AutoFail` directly changes its documented eligible states to `FAILED`.

## Eligibility distinction

The documented eligible states overlap substantially across `Fail` and `AutoFail`, including `PROJECTED`, `QUEUED`, specified `WAITING` variants, `READY`, `HOLD`, `ERROR`, `SWIFT_SUPPRESSED`, and `CASHFLOW_SUPPRESSED`.

`NOSTRO_MATCHED` appears only in the `AutoFail` eligibility set. The design gives no explanation for this asymmetry; see [[why-is-nostro-matched-autofail-eligible-but-not-manual-fail-eligible]].

## Scope caveat

The document describes the prior production behavior as `Fail` directly producing `FAILED` for both manual and scheduled scenarios. The matrix represents the proposed post-change behavior, so consumers must not treat it as confirmed current production behavior.

The listed failure eligibility of suppressed cashflows does not define their broader lifecycle semantics; see [[murex-2-11-cashflow-suppression]] and [[suspended-versus-projected-cashflow-status]].
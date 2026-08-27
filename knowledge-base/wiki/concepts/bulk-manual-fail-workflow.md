---
type: concept
title: Bulk Manual Fail Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, bulk-fail, maker-checker, workflow]
related: [ratan-fail-and-autofail-status-transitions, what-is-the-authoritative-bulk-fail-api-and-approval-contract, what-is-the-backend-enforcement-and-rollback-contract-for-pending-manual-fail, maker-checker-ssi-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail/Bulk Fail Technical Design.md"]
---
# Bulk Manual Fail Workflow

The proposed bulk manual-fail workflow in [[ratan]] separates failure initiation from terminal failure.

1. A user invokes `Fail` for an eligible cashflow.
2. The cashflow moves to `WAITING / Pending Verification / Pending Manual Fail`.
3. A reviewer invokes `Approve` to move the cashflow to `FAILED`, or invokes `Reject` to restore the previous state.

This is a cashflow lifecycle control, not evidence that SSI-specific controls in [[maker-checker-ssi-control]] govern this workflow. The source does not specify who may initiate, approve, or reject a manual failure, nor whether requester/checker separation is enforced.

## Difference from scheduled automatic failure

The workflow is intentionally distinct from `AutoFail`. A scheduled job invokes `AutoFail`, which directly changes eligible cashflows to `FAILED` without creating a pending-verification state. See [[ratan-fail-and-autofail-status-transitions]].

## Unspecified controls

The source does not define the approval/rejection API, audit records, event notifications, rollback snapshot semantics, or handling of concurrent lifecycle changes. It also says that the FE forbids manual action on `HOLD` and `ERROR`, while listing backend `Fail` transitions for those statuses. These gaps are tracked in [[what-is-the-backend-enforcement-and-rollback-contract-for-pending-manual-fail]] and [[what-is-the-authoritative-bulk-fail-api-and-approval-contract]].
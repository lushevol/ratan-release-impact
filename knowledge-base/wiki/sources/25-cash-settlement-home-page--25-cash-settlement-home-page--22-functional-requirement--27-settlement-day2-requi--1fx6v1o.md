---
type: source
title: Bulk Fail Technical Design
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, bulk-fail, settlement-day2, workflow, api]
related: [bulk-manual-fail-workflow, ratan-fail-and-autofail-status-transitions, what-is-the-authoritative-bulk-fail-api-and-approval-contract, why-is-nostro-matched-autofail-eligible-but-not-manual-fail-eligible, what-is-the-backend-enforcement-and-rollback-contract-for-pending-manual-fail]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail/Bulk Fail Technical Design.md"]
---
# Bulk Fail Technical Design

This technical design proposes separating manual and scheduled failure processing in [[ratan]]. The prior production behavior uses `Fail` for both scenarios and directly changes a cashflow to `FAILED`.

Under the proposed bulk-fail behavior:

- Manual `Fail` sends an eligible cashflow to `WAITING / Pending Verification / Pending Manual Fail`.
- `Approve` changes that pending-manual-fail cashflow to `FAILED`.
- `Reject` rolls the cashflow back to its previous status.
- A scheduled job uses `AutoFail`, which directly changes eligible cashflows to `FAILED`.

The design documents the transition matrix and several API examples, but it does not define events, approval/rejection APIs, entitlement controls, idempotency behavior, or the scheduled `AutoFail` invocation contract.

## Status-transition matrix

| # | Source Cashflow Status | Source Cashflow Sub Status | Source Cashflow Sub Status Type | Action | Target Cashflow Status | Target Cashflow Sub Status | Target Cashflow Sub Status Type | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PROJECTED | NA | NA | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 2 | QUEUED | NA | NA | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 3 | QUEUED | NA | Pending Exception | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 4 | WAITING | Pending Operator | Pending Exception | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 5 | WAITING | Pending Verification | Pending Exception | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 6 | WAITING | Pending Operator | Pending Netting | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 7 | WAITING | Pending Verification | Netting Review | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 8 | WAITING | NA | Pending Another Leg | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 9 | WAITING | Pending Verification | Reversal Rebook | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 10 | WAITING | Pending Operator | Pending Netting 4 Withdrawal | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 11 | READY | NA | NA | **Fail** | WAITING | Pending Verification | Pending Manual Fail | |
| 12 | READY | NA | Pending Ack | Fail | WAITING | Pending Verification | Pending Manual Fail | |
| 13 | HOLD | Pending Verification | NA | **Fail** | WAITING | Pending Verification | Pending Manual Fail | will not happen as it is forbidden to operate in the FE. |
| 14 | ERROR | NA | NA | **Fail** | WAITING | Pending Verification | Pending Manual Fail | will not happen as it is forbidden to operate in the FE. |
| 15 | SWIFT_SUPPRESSED | NA | NA | Fail | WAITING | Pending Verification | Pending Manual Fail | |
| 16 | CASHFLOW_SUPPRESSED | NA | NA | Fail | WAITING | Pending Verification | Pending Manual Fail | |
| 17 | WAITING | Pending Verification | Pending Manual Fail | Approve | FAILED | NA | NA | |
| 18 | WAITING | Pending Verification | Pending Manual Fail | Reject | NA | NA | NA | rollback previous status |
| 19 | PROJECTED | NA | NA | **AutoFail** | FAILED | NA | NA | |
| 20 | QUEUED | NA | NA | **AutoFail** | FAILED | NA | NA | |
| 21 | QUEUED | NA | Pending Exception | **AutoFail** | FAILED | NA | NA | |
| 22 | WAITING | Pending Operator | Pending Exception | **AutoFail** | FAILED | NA | NA | |
| 23 | WAITING | Pending Verification | Pending Exception | **AutoFail** | FAILED | NA | NA | |
| 24 | WAITING | Pending Operator | Pending Netting | **AutoFail** | FAILED | NA | NA | |
| 25 | WAITING | Pending Verification | Netting Review | **AutoFail** | FAILED | NA | NA | |
| 26 | WAITING | NA | Pending Another Leg | **AutoFail** | FAILED | NA | NA | |
| 27 | WAITING | Pending Verification | Reversal Rebook | **AutoFail** | FAILED | NA | NA | |
| 28 | WAITING | Pending Operator | Pending Netting 4 Withdrawal | **AutoFail** | FAILED | NA | NA | |
| 29 | READY | NA | NA | **AutoFail** | FAILED | NA | NA | |
| 30 | READY | NA | Pending Ack | **AutoFail** | FAILED | NA | NA | |
| 31 | NOSTRO_MATCHED | NA | NA | **AutoFail** | FAILED | NA | NA | |
| 32 | HOLD | Pending Verification | NA | **AutoFail** | FAILED | NA | NA | |
| 33 | ERROR | NA | NA | **AutoFail** | FAILED | NA | NA | |
| 34 | SWIFT_SUPPRESSED | NA | NA | **AutoFail** | FAILED | NA | NA | |
| 35 | CASHFLOW_SUPPRESSED | NA | NA | **AutoFail** | FAILED | NA | NA | |

## API information

| # | Function | URL | Parameters | Response | Notes |
| --- | --- | --- | --- | --- | --- |
| 10 | Manual Fail | [http://uklvadapp1340.uk.dev.net:8453/api](http://uklvadapp1340.uk.dev.net:8453/api/v1/ratan/cashflow/user/status/update)/v1/camunda/task/fail | `[ { "cashflowId": "eddie2023022301", "cashflowVersion": 0, "businessVersion": 0, "minorVersion": "2" }, { "cashflowId": "eddie2023022303", "cashflowVersion": 0, "businessVersion": 0, "minorVersion": "2" } ]` | `{ "status": "", "errorCode": "", "errorMessage": "" }` | |
| 12 | Swift Suppress Maker | [http://uklvadapp1340.uk.dev.net:8453/api](http://uklvadapp1340.uk.dev.net:8453/api/v1/ratan/cashflow/user/status/update)/v1/ratan/lifecycle/suppress/maker | `{ "action": "ManualSwiftSuppress", "comment": "123", "cashflows": [ { "cashflowId": "123", "businessVersion": "", "cashflowVersion": "", "minorVersion": "" }, { "cashflowId": "456", "businessVersion": "", "cashflowVersion": "", "minorVersion": "" } ] }` | `{ "status": "", "errorCode": "", "errorMessage": "" }` | |
| 13 | Swift Suppress Checker | [http://uklvadapp1340.uk.dev.net:8453/ap](http://uklvadapp1340.uk.dev.net:8453/api/v1/ratan/cashflow/user/status/update)i/v1/ratan/lifecycle/suppress/checker | `{ "action": "Approve / Reject", "comment": "123", "cashflows": [ { "cashflowId": "123", "businessVersion": "", "cashflowVersion": "", "minorVersion": "" }, { "cashflowId": "456", "businessVersion": "", "cashflowVersion": "", "minorVersion": "" } ] }` | `{ "status": "", "errorCode": "", "errorMessage": "" }` | |

## Documented gaps and ambiguities

The displayed API paths are malformed or internally inconsistent and require confirmation before implementation. The source gives no HTTP methods, authentication or authorization rules, batch-size limits, partial-failure behavior, optimistic-locking behavior, or audit/event definitions.

`NOSTRO_MATCHED` is eligible for `AutoFail` but is not listed for manual `Fail`. The rationale is not supplied. Although the front end is said to prohibit manual operations on `HOLD` and `ERROR`, the backend transition matrix includes both states.

The failure eligibility of `SWIFT_SUPPRESSED` and `CASHFLOW_SUPPRESSED` extends the unresolved downstream considerations in [[what-is-the-complete-accounting-behavior-for-failed-and-swift-suppressed-cashflows]] and [[what-is-the-canonical-swift-suppressed-cashflow-status-enumeration]].
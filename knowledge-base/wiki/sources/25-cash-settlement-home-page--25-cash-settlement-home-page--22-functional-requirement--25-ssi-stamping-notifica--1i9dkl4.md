---
type: source
title: Adhoc SI Status and Action Matrix
authors: []
year: 0
url: ""
venue: "Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, SSI, adhoc-SI, status-transition, functional-requirement]
related: [adhoc-ssi-workflow, ssi-exception-state-model, maker-checker-ssi-control, ssi, adhoc-si, cash-settlement-home-page, what-is-the-authoritative-adhoc-ssi-status-transition-matrix, what-notifications-are-triggered-by-ssi-stamping-actions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# Adhoc SI Status and Action Matrix

## Summary

This functional requirement defines status transitions for Adhoc Standing Instruction (SSI) processing in the Cash Settlement Home Page. It covers maker actions that initiate or input Adhoc SSI data and checker actions that approve or reject the data.

The matrix distinguishes between cashflows whose primary status is `WAITING` and those whose primary status is `READY`. A `WAITING` cashflow approved by a checker becomes `READY` and has its pending exception fields cleared. A `READY` cashflow can retain its primary `READY` status while an Adhoc SSI exception is pending.

The source does not specify notification recipients, delivery channels, payloads, validation rules, permissions, persistence semantics, or downstream integration behavior.

## Status and field model

The rows contain nine logical fields:

1. Source cashflow status
2. Source sub-status type
3. Source sub-status
4. Source SSI exception type
5. Action
6. Target cashflow status
7. Target sub-status type
8. Target sub-status
9. Target SSI exception type

`NA` and blank fields are reproduced as supplied. The source does not define whether they represent literal values, nulls, empty fields, or unchanged values.

## Status Action when it is in Waiting Status

```text
| **Source Status** | **Action** | **Target Status** |
| --- | --- | --- |
| Cashflow Status | Sub Status Type | Sub Status | SSI Exception Type | Action | Cashflow Status | Sub Status Type | Sub Status | SSI Exception Type |
| WAITING | Pending Exception | Pending Operator | NA | Maker Adhoc SSI | WAITING | Pending Exception | Pending Verification | Adhoc SI |
| WAITING | Pending Exception | Pending Verification | NA | Checker Reject | WAITING | Pending Exception | Pending Operator | Adhoc SI |
| WAITING | Pending Exception | Pending Operator | Adhoc SI | Maker Input Adhoc SSI | WAITING | Pending Exception | Pending Verification | Adhoc SI |
| WAITING | Pending Exception | Pending Verification | Adhoc SI | Checker Approve | READY | NA | NA | NA |
| WAITING | Pending Exception | Pending Verification | Adhoc SI | Checker Reject | WAITING | Pending Exception | Pending Operator | Adhoc SI |
| READY | NA | NA | NA | Maker Adhoc SSI | READY | Pending Exception | Pending Verification | Adhoc SI |
```

## Status Action when it is in Ready Status

```text
| **Source Status** | **Action** | **Target Status** |
| --- | --- | --- |
| Cashflow Status | Action | Target Status |
| Ready | | | NA | Maker Adhoc SSI | Ready | | | Adhoc SI |
| Ready | Pending Exception | Pending Verification | NA | Checker Reject | Ready | | | |
| Ready | | | Adhoc SI | Maker Input Adhoc SSI | Ready | Pending Exception | Pending Verification | Adhoc SI |
| Ready | Pending Exception | Pending Verification | Adhoc SI | Checker Approve | Ready | | | |
| Ready | Pending Exception | Pending Verification | Adhoc SI | Checker Reject | Ready | | | |
```

## Interpreted workflow behavior

- `Maker Adhoc SSI` changes a `WAITING` cashflow from `Pending Operator` with SSI exception type `NA` to `Pending Verification` with exception type `Adhoc SI`.
- `Maker Input Adhoc SSI` advances an existing `Adhoc SI` item from `Pending Operator` to `Pending Verification`.
- `Checker Approve` changes a `WAITING` cashflow from `Pending Verification` to `READY` and clears the pending exception fields.
- `Checker Reject` returns a `Pending Verification` item to `Pending Operator`.
- For a `READY` cashflow, maker processing can overlay a pending exception without changing the primary cashflow status.
- The distinction between `Maker Adhoc SSI` and `Maker Input Adhoc SSI` is suggested by the transitions but is not explicitly defined.

## Ambiguities and limitations

- The source uses both `READY` and `Ready`.
- The second table has a header that does not align with the nine logical fields represented by its rows.
- Blank target fields are not defined.
- The `READY` checker-rejection row with source exception type `NA` does not consistently specify the target exception type as `Adhoc SI`.
- Checker approval for `READY` does not describe any business effect beyond retaining `READY` and clearing or leaving blank workflow fields.
- Despite the source path referring to SSI stamping notification, no notification behavior is specified.

See [[adhoc-ssi-workflow]], [[ssi-exception-state-model]], and [[maker-checker-ssi-control]] for normalized domain interpretations. Open semantics are tracked in [[what-is-the-authoritative-adhoc-ssi-status-transition-matrix]] and [[what-notifications-are-triggered-by-ssi-stamping-actions]].
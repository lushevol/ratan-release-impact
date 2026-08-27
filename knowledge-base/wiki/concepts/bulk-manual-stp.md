---
type: concept
title: Bulk Manual STP
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, manual-stp, bulk-processing, group-blotter, operational-control]
related: [cash-settlement-home-page, settlement-day-2, group-blotter-bulk-stp-eligibility, group-blotter-pagination, is-pending-pre-group-or-pending-prev-group-the-authoritative-bulk-stp-status, why-does-pending-pre-group-use-case-require-bulk-manual-stp-error, what-is-the-partial-success-contract-for-bulk-manual-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# Bulk Manual STP

Bulk Manual STP is a proposed Group Blotter capability for manually pushing multiple selected exceptional cashflows to Cashflow Blotter in one operation.

## Intended Control

The action is intended for support-directed exceptional processing. Its confirmation warning must state:

> Please only perform bulk manual STP when informed by support team  
> [count] cashflow selected

The source does not define how support authorization is verified or logged.

## Eligibility and Results

The stated bulk eligibility rule is based on group status, not solely cashflow status. Eligible selected cashflows are expected to belong to groups in `PENDING_TRADE_VALIDATION` or `PENDING_PRE_GROUP`; other selections should trigger an error.

A successful batch is expected to:

- Move selected cashflows to `END`.
- Move associated groups to `COMPLETED`.
- Set `bookingSystemEvent` to `ManualDeliver`.

The source describes current single-record Manual STP as available for cashflows in `PENDING` or `ERROR`. It does not state whether those single-record rules are retained alongside the new bulk rule.

## Known Gaps

- `PENDING_PRE_GROUP` and `PENDING_PREV_GROUP` are both used in the source. See [[is-pending-pre-group-or-pending-prev-group-the-authoritative-bulk-stp-status]].
- A use case expects an error for selected `PENDING_PRE_GROUP` cashflows sharing a trade ID with another incomplete group. See [[why-does-pending-pre-group-use-case-require-bulk-manual-stp-error]].
- Partial-success, atomicity, retry, idempotency, and audit behavior are unspecified. See [[what-is-the-partial-success-contract-for-bulk-manual-stp]].

Bulk Manual STP is a proposed workflow within [[cash-settlement-home-page]] and its [[settlement-day-2]] requirements.
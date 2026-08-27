---
type: concept
title: Group Blotter Bulk Manual STP Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [group-blotter, manual-stp, eligibility, group-status, duplicate-payment-risk]
related: [bulk-manual-stp, cash-settlement-home-page, is-pending-pre-group-or-pending-prev-group-the-authoritative-bulk-stp-status, why-does-pending-pre-group-use-case-require-bulk-manual-stp-error]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# Group Blotter Bulk Manual STP Eligibility

Group Blotter bulk Manual STP is proposed as a status-controlled action intended to reduce duplicate-payment risk.

## Stated Rule

For multiple selected cashflows, Manual STP should be available only where all selected cashflows' group statuses are:

- `PENDING_TRADE_VALIDATION`
- `PENDING_PRE_GROUP`

Selections with other statuses should receive an error.

The source explicitly identifies generic `PENDING` as a duplicate-payment risk for bulk processing.

## Status-Level Distinction

The current single-cashflow capability is described using cashflow status: `PENDING` or `ERROR`.

The proposed bulk capability is described using group status. The requirement does not define whether:

- cashflow and group status must both pass validation;
- only selected groups are evaluated;
- every group associated with the same trade ID is evaluated;
- the single-record `PENDING` and `ERROR` rules remain valid; or
- `ERROR` can participate in any bulk action.

## Conflicting Evidence

The requirement details identify `PENDING_PRE_GROUP` as eligible, but the closed risk record uses `PENDING_PREV_GROUP`. See [[is-pending-pre-group-or-pending-prev-group-the-authoritative-bulk-stp-status]].

In Business Use Case 2, selected C3 and C4 are in `PENDING_PRE_GROUP`, yet the expected result is an error because another group with the same trade ID is incomplete and in `PENDING`. This may imply a same-trade or cross-group completeness rule that is absent from the stated eligibility contract. See [[why-does-pending-pre-group-use-case-require-bulk-manual-stp-error]].
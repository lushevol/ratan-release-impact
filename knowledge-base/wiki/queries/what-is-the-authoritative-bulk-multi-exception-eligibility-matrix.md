---
type: query
title: What Is the Authoritative Bulk Multi-Exception Eligibility Matrix?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bulk-processing, exceptions, eligibility, open-question]
related: [bulk-processing-for-multi-exceptions, bulk-exception-preview-eligibility, cashflow-bulk-submit-and-approve, failed-cashflow-status, cashflow-hold-unhold-authorization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# What Is the Authoritative Bulk Multi-Exception Eligibility Matrix?

## Question

How should user profile, cashflow state, sub-state, sub-state type, exception eligibility, risk permission, checker history, and authorization limits combine to determine bulk-action and bulk-preview eligibility?

## Evidence

The source defines:

- `Initial` plus `WAITING` / `Pending Operator` / `Pending Exception` → **Bulk Submit**.
- `Verify` plus `WAITING` / `Pending Verification` / `Pending Exception` → **Bulk Approve**.
- At least two selected cashflows.
- Identical `Counterparty`, `Booking Entity`, and `Payment Date` values.
- Preview blocking for checker self-submission, absent or ineligible exceptions, unauthorized high-risk exceptions, and blocked cashflow authorization limits.

## Unresolved Points

The source does not define mixed-status behavior, exception-level eligibility, the required high-risk permission, authorization-limit calculations, or whether validation is all-or-nothing.

## Desired Resolution

An authoritative matrix should specify the evaluation order, the scope of each check, the user-facing failure behavior, and whether the same validations are enforced server-side at submission or approval time.
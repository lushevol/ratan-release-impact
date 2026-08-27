---
type: concept
title: Bulk Cashflow Selection Homogeneity
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bulk-processing, validation, cashflow-selection]
related: [bulk-processing-for-multi-exceptions, cashflow-bulk-submit-and-approve, payment-date-override, cashflow-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# Bulk Cashflow Selection Homogeneity

Bulk cashflow selection homogeneity is the requirement that all cashflows selected for a bulk action share the same business attributes required by that action.

## Required Matching Attributes

For both **Bulk Submit** and **Bulk Approve**, all selected cashflows must have identical:

- `Counterparty`
- `Booking Entity`
- `Payment Date`

The requirement applies after the user selects the bulk right-menu action.

## Failure Behavior

If any required attribute differs among the selected cashflows, the system must:

1. Display a popup error alert.
2. Prevent navigation to bulk preview.

The source does not define the exact alert text or whether the user interface identifies the differing attribute or cashflow.

## Date Comparison Ambiguity

The design does not define whether `Payment Date` is compared using the stored value, displayed local date, UTC date, or another canonical representation. This is related to [[queries/how-are-payment-dates-compared-for-bulk-cashflow-validation]] and [[queries/what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]].
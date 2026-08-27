---
type: source
title: Bulk UI Technical Design
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, multi-exceptions, bulk-processing, ui-technical-design]
related: [bulk-processing-for-multi-exceptions, bulk-cashflow-selection-homogeneity, bulk-exception-preview-eligibility, cashflow-bulk-submit-and-approve]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# Bulk UI Technical Design

## Scope

This functional and UI technical design defines the bulk right-menu conditions, action-specific validation, and bulk-preview eligibility rules for multi-exception cashflow processing in the Cash Settlement Home Page.

## Bulk Right Menu

Conditions show bulk right menu:

1. At least select 2 cashflows
2. All cashflows matches states below could lead to specific action.

| User Profile | Cashflow State | Cashflow Sub State | Cashflow Sub State Type | Action |
| --- | --- | --- | --- | --- |
| Initial | WAITING | Pending Operator | Pending Exception | Bulk Submit |
| Verify | WAITING | Pending Verification | Pending Exception | Bulk Approve |

After click bulk right menu button, will do validation below

| Action | Counterparty | Booking Entity | Payment Date |
| --- | --- | --- | --- |
| Bulk Submit | all selected cashflows should be the same. | all selected cashflows should be the same. | all selected cashflows should be the same. |
| Bulk Approve | all selected cashflows should be the same. | all selected cashflows should be the same. | all selected cashflows should be the same. |

Otherwise, popup error alert without going to bulk preview.

## Bulk Preview

| Case | If eligible for bulk | |
| --- | --- | --- |
| checker stage, and is submitted by current checker. | No | |
| no exceptions for current cashflow sub state | No | |
| contains uneligible exception for current cashflow sub state | No | |
| has high risk exception for current cashflow sub state but no permission | No | |
| When checker making approve, but cashflow auth limits is blocked. | No | |

## Interpretation

The design establishes two validation stages:

1. **Bulk action eligibility:** At least two cashflows must be selected, and the selected cashflows must match the action-specific user-profile, state, sub-state, and sub-state-type criteria.
2. **Bulk preview eligibility:** The selected cashflows must have identical `Counterparty`, `Booking Entity`, and `Payment Date` values. Additional checker, exception, permission, and authorization-limit checks can still prevent entry to or completion of bulk preview.

The document does not define error text, the exact meaning of “submitted by current checker,” exception eligibility rules, authorization-limit calculations, date comparison semantics, or whether one ineligible cashflow rejects the complete selection.

## Related Wiki Context

This design extends the selection and exception behavior associated with the [[entities/cashflow-blotter]] and [[concepts/cashflow-filtering]]. Its maker/checker implications may relate to [[concepts/swift-value-date-maker-checker-control]], while the date comparison rule may depend on [[queries/what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]].
---
type: concept
title: Bulk Exception Preview Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bulk-processing, exceptions, preview, authorization]
related: [bulk-processing-for-multi-exceptions, cashflow-bulk-submit-and-approve, cashflow-hold-unhold-authorization, swift-value-date-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# Bulk Exception Preview Eligibility

Bulk exception preview eligibility is the second-stage assessment of whether a selected group of cashflows may proceed after a bulk action has been chosen and selection attributes have been validated.

## Preview-Blocking Conditions

The design marks bulk processing as ineligible when any of the following conditions applies:

- The cashflow is at checker stage and was submitted by the current checker.
- There are no exceptions for the current cashflow sub-state.
- The cashflow contains an ineligible exception for the current cashflow sub-state.
- The cashflow contains a high-risk exception for the current cashflow sub-state, but the current user lacks the required permission.
- A checker is approving, but cashflow authorization limits are blocked.

## Control Dimensions

Preview eligibility combines:

- Current workflow stage and current user history.
- Exception existence for the current sub-state.
- Exception eligibility for bulk handling.
- High-risk exception permissions.
- Checker authorization limits.

The source does not identify the permission name, define the exception taxonomy, or explain how authorization limits are calculated.

## Batch Semantics

The design does not state whether these checks are evaluated per cashflow with partial results, or whether one failing cashflow blocks the complete selection. This unresolved behavior is tracked in [[queries/does-one-ineligible-cashflow-block-the-entire-bulk-operation]].
---
type: query
title: Does One Ineligible Cashflow Block the Entire Bulk Operation?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bulk-processing, exceptions, validation, open-question]
related: [bulk-processing-for-multi-exceptions, bulk-exception-preview-eligibility, bulk-cashflow-selection-homogeneity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# Does One Ineligible Cashflow Block the Entire Bulk Operation?

## Question

When a selected cashflow fails a bulk-preview eligibility check, does the system reject the entire selection or allow eligible cashflows to continue?

## Evidence

The design states that selected cashflows must satisfy common action and attribute requirements, and it lists several conditions under which bulk processing is not eligible. It does not define whether the conditions apply to the whole batch or only to the affected cashflow.

## Required Clarification

Confirm whether the system should:

- Reject the complete batch.
- Remove ineligible cashflows and continue with the remainder.
- Present per-cashflow results while preventing final submission or approval.
- Allow preview but block the final action.

The resolution should also define the popup or inline error behavior and whether the backend repeats the decision at execution time.
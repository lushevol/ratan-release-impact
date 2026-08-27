---
type: query
title: Should Cashflow Sub State Be Added to Quick Search?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, quick-search, cashflow-sub-state, requirements-confirmation]
related: [cash-settlement-query-validation, cash-settlement-home-page, lms-cashflow-lifecycle-message-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# Should Cashflow Sub State Be Added to Quick Search?

Should Cashflow Sub State be added to the quick-search interface, and what validation should apply if it is approved?

## Evidence

The source explicitly conditions this addition on confirmation with the user. It provides no allowed values, multi-value behavior, operator rules, required combinations, or relationship to Cashflow State.

## Decision Needed

Obtain confirmation and define:

- Whether Cashflow Sub State is included.
- The accepted values and display labels.
- Whether multiple values are supported.
- Whether value date, booking entity, or counterparty remains required.
- Whether invalid or unknown sub-state values are rejected.
- Whether the field should also be available in custom filters.
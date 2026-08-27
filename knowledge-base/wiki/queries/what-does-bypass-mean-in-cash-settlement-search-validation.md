---
type: query
title: What Does “Bypass” Mean in Cash Settlement Search Validation?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, validation, bypass, quick-search, custom-filter]
related: [cash-settlement-query-validation, cash-settlement-filter-operator-allowlists]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# What Does “Bypass” Mean in Cash Settlement Search Validation?

What validation behavior is intended by “by pass” for trade original ID and fields ending in `_id`?

## Possible Interpretations

The term could mean that the field:

- Is accepted without any validation.
- Is exempt only from required-field or field-combination checks.
- Is exempt from the value-date requirement.
- Uses a separate identifier lookup mechanism.
- Bypasses validation but remains subject to execution or authorization rules.

## Decision Needed

Define the exact exemption, including whether it applies to quick search, custom filters, or both; whether it changes the required party context; and whether invalid identifier formats are still rejected.
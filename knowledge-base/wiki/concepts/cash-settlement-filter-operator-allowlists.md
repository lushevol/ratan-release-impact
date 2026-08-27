---
type: concept
title: Cash Settlement Filter Operator Allowlists
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, custom-filter, operators, validation, payment-date]
related: [cash-settlement-query-validation, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# Cash Settlement Filter Operator Allowlists

The custom-filter requirement defines field-specific operator allowlists for the [[cash-settlement-home-page]].

## Allowed Operators

| Field | Allowed operators |
|---|---|
| Payment date | `=`, `in`, `bet`, `<=`, `>=` |
| Booking entity FMID | `=`, `in` |
| Cashflow state | `=`, `in` |

A filter containing payment date, booking entity FMID, and cashflow state is described as passing validation.

## Unresolved Semantics

The source uses `bet` without defining it. It may represent a between-range operator, but its inclusivity, operand format, and date handling are not specified.

The source also states that fields ending in `_id` bypass validation. It does not establish whether this means automatic acceptance, exemption from a field-combination rule, exemption from value-date requirements, or use of a separate identifier lookup path. This ambiguity is tracked in [[what-does-bypass-mean-in-cash-settlement-search-validation]].
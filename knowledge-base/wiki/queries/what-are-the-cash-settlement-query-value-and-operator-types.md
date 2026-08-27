---
type: query
title: What Are the Cash Settlement Query Value and Operator Types?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-dsl, graphql, data-validation]
related: [cash-settlement-advanced-query-dsl, cashflow-ultra-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# What Are the Cash Settlement Query Value and Operator Types?

`FilterArg` is referenced but not defined in the design. Examples use strings, arrays, numeric values, dates, and Boolean values encoded as strings.

Establish the authoritative `FilterArg` schema and validation rules for:

- supported operators, including `EQ`, `IN`, and `NOTIN`;
- scalar versus list cardinality by operator;
- date, numeric, Boolean, and string coercion;
- null and empty-value behavior;
- wildcard-like field values;
- unsupported-field and unsupported-operator errors.

Without this contract, UI-generated filters and backend interpretation can diverge.
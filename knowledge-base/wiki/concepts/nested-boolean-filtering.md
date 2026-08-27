---
type: concept
title: Nested Boolean Filtering
created: 2026-08-24
updated: 2026-08-24
tags: [filtering, boolean-logic, query-builder, cash-settlement]
related: [cash-settlement-advanced-query-dsl, flat-filter-builder-vs-nested-query-dsl, cashflow-blotter, cashflow-ultra-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# Nested Boolean Filtering

Nested Boolean filtering lets a query builder represent conjunctions and disjunctions at multiple levels, such as:

```text
field1 = value AND field2 = value AND (field3 = value OR field4 = value)
```

This differs from a flat filter builder, where every condition is implicitly joined by `AND`.

For cash settlement, nested filtering enables business rules that cannot be expressed through all-match filtering alone, including the documented Commodity-or-PM UK-payment use case. The proposed implementation uses recursive `LogicFilter` groups in the [[cash-settlement-advanced-query-dsl]].

## Normalization

A normalized Boolean filter tree keeps one logical role at each node and removes redundant groups. In the documented design, a node should represent only an `and` group, an `or` group, or an atomic-filter collection. A one-child `and` or `or` group should normally be flattened into its parent.

These rules require precise validation because some source examples are structurally inconsistent with them.
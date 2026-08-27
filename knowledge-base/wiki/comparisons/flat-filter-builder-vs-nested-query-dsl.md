---
type: comparison
title: Flat Filter Builder versus Nested Query DSL
created: 2026-08-24
updated: 2026-08-24
tags: [query-builder, filtering, boolean-logic, cash-settlement]
related: [nested-boolean-filtering, cash-settlement-advanced-query-dsl, cashflow-ultra-query, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# Flat Filter Builder versus Nested Query DSL

## Flat filter builder

The existing model treats all selected filters as an implicit conjunction:

```text
field1 = value AND field2 = value AND field3 = value
```

It is simple but cannot represent alternative criteria or parenthesized business logic.

## Nested query DSL

The proposed model uses recursive `LogicFilter` nodes to represent `AND`, `OR`, and nested groups:

```text
field1 = value AND field2 = value AND (field3 = value OR field4 = value)
```

It supports complex cash-settlement filtering and can retain flat-query behavior as a subset of the new model.

## Trade-off

The nested model adds expressiveness and a migration-oriented abstraction for a future OpenSearch backend. It also requires validation, normalization, depth enforcement, and unambiguous translation rules. The source does not yet provide a complete `FilterArg` type or a verified SQL/OpenSearch mapping.
---
type: concept
title: Cash Settlement Advanced Query DSL
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-dsl, graphql, filtering, opensearch]
related: [nested-boolean-filtering, cashflow-ultra-query, cashflow-ultra-query-count, graphql, ratanone, what-is-the-canonical-cash-settlement-query-dsl, how-should-cash-settlement-filter-dsl-be-translated-to-sql-and-opensearch, what-are-the-cash-settlement-query-value-and-operator-types]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# Cash Settlement Advanced Query DSL

The Cash Settlement Advanced Query DSL is a recursive GraphQL filter structure for querying cashflow-related data. It distinguishes atomic field predicates (`FilterArg`) from logical composition nodes (`LogicFilter`).

```graphql
input LogicFilter {
  and: [LogicFilter!]
  or: [LogicFilter!]
  filters: [FilterArg!]
}
```

The design is used by [[cashflow-ultra-query]] and [[cashflow-ultra-query-count]] in the [[ratanone]] cash-settlement context.

## Intended invariants

A `LogicFilter` node should have exactly one structural role:

- `and` combines children conjunctively.
- `or` combines children disjunctively.
- `filters` holds atomic predicates.

The documented depth limit is three. The design also aims to flatten logically redundant single-child `and` and `or` groups. These invariants make the structure a constrained query abstract syntax tree rather than an arbitrary JSON object.

## Compatibility objective

The DSL must cover existing flat-query scenarios while enabling nested Boolean expressions. Its OpenSearch alignment is explicitly a future-migration objective. The source does not supply a formal mapping between the GraphQL structure and OpenSearch request bodies, SQL generation, or operator semantics.

## Unresolved contract details

`FilterArg` is not defined in the design. In particular, `EQ`, `IN`, `NOTIN`, wildcard-like values, dates, numbers, Boolean values, nulls, and arrays require a canonical typed contract. The source examples also conflict with the stated one-role-per-node invariant. [[what-is-the-canonical-cash-settlement-query-dsl]] tracks these issues.
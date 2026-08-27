---
type: entity
title: Cashflow Ultra Query
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, cashflow, query-api, pagination, cash-settlement]
related: [cashflow-ultra-query-count, cash-settlement-advanced-query-dsl, graphql, cashflow-blotter, dashboard, what-is-the-cash-settlement-query-pagination-and-sorting-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# Cashflow Ultra Query

`cashflowUltraQuery` is the proposed GraphQL result-retrieval API for advanced cashflow filtering in Cash Settlement Home Page.

```graphql
type Query {
  cashflowUltraQuery(payload: RatanUltraQuery): UltraQueryResult!
}

input RatanUltraQuery {
  filters: LogicFilter!
  pagingOption: PagingOption!
  pageIndex: Int!
  itemsPerPage: Int!
  orderArgs: [QueryOrder!]!
  # placeholder
  cursor: String
}
```

It consumes the recursive [[cash-settlement-advanced-query-dsl]] and returns a result page, hit count, last-page indicator, optional cursors, and `ResultNew` records.

## Pagination and ordering status

`PAGE_INDEX` is the required implemented pagination mode. `CURSOR` and `NO_PAGINATION` are exposed as placeholders. `orderArgs` is also a placeholder; the source states a default created-time ordering but does not establish its direction or custom-sort behavior.

The authoritative paging, cursor, and ordering behavior remains open in [[what-is-the-cash-settlement-query-pagination-and-sorting-contract]].
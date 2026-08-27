---
type: entity
title: Cashflow Ultra Query Count
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, cashflow, count-api, performance, cash-settlement]
related: [cashflow-ultra-query, cash-settlement-advanced-query-dsl, dashboard, ui-performance-metrics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# Cashflow Ultra Query Count

`cashflowUltraQueryCount` is the GraphQL API that returns the count of cashflow records matching a `LogicFilter`, without returning result records.

```graphql
type Query {
  cashflowUltraQueryCount(payload: RatanUltraQueryCount): UltraQueryCountResult!
}

input RatanUltraQueryCount {
  filters: LogicFilter!
}

type UltraQueryCountResult {
  count: Int!
}
```

The source reports that this count API outperformed the normal query API in Dashboard benchmark screenshots. This is a directional observation only: the documentation provides no reproducible measurements or workload methodology.

The count-request example in the source violates the documented rule that a `LogicFilter` node must contain only one of `and`, `or`, or `filters`. Its request shape should be validated before use as a canonical integration example.
---
type: concept
title: Exception Code Statistics Query
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, exception, statistics, cashflow, ratan]
related: [ratan, cashflow-blotter, nstp-exception-filter, cashflow-exception-read-model-enrichment, graphql-cashflow-blotter-aggregate-queries, what-is-the-authoritative-ratan-frontend-graphql-schema, what-are-the-semantic-and-nullability-rules-for-ratan-graphql-aggregate-filters]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# Exception Code Statistics Query

`exceptionCodeStatisticsByFilter` is a proposed RATAN GraphQL query that returns exception counts grouped by `exceptionCode` under cashflow-style filters.

```graphql
type Query {
  exceptionCodeStatisticsByFilter(filter:[FilterArg!]!): [ExceptionCodeStatistics!]!
}

type ExceptionCodeStatistics {
  exceptionCode: String!
  count: Int!
}
```

The source says its filters follow the same pattern as the cashflow query. Its non-null list of non-null `FilterArg` values differs from the nullable filter lists proposed for `cashflowsCount` and `topExposure`; the intended distinction is not explained.

## Scope boundary

The source uses the generic term `exceptionCode`. Although this is adjacent to [[nstp-exception-filter]] and [[cashflow-exception-read-model-enrichment]], it does not establish that these statistics are specifically NSTP-code statistics.

The proposal does not specify which exception lifecycle states qualify, the data source, aggregation timing, authorization, empty-result behavior, or resolver implementation.
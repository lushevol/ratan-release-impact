---
type: concept
title: GraphQL Cashflow Blotter Aggregate Queries
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, cashflow-blotter, aggregate-query, ratan]
related: [ratan, cashflow-blotter, cash-settlement-query-service-graphql-read-model, exception-code-statistics-query, currency-to-usd-rate-query, what-is-the-authoritative-ratan-frontend-graphql-schema, what-are-the-semantic-and-nullability-rules-for-ratan-graphql-aggregate-filters]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# GraphQL Cashflow Blotter Aggregate Queries

The GraphQL Schema Completion 2025 proposal extends RATAN's front-end GraphQL interface with aggregate queries intended for operational blotter views:

- `cashflowsCount(filter:[FilterArg]): ResultPageInfo!`
- `groupMessagesCount(filter:GroupMsgReq): ResultPageInfo!`
- `topExposure(filter: [FilterArg], top: Int!): [TopExposureRecord!]!`

The proposal states that `cashflowsCount` uses the same parameters as the cashflow query and that `groupMessagesCount` uses the same parameters as the group blotter query. This expresses an intended filter-alignment rule: displayed totals should be scoped consistently with the associated list view.

`topExposure` is intended to return the top *N* counterparties trading with SCB, with `counterparty`, `clientType`, and `amount` fields. The source does not define the exposure aggregation method, ranking direction, tie behavior, currency normalization, business-date scope, or whether the amount uses the separately proposed `rate2usd` query.

## Contract status

These signatures are proposal-level design artifacts, not confirmation of deployed RATAN behavior or of a backing resolver/read model. The source does not define `FilterArg`, `GroupMsgReq`, authorization, pagination, caching, performance requirements, or error handling.

The lowercase root declaration `type query` for `topExposure` conflicts with the `type Query` declarations used elsewhere and requires reconciliation because GraphQL type names are case-sensitive.

See [[cash-settlement-query-service-graphql-read-model]] for the related GraphQL read-model context and [[what-are-the-semantic-and-nullability-rules-for-ratan-graphql-aggregate-filters]] for unresolved filter consistency.
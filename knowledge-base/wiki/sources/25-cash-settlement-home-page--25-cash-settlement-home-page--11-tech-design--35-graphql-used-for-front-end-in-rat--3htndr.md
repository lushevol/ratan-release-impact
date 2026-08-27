---
type: source
title: GraphQL Schema Completion 2025
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, graphql, cashflow-blotter, netting, api-design]
related: [ratan, cashflow-blotter, graphql-cashflow-blotter-aggregate-queries, exception-code-statistics-query, currency-to-usd-rate-query, cash-settlement-query-service-graphql-read-model, what-is-the-authoritative-ratan-frontend-graphql-schema, what-are-the-authoritative-netting-preview-and-execution-graphql-contracts, what-are-the-semantic-and-nullability-rules-for-ratan-graphql-aggregate-filters]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# GraphQL Schema Completion 2025

This proposal extends an earlier RATAN front-end GraphQL schema for cashflow-detail retrieval. It proposes aggregate and auxiliary read operations for Cashflow Blotter, group blotter, exception analysis, and currency conversion. It also identifies Netting Preview and Netting Execution as required operations, but does not define GraphQL contracts for either.

The document is evidence of intended API design only. It does not establish implementation status, resolver ownership, backing read models, authorization, performance, or operational behavior.

## Proposed scenarios

### Cashflow Blotter

| Action | Type | Description | Proposal Schema |
| --- | --- | --- | --- |
| Cashflow Record Count | Query | Only get the count of cashflows. Have the same parameters with cashflows query. | type Query { cashflowsCount(filter:[FilterArg]): ResultPageInfo! } type ResultPageInfo { totalHits: Float! } |
| Top Exposure | Query | Get the top N counterparties trading with SCB. | type query { topExposure(filter: [FilterArg], top: Int!): [TopExposureRecord!]! } type TopExposureRecord { counterparty: String! clientType: String! amount: Float! } |

```graphql
type Query {
  cashflowsCount(filter:[FilterArg]): ResultPageInfo!
}

type ResultPageInfo {
  totalHits: Float!
}
```

```graphql
type query {
  topExposure(filter: [FilterArg], top: Int!): [TopExposureRecord!]!
}

type TopExposureRecord {
  counterparty: String!
  clientType: String!
  amount: Float!
}
```

### Group Blotter Query

| Action | Type | Description | Schema |
| --- | --- | --- | --- |
| Group Record Count | Query | Only get the count of group records. Have the same paramters with group blotter query. | type Query { groupMessagesCount(filter:GroupMsgReq): ResultPageInfo! } type ResultPageInfo { totalHits: Float! } |

```graphql
type Query {
  groupMessagesCount(filter:GroupMsgReq): ResultPageInfo!
}

type ResultPageInfo {
  totalHits: Float!
}
```

### Exception

| Action | Type | Description | Schema |
| --- | --- | --- | --- |
| Exception Statistic From Filter | Query | get exception statistic by filters, filters are the same pattern with cashflow query. | type Query { exceptionCodeStatisticsByFilter(filter:[FilterArg!]!): [ExceptionCodeStatistics!]! } type ExceptionCodeStatistics { exceptionCode: String! count: Int! } |

```graphql
type Query {
  exceptionCodeStatisticsByFilter(filter:[FilterArg!]!): [ExceptionCodeStatistics!]!
}

type ExceptionCodeStatistics {
  exceptionCode: String!
  count: Int!
}
```

### Rate

| Action | Type | Description | Schema |
| --- | --- | --- | --- |
| Rate to USD | Query | Get rate of current ccy to USD | type Query { rate2usd(ccy: [String!]!): [Rate2USDMapping] } type Rate2USDMapping { ccy: String! rate: Float! } |

```graphql
type Query {
  rate2usd(ccy: [String!]!): [Rate2USDMapping]
}

type Rate2USDMapping {
  ccy: String!
  rate: Float!
}
```

### Netting

| Action | Type | |
| --- | --- | --- |
| Netting Preview | Query | |
| Netting Execution | Mutation | |

## Design observations

The proposed `cashflowsCount`, `groupMessagesCount`, and `exceptionCodeStatisticsByFilter` operations are intended to align their filter behavior with corresponding cashflow or group views. The definitions of `FilterArg`, `GroupMsgReq`, and the underlying list-query contracts are not included, so semantic equivalence cannot be verified.

There are material unresolved schema issues:

- Most operations are declared on `Query`, while `topExposure` is declared on lowercase `query`. GraphQL type names are case-sensitive.
- Filter-list nullability differs across operations.
- `ResultPageInfo.totalHits` is a non-null `Float`, although record counts are ordinarily integral.
- `rate2usd` permits a nullable list and nullable elements despite a required currency input list.
- The meaning, currency basis, sort direction, tie handling, and business-date scope of `topExposure.amount` are not defined.
- No Netting inputs, outputs, authorization, idempotency, state, or failure semantics are supplied.

See [[graphql-cashflow-blotter-aggregate-queries]], [[exception-code-statistics-query]], and [[currency-to-usd-rate-query]]. Contract reconciliation is tracked in [[what-is-the-authoritative-ratan-frontend-graphql-schema]].
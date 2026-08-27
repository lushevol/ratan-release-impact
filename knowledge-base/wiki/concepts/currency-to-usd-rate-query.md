---
type: concept
title: Currency-to-USD Rate Query
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, fx-rate, currency-conversion, ratan]
related: [ratan, graphql-cashflow-blotter-aggregate-queries, what-is-the-authoritative-ratan-frontend-graphql-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# Currency-to-USD Rate Query

`rate2usd` is a proposed RATAN GraphQL query for retrieving a USD conversion rate for each requested currency code.

```graphql
type Query {
  rate2usd(ccy: [String!]!): [Rate2USDMapping]
}

type Rate2USDMapping {
  ccy: String!
  rate: Float!
}
```

The input requires a non-null list of non-null currency strings. The response list and its elements are nullable, leaving partial-result and missing-rate behavior unspecified.

## Unresolved semantics

The proposal does not identify the rate source, rate timestamp or validity period, rate direction, precision/rounding rules, treatment of USD itself, unsupported-currency behavior, or authorization and audit requirements. It also does not establish that the `amount` returned by `topExposure` is USD-denominated or calculated using this operation.
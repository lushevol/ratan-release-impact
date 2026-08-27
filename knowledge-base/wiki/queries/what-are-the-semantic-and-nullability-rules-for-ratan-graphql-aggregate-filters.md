---
type: query
title: What Are the Semantic and Nullability Rules for RATAN GraphQL Aggregate Filters?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, graphql, filters, nullability, aggregate-query]
related: [ratan, graphql-cashflow-blotter-aggregate-queries, exception-code-statistics-query, cash-settlement-query-service-graphql-read-model, what-is-the-authoritative-ratan-frontend-graphql-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# What Are the Semantic and Nullability Rules for RATAN GraphQL Aggregate Filters?

## Question

Do RATAN GraphQL aggregate operations apply the same filter semantics as their associated list views, and what do omitted, null, empty, and null-item filter lists mean?

## Evidence

The proposal uses three distinct signatures:

```graphql
cashflowsCount(filter:[FilterArg]): ResultPageInfo!
topExposure(filter: [FilterArg], top: Int!): [TopExposureRecord!]!
exceptionCodeStatisticsByFilter(filter:[FilterArg!]!): [ExceptionCodeStatistics!]!
groupMessagesCount(filter:GroupMsgReq): ResultPageInfo!
```

It states that the count and exception queries should use filters aligned with cashflow or group-blotter querying, but does not include definitions for `FilterArg`, `GroupMsgReq`, or the corresponding list-query contracts.

## Resolution criteria

Establish canonical input definitions and determine whether omitted filters, `null`, an empty list, and a list containing null entries have distinct behavior. Verify that filtering, default scopes, entitlements, business-date treatment, and error handling are equivalent between a list query and each related aggregate query.
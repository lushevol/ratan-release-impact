---
type: query
title: What Is the Authoritative RATAN Frontend GraphQL Schema?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, graphql, api-contract, cashflow-blotter]
related: [ratan, cashflow-blotter, cash-settlement-query-service-graphql-read-model, graphql-cashflow-blotter-aggregate-queries, exception-code-statistics-query, currency-to-usd-rate-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# What Is the Authoritative RATAN Frontend GraphQL Schema?

## Question

Which RATAN GraphQL schema is authoritative for front-end cashflow, group blotter, exposure, exception-statistics, and currency-rate operations?

## Why this is open

GraphQL Schema Completion 2025 proposes new root operations but does not identify a deployed schema version, service owner, resolver implementation, backing read model, or release status. It also contains inconsistent root-type casing: `type Query` for most operations and `type query` for `topExposure`.

## Evidence to reconcile

- The proposal defines `cashflowsCount`, `groupMessagesCount`, `topExposure`, `exceptionCodeStatisticsByFilter`, and `rate2usd`.
- [[cash-settlement-query-service-graphql-read-model]] documents related GraphQL read-model context.
- [[what-is-the-authoritative-cashflow-dashboard-graphql-contract]] may contain related contract evidence, but its dashboard scope must not be assumed to be identical to Cashflow Blotter scope.

## Resolution criteria

Confirm the published schema and root operation configuration; authoritative definitions of `FilterArg`, `GroupMsgReq`, and shared result types; resolver and read-model ownership; deployment status; and authorization, error, and performance contracts.
---
type: source
title: GraphQL Used For Front End In RATAN
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, ratan, ratanone, frontend, api-architecture, cash-settlement]
related: [ratanone-graphql-front-end-api-standard, graphql-query-performance-observability, data-modelling, ratan, rule-service, what-is-the-authoritative-ratanone-graphql-transport-and-bypass-policy, what-are-the-canonical-ratanone-graphql-schemas-and-subscription-semantics, what-performance-and-query-complexity-controls-govern-ratanone-graphql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN.md"]
---
# GraphQL Used For Front End In RATAN

This undated design guideline states intended principles for GraphQL between the RATANONE front end and backend APIs. It is an architectural and data-governance direction, not an implementation contract: the available content contains no GraphQL SDL, field definitions, resolver mappings, endpoint, transport configuration, or performance results.

## Stated GraphQL Characteristics

The source describes GraphQL as a query language for APIs and a server-side runtime that executes queries against a defined type system. It identifies the following reasons for use:

1. GraphQL APIs have a strongly typed schema.
2. GraphQL avoids overfetching and underfetching.
3. GraphQL enables rapid product development.
4. GraphQL APIs can be composed.
5. GraphQL has an open-source ecosystem and community.

The stated operation types are:

1. Query for reading data, recommended in Ratan.
2. Mutation for writing data.
3. Subscription for receiving real-time data over time, recommended in Ratan.

## RATANONE Standards and Principles

| Principal | Comment | Exceptions |
| --- | --- | --- |
| All RATANONE front end query to backend APIs are supposed to go via GraphQL |  |  |
| GraphQL schema should be defined clearly for each use cases before implementing it | Reduce the number of API calls from UI to backend, best utilize the capability of GraphQL to aggregate data. | If any aggregation party cause performance issue, we may consider to make it a single API call. |
| All fields/attributes used by GraphQL query need to be defined as standard logical model/Biz term natively in DM or RATAN extension. | All the fields should be from the fields defined in rule service, Data modelling indexed term is the first choice, Ratan specific fields should be defined otherwise and mark as `RATAN_DATA` |  |
| The performance of GraphQL query should be tracked and monitored |  |  |

The policy applies explicitly to frontend queries. Although mutations are listed as a GraphQL feature, the source does not recommend them for Ratan or state that frontend writes must use GraphQL.

## Intended Use Cases

| Case | Type | Schema or artifact | Description |
| --- | --- | --- | --- |
| Query Trade List | HTTPS GET | Click: |  |
| Query Trade Detail | HTTPS GET |  |  |
| Quick search on Trade blotter | HTTPS GET |  |  |
| Trade Notification | Subscription |  |  |
| Query Cashflow List | HTTPS GET | [Multi Exceptions - Exceptions in Cashflow CN](https://www.figma.com/proto/crlFDt3cKfWzIXWdUhrtQ7/Exceptions-in-Cashflow-CN?node-id=521-2&scaling=scale-down-width&page-id=0%3A1&starting-point-node-id=521%3A2) |  |
| Query Cashflow Detail | HTTPS GET |  |  |
| Quick search on Cashflow blotter | HTTPS GET |  |  |
| Cashflow Notification | Subscription |  |  |
| Query Counterparties Info | HTTPS GET | Click: |  |
| Query Exceptions List | HTTPS GET | Click: |  |
| Exceptions Notification | Subscription |  |  |
| Quick Search | UX |  | User can search by static fields. |
| Custom Filter | UX |  | User can build search conditions using multiple search fields. |
| Custom View | UX |  | User can customize table columns and query-list response structure. |

The source also includes headings for trade, cashflow (BCS), cashflow (Settlement CN), counterparty, and exception schemas. No diagram contents, schemas, types, arguments, results, or notification payloads appear beneath those headings in the available source text.

## Scope and Limitations

The source supports an intended GraphQL-first approach for RATANONE frontend reads, use-case-specific schema design, logical-field provenance, and performance monitoring. It does not establish:

- a mandatory GraphQL policy for frontend mutations;
- whether the performance exception permits a REST or direct-backend bypass;
- whether `HTTPS GET` is required, or whether GraphQL POST is supported;
- a canonical endpoint, authentication model, entitlement policy, pagination approach, or query-complexity limit;
- subscription transport, authorization, ordering, deduplication, reconnection, replay, or version semantics;
- performance targets, observability ownership, dashboards, or evidence that GraphQL outperforms REST;
- the implementation contract of existing [[cash-settlement-query-service-graphql-read-model]] or [[cashflow-notification-and-auto-refresh]] capabilities.

The source links to [Ratan UI Performance Analysis (2022 Dec)](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2608466605), but does not reproduce its methods or findings.
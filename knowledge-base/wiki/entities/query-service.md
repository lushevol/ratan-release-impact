---
type: entity
title: Query Service
created: 2026-08-24
updated: 2026-08-24
tags: ["cash-settlement", "query-service", "postgresql", "connection-pool", "performance", "api", "graphql", "entitlement"]
related: ["ultra-cashflow-query", "postgresql-work-mem-sizing", "jsonb-numeric-expression-indexing", "cash-settlement-performance-and-stress-testing", "ces", "ssdr", "cash-settlement-data-entitlement", "ces-data-entitlement-integration", "cashflow-blotter"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md"]
---
# Query Service

Query Service is the central preliminary enforcement point for Cash Settlement data-entitlement scope in this source.

## Identified Interfaces

| Consumer or feature | Interface | Stated change or status |
| --- | --- | --- |
| [[ssdr]] report | `v2/data/provider/query/cashflows` | Switch to CES |
| [[cashflow-blotter]] | `/graphql` | Add entitlement control; currently using mock entitlement |
| Cashflow notification | `/api/ratan/notification/subscriptions` (WebSocket) | Add entitlement control; currently using mock entitlement |
| Cashflow history | `/graphql` | In scope, but no change specified |
| Unconfirmed feature | `/v1/query/cashflows` | Unconfirmed |

The source does not specify whether Query Service performs authorization at request entry, filters returned records, delegates decisions to CES, or applies policy to GraphQL aggregates, subscriptions, exports, and cached results.
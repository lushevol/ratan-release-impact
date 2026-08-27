---
type: project
title: CES Data Entitlement Integration
created: 2026-08-24
updated: 2026-08-24
tags: [ces, entitlement, cash-settlement, regulatory-control, m7]
related: [ces, query-service, ssdr, cash-settlement-data-entitlement, what-is-the-authoritative-ces-entitlement-decision-and-enforcement-contract, which-cash-settlement-interfaces-are-in-the-ces-entitlement-scope, how-are-graphql-aggregates-and-websocket-subscriptions-filtered-by-cash-settlement-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md"]
status: planned
owner: ""
start_date: 2025-12-10
target_date: 2026-03-31
---
# CES Data Entitlement Integration

## Objective

Integrate Cash Settlement data access controls with [[ces]], described by the source as FM's strategic entitlement solution, to mitigate M7 regulatory risk.

The source targets go-live in March 2026. The `target_date` is recorded as the end of that month solely because the source provides month-level precision; an exact target date is not stated.

## Preliminary Scope

| Feature | Service | API | Planned change or status |
| --- | --- | --- | --- |
| [[ssdr]] report | [[query-service]] | `v2/data/provider/query/cashflows` | Switch to CES |
| [[cashflow-blotter]] | Query Service | `/graphql` | Add entitlement control; mock entitlement currently reported |
| Cashflow notification | Query Service | `/api/ratan/notification/subscriptions` | Add entitlement control; mock entitlement currently reported |
| Cashflow history | Query Service | `/graphql` | Change not specified |
| Group blotter | Group service | Not specified | Change not specified |
| Unconfirmed interface | Query Service | `/v1/query/cashflows` | Scope unconfirmed |
| BCS blotter | Data ambassador | `/graphql` | Not in day-one scope |

## Current State

As of 10 December 2025, the source states that RATAN-owned entitlement is enabled for SSDR and that Cashflow blotter uses mock entitlement. These are transition-status statements, not evidence of completed CES delivery or regulatory approval.

## Risks and Dependencies

- Final prohibitions depend on Country Compliance input.
- No CES decision, error, caching, or audit contract is documented.
- The retired RATAN-based fallback has no replacement contingency if CES readiness is delayed.
- Several interfaces have incomplete or unconfirmed scope.
- GraphQL aggregation and WebSocket reauthorization semantics remain unspecified.

## Completion Evidence Needed

Before treating this project as complete, confirm policy sign-off, authoritative identity attributes, interface-level enforcement behavior, negative and exception test coverage, audit evidence, rollout controls, and the treatment of deferred BCS blotter scope.
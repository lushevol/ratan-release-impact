---
type: query
title: Which Cash Settlement Interfaces Are in the CES Entitlement Scope?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, scope, cash-settlement, api, entitlement]
related: [ces-data-entitlement-integration, query-service, cash-settlement-data-entitlement, ssdr]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md"]
---
# Which Cash Settlement Interfaces Are in the CES Entitlement Scope?

The source provides a preliminary interface list but leaves material scope gaps.

## Confirmed or Stated Scope

- SSDR access through `v2/data/provider/query/cashflows` is to switch to CES.
- Cashflow blotter GraphQL access is to receive entitlement control.
- Cashflow notification WebSocket subscriptions are to receive entitlement control.
- Cashflow history GraphQL and Group blotter are listed, but no change is specified.

## Unresolved Scope

- Is `/v1/query/cashflows` part of the entitlement perimeter? The source marks it as unconfirmed.
- What concrete changes apply to Cashflow history and Group blotter?
- When will BCS blotter move beyond its explicitly deferred day-one scope?
- Are exports, batch interfaces, caches, downstream replicas, and administrative interfaces included?
- Does existing RATAN-owned entitlement for [[ssdr]] remain during or after CES migration?
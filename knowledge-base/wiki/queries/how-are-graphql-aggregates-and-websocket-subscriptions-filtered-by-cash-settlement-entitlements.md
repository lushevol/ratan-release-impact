---
type: query
title: How Are GraphQL Aggregates and WebSocket Subscriptions Filtered by Cash Settlement Entitlements?
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, websocket, entitlement, cash-settlement, information-leakage]
related: [cash-settlement-data-entitlement, query-service, ces-data-entitlement-integration, entitlement-based-notification-delivery, websocket-notification-delivery, graphql-cashflow-blotter-aggregate-queries]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md"]
---
# How Are GraphQL Aggregates and WebSocket Subscriptions Filtered by Cash Settlement Entitlements?

The source requires entitlement controls on Query Service GraphQL access and WebSocket notification subscriptions, but does not define the enforcement semantics.

## Questions to Resolve

- Are unauthorized records removed before GraphQL aggregation, grouping, counts, totals, pagination, and statistics are calculated?
- How are empty results distinguished from access denials without disclosing restricted data?
- Are exports, history results, cached responses, and error messages subject to the same policy?
- Is entitlement checked at WebSocket connection, subscription creation, event delivery, reconnection, or all of these points?
- What happens to an established subscription when a user's entitlement changes or is revoked?
- Are notification topic names, payload metadata, and delivery acknowledgements protected from information leakage?
- Which service evaluates CES policy for notifications: [[query-service]], [[notification-service]], or another component?

The source reports that Cashflow notification uses mock entitlement as of 10 December 2025; it does not define the guarantees provided by that implementation.
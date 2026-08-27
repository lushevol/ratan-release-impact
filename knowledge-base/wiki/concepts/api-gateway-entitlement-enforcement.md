---
type: concept
title: API-Gateway Entitlement Enforcement
created: 2026-08-24
updated: 2026-08-24
tags: [authorization, API gateway, function-entitlement, data-entitlement]
related: [api-gateway, auth-service, function-entitlement, data-entitlement, ems2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# API-Gateway Entitlement Enforcement

API-gateway entitlement enforcement is the per-request authorization step in which the gateway sends the Single-UI bearer token to [[auth-service]] and evaluates the resulting authorization context.

The documented flow explicitly covers function-entitlement checking. Data-entitlement information is also returned, but the source does not specify whether filtering is enforced at the gateway, BFF, GraphQL layer, or downstream RATAN services.

Per-request retrieval may improve entitlement freshness, but its latency, availability, caching, retry, and revocation implications are not defined.
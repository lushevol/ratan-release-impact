---
type: concept
title: Entitlement-Based Regional Routing
created: 2026-08-22
updated: 2026-08-22
tags: [entitlements, regional-routing, jwt, api-gateway, nginx]
related: [ces, ratan-id, indonesia-cash-settlement-onshoring, what-jwt-claims-and-ces-controls-authorize-indonesia-ratan-access]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Entitlement-Based Regional Routing

Entitlement-based regional routing selects the Ratan regional service endpoint using a user’s entitlement role and eligible legal-entity FMID rather than physical user location.

For the Indonesia design, CES determines Indonesia access. The UI may receive an Indonesia indicator through SSO/JWT, select Indonesia modules and API paths, and route calls to Ratan ID. The API Gateway must independently validate that the requested region matches the caller’s entitlement before forwarding a request.

A header-based routing alternative uses `X-Idns: true`, but client-controlled headers must not be trusted. Any externally supplied regional header requires sanitization and authorization enforcement before it influences routing. The source does not define JWT claims, token issuer responsibilities, multi-region user behavior, WebSocket authorization, audit evidence, or rejection semantics.
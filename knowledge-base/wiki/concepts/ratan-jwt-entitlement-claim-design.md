---
type: concept
title: Ratan JWT Entitlement Claim Design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, jwt, entitlement, authorization, token-size, routing]
related: [fmces, ratanone-api-gateway, fmces-based-ratan-entitlement-authorization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# Ratan JWT Entitlement Claim Design

The proposal considers embedding FMCES `entitlement_name` values in the `Single-UI-Entitlement` JWT for gateway routing, rather than embedding the full data-entitlement value list.

Limited entitlement-name claims reduce payload growth, but a production design still needs a claim schema, maximum token-size budget, TTL, cache rules, entitlement-change propagation, revocation behavior, and authorization rules for users with both, neither, or changed country entitlements. The source's `"8"` value-routing proposal is not defined sufficiently to implement safely.
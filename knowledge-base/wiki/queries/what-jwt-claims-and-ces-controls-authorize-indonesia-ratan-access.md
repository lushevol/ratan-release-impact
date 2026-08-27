---
type: query
title: What JWT Claims and CES Controls Authorize Indonesia Ratan Access?
created: 2026-08-22
updated: 2026-08-22
tags: [jwt, ces, authorization, indonesia, api-gateway]
related: [ces, entitlement-based-regional-routing, ratan-id, indonesia-cash-settlement-onshoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# What JWT Claims and CES Controls Authorize Indonesia Ratan Access?

The design assumes that a user’s Indonesia entitlement can be extracted from, or added to, a JWT. It also states that users can hold Indonesia and global entitlements concurrently and that region selection should use entitlement role and eligible legal-entity FMID.

The authorization design must define:

- The authoritative CES roles and legal-entity FMID mappings.
- JWT issuer, claim names, audience, expiry, and enrichment responsibility.
- How users with multiple region entitlements select or receive a region.
- API Gateway checks for requested-region and entitlement matching.
- UI and WebSocket routing enforcement.
- Rejection, logging, audit, token-refresh, and entitlement-change behavior.
- Controls preventing `X-Idns` or equivalent client-header spoofing.

No final access-control specification is present in the source.
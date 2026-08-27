---
type: query
title: Does One-Hour CES Entitlement Cache TTL Meet Access-Revocation Requirements?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, cache, redis, access-revocation, data-sovereignty]
related: [ces, auth-service, redis, cash-settlement-data-entitlement, ces-data-entitlement-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
---
# Does One-Hour CES Entitlement Cache TTL Meet Access-Revocation Requirements?

auth-service caches CES results in Redis for a default of 3,600 seconds. The design assumes that one hour of entitlement-data latency is tolerated and provides a maintenance cache-reset endpoint for early invalidation.

The source does not provide approval that this delay is acceptable for urgent access removal, user-role changes, or country and data-sovereignty policy changes.

## Questions

- What is the maximum acceptable delay for entitlement revocation and restriction changes?
- Which CES policy changes require immediate cache invalidation?
- Who can invoke individual and wildcard cache reset, and how is that action audited?
- Is CES able to notify RATAN of policy changes, or must RATAN rely solely on expiry and manual invalidation?
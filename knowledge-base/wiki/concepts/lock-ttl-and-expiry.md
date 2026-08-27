---
type: concept
title: Lock TTL and Expiry
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, TTL, reliability, deadlock-avoidance]
related: [watchdog-lock-renewal, ratan-distributed-lock-ownership, cross-service-lock-validation, redis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Lock TTL and Expiry

A lock TTL is the duration after which a lock expires automatically if it has not been released or renewed.

The source identifies two opposing failure modes:

- A short TTL can expire while processing is still active, allowing a competing request to acquire the resource.
- A long or unreleased TTL can block recovery when an owner fails to release the lock.

RATAN requires reasonable TTL values, exceptional-path auto-unlock, and watchdog renewal for processing that legitimately exceeds its initial lease. Expiry must also invalidate propagated client identities; a downstream service must not re-enter and revive an expired lock.

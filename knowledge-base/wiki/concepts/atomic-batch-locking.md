---
type: concept
title: Atomic Batch Locking
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, batch-processing, netting, atomicity]
related: [redisson, redisson-faster-multi-lock, resource-lock-manager, ratan-distributed-lock-ownership, lock-ttl-and-expiry]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Atomic Batch Locking

Atomic batch locking acquires locks for multiple resources as one logical operation: either all requested resources are locked or none remain locked.

This is required for netting, where a request may include 1,000 payments and BIC netting may exceed 5,000 component payments. Sequential acquisition can lock ten payments, fail on the eleventh, reject the netting request, and leave the first ten locks until TTL expiry.

A valid implementation must define:

- All-or-nothing acquisition.
- Rollback of successfully acquired keys after any failure.
- Mutual exclusion with single-resource locks.
- Behavior for duplicate keys and empty batches.
- Watchdog resource usage.
- Acquisition timeout and failure errors.

The source identifies `RedissonMultiLock` as potentially too slow at high volume and `RedissonFasterMultiLock` as a candidate requiring further compatibility work.

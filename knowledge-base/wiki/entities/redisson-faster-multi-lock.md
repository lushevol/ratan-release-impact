---
type: entity
title: RedissonFasterMultiLock
created: 2026-08-24
updated: 2026-08-24
tags: [Redisson, Redis, batch-locking, netting]
related: [redisson, atomic-batch-locking, ratan-distributed-lock-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# RedissonFasterMultiLock

`RedissonFasterMultiLock` is a proposed or candidate multi-resource lock implementation for high-volume RATAN netting.

## Claimed characteristics

| Property | Value |
|---|---:|
| Time complexity | O(1) |
| Network I/O | 2 |
| Lock failure cost | 1 |
| Watchdog thread count | 1 |
| Intended volume | >1000 resources |

The source contrasts it with `RedissonMultiLock`, whose acquisition is described as O(N), uses 2N network operations, and may create one watchdog thread per resource.

## Unresolved implementation requirement

The faster implementation uses a data structure that differs from the existing single-lock implementation. It must be enhanced to provide mutual exclusion with single locks before it can be treated as a safe production option. The source does not provide benchmark evidence or confirm implementation status.

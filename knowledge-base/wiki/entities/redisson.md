---
type: entity
title: Redisson
created: 2026-08-24
updated: 2026-08-24
tags: [Redisson, Redis, Java, distributed-locking]
related: [redis, redisson-faster-multi-lock, ratan-distributed-lock-ownership, cross-service-lock-validation, watchdog-lock-renewal, atomic-batch-locking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Redisson

Redisson is the Redis client and locking library evaluated for the RATAN distributed-lock redesign.

## Relevant capabilities

The source attributes the following capabilities to Redisson:

- Atomic lock and unlock operations implemented with Redis Lua scripts.
- Lock expiry and automatic watchdog renewal.
- Retry through subscription.
- Single-key and multi-key lock types.
- Fair, read/write, spin, and other lock variants.
- Lock notifications through listeners, events, and Redis Pub/Sub.

The watchdog is described as renewing a lock every 10 seconds until unlock or process/thread shutdown.

## RATAN limitation

Redisson's default re-entrance is thread-level within a JVM. RATAN workflows cross service and JVM boundaries, so Redisson requires a RATAN-specific protocol for propagated identity validation and ownership responsibility. Selecting Redisson does not, by itself, solve the current process-level ownership race.

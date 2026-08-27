---
type: entity
title: resourceLockManager
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, foundation-service, api, RATANONE]
related: [redisson-watchdog-lock-renewal, lock-propagation-depth-control, batch-distributed-locking, what-are-the-retry-time-watchdog-and-failure-semantics-of-resourcelockmanager, resource-lock, atomic-batch-locking, cross-service-lock-validation, ratan-distributed-lock-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Distribution lock test cases  && Uber orchestration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# resourceLockManager

`resourceLockManager` / `ResourceLockManager` is a lock-management API for executing domain-service commands under a single-resource lock or a multi-resource lock. The RATANONE Distributed Lock ReDesign source describes it as the high-level RATAN lock starter API.

## API

The RATANONE Distributed Lock ReDesign source specifies the following overloads:

| Method | Return | Parameters |
|---|---|---|
| `run` | `void` | `key(String)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `commandNoReturn(CommandNoReturn)` |
| `run` | `void` | `keys(List<String>)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `commandNoReturn(CommandNoReturn)` |
| `get` | `T` | `key(String)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `command(Command<T>)` |
| `get` | `T` | `keys(List<String>)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `command(Command<T>)` |

According to that source, `waitTimeSeconds` is the maximum time to wait for lock acquisition. It does not define exception types, invalid-lock behavior, partial-failure semantics, or lock-renewal and cancellation APIs.

## Lock-time semantics and renewal

The Distribution lock test cases && Uber orchestration source records a migration-sensitive semantic change: under the new Foundation Service lock implementation, the second argument to `get(...)` is retry time rather than locking time. Lock expiry is instead renewed by the [[redisson-watchdog-lock-renewal|Redisson watchdog]].

This source does not verify the exact API signature, retry unit, result type, timeout behavior, exception contract, or bulk-acquisition rollback semantics. See [[what-are-the-retry-time-watchdog-and-failure-semantics-of-resourcelockmanager]].

## Observed usage

The Distribution lock test cases && Uber orchestration source shows use with:

- A single cashflow ID.
- A batch list of keys.

These observed patterns correspond to the single-key and multi-key forms, but the source does not verify their bulk-acquisition rollback semantics.
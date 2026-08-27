---
type: source
title: RATANONE Distributed Lock Redesign
authors: []
year: 2025
url: ""
venue: "RATANONE Design Principle"
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, distributed-locking, Cash-Settlement, Redis, Redisson, concurrency]
related: [redis, redisson, ratan-distributed-lock-ownership, cross-service-lock-validation, watchdog-lock-renewal, atomic-batch-locking, lock-ttl-and-expiry, parent-client-timeout-consistency, synchronized-process-lock-scope, redis-redisson-vs-zookeeper-vs-relational-db-locking, which-ratan-distributed-lock-ownership-model-is-approved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# RATANONE Distributed Lock Redesign

## Summary

This design document describes the redesign of distributed locking for RATAN, a distributed microservice platform supporting Cash Settlement, Trade Control, and BCS settlement flows. The redesign addresses race conditions, unclear ownership, fixed lock TTL limitations, partial batch locking, and parent–client failures in asynchronous service interactions.

Locking evolved from no same-resource concurrency control in the 2020 RATAN TRF implementation, through high-concurrency BCS Cash Settlement processing in 2021, to a redesign initiated in 2025 after issues were identified across strategic Cash Settlement deployments.

## Concurrency problems

The source identifies three principal concurrent business cases:

1. Cashflow workflow STP processing.
2. Manual user actions for SI exception handling.
3. User netting and unnetting.

Observed or anticipated effects include:

- Payments released after netting had occurred.
- One maker's input overwriting another maker's input.
- Exception replay causing unnecessary reprocessing.
- Locks remaining until TTL expiry after an unsuccessful release.
- Partial batch locks blocking unrelated processing.

### Early-release race

A Lifecycle process locks a cashflow and publishes it to a workflow. Orchestration validates the propagated lock identity and later re-enters and extends the lock after Lifecycle has released it. Orchestration then cannot release the lock because ownership remains associated with Lifecycle. The lock remains active until TTL expiry, preventing Swift from releasing the payment.

### Group-message race

A Murex adaptor locks a trade and publishes payment and force-cancellation messages. Group Service processes both messages concurrently, and one operation can fail because of a PostgreSQL lock optimization conflict. Group Service cannot release the lock because ownership remains associated with the adaptor.

These cases show that passing a process identity between services does not by itself provide safe ownership transfer or release.

## Design principles

The proposed principles are:

- **Atomicity:** Lock and unlock operations should be atomic.
- **Clear responsibility:** The lock owner creates, extends, renews, retries, and releases the lock.
- **Client validation:** A re-entrant client validates the propagated lock identity but does not assume ownership or release responsibility.
- **Deadlock avoidance:** Reasonable TTLs and automatic unlock on exceptional paths should prevent indefinite lock retention.
- **Synchronized-process scope:** Lock only operations that cannot safely run concurrently. Stateless processing may remain parallel.

## Current lock summary

| Business flow | Lock creation | Initial TTL | Lock extension | Unlock |
|---|---|---:|---|---|
| Workflow | Orchestration | 360s | Lifecycle, Netting, NSTP, SSI | Orchestration |
| Swift Generation | Swift | 360s | Lifecycle | Swift |
| Auto Affirm | Orchestration | 10s | Lifecycle | Orchestration |
| Maker Submit | Lifecycle | 2s | None stated | Lifecycle |
| Checker Approve | Lifecycle | 2s | None stated | Lifecycle |
| Manual Fail | Lifecycle | 2s | None stated | Lifecycle |
| Manual Reinstate | Lifecycle | 2s | None stated | Lifecycle |
| Net/Unnet | Netting | 360s | Lifecycle | Netting |

The distribution of creation, extension, and release responsibilities is the central source of ownership ambiguity.

## Redisson direction

The source favors Redis with Redisson over relational database locks and Zookeeper/Curator. Redisson provides Lua-script-based atomic operations, lock expiry, watchdog renewal, retry through subscription, multiple lock types, and lock notifications.

Redisson's default re-entrance is thread-level within a JVM. RATAN's asynchronous workflows require a separate application-level validation and ownership protocol for cross-service interactions. The source presents two proposal variants:

1. Require client validation and enhance lock propagation to pass the process identity.
2. Do not perform client validation; processing without a valid lock is unsafe.

The document does not clearly identify which proposal is approved.

## Batch locking

Netting may require locking thousands of component payments. Sequential acquisition can leave already acquired locks in place when a later key cannot be acquired. For example, ten locks may succeed before the eleventh fails in a 1,000-payment netting request.

| Property | RedissonMultiLock | RedissonFasterMultiLock |
|---|---:|---:|
| Time complexity | O(N) | O(1) |
| Network I/O | 2N | 2 |
| Lock failure cost | 2S, where S is the number of successfully acquired locks | 1 |
| Watchdog thread count | N | 1 |
| Suitable volume | <100 | >1000 |

The source states that BIC netting may involve more than 5,000 component payments and that standard multi-lock acquisition can take more than 20 seconds. `RedissonFasterMultiLock` is a potential solution, but it requires compatibility with the existing single-lock data structure and mutual-exclusion semantics.

## API contracts

### `ResourceLockManager`

| Method | Return | Parameters |
|---|---|---|
| `run` | `void` | `key(String)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `commandNoReturn(CommandNoReturn)` |
| `run` | `void` | `keys(List<String>)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `commandNoReturn(CommandNoReturn)` |
| `get` | `T` | `key(String)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `command(Command<T>)` |
| `get` | `T` | `keys(List<String>)`, `waitTimeSeconds(long)`, `actionInProgress(String)`, `command(Command<T>)` |

`waitTimeSeconds` is the maximum time to wait for lock acquisition. The manager supports both single-key and multi-key operations and commands with or without return values.

### `ResourceLock`

| Method | Return | Parameters |
|---|---|---|
| `lock` | `void` | `key(String)`, `waitTimeSeconds(long)`, `actionInProgress(String)` |
| `lock` | `void` | `keys(List<String>)`, `waitTimeSeconds(long)`, `actionInProgress(String)` |
| `releaseLock` | `void` | `key(String)`, `actionInProgress(String)` |
| `releaseLock` | `void` | `keys(List<String>)`, `actionInProgress(String)` |

Manual users are required to release locks in a `finally` block:

```java
finally {
    resourceLock.release(key, "xxxxx has been released");
}
```

The API table names `releaseLock`, while the example uses `release`. The public method name must be clarified.

## Parent–client consistency risks

The document distinguishes one-to-one payment processing from one-to-many netting:

- In one-to-one processing, a parent crash or client timeout may result in a technical failure that can be retried through Reinstate.
- In one-to-many netting, a timeout or parent failure can leave Netting Service and Lifecycle Service out of sync.

Suggested mitigations include idempotent APIs, parent retries or result reconciliation, appropriate Feign timeout configuration, and Kafka rebalance configuration.

## Technical comparison

| Capability | Relational DB | Zookeeper / Curator | Redis / Redisson |
|---|---:|---:|---:|
| Re-entrant locking | No | Requires custom implementation | Yes, thread-level within JVM |
| Lock expiry | No | Session-close behavior | Yes |
| Lock extension | No | Session-close behavior | Yes |
| Lock watcher | No | Yes | Yes |
| Unfair lock | Yes | Yes | Yes |
| Fair lock | No | Yes | Yes |
| Multi-lock | No | Requires custom implementation | Yes |
| Community activity | N/A | Medium | High |

Zookeeper offers strong consistency and ordered ephemeral nodes, but the source identifies node-management overhead, implementation complexity, lack of native batch locking, and limited strategic value because the Zookeeper deployment supporting Kafka is expected to be decommissioned.

## Open questions

- Which proposal is approved?
- Is ownership transferred between services, or retained by one owner throughout a workflow?
- What is the authoritative lock identity?
- What happens when a downstream service receives an expired identity?
- Does `keys(List<String>)` guarantee all-or-nothing acquisition and rollback?
- Is `RedissonFasterMultiLock` implemented, prototyped, or only a candidate?
- How does watchdog renewal stop after process failure or network partition?
- What are the exact acquisition, validation, renewal, and release error semantics?
- Why do the API table and example use different release method names?
- What benchmark validates support for more than 5,000 netting payments?

## Related services

The design affects [[entities/ratan-cashflow-lifecycle-service]], [[entities/ratan-cash-settlement-netting-service]], [[entities/ratan-cash-settlement-orchestration]], [[entities/swift-service]], [[entities/murex]], and existing cashflow state-management concepts such as [[concepts/cashflow-group-and-message-state-machines]] and [[concepts/automatic-un-netting-error-handling]].

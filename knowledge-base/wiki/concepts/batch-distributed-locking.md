---
type: concept
title: Batch Distributed Locking
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, distributed-locking, redis, concurrency, batch-processing]
related: [lifecycle-batch-status-update-api, cashflow-release-and-netting-race-condition, cashflow-batch-transaction-atomicity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md"]
---
# Batch Distributed Locking

Batch distributed locking acquires coordination locks for a list of cashflow IDs rather than performing separate lock operations sequentially for each cashflow.

## Motivation

The source identifies Redis read and write operations during individual cashflow locking as a significant time cost. In the reported DEV test, locking approximately 2,300 cashflows after tuning took about 8.7 seconds, while the UAT1 comparison reported approximately 54.4 seconds between the first lock and the last release.

## Proposed approaches

Two approaches are described:

1. **Parallel lock acquisition:** Use `CompletableFuture` or `CyclicBarrier` to acquire individual locks concurrently. If one acquisition fails, all acquired locks should be released.
2. **Lua script acquisition:** Execute Redis key-setting operations in a Lua script so the list operation can be coordinated more efficiently and transactionally at the Redis-script level.

The source also notes that the current starter supports list locking through a `foreach` mechanism that could be optimized.

## Required semantics

A production-ready implementation should define:

- Lock ownership tokens.
- Atomicity of list acquisition.
- Behavior on partial acquisition.
- Release behavior when one acquisition fails.
- Expiration and renewal.
- Retry and timeout policy.
- Recovery after application or network failure.
- Interaction with database transaction rollback.

Atomicity within Redis does not prove atomicity of the complete cashflow update. The locking design must therefore be evaluated with [[cashflow-batch-transaction-atomicity]].
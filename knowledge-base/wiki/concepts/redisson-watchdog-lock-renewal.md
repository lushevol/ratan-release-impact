---
type: concept
title: Redisson Watchdog Lock Renewal
created: 2026-08-24
updated: 2026-08-24
tags: [redisson, distributed-locking, lease-renewal, reliability]
related: [resource-lock-manager, batch-distributed-locking, what-are-the-retry-time-watchdog-and-failure-semantics-of-resourcelockmanager]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Distribution lock test cases  && Uber orchestration.md"]
---
# Redisson Watchdog Lock Renewal

Redisson watchdog lock renewal extends a lock's expiry while its holder continues processing. In the documented new Foundation Service lock implementation, it replaces caller-specified locking duration: the second `resourceLockManager.get(...)` parameter is described as retry time.

A mocked 60-second bulk-lock test records repeated renewal messages before release. This supports the intended behaviour but does not establish watchdog timeout, renewal cadence, Redis failure handling, owner-death detection, or lock behaviour during partitions.

The migration changes operational behaviour for callers that previously interpreted the second argument as a lease duration. The complete contract is tracked in [[what-are-the-retry-time-watchdog-and-failure-semantics-of-resourcelockmanager]].
---
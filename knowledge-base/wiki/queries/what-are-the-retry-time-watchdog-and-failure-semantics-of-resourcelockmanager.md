---
type: query
title: What Are the Retry-Time, Watchdog, and Failure Semantics of resourceLockManager?
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, resource-lock-manager, redisson, api-contract]
related: [resource-lock-manager, redisson-watchdog-lock-renewal, lock-propagation-depth-control, batch-distributed-locking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Distribution lock test cases  && Uber orchestration.md"]
---
# What Are the Retry-Time, Watchdog, and Failure Semantics of resourceLockManager?

The documented new-lock migration changes the second `resourceLockManager.get(...)` parameter from locking time to retry time and delegates lock expiry extension to the Redisson watchdog. The source does not define the contract sufficiently for production adoption.

Required verification includes:

- The precise API signature, return type, and exception or timeout outcome.
- The unit and retry behaviour of values such as `30`.
- Watchdog lease timeout, renewal interval, and owner validation.
- Redis topology, availability assumptions, and partition behaviour.
- Behaviour after service crash, watchdog interruption, duplicate release, and cancellation.
- Whether bulk-key acquisition is atomic and how partial contention is rolled back.
- Whether the two-level propagation limit is configurable and how denial is surfaced.

Until resolved, migration should be treated as an API semantic change rather than a dependency-only upgrade.
---
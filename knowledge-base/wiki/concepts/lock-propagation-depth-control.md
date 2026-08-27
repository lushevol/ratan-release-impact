---
type: concept
title: Lock Propagation Depth Control
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, orchestration, nested-calls, reentrance]
related: [resource-lock-manager, batch-distributed-locking, redisson-watchdog-lock-renewal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Distribution lock test cases  && Uber orchestration.md"]
---
# Lock Propagation Depth Control

Lock propagation depth control constrains how far a distributed-lock context may be transferred through nested service calls.

A three-service test involving an adaptor, Lifecycle Service, and Batch Service records `Lock can not be locked exceed 2 level` on the third-level request. The source also records a lock-process-ID bypass for a downstream request, indicating that nested calls can avoid acquiring a duplicate lock.

The evidence does not state whether the two-level limit is configurable, whether rejection skips locking or fails the workflow, or which orchestration paths require deeper nesting. It should therefore be treated as an observed test behaviour rather than a complete policy specification.
---
---
type: concept
title: Cross-Service Lock Validation
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, microservices, validation, re-entrance]
related: [ratan-distributed-lock-ownership, redisson, lock-ttl-and-expiry, parent-client-timeout-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Cross-Service Lock Validation

Cross-service lock validation is the downstream check that a propagated lock identity is still valid before a service operates on a protected resource.

Redisson's native re-entrance is thread-level within one JVM, whereas RATAN workflows propagate lock identities across services and JVMs. The application must therefore define how a client validates the resource key, process identity, owner, lease, and current lock version.

An invalid or expired identity should cause the client to reject the operation rather than revive a stale lock. Validation alone does not define who may renew or release the lock; those responsibilities remain governed by [[ratan-distributed-lock-ownership]].

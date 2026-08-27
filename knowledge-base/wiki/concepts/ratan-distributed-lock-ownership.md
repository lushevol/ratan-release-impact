---
type: concept
title: RATAN Distributed Lock Ownership
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, distributed-locking, ownership, microservices]
related: [cross-service-lock-validation, watchdog-lock-renewal, lock-ttl-and-expiry, redis, redisson, resource-lock-manager, resource-lock]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# RATAN Distributed Lock Ownership

RATAN distributed lock ownership is the responsibility model for creating, extending, renewing, retrying, and releasing a lock around a synchronized business process.

## Proposed model

The redesign separates two roles:

- **Lock owner:** Creates the lock, controls renewal and extension while processing continues, retries when appropriate, and releases the lock.
- **Re-entrant client:** Validates the propagated lock identity and rejects processing when the identity is expired or invalid. It does not assume release responsibility.

This model addresses races in which Lifecycle, Orchestration, Group Service, Netting, or other downstream services re-enter a lock created by another service but cannot release it because the original owner remains recorded.

## Required identity contract

The source does not define whether the authoritative identity is a resource key, process ID, service, execution attempt, lock version, or composite. The redesign therefore requires an explicit identity and ownership-transfer contract before implementation.

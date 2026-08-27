---
type: concept
title: Payment Release Concurrency Control
created: 2026-08-22
updated: 2026-08-22
tags: [concurrency, payment-release, idempotency, lifecycle, RATAN]
related: [ratan, lifecycle-service, netting-service, last-mile-payment-release-control, auto-netting-rule-check, auto-netting-persistence-model, event-driven-component-cashflow-status-management, cashflow-netting-renetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# Payment Release Concurrency Control

## Definition

Payment-release concurrency control is the layered protection used to prevent conflicting user actions, system jobs, and integration events from producing invalid lifecycle transitions or duplicate outbound payments.

The source distinguishes serialization from semantic validation. A cache-based lock can ensure that only one process operates at a time, but the process must still recheck the current status and version after acquiring the lock.

## Control Layers

The documented design includes:

1. **Cache-based locking.** Locks block competing OPS actions and system processes on the same cashflow until the active operation completes.
2. **Current-state validation.** Lifecycle processing checks the current status, not only whether the requested action is generally permitted.
3. **Version-aware processing.** Workflow-level filtering is described using cashflow ID, business version, and minor version. The source separately reports that the status-movement API no longer validates minor version, so the end-to-end boundary remains unclear.
4. **Workflow publication gating.** Workflow should publish only cashflows currently in `READY + NA + NA`.
5. **SWIFT-service gating.** The SWIFT service should generate a message only for cashflows currently in `READY + NA + PendingAck`.
6. **Message deduplication.** Message Bridge uses tracking IDs, while SWIFT publication uses cashflow ID and business version checks.
7. **Completion marking.** The auto-release job marks processing as complete in the database to prevent another scan from processing the same item.
8. **Event-group controls.** Additional upstream cashflows, non-economic amendments, and post-release reversal/rebook events receive special treatment to avoid duplicate payment consequences.

## Failure Demonstrated by the Netting Incident

In the reported incident, `user1` completed netting and released the lock, after which `user2` acquired the lock and completed another netting operation. The source states that `N00000266337` then lost component cashflows from its netting ID.

The stated causes were that `NETTED` still allowed `Net` and that the status-movement API no longer validated minor version. This supports conditional status-and-version updates at commit time, in addition to locking.

## Limitations

The source does not confirm that synchronized release processing, minor-version validation, or the last-mile gate is implemented in production. It also contains unresolved process interactions marked `??`, “rare,” or “may break the manual action.”
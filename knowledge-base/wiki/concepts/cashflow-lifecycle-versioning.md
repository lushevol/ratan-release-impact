---
type: concept
title: Cashflow Lifecycle Versioning
tags: [cashflow, versioning, ratan, concurrency, event-processing]
related: [ratan-cashflow-lifecycle-state-machine, ratan-external-and-internal-lifecycle-requests, ratan, murex-2-11, stella, what-is-the-authoritative-ratan-lifecycle-transition-matrix]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# Cashflow Lifecycle Versioning

The documented RATAN lifecycle design uses three independent version dimensions to order trade-originated and RATAN-originated cashflow actions.

- **Business Version** increments when a trade action affects the cashflow, including trade booking, amendment, and cancellation.
- **Cashflow Version** increments when Business Version increments or when STELLA changes a cashflow status.
- **Minor Version** increments for every action, including STELLA/Murex events and RATAN STP or manual operations.

External requests update all three dimensions. Internal RATAN actions leave Business Version and Cashflow Version unchanged but increment Minor Version.

This model provides an intended basis for sequencing and audit history, but the source does not specify how RATAN resolves stale, duplicate, skipped, or concurrent version requests. It should therefore not be assumed to define complete optimistic-concurrency behavior. See [[ratan-external-and-internal-lifecycle-requests]] and [[ratan-cashflow-lifecycle-state-machine]].
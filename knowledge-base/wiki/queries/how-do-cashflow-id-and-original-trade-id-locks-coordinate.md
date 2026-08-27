---
type: query
title: How Do Cashflow Id and Original Trade Id Locks Coordinate?
tags: [cash-settlement, locking, original-trade-id, cashflow-id, concurrency]
related: [cashflow-locking-and-retry-policy, adaptor, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# How Do Cashflow Id and Original Trade Id Locks Coordinate?

The source uses `Cashflow Id` for UI operations, workflow processing, SWIFT updates, and Accounting updates, while an Adaptor retry flow uses `Original Trade Id`.

It is unknown how these lock scopes compose when one original trade maps to multiple cashflows or when cashflows are split, grouped, netted, or unnetted.

## Evidence Needed

- Lock hierarchy and acquisition ordering across services.
- Trade-to-cashflow cardinality and lifecycle rules.
- Behavior for concurrent trade-level and cashflow-level processing.
- Deadlock, starvation, and duplicate-processing test results.
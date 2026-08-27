---
type: concept
title: Concurrency-Safe ID Allocation
created: 2026-08-22
updated: 2026-08-22
tags: [concurrency, identifiers, sequencing, cash-settlement, netting]
related: [ratan, ratan-cashflow-id-management, ratan-cash-settlement-netting, how-is-ratan-cashflow-id-uniqueness-enforced]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md"]
---
# Concurrency-Safe ID Allocation

Concurrency-safe ID allocation ensures that simultaneous requests cannot receive the same identifier.

For [[ratan]], this is required because netting and split cashflow IDs must be unique across services and processes. A sequential format alone does not provide that guarantee if independent processes can read and increment the same value concurrently.

The source requires concurrency handling but does not select an implementation mechanism. Any implementation must establish durable, atomic allocation at the stated cross-service/process scope and define behavior for retries, restarts, allocation failures, and numeric-sequence exhaustion.
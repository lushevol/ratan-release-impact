---
type: concept
title: Synchronized Process Lock Scope
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, concurrency, process-design]
related: [ratan-distributed-lock-ownership, atomic-batch-locking, cashflow-group-and-message-state-machines]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Synchronized Process Lock Scope

A synchronized process is a process in which concurrent execution against the same resource is not permitted. The RATAN redesign limits locking to these processes rather than applying locks indiscriminately.

Cashflow workflow processing, user SI exception actions, netting, unnetting, payment processing, and trade handling may require synchronization where they write shared state. Stateless processing can remain parallel because it does not create the same resource-write conflict.

The scope decision should be explicit for each workflow, including the protected resource, lock owner, downstream validation behavior, and release condition.

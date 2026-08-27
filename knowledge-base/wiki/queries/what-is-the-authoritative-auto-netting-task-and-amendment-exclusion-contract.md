---
type: query
title: What Is the Authoritative Auto-Netting Task and Amendment Exclusion Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, auto-netting, cashflow, database, idempotency, open-question]
related: [netting-service, t-auto-netting-task, auto-netting, amendment-cashflow-exclusion-from-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Auto Netting design.md"]
---
# What Is the Authoritative Auto-Netting Task and Amendment Exclusion Contract?

The available design specifies only this order: collect tasks, exclude amendment cashflows, then execute auto-netting.

The authoritative design must clarify:

- What service or process creates records in [[t-auto-netting-task]]?
- What is the complete table DDL, including ownership, keys, relationships, indexes, constraints, and retention rules?
- What makes a cashflow an amendment cashflow?
- Does removal mean deletion, state transition, cancellation, exclusion from a processing batch, or rerouting?
- What happens to excluded tasks and cashflows afterward, including audit and operational visibility?
- What selection, batching, ordering, locking, and scheduling rules govern task collection?
- What netting algorithm, persistence model, atomicity, idempotency, concurrency, failure handling, retry policy, and recovery procedure govern execution?

Resolution should distinguish this [[auto-netting]] workflow from unrelated netting APIs or cashflow-processing flows unless explicit evidence establishes an integration.
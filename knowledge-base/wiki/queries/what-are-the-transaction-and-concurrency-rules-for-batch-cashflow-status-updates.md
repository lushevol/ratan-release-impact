---
type: query
title: What Are the Transaction and Concurrency Rules for Batch Cashflow Status Updates?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, jdbc-template, transaction, batch-update, concurrency, netting]
related: [cashflow-lifecycle-state-machine-restructuring, what-is-the-authoritative-cashflow-lifecycle-state-transition-and-persistence-contract, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--13iana4]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# What Are the Transaction and Concurrency Rules for Batch Cashflow Status Updates?

The source proposes `JdbcTemplate` batch updates of status and netting ID for Netting, UnNetting, and component-status updates, while “Net New” performs inserts only. It labels these as transactional cases without specifying their transaction model.

## Questions to resolve

- Are the batch operations enclosed in a single database transaction, and at which service boundary?
- Which isolation level and optimistic-lock or version checks protect competing updates?
- What happens if one row fails during a batch operation?
- How are duplicate commands and replayed events made idempotent?
- Which audit fields, reconciliation jobs, and rollback procedures are required?
- How does parallel `process` execution coordinate with persistence in `postprocess`?
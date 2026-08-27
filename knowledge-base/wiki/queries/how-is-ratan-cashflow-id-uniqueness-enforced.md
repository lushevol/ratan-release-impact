---
type: query
title: How Is Ratan Cashflow ID Uniqueness Enforced?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, cashflow-id, concurrency, netting, split]
related: [ratan, ratan-cashflow-id-management, concurrency-safe-id-allocation, ratan-cash-settlement-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md"]
---
# How Is Ratan Cashflow ID Uniqueness Enforced?

The requirement mandates unique cashflow IDs across Ratan services and processes and notes concurrent requests, but it does not define the allocation architecture.

## Questions to resolve

- Which component owns allocation of `N` and `S` sequence values?
- Is allocation atomic and durable across all Ratan processes and services?
- Do netting and split IDs use independent sequences or a shared numeric sequence?
- What happens after allocator restart, transaction rollback, duplicate-key detection, or request retry?
- What is the behavior when the 11-digit numeric range is exhausted?
- Are invalid or missing `CashflowId_Type` values rejected rather than silently classified as Split?

Until these points are confirmed, the source establishes a required uniqueness outcome rather than an approved technical design.
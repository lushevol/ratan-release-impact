---
type: query
title: Which Cashflow Domain Events Trigger NSTP Exception Refresh?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, domain-events, nstp, event-processing, query-service]
related: [nstp-exception-filter, cashflow-exception-read-model-enrichment, exception-platform-service, query-service, cashflow-status-write-back]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Which Cashflow Domain Events Trigger NSTP Exception Refresh?

The design identifies Create, Amend, and Status Update events on `cash_settlement_cashflow_domain_events` as potential triggers, but does not define an authoritative trigger policy.

## Evidence

The source includes a `CashflowStatusUpdateEvent` for a cashflow in `WAITING` status with `Pending Verification` and `Pending Exception` sub-status values. This shows that a status update contains a `cashflowId` and relevant state, but does not prove that every status update requires an exception-platform lookup.

## Questions to resolve

- Which event types require exception refresh?
- Are lookups limited to transitions into or out of exception-related states?
- Can event payload state determine whether a lookup is necessary?
- How are duplicate, replayed, late, and out-of-order events handled?
- What retry and reconciliation policy applies when the exception platform is unavailable?
- Does enrichment block event processing or occur asynchronously?

The outcome should define load expectations for [[exception-platform-service]] and correctness controls for [[cashflow-exception-read-model-enrichment]].
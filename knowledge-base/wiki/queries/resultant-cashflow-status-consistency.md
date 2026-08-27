---
type: query
title: How Are Resultant Cashflow Creation and Status Updates Made Consistent?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, netting, transactions, consistency, domain-events]
related: [netting-resultant-cashflow, lifecycle-netting-responsibility-separation, event-driven-component-cashflow-status-management, cashflow-netting-renetting, netting-service, lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# How Are Resultant Cashflow Creation and Status Updates Made Consistent?

The source identifies that the current update-status API both updates cashflow statuses and generates resultant cashflows. The proposed refactor separates these responsibilities but does not define their consistency boundary.

## Questions to Resolve

- Must resultant-cashflow creation happen before or after component-cashflow status updates?
- Which operations must be atomic: net-request persistence, resultant creation, component updates, and SCBML publication?
- How are partial failures detected and recovered?
- What idempotency controls prevent duplicate resultant cashflows during retries or `renet` processing?
- How are component updates reconciled when `released` or `settled` domain-event processing fails?
- Does publication to `Cash_Settlement_Orchestration_Process_In` use an outbox or equivalent reliable-delivery mechanism?

## Why It Matters

Without an explicit consistency and recovery model, moving responsibilities from a single large transaction to multiple services or event consumers can exchange synchronous performance problems for incomplete processing, duplicate messages, or incorrect component-cashflow states.
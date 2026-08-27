---
type: query
title: What Are the Scheduled Netting Scan Idempotency and Locking Rules?
tags: [cashflow, netting, cron, idempotency, concurrency, locking]
related: [nds-cashflow-processing, netting-service, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--30-nds-cashflow-processing-design--yw8sda]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Are the Scheduled Netting Scan Idempotency and Locking Rules?

The design adds a cron job to `ratan-cash-settlement-netting-service` to scan cashflow candidates and perform netting. It provides no operational contract for the scheduled path.

## Questions to Resolve

- What is the cron frequency and execution-time expectation?
- Which cashflows are eligible candidates, and what state transition reserves them for processing?
- Can concurrent scheduled or event-driven workers process the same cashflow?
- What locks, optimistic-concurrency checks, or deduplication keys prevent duplicate netting?
- What retry, dead-letter, reconciliation, and observability behavior applies after a failed scan or netting attempt?
- Are scanning and netting performed within one transaction or separate stages?
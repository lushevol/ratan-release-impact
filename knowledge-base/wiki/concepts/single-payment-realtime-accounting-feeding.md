---
type: concept
title: Single-Payment Realtime Accounting Feeding
created: 2026-08-23
updated: 2026-08-23
tags: [realtime, accounting, payment, feeding, cash-settlement]
related: [ebbs, bcdf, entity-based-eod-feeding, cashflow-accounting-eligibility, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Single-Payment Realtime Accounting Feeding

## Definition

Single-payment realtime accounting feeding is an approach in which an accounting feed is transmitted for each payment as it occurs rather than only through an end-of-day batch.

The source lists this as one of the two EBBS feeding approaches.

## Status

The source does not determine whether realtime feeding is:

- An alternative to entity-based EOD feeding.
- A complementary path.
- Restricted to specific payment types.
- A fallback or exception process.

No latency target, delivery protocol, idempotency rule, acknowledgement behavior, or replay process is defined.

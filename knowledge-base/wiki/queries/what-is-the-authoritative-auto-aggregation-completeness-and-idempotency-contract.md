---
type: query
title: What Is the Authoritative Auto-Aggregation Completeness and Idempotency Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [aggregation, idempotency, cashflow, netting, concurrency]
related: [product-agnostic-cashflow-aggregation, normalized-payment-schedule-completeness-check, netting-service, cashflow, uber-inbound-message-idempotency-and-error-state, what-causes-duplicate-cashflow-ids-and-major-versions-in-uber-trades]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# What Is the Authoritative Auto-Aggregation Completeness and Idempotency Contract?

The draft proposes aggregation when the schedule-derived expected count is not greater than the received eligible-cashflow count. It does not define a complete correctness or recovery contract.

## Questions to Resolve

- Is `tradeId`, currency, and payment date a sufficient aggregation key?
- Are individual schedule legs and cashflows correlated by stable identifiers rather than count alone?
- Must aggregation require `cf_count == expected_num`, and what happens when `cf_count > expected_num`?
- How are duplicate, replayed, amended, cancelled, or out-of-order cashflows handled?
- What locking, transaction, or idempotency mechanism prevents concurrent arrivals from triggering premature or duplicate aggregation?
- What exact status represents “pending another leg,” which service owns it, and what event releases it?
- How are incomplete or mismatched groups reconciled operationally?

This question should be resolved before the draft algorithm is implemented as an automatic settlement decision.
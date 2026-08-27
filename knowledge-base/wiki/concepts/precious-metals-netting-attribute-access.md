---
type: concept
title: Precious-Metals Netting Attribute Access
created: 2026-08-24
updated: 2026-08-24
tags: [netting, uber, precious-metals, lifecycle, data-access]
related: [netting-service, product-agnostic-cashflow-aggregation, schema-evolution-for-cash-settlement, should-netting-read-precious-metals-attributes-from-raw-uber-messages-or-lifecycle-storage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# Precious-Metals Netting Attribute Access

Precious-metals netting requires [[netting-service]] to access `Custodian_SCI_FMID`, `Delivery_Location`, and `Settlement_Method` while generating resultant cashflows.

The source offers two unselected implementation approaches.

## Raw-message deserialization

The trade layer deserializes each raw UBER message to recover the fields. The source estimates raw payload volume at approximately 150 MB for 10,000 cashflows with 15 KB messages.

This estimate does not account for object allocation, heap overhead, concurrency, garbage collection, throughput, latency, failure recovery, or caching.

## Lifecycle persistence

Lifecycle Service persists the fields and supports retrieval by `cashflowIds`. This avoids repeated raw-message parsing but introduces schema ownership, persistence, historical backfill, indexing, API, consistency, and idempotency obligations.

Neither approach is approved by the source. The architectural decision remains open in [[should-netting-read-precious-metals-attributes-from-raw-uber-messages-or-lifecycle-storage]].
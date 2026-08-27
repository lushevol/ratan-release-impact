---
type: query
title: Should Netting Read Precious-Metals Attributes from Raw UBER Messages or Lifecycle Storage?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, uber, precious-metals, lifecycle, architecture]
related: [netting-service, precious-metals-netting-attribute-access, schema-evolution-for-cash-settlement, product-agnostic-cashflow-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# Should Netting Read Precious-Metals Attributes from Raw UBER Messages or Lifecycle Storage?

[[netting-service]] must obtain `Custodian_SCI_FMID`, `Delivery_Location`, and `Settlement_Method` for precious-metals resultant generation. The source presents raw-message deserialization and lifecycle-storage retrieval as alternatives but does not select one.

## Decision evidence needed

- Peak and concurrent cashflow volumes for netting runs.
- Heap, garbage-collection, CPU, and latency measurements for raw-message deserialization.
- Lifecycle storage capacity, index, API, and query-latency estimates.
- Lifecycle schema ownership and migration approach.
- Historical backfill requirements for existing UBER cashflows.
- Consistency expectations when source messages or stamped fields change.
- Idempotency and recovery behavior for either implementation.
- A clear acceptance threshold for memory, latency, operational risk, and delivery effort.

The cited 150 MB figure is a raw-payload estimate for 10,000 messages at 15 KB each; it is not sufficient evidence to reject deserialization.
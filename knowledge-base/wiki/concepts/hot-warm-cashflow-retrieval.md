---
type: concept
title: Hot-Warm Cashflow Retrieval
tags: [cashflow, retrieval, hot-data, warm-data, value-date]
related: [cash-settlement-home-page, cashflow-data-retention-lifecycle, ratan-cashflow-dashboard, dashboard-quick-search-filtering]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Archival & Retrieval.md"]
---
# Hot-Warm Cashflow Retrieval

Hot-warm retrieval is the proposed separation of cashflow searches by value date:

- `value date >= current - 6 months`: query hot data through the Current Cashflow Blotter.
- `value date < current - 6 months`: query warm data through a proposed new tile with a value-date-range condition.

This is an unresolved design proposal, not an approved user-interface or service contract.

## Design Questions

The implementation must clarify:

- Whether users receive two tiles or one federated search.
- Whether the six-month boundary is inclusive and timezone-aware.
- Whether cold data can be searched.
- Whether filtering, sorting, permissions, pagination, and export are consistent across tiers.
- How records are deduplicated when they remain in production after becoming logically historical.
- How late reprocessing, corrections, reversals, and cancellations are represented across stores.
- What SLA, timeout, result-volume, and concurrency limits apply.

The six-month value-date boundary must be kept distinct from the proposed physical movement rule of 15 months after trade expiry. The current [[ratan-cashflow-dashboard]] and [[dashboard-quick-search-filtering]] documentation may provide related operational search context, but this source does not establish that their behavior applies to archival retrieval.

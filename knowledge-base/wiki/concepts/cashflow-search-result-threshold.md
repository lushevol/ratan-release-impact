---
type: concept
title: Cashflow Search Result Threshold
tags: [cashflow, search, performance, pagination, sla]
related: [hot-warm-cashflow-retrieval, dashboard-quick-search-filtering, ratan-cashflow-dashboard]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Archival & Retrieval.md"]
---
# Cashflow Search Result Threshold

The source proposes removing the existing 30-day search limitation and replacing it with a limit based on result volume. It does not specify the supported date range, threshold, response-time target, or behavior when the threshold is exceeded.

A result-based control could protect the [[cash-settlement-home-page]] from expensive broad searches while allowing users to search more than 30 days when the matching population is small.

## Requirements to Define

The search contract should specify:

- Maximum date range before execution.
- Maximum result count and whether it is estimated or exact.
- Pagination and continuation behavior.
- Whether results are sorted consistently across hot and warm stores.
- Export limits and asynchronous export behavior.
- Query timeout, cancellation, and retry behavior.
- User-facing threshold messages.
- Authorization and data-volume controls.
- Monitoring metrics and SLA targets.

Removing the 30-day limit without measurable performance controls would create a scalability risk. Any threshold must also account for searches spanning multiple retrieval tiers and avoid duplicate records at the hot-warm boundary.

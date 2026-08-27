---
type: concept
title: Payment-Date Scoping for Cashflow Blotter
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, payment-date, query-selectivity, cashflow-blotter, performance]
related: [value-date-bounded-cashflow-queries, cashflow-blotter-default-query, cashflow-blotter-query-performance, cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow Blotter default query solution.md"]
---
# Payment-Date Scoping for Cashflow Blotter

Payment-date scoping limits Cashflow Blotter queries to a bounded `Payment_Date` interval extracted from the `cashflow` JSON document. In the reported tests, this was the strongest demonstrated mitigation for the broad active-state query.

For the default `NOT IN (DEAD, NETTED)` query, a one-month range returned 46,146 matching rows and took 10.11 seconds. Reducing the range to approximately half a month returned 19,944 matching rows and took 1.96 seconds. The same restriction improved `WAITING` from 1.70 to 1.05 seconds, while `READY` remained approximately 0.35 seconds because its result set was already very small.

The improvement is explained by a smaller candidate population, but the source does not establish whether a Payment_Date expression index was used. It also does not establish the optimal default range, usability impact, or production p95 and p99 behavior.

Terminal-state searches may use a different policy. A query for `NETTED`, `DEAD`, `CANCELLED`, and `SETTLED` over a seven-day period returned 1,070 rows in 1.17 seconds.

Payment-date bounds therefore support the policy under investigation in [[queries/what-is-the-approved-cashflow-blotter-value-date-search-policy]], but they should be combined with execution-plan analysis and historical-search requirements before adoption.
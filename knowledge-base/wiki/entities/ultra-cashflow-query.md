---
type: entity
title: Ultra Cashflow Query
tags: [cash-settlement, cashflow-blotter, query, performance]
related: [cashflow-blotter, legacy-cashflow-query, cashflow-blotter-query-performance]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Page Size Performance.md"]
---
# Ultra Cashflow Query

Ultra Cashflow Query is the newer Cashflow Blotter query implementation compared with [[legacy-cashflow-query|Legacy]] in the source's 2025-04-12 Staging performance test.

Under the documented workload, Ultra was faster in many query rows, including default WAITING, INDIA, and several VD-bounded status searches. It was slower in some individual readings. The source-reported conclusion of no material regression is limited to that test configuration and does not establish production equivalence.

The source does not describe Ultra's architecture, release contents, SQL implementation, page size, or acceptance criteria.
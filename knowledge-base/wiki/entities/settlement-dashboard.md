---
type: entity
title: Settlement Dashboard
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, dashboard, user-interface, performance]
related: [settlement-dashboard-performance, cash-settlement-performance-and-stress-testing, cashflow-blotter, grouping-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Settlement Dashboard Performance.md"]
---
# Settlement Dashboard

The Settlement Dashboard is a Cash Settlement user-interface surface that presents the full dashboard query experience.

A reported performance test exercised full dashboard queries at **10 QPS** with **50 users** for **one hour**. The maximum observed response time was **712 ms**, below the stated **5-second NFR baseline**. This evidence is documented in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--32-s--zm3bnd]].

The result is specific to the full dashboard query workload described in that test. It does not by itself characterize [[cashflow-blotter]] queries, [[grouping-blotter]], client-side rendering, downstream dependencies, or production-scale behavior.
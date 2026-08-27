---
type: query
title: Does Settlement Dashboard Performance Meet the Production SLA at Expected Peak Load?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, settlement-dashboard, production-readiness, performance-SLA, open-question]
related: [settlement-dashboard, settlement-dashboard-performance, cash-settlement-performance-and-stress-testing, cashflow-blotter-query-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Settlement Dashboard Performance.md"]
---
# Does Settlement Dashboard Performance Meet the Production SLA at Expected Peak Load?

## Known evidence

A performance test reported that full Settlement Dashboard queries ran at **10 QPS** with **50 users** for **one hour**. The maximum observed response time was **712 ms**, against a stated **5-second NFR baseline**, and the source marked the requirement as **MET**.

This supports a scenario-specific pass result, but not yet a complete production-SLA conclusion.

## Questions to resolve

1. What exact metric does the 5-second NFR represent: backend response time, end-to-end page rendering, a percentile threshold, or every dashboard request?
2. What were the p50, p95, and p99 response times?
3. Were any requests failed, timed out, or retried?
4. What data volumes, query mix, infrastructure, and dependency versions were used?
5. Is the expected peak production load greater than 10 QPS or 50 concurrent users?
6. Does the test include client-side rendering and all downstream dependencies?
7. Is the reported QPS aggregate across users and dashboard endpoints, or measured at another scope?

## Evidence boundary

Until these questions are answered, the result should be described as a successful sustained-load test for the reported full-dashboard scenario, rather than proof of production scalability or availability. It should not be used to infer the performance of [[cashflow-blotter-query-performance]] or other Cash Settlement components.
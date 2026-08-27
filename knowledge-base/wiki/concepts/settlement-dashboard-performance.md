---
type: concept
title: Settlement Dashboard Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, dashboard-performance, performance-testing, sustained-load-testing, NFR]
related: [settlement-dashboard, cash-settlement-performance-and-stress-testing, does-settlement-dashboard-performance-meet-production-sla-at-expected-peak-load]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Settlement Dashboard Performance.md"]
---
# Settlement Dashboard Performance

Settlement Dashboard performance testing measures the responsiveness of full dashboard queries under concurrent, sustained usage.

## Reported test

The reported scenario used:

- **10 QPS**
- **50 concurrent users**
- **One hour** of sustained load
- **712 ms maximum response time**
- **5-second NFR baseline**

The source records this as a successful test: the maximum observed response time was below the stated threshold.

## Interpretation

The result provides evidence that the full Settlement Dashboard query workload met the stated response-time threshold in the reported test environment. A 712 ms maximum is approximately 7 times faster than the 5-second limit.

The evidence is insufficient to assess complete production readiness. The source does not report p50, p95, or p99 latency; failures, timeouts, or retries; infrastructure utilization; dataset size; query mix; warm-up behavior; or whether the QPS figure is aggregate, per user, per endpoint, or per subquery. The meaning of the 5-second NFR is also not formally specified.

This concept must remain scoped to the tested dashboard workload and must not be conflated with [[cashflow-blotter-query-performance]], lifecycle-job performance, netting performance, or other Cash Settlement performance results.
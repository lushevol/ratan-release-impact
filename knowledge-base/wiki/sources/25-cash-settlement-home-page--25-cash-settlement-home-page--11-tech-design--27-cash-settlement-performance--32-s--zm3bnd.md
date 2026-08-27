---
type: source
title: Settlement Dashboard Performance
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, settlement-dashboard, performance-testing, NFR]
related: [settlement-dashboard, settlement-dashboard-performance, cash-settlement-performance-and-stress-testing, does-settlement-dashboard-performance-meet-production-sla-at-expected-peak-load]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Settlement Dashboard Performance.md"]
---
# Settlement Dashboard Performance

## Summary

This document reports a performance test of full Cash Settlement dashboard queries. The test ran at an aggregate rate of **10 queries per second (QPS)** with **50 users** for **one hour**.

The maximum response time observed across all queries was **712 ms**, compared with a stated NFR baseline of **5 seconds**. The source concludes that Settlement Dashboard performance **MET** the stated requirement.

## Reported test results

| Test parameter | Reported value |
|---|---:|
| Dashboard query rate | 10 QPS |
| Concurrent users | 50 |
| Test duration | 1 hour |
| Maximum response time | 712 ms |
| NFR baseline | 5 s |
| Conclusion | MET |

The reported maximum was 4.288 seconds below the threshold and approximately 14.2% of the 5-second baseline.

## Evidence and limitations

The source identifies the following attachment as PT result evidence:

![PT result evidence](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--32-s--zm3bnd/image-2025-2-24_18-52-13.png)

The result supports a narrow pass/fail conclusion for the reported workload. It does not establish percentile latency, error or timeout rates, resource utilization, warm-up behavior, data volume, test-environment comparability, or performance above 10 QPS and 50 users. The document also does not define whether the 5-second NFR applies to backend query response, end-to-end page rendering, a particular percentile, or every request.

This result applies to full Settlement Dashboard queries only. It should not be generalized to Cashflow Blotter, Grouping Blotter, lifecycle jobs, netting, orchestration, or other Cash Settlement services without matching evidence. See [[does-settlement-dashboard-performance-meet-production-sla-at-expected-peak-load]] for the unresolved production-readiness questions.

## Source context

> Full dashboard queries triggered per second (QPS: 10) with 50 users for one hour, the overall performance met requirements from NFR. Maximum response time of all queries is 712ms, far less than the baseline 5s. so the conclusion is, dashboard performance **MET** the requirements.
>
> PT result evidence
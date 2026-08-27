---
type: source
title: Batch Job Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, performance, batch-jobs, ratan, uk]
related: [ratan, cash-settlement-batch-job-performance, paginated-cashflow-batch-processing, long-running-batch-job-api-execution, is-six-gb-jvm-heap-sufficient-for-ratan-auto-materialize-at-uk-volume, should-ratan-long-running-batch-jobs-use-asynchronous-execution, does-the-ebbs-accounting-job-meet-uk-volume-performance-requirements, why-does-auto-release-group-lock-filtering-dominate-runtime]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
authors: []
year: 2024
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5856273"
venue: ""
---
# Batch Job Performance

This document records Dev-environment performance tests for Cash Settlement batch jobs under Story 5856273, **[Extra] Jobs optimization**. Its definition of done is operation at an assumed UK daily volume of 40,000 cashflows for materialization, auto fail, auto release for SWIFT generation, and accounting feeds for EBBS.

The reported evidence does not qualify all four jobs. In particular, no accounting-job result is included.

## Reported conclusions and qualifications

The source recommends using Auto Materialize V2 rather than V1 in production, increasing JVM settings to:

```text
-Xms3072m -Xmx6144m -XX:MaxMetaspaceSize=3072m
```

and deciding whether to extend the API gateway circuit-breaker timeout from 65 seconds to 30 minutes or use asynchronous job execution.

At 50k, Auto Materialize V2 completed in 406.13 seconds compared with 790 seconds for V1. At 100k, V1 produced no result at a 2 GB maximum heap; V2 failed on page 48 of 50 with `java.lang.OutOfMemoryError: Java heap space` at 1.99 GB (99.7%). The proposed 6 GB heap configuration was not tested for Auto Materialize in this source.

The Auto Release V1 section is marked TBD and repeats the Auto Materialize V1 values. It is not reliable Auto Release V1 evidence unless corrected.

## Auto Materialize: 50k, V1

| Field | Value |
| --- | --- |
| Job Name | Auto Materialize |
| Data Volume | 50k |
| Environment | Dev |
| Job URL | `/v1/ratan/cashflow/auto/materialization` |
| JVM options | `-Xms1024m -Xmx2048m -XX:MaxMetaspaceSize=1024m` |
| Page size | NA |
| Page amount | NA |
| Time cost for data process | 0.1635592s |
| Total Time cost | 790s |
| Max Memory Usage | 1.75G(87.3%) |
| Success rate | 5534 not materialized due to mocked data is invalid |

![Auto Materialize V1 50k](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--21--1yk3s57/image2024-10-20_12-32-53.png)

## Auto Materialize: 50k, V2

| Field | Value |
| --- | --- |
| Job Name | Auto Materialize |
| Data Volume | 50k |
| Environment | Dev |
| Job URL | `/v2/ratan/cashflow/auto/materialization` |
| JVM options | `-Xms1024m -Xmx2048m -XX:MaxMetaspaceSize=1024m` |
| Page size | 2k |
| Page amount | 25 |
| Time cost for data loading(by condition) | 0.1635592s |
| Time cost for each page(query by ID + run lifecycle) | p1: 21.47(21.39s), p2: 15.85(15.81s), P3: 18.67(18.63s), P4: 15.96(15.93s), P5: 17.73(17.69s) P6: 14.65(14.61s), P7: 16.68(16.64s), P8: 15.23(15.2s), P9: 15.5(15.46s), P10: 16.03(16s) P11: 16.17(16.14s), P12: 15.62(15.57s), P13: 17.19(17.16s), P14: 17.59(17.54), P15: 16.26(16.22s) P16: 14.9(14.87s), P17: 13.17(13.13s), P18: 15.07(15.03s), P19: 15.5(15.45s), P20: 15.16(15.12s) P21: 16.58(16.55s), P22: 18.31(18.27s), P23: 16.53(16.49s), P24: 15.09(15.05s), P25: 15.04(15s) |
| Total Time cost | 406.13s |
| Max Memory Usage | 1.74G(87%) |
| Success rate | 5614 not materialized due to mocked data is invalid |

![Auto Materialize V2 50k](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--21--1yk3s57/image2024-10-20_11-22-53.png)

## Auto Materialize: 100k

| Version | Page size | Page amount | Loading time | Per-page time | Total time | Maximum memory | Success rate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 | NA | NA |  |  | No result | 2G(100%) | NA |
| V2 | 2k | 50 | 0.32s | each page average time cost : 21s | 17 m 31.26 s(1051.26) | 1.99G(99.7%) - Handler dispatch failed: `java.lang.OutOfMemoryError: Java heap space` on page 48 | 20450 not materialized due to mocked data is invalid |

Both versions used:

```text
Job Name: Auto Materialize
Data Volume: 100k
Environment: Dev
V1 Job URL: /v1/ratan/cashflow/auto/materialization
V2 Job URL: /v2/ratan/cashflow/auto/materialization
JVM options: -Xms1024m -Xmx2048m -XX:MaxMetaspaceSize=1024m
```

## Auto Fail: 50k, V1

| Field | Value |
| --- | --- |
| Job Name | Auto Fail |
| Data Volume | 50k |
| Environment | Dev |
| Job URL | `/v1/cashflow/jobs/cashflows/autoFail` |
| JVM options | `-Xms3072m -Xmx6144m -XX:MaxMetaspaceSize=3072m` |
| Page size | NA |
| Page amount | NA |
| Time cost for data process | 3m13s |
| Total Time cost | 4m53.76 s |
| Max Memory Usage | 1.84G(31% of 6G) |

## Auto Release: 50k, V2

| Field | Value |
| --- | --- |
| Job Name | Auto Release |
| Data Volume | 50k(427resultant + 49573 gross) |
| Environment | Dev |
| Job URL | `/v2/cashflow/holding-release` |
| JVM options | `-Xms1024m -Xmx2048m -XX:MaxMetaspaceSize=1024m` |
| Page size | 2k |
| Page amount | 25 |
| Time cost for group lock filter | 5min37s(12.1s for resultant filter + 5mins 25s) |
| Time cost for each page(query by ID + run lifecycle) | ~2.7s for each page |
| Total Time cost | 6min49s |
| Max Memory Usage | < 900M |
| Success rate | 7095 filtered by group lock check, others 100% success |

The group-lock stage accounts for approximately 82% of the reported elapsed time. The source does not identify the operation represented by the remaining approximately 5 minutes 25 seconds in its breakdown.

## Related pages

- [[cash-settlement-batch-job-performance]]
- [[paginated-cashflow-batch-processing]]
- [[long-running-batch-job-api-execution]]
- [[cashflow-release-and-netting-race-condition]]
- [[is-six-gb-jvm-heap-sufficient-for-ratan-auto-materialize-at-uk-volume]]
- [[does-the-ebbs-accounting-job-meet-uk-volume-performance-requirements]]
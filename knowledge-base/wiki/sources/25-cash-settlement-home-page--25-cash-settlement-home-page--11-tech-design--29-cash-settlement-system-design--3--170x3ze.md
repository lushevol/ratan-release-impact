---
type: source
title: Cashflow Data Provider Query Solution for Big Volume
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, performance-testing, large-volume-query, streaming, jdbc]
related: [cashflow-data-provider, streaming-large-cashflow-query-responses, cashflow-query-connection-pool-capacity, cashflow-data-provider-large-volume-query-implementations, cash-settlement-query-cn-cashflow-data, database-connection-pool-saturation, postgresql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/PT for big volume query.md"]
---
# Cashflow Data Provider Query Solution for Big Volume

## Summary

This document records UAT performance testing for large-volume Cashflow Data Provider queries against `cash_settlement_query_cn.cashflow_data`. It compares three implementations:

- **V1 — once query:** retrieves the complete result set in one response.
- **V2 Draft — loop query with aggregation:** retrieves 10,000-row chunks but accumulates all JSON results into one in-memory list.
- **V2 Final — loop query with streaming:** retrieves 5,000-row chunks, converts each chunk to bytes, and streams the bytes iteratively through Spring MVC.

The evidence shows that chunked database retrieval does not by itself solve memory pressure. The V2 Draft still approaches the JVM limit or fails with OOM because it retains the complete response. V2 Final avoids the documented OOM failure mode in the tested cases, although database query shape and JDBC connection-pool capacity remain important constraints.

## Test Environment

| Environment | OS | CPU | Memory |
|---|---|---|---|
| UAT hostname: `uklvadapp1341` | RedHat_8.9 x86_64 | Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz, 16 cores | Total: 125G; used: 62.77G |

The results are environment-specific. The source does not provide database hardware or configuration, dataset shape, response-size distribution, JVM garbage-collection metrics, network conditions, or formal latency and throughput targets.

## API Requests

### V1

```sql
curl -k -i -s -H 'Content-Type: application/json' -XPOST 'https://10.198.199.161:9006/v1/data/provider/query/cashflows' -d '{"queryCondition": "Select Cashflow.Cashflow_Id, Cashflow.Audit, * from cash_settlement_query_cn.cashflow_data LIMIT ${VOLUME_AMOUNT} OFFSET 0"}'
```

### V2

```sql
curl -k -i -s -H 'Content-Type: application/json' -XPOST 'https://10.198.199.161:9006/v2/data/provider/query/cashflows/loop' -d '{"queryCondition": "Select Cashflow.Cashflow_Id, Cashflow.Audit, * from cash_settlement_query_cn.cashflow_data LIMIT ${VOLUME_AMOUNT} OFFSET 0"}'
```

The request contract shown in the source accepts a caller-provided `queryCondition` containing SQL-like text. The document does not specify validation, parameterization, authorization, data-entitlement enforcement, row limits, query timeouts, or SQL-injection protections.

## V1: Whole-Result Retrieval

V1 retrieves the full result set in one response.

| Query Volume | Number | Time (s) | JVM Memory | Comment |
|---|---:|---:|---|---|
| 300k | 1 | 1 | `-Xms1024m -Xmx4096m -XX:MaxMetaspaceSize=256m` | OOM |
| 300k | 3 | 1 | `-Xms1024m -Xmx8192m -XX:MaxMetaspaceSize=256m` | OOM |
| 300k | 5 | 1 | `-Xms10240m -Xmx12288m -XX:MaxMetaspaceSize=256m` | OOM |

Increasing the maximum heap from 4 GB to 12 GB did not make the documented 300k-row V1 workload safe.

## V2 Draft: Chunked Retrieval with Full Aggregation

The draft implementation:

1. Queries 10k rows per loop.
2. Collects each loop's JSON data list into one large data list.
3. Returns the complete large list in one response.

| Query Volume | Number | JVM Memory | One Query Time (s) | Comment |
|---|---:|---|---:|---|
| 300k | 1 | `-Xms1024m -Xmx4096m -XX:MaxMetaspaceSize=256m` | — | Close to maximum JVM memory |
| 300k | 3 | `-Xms1024m -Xmx8192m -XX:MaxMetaspaceSize=256m` | 192 | Close to maximum JVM memory |
| 300k | 5 | `-Xms1024m -Xmx8192m -XX:MaxMetaspaceSize=256m` | — | OOM |
| 300k | 3 | `-Xms10240m -Xmx12288m -XX:MaxMetaspaceSize=256m` | 86 | Close to maximum JVM memory |
| 300k | 5 | `-Xms10240m -Xmx12288m -XX:MaxMetaspaceSize=256m` | 108 | OOM |
| 300k | 10 | `-Xms10240m -Xmx12288m -XX:MaxMetaspaceSize=256m` | 395 | Pool size 10 caused JDBC timeout and connection-acquisition failure; pool size 30 resulted in OOM |

A larger connection pool changed the failure mode in the ten-query test but did not resolve the underlying memory problem.

## V2 Final: Chunked Retrieval with Streaming

The final implementation:

1. Queries 5k rows per loop.
2. Transforms each JSON data list into bytes.
3. Streams the bytes iteratively through Spring MVC.

Configured JVM memory:

```text
-Xms10240m -Xmx12288m -XX:MaxMetaspaceSize=256m
```

| Query Volume | Number | Query Method | Pool Maximum | One Query Time (s) | Comment |
|---|---:|---|---:|---:|---|
| 300k | 5 | — | — | 267 | — |
| 500k | 3 | `created_at` descending with `created_at <= now()` | 10 | 391 | All success |
| 500k | 5 | `created_at` descending with `created_at <= now()` | 10 | 218 | Three loop queries failed to obtain JDBC connections |
| 500k | 5 | `created_at` descending with `created_at <= now()` | 20 | 197 | All success |
| 500k | 3 | `cashflow_Ids` | 10 | 265 | All success |
| 500k | 5 | `cashflow_Ids` | 10 | 379 | Two loop queries failed to obtain JDBC connections |
| 500k | 5 | `cashflow_Ids` | 20 | 166 | All success |
| 1200k | 3 | `created_at` descending with `created_at <= now()` | 10 | 3357 | — |
| 1200k | 3 | `cashflow_Ids` | 20 | 320 | Success log recorded |
| 1200k | 5 | `cashflow_Ids` | 20 | 334 | Success log recorded |

The 1,200k-row `created_at` case took 3,357 seconds, approximately 55.95 minutes. The `cashflow_Ids` cases took 320–334 seconds, approximately 5.33–5.57 minutes. These comparisons are not fully controlled because the pool sizes differ and the source does not provide exact SQL, indexes, execution plans, or cache state.

## Findings

- Whole-result retrieval was not viable for the documented 300k-row V1 tests.
- Chunking without streaming remained unsafe because V2 Draft retained the full response.
- V2 Final's bounded chunking and byte streaming avoided the documented OOM outcome in the listed tests.
- A maximum JDBC pool size of 10 was insufficient for several five-request, 500k-row tests; the corresponding pool size of 20 cases were recorded as successful.
- Pool expansion is not a general solution: in V2 Draft, increasing the pool from 10 to 30 enabled more concurrent memory-intensive work and ended in OOM.
- Query shape materially affected runtime, but the source does not support attributing the 1,200k-row difference solely to `created_at` ordering.
- Successful completion is not the same as an acceptable operational latency. No formal SLA, response-size limit, concurrency target, or error-rate target is stated.

## Open Questions

The source does not define:

- The meanings of `Number`, `Time (s)`, and `One Query time (s)`.
- The exact SQL executed on each loop iteration.
- Whether pagination uses safe deterministic ordering and snapshot semantics.
- Whether framework, proxy, compression, or client buffering undermines streaming.
- Query-volume, response-size, concurrency, timeout, and cancellation limits.
- The execution plan and index support for the `created_at` ordering query.
- Data-entitlement, authorization, sensitive-field masking, and audit controls.
- Slow-client, back-pressure, partial-response, and cancellation behavior.

## Source Attachments

The original document references memory and success-log screenshots under `attachments/`, including `Picture3.png`, `Picture4.png`, `Picture5.png`, `Picture6.png`, and multiple `image2024-*.png` files. The screenshots are evidence for the recorded test observations but do not replace missing metric definitions or execution-plan data.
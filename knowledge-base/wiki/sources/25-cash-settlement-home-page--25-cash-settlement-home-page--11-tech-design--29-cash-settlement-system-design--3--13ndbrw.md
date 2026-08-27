---
type: source
title: Cashflow Data Provider Query Solution for Big Volume
authors: []
year: 2026
url: ""
venue: "Cash Settlement System Design"
tags: [cashflow, data-provider-api, high-volume-query, streaming, PostgreSQL, UAT]
related: [cashflow-data, cashflow-data-history, postgresql, query-service, cashflow-data-report, streaming-response-body, cashflow-data-api-streaming, cashflow-api-payload-expansion, cashflow-large-volume-transfer-options, approved-cashflow-large-volume-query-and-streaming-contract, does-solution-d-support-1-2-million-cashflow-records-at-qps-greater-than-5]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# Cashflow Data Provider Query Solution for Big Volume

## Summary

This design addresses application-memory exhaustion and response latency when the cashflow data provider API returns large result sets. The evidence comes from a UAT environment using the PostgreSQL `cashflow_data` table and the API endpoint `/v1/data/provider/query/cashflows`.

The document compares REST/JSON, gzipped JSON, gRPC binary transfer, and HTTP streaming. It prefers Solution D: the existing client remains unchanged while the cashflow query service executes smaller PostgreSQL queries and writes each result incrementally through Spring WebMvc `StreamingResponseBody`.

The recommendation is architecturally plausible for reducing peak application memory, but the stated capacity of at least 1.2 million records at QPS greater than 5 is not supported by benchmark evidence in the source.

## UAT Record and Payload Estimates

| SELECT count(*) FROM cashflow_data | 439668 (num) |
| --- | --- |
| SELECT pg_relation_size('cashflow_data') | 473743360 (Byte) |
| One record size of "cashflow_data" in DB = 473743360 / 439668 = 1077 (Byte) = **1KB** |

| API call "/v1/data/provider/query/cashflows" | Payload size |
| --- | --- |
| {"queryCondition": "Select * from cash_settlement_query_cn.cashflow_data LIMIT 1 OFFSET 0"} | 10.11KB |
| {"queryCondition": "Select * from cash_settlement_query_cn.cashflow_data LIMIT 100 OFFSET 0"} | 941.29KB |
| One record size of "cashflow_data" in response payload = **9.4KB** |

The source attributes the expansion to the long names of the fields and JSON representation. These figures are UAT observations rather than universal row-size guarantees. `pg_relation_size` can include relation-level storage overhead, and the API measurement may include JSON envelopes, metadata, escaping, or other response overhead.

| Records | 10k | 30k | 100k | 1200k |
| --- | --- | --- | --- | --- |
| DB data size | 10M | 30M | 100M | 1.2G |
| Payload data size | 94M | 275M | 940M | 10.74G |

## Reported Problem

Calling the data provider API eight times, with each request fetching 30,000 records, causes an out-of-memory condition. The design therefore asks:

1. How can application OOM risk be mitigated?
2. How can response time be reduced?

At the estimated 9.4 KB per serialized record, a 30,000-record response is approximately 282 MB before database-driver buffers, object graphs, serialization buffers, JVM overhead, garbage collection, and concurrent requests are considered.

## Proposed Solutions

### Solution A: Precomputed Report and Compressed Files

The design proposes periodically preparing processed cashflow data in a `cashflow_data_report` table, either daily or hourly. This could reduce duplicate database queries and internal API calls when the same report data is requested repeatedly.

For transmission, the query service would:

1. Query cashflow data in smaller slices.
2. Write each slice to a JSON report file.
3. Compress the files.
4. Read each compressed file.
5. Send the files to SSDR through a gRPC stream.

This approach requires decisions about freshness, report lifecycle, disk capacity, cleanup, archiving, and whether a file server is available.

### Solution B: DQSL as gRPC Server

Under this option:

1. DQSL exposes a gRPC server port.
2. The cashflow query service acts as a gRPC client.
3. The query service may return `"Received"` shortly after accepting the request while file transmission continues in the background.

### Solution C: Cashflow Query Service as gRPC Server

Under this option:

1. DQSL acts as a gRPC client.
2. The cashflow query service acts as a gRPC server.
3. The query service may return `"Received"` shortly after accepting the request while file transmission continues in the background.

This option requires the relevant SDKs, a gRPC server port on the query service, and compatible gateway behavior.

### Solution D: Spring WebMvc HTTP Streaming

Under the preferred option:

1. The DQSL client requires no modification.
2. The cashflow query service loops over smaller cashflow queries.
3. Each query result is written incrementally as stream bytes using `StreamingResponseBody`.

The stated benefits are:

- No large query result set remains in application memory.
- No large report file remains on disk.
- Reduced exposure to circuit-breaker timeout settings.

The stated defect is that multiple PostgreSQL calls may take longer than one large query because of additional database round trips and execution overhead.

## Design Questions

The source leaves the following decisions unresolved:

- What are the request scenarios and concurrency levels for SSDR users?
- Should a large request be split by day or by record number?
- How frequently does cashflow data change?
- Can the same report data be returned for a defined period?
- Is a file server available for report storage?
- If VM disk is used, when should files be deleted or archived?
- What stable ordering and pagination key will make slices deterministic?
- Can all slices observe one consistent database snapshot?
- What are the gateway, client, circuit-breaker, and idle-timeout limits?
- How are cancellation, retries, duplicate requests, and partial transfers handled?

## Assessment

Streaming is a transport and buffering strategy, not a substitute for database indexing, query-plan tuning, or read-model design. Smaller queries can lower peak memory but may increase total duration and can introduce consistency problems if the underlying table changes between slices.

The implementation should define database fetch behavior, serialization buffering, backpressure, cancellation, stable ordering, slice boundaries, authorization, response semantics, and observability. The 1.2 million-record and QPS greater than 5 claim requires reproducible testing at 30,000, 100,000, and 1.2 million records under realistic concurrency.

## Related Wiki Context

This source complements existing work on [[concepts/denormalized-cashflow-query-read-model]], [[concepts/cash-settlement-query-service-graphql-read-model]], [[concepts/cashflow-blotter-query-performance]], [[concepts/value-date-bounded-cashflow-queries]], and [[concepts/paginated-cashflow-batch-processing]]. It should also be considered alongside [[queries/which-indexes-and-data-retention-controls-are-required-for-cashflow-query-tables]] and [[queries/what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]].
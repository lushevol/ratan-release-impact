---
type: concept
title: Cashflow Data API Streaming
tags: [cashflow, API, streaming, chunking, backpressure, pagination]
related: [cashflow-data, query-service, streaming-response-body, paginated-cashflow-batch-processing, long-running-batch-job-api-execution, cashflow-large-volume-transfer-options, approved-cashflow-large-volume-query-and-streaming-contract]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# Cashflow Data API Streaming

Cashflow Data API Streaming is the incremental retrieval and transmission of a large cashflow result set. The query service executes bounded database queries and writes each result to the response as it becomes available instead of retaining the complete result in application memory.

## Why It Matters

The source reports an out-of-memory condition when the data provider API is called eight times with 30,000 records per request. At an estimated 9.4 KB serialized payload per record, large responses can consume hundreds of megabytes before accounting for framework, driver, JVM, and concurrency overhead.

Streaming can reduce peak memory and avoid intentional temporary-file staging. It may, however, increase total duration because one logical request becomes multiple PostgreSQL calls.

## Required Contract

A production contract should specify:

- Stable ordering and a keyset or range-based slice boundary.
- Maximum slice size and maximum total result size.
- Snapshot or report-version consistency across slices.
- Serialization format and authorization behavior for every slice.
- Backpressure and slow-consumer handling.
- Cancellation, retry, duplicate-request, and partial-result semantics.
- Gateway, proxy, client, circuit-breaker, and idle-timeout behavior.
- Metrics for memory, query duration, throughput, bytes sent, and incomplete streams.

Offset-based pagination should not be assumed to be safe at high volume without deterministic ordering and performance validation.

## Evidence Boundary

The source prefers Spring WebMvc `StreamingResponseBody`, but does not provide benchmark data proving support for 1.2 million records at QPS greater than 5. That claim remains an open capacity question tracked in [[queries/does-solution-d-support-1-2-million-cashflow-records-at-qps-greater-than-5]].
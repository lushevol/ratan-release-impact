---
type: query
title: Does Solution D Support 1.2 Million Cashflow Records at QPS Greater Than 5?
tags: [cashflow, performance, capacity, streaming, benchmark]
related: [cashflow-data-api-streaming, cashflow-large-volume-transfer-options, cashflow-api-payload-expansion, query-service, postgresql]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# Does Solution D Support 1.2 Million Cashflow Records at QPS Greater Than 5?

The source concludes that Solution D can support at least 1.2 million records with QPS greater than 5 and almost no OOM risk. No benchmark evidence is included to validate that capacity claim.

## Required Validation

Testing should include at least 30,000, 100,000, and 1.2 million records under representative concurrency. Measurements should include:

- End-to-end latency and percentile distribution.
- Sustained throughput and request completion rate.
- JVM heap, allocation rate, garbage collection, and out-of-memory behavior.
- PostgreSQL execution time, connection usage, and query-plan stability.
- Serialized and transferred bytes, with and without compression.
- Gateway, proxy, client, and circuit-breaker timeout behavior.
- Cancellation, retry, duplicate-request, and partial-stream behavior.

The result should be recorded as a reproducible capacity baseline rather than inferred from the approximate 9.4 KB payload-per-record estimate.
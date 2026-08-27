---
type: concept
title: Streaming Large Cashflow Query Responses
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, streaming, memory-management, spring-mvc, large-volume-query]
related: [cashflow-data-provider, cashflow-query-connection-pool-capacity, paginated-cashflow-batch-processing, cashflow-blotter-query-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/PT for big volume query.md"]
---
# Streaming Large Cashflow Query Responses

Streaming large query responses means retrieving data in bounded chunks, serializing each chunk, and sending it to the client without retaining the complete response in the server heap.

## Design Principle

The source contrasts two forms of chunking:

- V2 Draft retrieves 10k-row chunks but aggregates every chunk into one large JSON data list.
- V2 Final retrieves 5k-row chunks, converts each result list into bytes, and streams the bytes iteratively through Spring MVC.

The second design reduces heap retention because completed chunks can be released after serialization and transmission. This addresses response-materialization pressure that heap-size increases did not solve for V1 and V2 Draft.

## Boundaries

Streaming does not automatically solve:

- Slow database execution.
- Long-held JDBC connections.
- Connection-pool exhaustion.
- Proxy or framework buffering.
- Client-side aggregation.
- Output-buffer pressure.
- Missing cancellation, timeout, or back-pressure controls.

The UAT evidence supports streaming as a memory-safety improvement, not as a universal latency or capacity guarantee. See [[cashflow-data-provider]] and [[cashflow-query-connection-pool-capacity]].
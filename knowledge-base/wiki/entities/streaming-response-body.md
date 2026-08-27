---
type: entity
title: Spring WebMvc StreamingResponseBody
tags: [Spring WebMvc, HTTP streaming, response-body, cashflow]
related: [query-service, cashflow-data-api-streaming, cashflow-large-volume-transfer-options, long-running-batch-job-api-execution]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# Spring WebMvc StreamingResponseBody

`StreamingResponseBody` is the Spring WebMvc mechanism proposed for incrementally writing cashflow query results to an HTTP response.

## Use in the Design

The cashflow query service would execute smaller PostgreSQL queries and write each result to the response stream rather than constructing one large in-memory response. This is the implementation basis of preferred Solution D, which preserves the existing DQSL client contract.

## Operational Conditions

Using `StreamingResponseBody` does not by itself prove end-to-end streaming. Validation must cover:

- PostgreSQL fetch and driver buffering.
- JSON serialization behavior.
- Servlet-container buffering.
- Reverse-proxy and gateway buffering.
- Client-side buffering and consumption.
- Backpressure and slow consumers.
- Cancellation and connection resets.
- Request, idle, circuit-breaker, and client-deadline behavior.

The mechanism can reduce peak application memory, but it does not guarantee that timeout risk or buffering disappears at every infrastructure layer.
---
type: comparison
title: Cashflow Large-Volume Transfer Options
tags: [cashflow, API, REST, gRPC, streaming, performance]
related: [cashflow-data-api-streaming, cashflow-api-payload-expansion, streaming-response-body, cashflow-data-report, query-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# Cashflow Large-Volume Transfer Options

The source compares four transfer patterns for large cashflow data requests.

| Option | Request and response | Main strategy | Main benefit | Main cost or condition |
| --- | --- | --- | --- | --- |
| 1 | HTTP RESTful request; JSON response | DQSL splits the request into smaller requests | Reduces large-result retention in the query service | Each response remains large; DQSL requires an SDK |
| 2 | HTTP RESTful request; gzipped JSON response | Query slices are written to files, compressed, and returned | Reduces transfer size and transfer time | Requires disk storage, cleanup, and an SDK |
| 3 | RESTful request; gRPC binary response | Query service acknowledges, creates compressed files, and streams binary data | Smaller binary chunks and potentially more efficient HTTP/2 transfer | Requires DQSL to expose a gRPC server port and use the SDK |
| 4 | gRPC client request; gRPC binary response | DQSL sends a gRPC request and the query service streams binary data | Similar chunking and transfer benefits | Requires gateway HTTP/2 and HTTP/1.1 support and AA support in Ratan API Gateway |
| Solution D | Existing client; HTTP streaming response | Smaller PostgreSQL queries write incrementally through `StreamingResponseBody` | Avoids intentional large in-memory results and large files | Multiple PostgreSQL calls may increase duration |

## Comparison Dimensions

The options are not fully equivalent: some change protocol direction, some change storage strategy, and Solution D changes response buffering while retaining the client contract. A complete decision should compare:

- Peak memory at the query service and client.
- Disk usage and cleanup requirements.
- Transfer compression and serialization cost.
- Database round trips and total duration.
- Gateway and client compatibility.
- Timeout and circuit-breaker behavior.
- Cancellation, retry, and partial-result semantics.
- Snapshot consistency across slices.
- Operational complexity and observability.

The source prefers Solution D, but its stated capacity of 1.2 million records at QPS greater than 5 requires validation.
---
type: concept
title: Scroll-Query-and-Publish Processing
created: 2026-08-23
updated: 2026-08-23
tags: [concurrency, pagination, batch-processing, event-publication, ssi-stamping]
related: [code-concurrent-issues, nostro-refresh-command, ssi-exception-command, ratan-cash-settlement-ssi-stamping-service, ssi-stamping-retry-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Code Concurrent Issues.md"]
---
# Scroll-Query-and-Publish Processing

Scroll-query-and-publish processing is a batch or pagination workflow that reads records through a scrolling query and publishes the resulting records or messages.

The source identifies two implementations for concurrency review:

- `NostroRefreshCommand.scrollQueryAndPublish`, using `queryResult`
- `SsiExceptionCommand.scrollQueryAndPublish`, using `queryResult`

Potential areas for investigation include overlapping runs, paging drift, records changing during a scan, duplicate publication, omissions, ordering, retries, and idempotency. The source does not state that any of these outcomes has occurred or that either `queryResult` collection is shared state.
---
type: entity
title: SsiExceptionCommand
created: 2026-08-23
updated: 2026-08-23
tags: [code-command, ssi, exception-handling, query-and-publish, concurrency-review]
related: [ratan-cash-settlement-ssi-stamping-service, scroll-query-and-publish-processing, ssi-stamping, ssi-stamping-retry-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Code Concurrent Issues.md"]
---
# SsiExceptionCommand

`SsiExceptionCommand` is a code command named in the concurrency issue inventory for `scrollQueryAndPublish`, with `queryResult` identified as the review point.

The source does not define the exception records processed, query and pagination semantics, publication destination, retry behavior, deduplication, or idempotency. The entry identifies a location for investigation, not a confirmed SSI concurrency defect.
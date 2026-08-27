---
type: source
title: Code Concurrent Issues
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page — Settlement Day2 Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, concurrency, code-review]
related: [cashflow-processing-concurrency, scroll-query-and-publish-processing, message-holding-and-release, ratan-cashflow-lifecycle-service, ratan-cash-settlement-ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Code Concurrent Issues.md"]
---
# Code Concurrent Issues

## Summary

This document is a short inventory of code locations selected for concurrency review under the Settlement Day 2 requirement. It identifies review points in `ratan-cashflow-lifecycle-service` and `ratan-cash-settlement-ssi-stamping-service`, but does not document confirmed race conditions, observed failures, remediation proposals, execution paths, or test evidence.

The listed locations include filtering of netting-resultant and regular cashflows, plus scroll-query-and-publish processing for Nostro refresh and SSI exception handling. `MessageHoldingServiceImpl.releaseV2` is explicitly marked as having “no concurrency point.”

## Issue points

| | service | point | service | comment |
| --- | --- | --- | --- | --- |
| 1 | ratan-cashflow-lifecycle-service | MessageHoldingServiceImpl.filterNettingResultantCashflowsV2 filteredHoldingMessageVos | | |
| 2 | MessageHoldingServiceImpl.filterRegularCashflowsV2 filteredData | | | |
| 3 | MessageHoldingServiceImpl.releaseV2 successHoldingIds | | | no concurrency point |
| 4 | ratan-cash-settlement-ssi-stamping-service | NostroRefreshCommand.scrollQueryAndPublish queryResult | | |
| 5 | | SsiExceptionCommand.scrollQueryAndPublish queryResult | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

## Evidence and limitations

The table establishes candidate code locations for review and distinguishes lifecycle-service points from SSI-stamping-service points. It does not establish whether the named collections are shared mutable state or merely method-local variables. The actual concurrency questions—such as overlapping executions, transaction boundaries, pagination consistency, duplicate publication, idempotency, and stale reads—remain unresolved.

See [[cashflow-processing-concurrency]] and [[scroll-query-and-publish-processing]] for the review scope, and [[what-are-the-confirmed-concurrency-failure-modes-in-ratan-cashflow-and-ssi-processing]] for the open technical questions.
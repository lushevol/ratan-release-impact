---
type: query
title: Does SSDR Cashflow Exposure Meet Its Required Latency and Pagination SLA?
created: 2026-08-24
updated: 2026-08-24
tags: [SSDR, cashflow-data, performance, SLA, pagination]
related: [ssdr, query-service, wide-cashflow-read-projection-performance, cashflow-blotter-query-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/PT-Ratan expose the cashflow data to SSDR.md"]
---
# Does SSDR Cashflow Exposure Meet Its Required Latency and Pagination SLA?

The source provides elapsed-time measurements but no target latency, percentile, maximum page size, expected selectivity, consumer concurrency, extraction frequency, or production-load baseline. It therefore cannot establish whether the cashflow-data exposure meets SSDR requirements.

The broad benchmark uses `LIMIT ... OFFSET 0` without `ORDER BY`; it does not specify stable ordering, continuation tokens, page consistency, or performance at non-zero offsets.

## Resolution needed

Define and approve:

- Maximum and typical projection widths and page sizes.
- Required p50, p95, and p99 latency under expected and peak concurrency.
- Maximum allowed extraction volume and frequency.
- Stable ordering and pagination/continuation contract.
- Snapshot consistency, retry, and duplicate/missing-record handling.
- Production-representative performance evidence for the final contract.
---
type: concept
title: Cashflow API Payload Expansion
tags: [cashflow, JSON, serialization, payload, capacity-planning]
related: [cashflow-data, query-service, cashflow-data-api-streaming, cashflow-blotter-query-performance, postgresql]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# Cashflow API Payload Expansion

Cashflow API Payload Expansion is the observed difference between the approximate PostgreSQL storage size of a `cashflow_data` record and its serialized API response size.

## UAT Observation

The source reports approximately 1 KB per record in PostgreSQL and approximately 9.4 KB per record in the response payload:

- `cashflow_data` row count: 439,668.
- PostgreSQL relation size: 473,743,360 bytes.
- Calculated relation-size-per-row estimate: 1,077 bytes.
- One-record API response: 10.11 KB.
- One-hundred-record API response: 941.29 KB.
- Approximate response size per record: 9.4 KB.

The source attributes the expansion partly to long field names and JSON representation.

## Interpretation

These values are useful for UAT capacity estimates but are not a universal logical row-size ratio. Relation size may include page and storage overhead. API measurements may include envelopes, metadata, escaping, or other fixed costs. Compression, selected columns, null representation, and serialization implementation can also change the result.

Capacity planning should measure complete end-to-end payloads under representative data and concurrency rather than extrapolating from a single row-size division.
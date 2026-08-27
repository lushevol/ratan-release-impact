---
type: query
title: Which Indexes Were Used in the SSDR Cashflow Data Benchmarks?
created: 2026-08-24
updated: 2026-08-24
tags: [SSDR, cashflow-data, PostgreSQL, indexes, benchmarking]
related: [ssdr, query-service, cash-settlement-query-cn-cashflow-data, postgresql-jsonb-expression-index-matching, which-indexes-and-data-retention-controls-are-required-for-cashflow-query-tables]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/PT-Ratan expose the cashflow data to SSDR.md"]
---
# Which Indexes Were Used in the SSDR Cashflow Data Benchmarks?

The source reports materially lower DEV latency “with index” for both JSONB and physical-column retrieval, particularly at 1,000–5,000 records. It does not provide index names, `CREATE INDEX` statements, operator classes, query predicates, index sizes, write overhead, or `EXPLAIN (ANALYZE, BUFFERS)` output.

## Evidence needed

- Exact `CREATE INDEX` DDL and schema name for every index enabled in the comparison.
- Query text and API implementation for JSONB and column paths.
- `EXPLAIN (ANALYZE, BUFFERS)` before and after indexing.
- Index-maintenance and write-path impact.
- Repeated production-representative measurements under defined concurrency and cache conditions.

Until that evidence is supplied, this benchmark supports an observed association with indexing but not a production recommendation for a specific access path.
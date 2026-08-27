---
type: query
title: Is the NSTP Exception Regex Filter Compatible with Cashflow Blotter Performance SLAs?
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, regex, cashflow-blotter, performance, graphql, nstp]
related: [nstp-exception-filter, cashflow-blotter-query-performance, value-date-bounded-cashflow-queries, cashflow-data, postgresql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Is the NSTP Exception Regex Filter Compatible with Cashflow Blotter Performance SLAs?

The proposed NSTP filter uses a `${RegExp_String}` representation and relies on PostgreSQL POSIX regular-expression support. PostgreSQL support alone does not demonstrate acceptable performance, predictable execution plans, or safe input behavior.

## Required validation

- Define the GraphQL filter contract and allowed regex subset.
- Confirm escaping, length limits, case-sensitivity, and protection against expensive expressions.
- Capture `EXPLAIN (ANALYZE, BUFFERS)` plans for representative status, horizon, and NSTP exception combinations.
- Test realistic data volumes and pagination patterns.
- Establish whether an index can support the required predicates or whether equality, array, join-table, or normalized-code filtering is preferable.
- Evaluate interaction with existing Cashflow Blotter predicates and performance guardrails.

The design should not proceed to production on the assumption that regex matching preserves the performance expectations documented in [[cashflow-blotter-query-performance]].
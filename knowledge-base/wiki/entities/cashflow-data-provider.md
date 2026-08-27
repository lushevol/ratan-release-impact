---
type: entity
title: Cashflow Data Provider
created: 2026-08-24
updated: 2026-08-23
tags: ["cash-settlement", "cashflow-data", "query-service", "data-provider", "cashflow", "api", "performance"]
related: ["cashflow-data", "cashflow-data-history", "query-service", "multi-version-cashflow-query", "cashflow-data-provider-query-performance", "cash-settlement-platform", "cash-settlement-query-cn-cashflow-data", "streaming-large-cashflow-query-responses", "cashflow-query-connection-pool-capacity"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/Cashflow data provider query with multiple versions.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/PT for big volume query.md"]
---
# Cashflow Data Provider

The Cashflow Data Provider exposes large-volume cashflow query endpoints over HTTP. The newly generated source documents:

- `/v1/data/provider/query/cashflows` for whole-result retrieval.
- `/v2/data/provider/query/cashflows/loop` for chunked retrieval and, in the final implementation, iterative byte streaming.

That source states that the provider queries `cash_settlement_query_cn.cashflow_data`, a cashflow query read model. The tested request body contains a caller-supplied `queryCondition` string with SQL-like query text.

## Performance Role and Implementations

The documented UAT testing in the newly generated source compares V1, V2 Draft, and V2 Final:

- **V1** failed with OOM for the tested 300k-row cases.
- **V2 Draft** reduced database fetch size but aggregated all chunks in memory, and also reached the JVM limit or failed with OOM.
- **V2 Final** used 5k-row chunks and streaming, supporting the listed tests up to 1,200k rows without a documented OOM outcome.

The provider's performance boundary is not only JVM memory. JDBC connection acquisition failed in several five-request, 500k-row tests when the connection-pool maximum was 10, while corresponding cases with a pool maximum of 20 were recorded as successful.

## Recorded Performance Evidence

The source documenting the multiple-version cashflow query performance records the following measurements:

| Environment | Reported count | Reported cost |
|---|---:|---:|
| `uat1` | `42w` | `55s` |
| `fmrp1` | `120w` | `133s` |

The source does not define the units of the counts or the exact meaning of the cost metric. Because environment and volume vary together, these measurements cannot determine whether the runtime difference is caused by data volume, environment configuration, database state, query plans, or another factor.

## Relationship to Other Components

The provider concerns [[cashflow-data]] and may interact with [[cashflow-data-history]] when multiple versions are retained.

The relationship to [[query-service]] and the [[cash-settlement-query-service-graphql-read-model]] is architectural context in the multiple-version performance source; that source does not confirm that its specific test used the Query Service or a GraphQL read model. Separately, the newly generated source identifies `cash_settlement_query_cn.cashflow_data` as the read model queried by the provider.

## Governance Concerns

The newly generated source does not establish whether `queryCondition` is:

- Parsed or parameterized.
- Allowlisted.
- Authorized or entitlement-filtered.
- Row-limited.
- Subject to a timeout.
- Audit-logged.

These controls should be confirmed before treating the endpoint as a general-purpose query interface.

See [[streaming-large-cashflow-query-responses]], [[cashflow-query-connection-pool-capacity]], and [[what-controls-govern-data-provider-querycondition-sql]].

## Evidence Limitations

Across the source documents, no query text, schema, indexes, version-selection predicates, concurrency model, hardware profile, cache state, or performance acceptance criterion is documented. The observed timings must not be generalized to [[cashflowsnew]], [[cashflow-blotter]], [[ultra-cashflow-query]], or [[legacy-cashflow-query]].
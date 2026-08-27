---
type: query
title: What Batch Size and Generated-Key Contract Avoid PgJDBC Blocking in Lifecycle Service?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lifecycle-service, pgjdbc, jdbc, batch-processing, generated-keys, performance]
related: [cashflow-lifecycle-service, pgjdbc, spring-jdbctemplate, keyholder, pgjdbc-batch-client-server-deadlock, generated-key-column-projection, cash-settlement-batch-job-performance, cash-settlement-lifecycle-job-batch-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/ProgreSQL JDBC Driver.md"]
---
# What Batch Size and Generated-Key Contract Avoid PgJDBC Blocking in Lifecycle Service?

## Question

What explicit generated-key column contract and batch-size range should the Cashflow Lifecycle Service use for CQRS domain-event inserts to avoid PgJDBC transport blocking while meeting throughput and latency requirements?

## Why this remains open

The source identifies a credible PgJDBC client/server socket-buffer deadlock risk and recommends requesting only necessary generated-key columns while tuning batch size. It does not provide a validated configuration or measured result.

`MAX_BUFFERED_RECV_BYTES = 64000` is an internal PgJDBC receive-buffer estimate, not a universal safe batch-size target.

## Evidence required

- Deployed PgJDBC and PostgreSQL versions.
- The exact `JdbcTemplate.batchUpdate()` overload and `KeyHolder` configuration.
- Explicit generated-key column names and actual returned result-set metadata.
- SQL statement shape, including whether one statement can return multiple keys.
- Baseline batch size, rows per batch, and generated-key payload size.
- Whether `reWriteBatchedInserts` was enabled.
- Thread dumps showing whether the application blocks in socket write, result processing, application synchronization, or another path.
- PostgreSQL lock and wait diagnostics captured during the event.
- Controlled before/after testing over candidate batch sizes with throughput, latency, error rate, and blocking-duration results.

## Working policy

Until workload-specific evidence is available:

1. Request only required generated-key columns.
2. Keep CQRS domain-event batches bounded.
3. Treat transport blocking as distinct from database locking during incident triage.
4. Do not generalize findings to other Cash Settlement services without confirming the same JDBC driver, generated-key contract, statement shape, and batch behavior.
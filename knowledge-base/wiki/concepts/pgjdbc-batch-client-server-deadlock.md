---
type: concept
title: PgJDBC Batch Client/Server Deadlock
created: 2026-08-24
updated: 2026-08-24
tags: [pgjdbc, postgresql, jdbc, tcp, batch-processing, deadlock]
related: [pgjdbc, spring-jdbctemplate, keyholder, generated-key-column-projection, cash-settlement-batch-job-performance, cash-settlement-lifecycle-job-batch-performance, what-batch-size-and-generated-key-contract-avoid-pgjdbc-blocking-in-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/ProgreSQL JDBC Driver.md"]
---
# PgJDBC Batch Client/Server Deadlock

A PgJDBC batch client/server deadlock is a transport-level stalemate between a JDBC driver's request-writing flow and PostgreSQL's result-writing flow.

## Mechanism

The driver sends batch requests over one direction of a TCP connection while PostgreSQL reads requests, executes them, and writes results in the other direction.

A deadlock can arise when:

1. PostgreSQL fills the server-to-client buffer with results and blocks on further writes.
2. The driver continues sending requests instead of reading pending results.
3. The driver-to-server buffer fills and the driver blocks on socket `write()`.
4. PostgreSQL cannot read additional requests because it remains blocked writing results.

This is distinct from a PostgreSQL row-lock deadlock, transaction deadlock, slow query, or sequential scan. Incident triage should inspect application thread state, driver behavior, network/socket state, and PostgreSQL wait events before classifying a reported “DB block.”

## PgJDBC safeguard and limitation

PgJDBC's `QueryExecutorImpl.flushIfDeadlockRisk(...)` tracks an estimated pending receive payload. When the estimate reaches `MAX_BUFFERED_RECV_BYTES` (recorded in the source as `64000`), it sends a protocol `Sync`, processes results through `ReadyForQuery`, resets its estimate, and resumes batching.

This is a best-effort safeguard, not a hard safety boundary. Its estimate is coarse, is applied at query level rather than actual response-message level, assumes a nominal response size, and does not account for every possible message type. A batch whose estimated size remains below 64 KB is not guaranteed safe.

## Exposure factors

Exposure increases with:

- large batch sizes;
- generated-key retrieval;
- wide generated-key result rows;
- statements that return many keys per execution;
- multi-row `VALUES` inserts or `INSERT INTO ... SELECT ...` patterns;
- network and socket-buffer conditions; and
- driver-specific implementation behavior.

For the Lifecycle Service CQRS domain-event workload, reduce returned generated-key data and establish an evidence-based batch size. See [[generated-key-column-projection]] and [[what-batch-size-and-generated-key-contract-avoid-pgjdbc-blocking-in-lifecycle-service]].
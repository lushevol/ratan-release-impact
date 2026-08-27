---
type: source
title: PgJDBC Batch Execution and Generated-Key Deadlock Risk
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, postgresql, pgjdbc, jdbc, batch-processing, generated-keys, performance]
related: [pgjdbc, spring-jdbctemplate, keyholder, pgjdbc-batch-client-server-deadlock, generated-key-column-projection, what-batch-size-and-generated-key-contract-avoid-pgjdbc-blocking-in-lifecycle-service, cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/ProgreSQL JDBC Driver.md"]
authors: []
year: 2025
url: ""
venue: Internal technical design
---
# PgJDBC Batch Execution and Generated-Key Deadlock Risk

## Summary

This technical investigation concerns an apparent database-process block while the Cashflow Lifecycle Service persisted CQRS domain events through Spring `JdbcTemplate.batchUpdate()` with a `KeyHolder` for generated keys.

The source attributes the observed risk to a PgJDBC client/server transport-level deadlock during batch execution. It does not establish a PostgreSQL transaction deadlock, row-lock deadlock, or SQL lock wait. The proposed mitigation is to request only required generated-key columns and tune the batch size against the actual workload.

The source does not record the PgJDBC version, PostgreSQL version, exact SQL, returned-key payload, selected batch size, or measured before/after outcome. Consequently, the diagnosis is strong as an explanation of a PgJDBC risk but remains unconfirmed for the specific Lifecycle Service incident.

## Scope and diagnostic boundary

The reported execution route is:

```text
Spring JdbcTemplate
  → PgJDBC PgStatement
    → QueryExecutorImpl.execute(...) [loop handling]
      → QueryExecutorImpl.sendQuery(...)
        → sendOneQuery() [can block]
      → QueryExecutorImpl.flushIfDeadlockRisk(...)
```

The relevant diagnostic distinction is:

```text
Application batch and generated-key handling
  → PgJDBC request/response pipelining
  → bidirectional TCP socket buffering
  → PostgreSQL backend request and result handling
```

A stalled application thread at this layer should not automatically be interpreted as PostgreSQL lock contention. Database lock and wait diagnostics, socket-level evidence, driver version, and thread-dump state are needed to classify an actual incident.

## Client/server deadlock mechanism

PgJDBC documents a possible bidirectional socket-buffer deadlock when a single execution flow continues sending requests while the server attempts to return results.

```java
// It's possible for the send and receive streams to get "deadlocked" against each other since
// we do not have a separate thread. The scenario is this: we have two streams:
//
// driver -> TCP buffering -> server
// server -> TCP buffering -> driver
//
// The server behaviour is roughly:
// while true:
// read message
// execute message
// write results
//
// If the server -> driver stream has a full buffer, the write will block.
// If the driver is still writing when this happens, and the driver -> server
// stream also fills up, we deadlock: the driver is blocked on write() waiting
// for the server to read some more data, and the server is blocked on write()
// waiting for the driver to read some more data.
```

The sequence is:

1. The driver writes batched requests.
2. PostgreSQL executes requests and writes results.
3. The server-to-driver TCP buffer fills and the server blocks while writing results.
4. The driver continues writing requests rather than draining results.
5. The driver-to-server TCP buffer fills and the driver blocks on `write()`.
6. Neither side can progress: the server is waiting for the client to read, while the client is waiting for the server to read.

See [[pgjdbc-batch-client-server-deadlock]].

## Generated-key return risk

The source notes that batch execution returning generated keys increases response volume and therefore exposure to this condition. The concern is particularly relevant where one execution can return many rows or keys, including a large multi-row `VALUES` insert or `INSERT INTO ... SELECT ...`.

PgJDBC's batching assumptions are more suitable when each execution returns one generated key. A `KeyHolder` is not intrinsically unsafe, but broad generated-key result sets increase the amount of data that must be returned and drained.

The proposed implementation control is [[generated-key-column-projection]]: explicitly request only the generated-key column names required by the caller, rather than relying on broad `Statement.RETURN_GENERATED_KEYS` behavior.

## PgJDBC deadlock-avoidance heuristic

The source records the `QueryExecutorImpl.flushIfDeadlockRisk(...)` control flow and its constants:

```java
// We know this is deprecated, but still respect it in case anyone's using it.
// PgJDBC its self no longer does.
@SuppressWarnings("deprecation")
boolean disallowBatching = (flags & QueryExecutor.QUERY_DISALLOW_BATCHING) != 0;
---------------------------------------------------------------------------------------------
/**
  private static final int MAX_BUFFERED_RECV_BYTES = 64000;
  private static final int NODATA_QUERY_RESPONSE_SIZE_BYTES = 250;
**/
private void flushIfDeadlockRisk(Query query, boolean disallowBatching,
      ResultHandler resultHandler,
      @Nullable BatchResultHandler batchHandler,
      final int flags) throws IOException {
    // Assume all statements need at least this much reply buffer space,
    // plus params
    estimatedReceiveBufferBytes += NODATA_QUERY_RESPONSE_SIZE_BYTES;

    SimpleQuery sq = (SimpleQuery) query;
    if (sq.isStatementDescribed()) {
      // ignore no use code
    } else {
      /*
       * We only describe a statement if we're expecting results from it, so it's legal to batch
       * unprepared statements. We'll abort later if we get any uresults from them where none are
       * expected. For now all we can do is hope the user told us the truth and assume that
       * NODATA_QUERY_RESPONSE_SIZE_BYTES is enough to cover it.
       */
    }

    if (disallowBatching || estimatedReceiveBufferBytes >= MAX_BUFFERED_RECV_BYTES) {
      LOGGER.log(Level.FINEST, "Forcing Sync, receive buffer full or batching disallowed");
      sendSync();
      processResults(resultHandler, flags);
      estimatedReceiveBufferBytes = 0;
      if (batchHandler != null) {
        batchHandler.secureProgress();
      }
    }
```

The driver's avoidance strategy is to estimate pending response data. At the estimated threshold, or when batching is disallowed, it sends `Sync`, drains results through `ReadyForQuery`, resets the estimate, and resumes work.

The source preserves the driver's qualifications: this control is not fully reliable. It applies only in batch-query cases, estimates at query rather than message granularity, assumes 250 bytes even when actual results differ, and ignores asynchronous notifications and informational messages. `MAX_BUFFERED_RECV_BYTES = 64000` is a conservative heuristic, not a universal safe payload or batch-size limit.

```java
// Deadlock avoidance:
//
// It's possible for the send and receive streams to get "deadlocked" against each other since
// we do not have a separate thread. The scenario is this: we have two streams:
//
// driver -> TCP buffering -> server
// server -> TCP buffering -> driver
//
// The server behaviour is roughly:
// while true:
// read message
// execute message
// write results
//
// If the server -> driver stream has a full buffer, the write will block.
// If the driver is still writing when this happens, and the driver -> server
// stream also fills up, we deadlock: the driver is blocked on write() waiting
// for the server to read some more data, and the server is blocked on write()
// waiting for the driver to read some more data.
//
// To avoid this, we guess at how much response data we can request from the
// server before the server -> driver stream's buffer is full (MAX_BUFFERED_RECV_BYTES).
// This is the point where the server blocks on write and stops reading data. If we
// reach this point, we force a Sync message and read pending data from the server
// until ReadyForQuery, then go back to writing more queries unless we saw an error.
//
// This is not 100% reliable -- it's only done in the batch-query case and only
// at a reasonably high level (per query, not per message), and it's only an estimate
// -- so it might break. To do it correctly in all cases would seem to require a
// separate send or receive thread as we can only do the Sync-and-read-results
// operation at particular points, and also as we don't really know how much data
// the server is sending.
//
// Our message size estimation is coarse, and disregards asynchronous
// notifications, warnings/info/debug messages, etc, so the response size may be
// quite different from the 250 bytes assumed here even for queries that don't
// return data.
```

## Recommended controls

1. Explicitly request only generated-key columns required by the application.
2. Establish a workload-specific batch size based on actual generated-key response volume, statement shape, network conditions, driver version, and concurrency.
3. Validate the configuration through measurements of throughput, latency, error rate, and blocking behavior.
4. During incidents, distinguish driver socket blocking from PostgreSQL lock waits before applying database-index or lock remedies.

These recommendations extend [[cash-settlement-batch-job-performance]] and [[cash-settlement-lifecycle-job-batch-performance]] with a driver transport constraint.

## Supporting references

- [PgJDBC can experience client/server deadlocks during batch execution · Issue #194 · pgjdbc/pgjdbc](https://github.com/pgjdbc/pgjdbc/issues/194)
- [PgJDBC does not pipeline batches that return generated keys · Issue #195 · pgjdbc/pgjdbc](https://github.com/pgjdbc/pgjdbc/issues/195)
- [Batch returning support by ringerc · Pull Request #204 · pgjdbc/pgjdbc](https://github.com/pgjdbc/pgjdbc/pull/204)
- [BatchInsert + generatedKeys will cause insert block in DB · Issue #3726 · pgjdbc/pgjdbc](https://github.com/pgjdbc/pgjdbc/issues/3726)
- [getGeneratedKeys returns all columns for Statement.RETURN_GENERATED_KEYS · Issue #99 · pgjdbc/pgjdbc](https://github.com/pgjdbc/pgjdbc/issues/99)
- [Enable reWriteBatchedInserts by default · Issue #3694 · pgjdbc/pgjdbc](https://github.com/pgjdbc/pgjdbc/issues/3694)
- [Netting Compare - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Netting+Compare)

The linked Confluence test-results page is not reproduced in this source. Its relationship to the Lifecycle Service scenario and its validation evidence require confirmation.
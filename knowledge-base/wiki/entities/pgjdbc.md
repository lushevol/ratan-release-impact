---
type: entity
title: PgJDBC
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, jdbc, java, database-driver, batch-processing]
related: [spring-jdbctemplate, keyholder, pgjdbc-batch-client-server-deadlock, generated-key-column-projection, what-batch-size-and-generated-key-contract-avoid-pgjdbc-blocking-in-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/ProgreSQL JDBC Driver.md"]
---
# PgJDBC

PgJDBC is the PostgreSQL JDBC driver used by Java applications to communicate with PostgreSQL.

In the documented Cashflow Lifecycle Service investigation, PgJDBC is the relevant layer between Spring `JdbcTemplate` batch submission and PostgreSQL request/result processing. Its `PgStatement` and `QueryExecutorImpl` execution path can encounter a client/server socket-buffer deadlock when batched requests are sent while result data is not drained quickly enough.

`QueryExecutorImpl.flushIfDeadlockRisk(...)` attempts to mitigate this risk using an estimated response-buffer threshold. The safeguard is heuristic and is explicitly not a guarantee against all transport stalls.

Generated-key batch operations are an important risk multiplier because returned key data increases the server-to-client response payload. See [[pgjdbc-batch-client-server-deadlock]] and [[generated-key-column-projection]].

The source does not identify the deployed PgJDBC version. Any incident conclusion or configuration decision must therefore validate behavior against the exact driver version in use.
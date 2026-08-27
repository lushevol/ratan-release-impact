---
type: concept
title: Generated-Key Column Projection
created: 2026-08-24
updated: 2026-08-24
tags: [jdbc, generated-keys, pgjdbc, postgresql, batch-processing]
related: [keyholder, spring-jdbctemplate, pgjdbc, pgjdbc-batch-client-server-deadlock, cash-settlement-batch-job-performance, what-batch-size-and-generated-key-contract-avoid-pgjdbc-blocking-in-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/ProgreSQL JDBC Driver.md"]
---
# Generated-Key Column Projection

Generated-key column projection is the practice of explicitly requesting only the generated-key columns required by an application rather than accepting a broad generated-key result.

In JDBC batch inserts, the amount of generated-key data returned to the client contributes to server-to-client response volume. Reducing the result width can reduce pressure on PgJDBC result buffering and lower exposure to [[pgjdbc-batch-client-server-deadlock]].

## Application to Spring JDBC

When Spring `JdbcTemplate.batchUpdate()` is used with a [[keyholder]], the generated-key contract should identify:

- the required generated-key column names;
- the expected number of returned keys per statement;
- the expected result shape;
- whether callers actually require every returned key; and
- the maximum batch size validated for that return payload.

Generic `Statement.RETURN_GENERATED_KEYS` behavior should not be assumed to be equivalent to requesting an explicit minimal set of columns. The source cites PgJDBC Issue #99 as relevant to cases in which `getGeneratedKeys` returns all columns.

## Limits

Column projection is a risk reduction, not a complete fix. A narrow key result can still be large at high row counts, and safety also depends on statement shape, batch size, PgJDBC version, connection buffering, and concurrent workload. The required configuration remains open in [[what-batch-size-and-generated-key-contract-avoid-pgjdbc-blocking-in-lifecycle-service]].
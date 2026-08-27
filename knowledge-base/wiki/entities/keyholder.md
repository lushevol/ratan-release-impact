---
type: entity
title: KeyHolder
created: 2026-08-24
updated: 2026-08-24
tags: [spring, jdbc, generated-keys, batch-processing]
related: [spring-jdbctemplate, pgjdbc, generated-key-column-projection, pgjdbc-batch-client-server-deadlock]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/ProgreSQL JDBC Driver.md"]
---
# KeyHolder

`KeyHolder` is a Spring JDBC API type used to collect database-generated keys after SQL execution.

In the documented CQRS domain-event batch insert scenario, `KeyHolder` accompanies Spring `JdbcTemplate.batchUpdate()`. Generated-key retrieval can enlarge PostgreSQL-to-client result traffic, which increases exposure to a PgJDBC batch client/server transport stall when batches return substantial data.

`KeyHolder` use is not, by itself, proof of a problem. The material factor is the generated-key return contract: required columns, result width, number of keys returned by each statement, and batch size. Prefer [[generated-key-column-projection]] when callers need only a defined subset of generated columns.
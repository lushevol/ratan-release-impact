---
type: entity
title: pg_hint_plan
tags: [PostgreSQL, query-planning, query-hints, database-extension]
related: [postgresql, cashflow-blotter-query-optimization-options, value-date-query-performance-guardrail, what-is-the-approved-cashflow-blotter-value-date-search-policy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Query Performance Optimization.md"]
---
# pg_hint_plan

`pg_hint_plan` is a PostgreSQL extension that supports query hints for influencing the database query planner. The Cashflow Blotter performance design identifies it as Proposal B for investigation.

The source does not document an implementation, approval, benchmark, PostgreSQL-version compatibility result, or operational decision for this extension. It should therefore be treated as an exploratory alternative rather than an adopted component.

## Role in Cashflow Blotter Optimization

`pg_hint_plan` represents a database-level optimization path, in contrast to the application-level [[value-date-query-performance-guardrail]], which narrows the search predicate by adding a value-date condition.

Relevant evaluation questions include:

- Whether hints improve latency for the actual Cashflow Blotter workload.
- Whether the extension is compatible with the deployed PostgreSQL versions and operating model.
- Whether hints remain reliable as data distributions, indexes, and query plans change.
- Whether operational support, monitoring, rollback, and upgrade procedures are acceptable.

The source references the project at [github.com/ossc-db/pg_hint_plan](https://github.com/ossc-db/pg_hint_plan).
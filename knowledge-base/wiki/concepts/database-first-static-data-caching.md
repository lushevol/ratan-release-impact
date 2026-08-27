---
type: concept
title: Database-First Static Data Caching
created: 2026-08-24
updated: 2026-08-24
tags: [database, caching, static-data, NFRs, Redis, reference-data]
related: [redis, static-reference-data-synchronization, cached-rule-loading, when-does-the-static-data-cache-decision-matrix-require-cache-db-or-golden-source-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# Database-First Static Data Caching

Database-first static-data caching is the policy of persisting static data in a database before using an in-memory cache. The cache is an acceleration layer, not the durable source of the local copy.

## Proposed decision logic

The source states that database access should be preferred when it meets business NFRs. Cache is proposed for frequently used data when database performance does not meet those NFRs. For large datasets, only frequently accessed portions may be cached while the complete dataset remains in the database. Infrequently used data may remain database-backed, or may be queried from the golden source when it changes frequently.

The source decision matrix categorizes choices by:

- Data origin: reference data or RatanOne-owned data
- Data volume: small or large
- Use frequency: common or special-case access
- Change frequency: more or less than one hour
- Whether business NFRs are met

## Limitations

Every matrix row marks the business NFR condition as `not match`, which may mean that database NFRs do not match, but this is not explicit. No quantitative latency, throughput, freshness, capacity, availability, or cache-staleness thresholds are defined.

This concept is distinct from [[concepts/cached-rule-loading]]: the present design concerns static reference and operational data, while cached rule loading concerns rule materialization and evaluation.

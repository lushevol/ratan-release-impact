---
type: decision
title: Adopt Redis v6+ for the Day 1 Static Data Cache
status: proposed
deciders: []
date: 2026-08-24
supersedes: ""
created: 2026-08-24
updated: 2026-08-24
tags: [architecture-decision, Redis, cache, Day-1, static-data]
related: [redis, hazelcast-imdg, database-first-static-data-caching, redis-vs-hazelcast-for-ratanone-static-data, static-reference-data-synchronization, what-is-the-production-redis-ha-dr-and-security-design-for-ratanone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# Adopt Redis v6+ for the Day 1 Static Data Cache

## Status

Proposed. The source states a Day 1 direction, but does not provide evidence that the decision was formally approved or deployed.

## Context

RatanOne needs static data for STP cashflow processing, including Vostro, Nostro, and Counterparty information. The design prefers database persistence and uses cache middleware only when database performance does not meet business NFRs.

RatanOne already uses Redis. The source also reports an unofficial development test in which Redis 5 averaged 285.7 ms for a Nostro fuzzy query compared with 814 ms for PostgreSQL 12.

## Decision

Use Redis 6+ as the proposed Day 1 cache middleware. Continue to persist cached static data in the database. Use Redis for the additional middleware use cases identified by the design:

- Distributed locks
- Duplicate checks
- `X-Token` user sessions
- API Gateway URL whitelist
- Static-data caching

Defer Hazelcast IMDG as a possible post-Day 1 improvement for NFRs.

## Consequences

### Benefits

- Reuses an existing RatanOne technology.
- Reduces initial adoption cost and implementation risk.
- Provides one middleware platform for caching and several coordination use cases.
- Preserves a database-backed recovery copy of static data.

### Risks and follow-up work

The decision does not establish a production Redis topology, persistence mode, eviction policy, security controls, monitoring, backup strategy, cross-site replication, failover behavior, RPO, RTO, or cache-staleness tolerance. The benchmark is not sufficient to prove production performance.

These items must be resolved before treating the proposal as an approved production architecture. See [[queries/what-is-the-production-redis-ha-dr-and-security-design-for-ratanone]] and [[queries/when-does-the-static-data-cache-decision-matrix-require-cache-db-or-golden-source-query]].

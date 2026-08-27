---
type: concept
title: Cached Rule Loading
created: 2026-08-24
updated: 2026-08-24
tags: [cache, redis, postgresql, rule-engine, consistency]
related: [cn-rule-service, ratan-rule-service-ratan-rule, what-is-the-authoritative-cn-rule-cache-consistency-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# Cached Rule Loading

Cached rule loading is the proposed practice of serving CN Rule Service rules from Redis rather than querying PostgreSQL during each evaluation.

## Archived proposal

The source recommends preserving PostgreSQL/Redis consistency and hiding alternate loading mechanisms behind a strategy-pattern abstraction. The intended benefit is lower rule-loading cost and future flexibility in rule-source selection.

However, the same note says that rule loading may not be the performance bottleneck. Special NSTP rules can call external services, so cache optimization does not by itself address latency dominated by remote dependency calls.

## Required but unspecified contract

The proposal does not specify:

- the system of record for mutable rules;
- write, publish, and cache-warming sequence;
- invalidation, TTL, refresh, or version checks;
- behavior when Redis is unavailable or stale;
- rollback and recovery semantics; or
- permitted stale-rule duration.

These omissions prevent the proposal from establishing a reliable cache-consistency design. See [[what-is-the-authoritative-cn-rule-cache-consistency-contract]].
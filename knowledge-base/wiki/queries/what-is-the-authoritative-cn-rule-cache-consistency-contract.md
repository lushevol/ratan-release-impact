---
type: query
title: What Is the Authoritative CN Rule Cache Consistency Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cn-rule-service, redis, postgresql, cache-consistency]
related: [cached-rule-loading, cn-rule-service, ratan-rule-service-ratan-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# What Is the Authoritative CN Rule Cache Consistency Contract?

The archived proposal requires PostgreSQL/Redis consistency if rules are loaded from Redis, but does not define the contract.

## Questions

- Which store is authoritative for rule reads and writes?
- How are rule changes versioned, validated, propagated, invalidated, and rolled back?
- What happens on cache miss, stale cache entry, cache publication failure, or Redis outage?
- What stale-rule window is acceptable for each rule type?
- How is cache warm-up completed and verified after deployment or recovery?

## Evidence needed

Current write-path design, cache configuration, refresh or invalidation implementation, operational runbooks, and tests for stale-data and outage recovery.
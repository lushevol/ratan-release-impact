---
type: query
title: What Is the Production Redis HA DR and Security Design for RatanOne?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, Redis, high-availability, disaster-recovery, security, operations]
related: [redis, hazelcast-imdg, redis-vs-hazelcast-for-ratanone-static-data, 001-adopt-redis-v6-for-day-1-static-data-cache, static-reference-data-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# What Is the Production Redis HA DR and Security Design for RatanOne?

## Question

What production Redis architecture and operating contract will support RatanOne static data and Redis-based middleware functions?

## Evidence

The source proposes Redis 6+ for Day 1 but provides no equivalent deployment design. Hazelcast is described with a six-node-per-site ARK and Watford topology, although it is deferred rather than selected.

## Required resolution

Specify:

- Cluster, Sentinel, or another topology
- ARK and Watford behavior and cross-site replication
- Persistence, backup, restore, and data-loss expectations
- Failover and split-brain handling
- Eviction, TTL, memory sizing, and cache warm-up
- Monitoring, alerting, and operational ownership
- TLS, authentication, authorization, and sensitive-data controls
- RPO, RTO, availability, and cache-staleness targets
- Separate treatment of locks, deduplication, sessions, whitelist data, and static reference data

The unofficial Redis 5 development benchmark cannot substitute for this production contract.

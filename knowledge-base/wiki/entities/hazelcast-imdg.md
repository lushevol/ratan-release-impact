---
type: entity
title: Hazelcast IMDG
created: 2026-08-24
updated: 2026-08-24
tags: [Hazelcast, IMDG, distributed-cache, high-availability, cash-settlement]
related: [redis, redis-vs-hazelcast-for-ratanone-static-data, 001-adopt-redis-v6-for-day-1-static-data-cache, what-is-the-production-redis-ha-dr-and-security-design-for-ratanone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# Hazelcast IMDG

## Role in the design

Hazelcast IMDG is presented as a possible post-Day 1 improvement for RatanOne system NFRs. It is not the selected Day 1 cache middleware; the source selects Redis 6+ instead.

The source describes Hazelcast as a distributed in-memory object store supporting maps, multimaps, atomic longs, queues, lists, and sets. Hazelcast Management Center is proposed for cluster monitoring and operational inspection.

## Proposed topology

The design proposes a Hazelcast cluster with instances on each of six production nodes in both ARK and Watford. The two sites are described as active-active, and the DR strategy is stated to be the same as the HA strategy.

The proposal does not define partition backups, WAN replication, split-brain prevention, cross-site consistency, failover behavior, RPO, RTO, or production sizing. Hazelcast should therefore be treated as a deferred option rather than an implementation commitment.

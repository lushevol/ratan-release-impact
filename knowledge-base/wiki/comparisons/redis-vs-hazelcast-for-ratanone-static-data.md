---
type: comparison
title: Redis vs Hazelcast for RatanOne Static Data
created: 2026-08-24
updated: 2026-08-24
tags: [Redis, Hazelcast, cache, architecture, cash-settlement]
related: [redis, hazelcast-imdg, database-first-static-data-caching, 001-adopt-redis-v6-for-day-1-static-data-cache, what-is-the-production-redis-ha-dr-and-security-design-for-ratanone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# Redis vs Hazelcast for RatanOne Static Data

| Dimension | Redis | Hazelcast IMDG |
| --- | --- | --- |
| Position in source | Proposed Day 1 choice | Deferred post-Day 1 improvement |
| Rationale | Existing RatanOne footprint; lower stated cost and risk | Potential improvement for system NFRs |
| Stated uses | Cache, locks, duplicate checks, sessions, API Gateway URL whitelist | Distributed in-memory data structures and caching |
| Deployment detail | Version 6+ is proposed, but topology and operations are unspecified | Six production nodes in each of ARK and Watford are proposed |
| High availability | Not specified | ARK and Watford are described as active-active |
| Monitoring | Not specified | Hazelcast Management Center is proposed |
| Persistence authority | Database remains the intended persistent store | Database remains the intended persistent store |
| Production readiness evidence | One unofficial development benchmark using Redis 5 | No production benchmark or sizing evidence |

## Conclusion

The source makes Redis the practical Day 1 direction but does not provide enough evidence to conclude that either platform satisfies production HA, DR, security, capacity, consistency, or recovery requirements. Hazelcast should not be represented as deployed merely because its topology is described in more detail.

The decision and its consequences are recorded in [[001-adopt-redis-v6-for-day-1-static-data-cache]]. The missing Redis production contract is tracked in [[queries/what-is-the-production-redis-ha-dr-and-security-design-for-ratanone]].

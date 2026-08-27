---
type: entity
title: Redis
created: 2026-08-24
updated: 2026-08-25
tags: [redis, api-gateway, route-management, pub-sub, distributed-locking, infrastructure, cash-settlement, cache, middleware, distributed-systems, disaster-recovery, ratan, datastore, high-availability]
related: [api-gateway, dynamic-openapi-routing, batch-distributed-locking, cashflow-release-and-netting-race-condition, lifecycle-batch-status-update-api, database-first-static-data-caching, static-reference-data-synchronization, redis-vs-hazelcast-for-ratanone-static-data, 001-adopt-redis-v6-for-day-1-static-data-cache, what-is-the-production-redis-ha-dr-and-security-design-for-ratanone, redisson, atomic-batch-locking, watchdog-lock-renewal, ratan-distributed-lock-ownership, redis-redisson-vs-zookeeper-vs-relational-db-locking, ratan-ktlo-tracker, ratan-disaster-recovery-automation, ratan, wat, ark, redis-and-vip-failover, ratan-disaster-recovery-failover]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md", "RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md", "RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---

# Redis

Redis is used in the Cash Settlement architecture for API Gateway route management and distributed locking. It is also proposed as cache middleware for RatanOne static data and as an infrastructure foundation for RATAN distributed locking.

The RATAN DR Plan separately identifies Redis as a critical RATAN failover dependency. The RATAN KTLO tracker also identifies Redis as a data-store or infrastructure dependency that can create processing risk during an outage.

## API Gateway route definitions

According to the **API Gateway Feature Upgrade** source, Redis provides storage and distribution for API Gateway route definitions:

- `RedisOpenApiRepository` reads OpenAPI configuration from Redis.
- `RedisPubSubOpenApiRefresher` distributes route-refresh events across Kubernetes deployments.

Redis therefore supports both dynamic route persistence and multi-instance route synchronization. The Cache Data Layer Design also lists URL whitelist storage for [[api-gateway]] as a proposed Redis use case.

## Cash Settlement distributed locking

According to the **Batch Status Update API Tuning** source, Redis is the distributed-lock storage used by Cash Settlement processing. Redis read and write operations for individual cashflow locks are identified as a performance bottleneck in batch status updates.

The proposed optimizations are:

- List-level lock acquisition.
- Concurrent lock acquisition using `CompletableFuture` or `CyclicBarrier`.
- Lua-script execution for coordinated key setting.

Redis lock atomicity must be distinguished from the atomicity of the database update and downstream side effects. See [[batch-distributed-locking]] and [[cashflow-batch-transaction-atomicity]].

## RATAN distributed-lock redesign

According to the **RATAN Distributed Lock ReDesign** source, Redis is the proposed infrastructure foundation for RATAN distributed locking. The source describes Redis as supporting:

- Lock expiry.
- Lock extension.
- Atomic Lua-script operations.
- Lock notifications.
- Integration through [[redisson]].

The redesign uses resource keys such as cashflow IDs and trade IDs. It requires application-level ownership and validation rules because Redis alone does not resolve cross-service ownership transfer.

For this RATAN distributed-lock use case, the redesign source prefers Redis over relational-database locks and Zookeeper/Curator because Redis provides lock expiry, extension, multi-lock support, and an active ecosystem. This comparison is specific to the redesign source and should not be generalized to every locking use case.

The same source does not define the required Redis topology, failover model, persistence settings, or consistency guarantees for the RATAN locking use case.

## Proposed RatanOne cache middleware role

According to the **Cache Data Layer Design**, Redis is proposed as the Day 1 cache middleware for RatanOne static data. The proposed version is Redis 6+ because Redis is already used in the system and is considered lower risk and lower cost than introducing Hazelcast immediately.

The source lists these proposed Redis use cases:

- Static-data caching.
- Distributed locks.
- Duplicate checks.
- User sessions using `X-Token`.
- URL whitelist storage for [[api-gateway]].

The source does not establish whether Redis 6+ was formally approved or deployed.

## Static-data architectural position

According to the **Cache Data Layer Design**, Redis is a cache and middleware component rather than the authoritative persistent store for static data. The design states that static data should be stored in the database first and kept updated when a cache is used.

## RATAN DR failover dependency

According to the **RATAN DR Plan**, Redis is a critical RATAN failover dependency. The DR plan requires the Redis master role to be:

- On ARK during a WAT→ARK failover.
- On WAT during an ARK→WAT failover.

The source references the Rundeck `Redis_slave_tkeover` job. It also describes a manual or job-based recovery path for cases where the Redis master does not roll after service-stop actions.

The DR Plan contains a plaintext Redis credential in a CLI example. That credential is intentionally excluded from this page.

These master-placement and recovery details come from the RATAN DR Plan and are separate from the proposed cache and distributed-locking designs described above.

## Production design gaps

The **Cache Data Layer Design** leaves the following production concerns unspecified:

- Topology.
- Persistence.
- Eviction.
- Authentication.
- Authorization.
- Encryption.
- Backup.
- Monitoring.
- Failover.
- Cross-data-center behavior.

These gaps are tracked in [[what-is-the-production-redis-ha-dr-and-security-design-for-ratanone]].

Separately, the **RATAN Distributed Lock ReDesign** source does not define the Redis topology, failover model, persistence settings, or consistency guarantees required for the RATAN locking use case.

The RATAN DR Plan supplies specific master-placement and recovery procedures, but it does not, in the claims summarized here, define all of the broader production cache and locking concerns listed above.

## Disaster-recovery and outage context

According to the **RATAN KTLO Tracker**, STORY 6832041 requests automatic handling of Redis outages to avoid processing impact. The issue is linked to a problem encountered during disaster recovery and is expected to be addressed before the next DR exercise.

The tracker does not specify:

- Redis topology.
- Dependency boundaries.
- Outage-detection mechanism.
- Fallback behavior.
- Recovery-time objective.
- Data-consistency controls.

This disaster-recovery context comes from the RATAN KTLO Tracker and is separate from both the proposed cache and locking designs and the specific failover procedures in the RATAN DR Plan. See [[ratan-disaster-recovery-automation]] and [[ratan-ktlo-tracker]].
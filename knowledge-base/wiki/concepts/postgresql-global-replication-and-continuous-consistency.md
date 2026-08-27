---
type: concept
title: PostgreSQL Global Replication and Continuous Consistency
tags: [postgresql, replication, high-availability, disaster-recovery, consistency]
related: [postgresql, cash-settlement-platform, kafka-dual-cluster-disaster-recovery, minio-cross-site-disaster-recovery, cash-settlement-data-store-requirements, what-is-the-approved-postgresql-replication-and-failover-topology]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# PostgreSQL Global Replication and Continuous Consistency

The Cash Settlement datastore requirements identify global replication, high availability, and real-time continuous consistency as PostgreSQL must-haves.

The requirements state that writes to one instance must propagate automatically to others and that disaster recovery should be transparent, with database-operation failure not accepted. These statements express desired outcomes, not an approved topology.

Replication approaches make different trade-offs:

- Synchronous single-primary replication can reduce acknowledged-write loss but may increase write latency and lose write availability when quorum is unavailable.
- Asynchronous replication can preserve lower write latency and remote availability but permits replication lag and non-zero data loss on failover.
- Multi-primary or active-active designs introduce conflict resolution, routing, and operational complexity.

The source does not define RPO, RTO, maximum replication lag, synchronous-commit policy, cluster locations, quorum, split-brain prevention, failover authority, or network-partition behavior. Guarantees described for [[kafka-dual-cluster-disaster-recovery]] or [[minio-cross-site-disaster-recovery]] must not be assumed to apply to PostgreSQL.
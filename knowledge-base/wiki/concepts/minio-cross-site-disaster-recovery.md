---
type: concept
title: MinIO Cross-Site Disaster Recovery
created: 2026-08-24
updated: 2026-08-24
tags: [minio, disaster-recovery, replication, rpo, rto]
related: [minio, cash-settlement-dc-failover-strategy, controlled-dc-switchover, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# MinIO Cross-Site Disaster Recovery

MinIO cross-site disaster recovery replicates bucket data asynchronously between a primary cluster and a DR cluster. The proposal suggests a four-node Distributed Mode cluster, replication lag below 30 seconds, alerting at five minutes, and object versioning to help recover accidental deletion.

The source assigns distinct guarantees to different failure scopes: local node failure is proposed as RPO 0 and RTO under one minute, while full-site failure has proposed RPO below 30 seconds and RTO under 15 minutes. Local high availability must not be presented as a zero-loss cross-site guarantee.

The source's Shanghai/Beijing example requires explicit approval if intended for Indonesia data. Failover orchestration, replication direction, DNS/VIP cutover, database alignment, and recovery testing are not specified.
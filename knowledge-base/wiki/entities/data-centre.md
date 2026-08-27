---
type: entity
title: Data Centre
created: 2026-08-24
updated: 2026-08-24
tags: [infrastructure, data-centre, disaster-recovery, indonesia]
related: [cash-settlement-platform, cluster, cash-settlement-dc-failover-strategy, controlled-dc-switchover]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Data Centre

The Indonesia architecture note considers a primary and backup data centre for the Cash Settlement Platform.

In Option-1, applications connect to only one data centre at a time. A switchover requires stopping and verifying the primary services, switching VIPs, and starting and verifying the backup services.

In Option-2, the two data centres are described as totally isolated. The source does not explain how deployment coordination, data replication, monitoring, rollback, or message ownership operate across that isolation boundary.

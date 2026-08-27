---
type: concept
title: Controlled Data-Centre Switchover
created: 2026-08-24
updated: 2026-08-24
tags: [failover, data-centre, active-passive, operations, virtual-ip]
related: [cash-settlement-dc-failover-strategy, virtual-ip, data-centre]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Controlled Data-Centre Switchover

A controlled data-centre switchover is an ordered transition from a primary site to a backup site intended to prevent simultaneous processing.

The procedure specified for Option-1 is:

1. Stop primary-data-centre applications.
2. Confirm that all primary-data-centre services are down.
3. Switch VIPs.
4. Start backup-data-centre applications.
5. Confirm that all backup-data-centre services are up.

The shutdown verification step is the stated guard against both sites being active at the same time. The source does not state whether this process is automated, regularly tested, monitored, or auditable, and it provides no RTO, RPO, or data-consistency evidence.

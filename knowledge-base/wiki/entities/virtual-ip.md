---
type: entity
title: Virtual IP
created: 2026-08-24
updated: 2026-08-24
tags: [networking, virtual-ip, failover, infrastructure]
related: [cash-settlement-platform, cash-settlement-dc-failover-strategy, controlled-dc-switchover]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Virtual IP

A Virtual IP (VIP) is the movable infrastructure endpoint used by Option-1 of the Indonesia Cash Settlement Platform architecture.

The design states that six servers in each cluster require six VIPs. During a controlled data-centre switchover, the primary applications are stopped and verified as down before the VIPs are switched to the backup data centre.

The source presents VIP switching as transparent to domain applications. It does not specify VIP ownership, routing protocols, health checks, network failover automation, or the behavior of stateful dependencies.

---
type: concept
title: Cash Settlement Data-Centre Failover Strategy
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, failover, active-passive, active-active, disaster-recovery]
related: [cash-settlement-platform, virtual-ip, controlled-dc-switchover, message-racing-prevention-in-dual-dc-deployments, cluster]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Cash Settlement Data-Centre Failover Strategy

Cash Settlement data-centre failover strategy is the choice of how services are deployed and switched between two data centres.

## Strategy Patterns

### One-Profile VIP-Based Active-Passive

The first pattern uses one deployment profile and VIPs. Only one data centre is available to applications at a time. The primary site is stopped and verified before VIPs are moved and the backup site is started.

This provides an explicit Active-Passive model and limits configuration maintenance, but depends on six VIPs per cluster and an ordered manual switchover.

### Two-Profile Isolated Clusters

The second pattern uses two independently maintained profiles for two isolated clusters. It removes the need for additional VIPs and isolates the data centres, but increases deployment and configuration-management complexity.

The source warns that the design could become Active-Active and cause message racing unless MB startup is manually restricted.

## Design Boundary

VIP movement establishes an endpoint transition; it does not by itself establish safe transfer of stateful processing. A complete strategy also requires decisions about message ownership, fencing, state replication, duplicate handling, monitoring, recovery objectives, and failover testing.

The source compares alternatives but does not select an approved strategy. Related operational controls include [[cashflow-event-control]] and [[cashflow-batch-control]], although this source does not confirm their deployment in Indonesia.

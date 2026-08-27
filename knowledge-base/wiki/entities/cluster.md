---
type: entity
title: Cluster
created: 2026-08-24
updated: 2026-08-24
tags: [infrastructure, deployment, cluster, data-centre]
related: [cash-settlement-platform, data-centre, cash-settlement-dc-failover-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Cluster

A cluster is the deployment unit used by both architecture options for the Indonesia Cash Settlement Platform. The source implies two clusters, associated with two data centres.

Option-1 uses one deployment profile and VIPs to switch service connectivity between clusters. Option-2 uses two independently maintained profiles and keeps the data centres isolated.

The source does not define cluster membership, service placement, shared state, replication, or the relationship between a cluster and the six servers mentioned in Option-1.

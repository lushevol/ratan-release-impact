---
type: query
title: What Is the Approved PostgreSQL Replication and Failover Topology?
tags: [postgresql, replication, failover, rpo, rto, cash-settlement]
related: [postgresql, cash-settlement-platform, postgresql-global-replication-and-continuous-consistency, kafka-dual-cluster-disaster-recovery, minio-cross-site-disaster-recovery, cash-settlement-data-store-requirements]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# What Is the Approved PostgreSQL Replication and Failover Topology?

The source requires automatic write propagation, transparent disaster recovery, and real-time synchronization, but does not select a PostgreSQL topology.

## Questions to Resolve

- Is the topology single-primary with replicas, multi-primary, or active/passive by region?
- How many instances exist, where are they located, and which instance accepts writes?
- What are the target RPO, RTO, maximum replication lag, and failover duration?
- Which writes require synchronous acknowledgment, and what happens when synchronous replicas are unavailable?
- How are quorum, fencing, split-brain prevention, network partitions, and failback handled?
- What measurable availability standard replaces the absolute statement that database-operation failure is not accepted?

## Evidence

[[cash-settlement-data-store-requirements]] defines the requirements but no implementation. Related resilience designs for Kafka and MinIO provide context only; they do not establish PostgreSQL guarantees.
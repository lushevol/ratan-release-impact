---
type: concept
title: Kafka Dual-Cluster Disaster Recovery
tags: [kafka, disaster-recovery, active-passive, replication, failover]
related: [cash-settlement-platform, kafka, cash-settlement-dc-failover-strategy, application-level-dual-write, can-dual-write-prove-zero-rpo-for-cash-settlement, what-is-the-kafka-consumer-offset-and-failback-policy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Kafka Dual-Cluster Disaster Recovery

Kafka dual-cluster disaster recovery uses separate Kafka clusters in active and passive data centres rather than one cluster shared across both sites. It supports the Indonesia Cash Settlement Platform's proposed Active-Passive topology.

The required operational scope is broader than topic replication. A working design must coordinate topics, partitions, ACLs, consumer-group state, offsets, routing, producer and consumer promotion, reverse replication, reconciliation, and controlled failback.

## Available approaches

The source evaluates asynchronous replication through MM2 or Confluent Cluster Linking / Replicator, application-level dual-write, and object-store log shipping.

Asynchronous replication lowers application-change requirements but retains exposure to replication lag and thus does not establish zero RPO. Dual-write removes dependency on replication lag but introduces producer-side consistency and idempotence requirements. Object-store restoration favors retention and replay over real-time recovery.

## Acceptance requirements

The stated requirements are automated RTO of no more than two hours and RPO of zero minutes. These are targets, not demonstrated guarantees in the source.

A DR design should specify:

- Failure scenarios and corresponding recovery behavior.
- Cluster readiness and promotion health criteria.
- DNS, Virtual IP, or endpoint-routing automation.
- Consumer-group offset policy at promotion and failback.
- Duplicate, gap, and ordering detection.
- Reconciliation and audit evidence.
- Measured DR-drill acceptance criteria.

See [[what-is-the-kafka-consumer-offset-and-failback-policy]] for the unresolved consumer-state model.
---
type: query
title: What Is the Kafka Consumer Offset and Failback Policy?
tags: [kafka, consumer-offsets, failover, failback, disaster-recovery]
related: [kafka-dual-cluster-disaster-recovery, kafka, cash-settlement-platform, application-level-dual-write]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# What Is the Kafka Consumer Offset and Failback Policy?

The source identifies consumer offsets and failback coordination as essential concerns for MM2 and Confluent replication, but it does not prescribe a canonical policy.

## Questions to resolve

- How are consumer-group offsets synchronized or reconstructed at passive-site promotion?
- Which cluster and consumer group are authoritative during failover?
- How are duplicates and skipped records detected and remediated?
- Does the policy vary by topic, consumer group, or cashflow-processing criticality?
- How is reverse replication performed before failback?
- What fencing prevents active and passive consumers from processing the same business event concurrently?
- What audit evidence proves consumer state is safe after a DR drill?

## Required outcome

Define a tested promotion and failback runbook with consumer-group ownership, offset handling, replay boundaries, idempotence expectations, reconciliation, and success criteria.
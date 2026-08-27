---
type: query
title: Does FM Solace Meet Indonesia Cash Settlement RTO and RPO?
tags: [solace, disaster-recovery, rto, rpo, indonesia]
related: [solace, kafka-to-solace-semantic-migration, cash-settlement-dc-failover-strategy, cash-settlement-platform]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Does FM Solace Meet Indonesia Cash Settlement RTO and RPO?

The source initially assumes that FM Solace fulfils the required RTO of two hours and RPO of zero minutes, but later explicitly states that the team does not know whether FM Solace meets those requirements.

## Evidence required

- Contractual or platform-supported RTO and RPO for full data-centre loss.
- Primary, backup, replication, and failover topology.
- Endpoint, DNS, or VIP failover mechanism and automation criteria.
- Message persistence, replication, replay, ACK, redelivery, and duplicate-delivery guarantees.
- Partition-key ordering behavior under the intended queue and consumer-flow topology.
- Queue and topic provisioning process, lead time, and change ownership.
- DR drill evidence demonstrating recovery within the required objectives.
- Support and troubleshooting operating model for the Cash Settlement application team.

## Decision impact

A Solace migration should not be treated as a compliant replacement for Kafka until this evidence is available and Kafka-specific retry, CQRS, ordering, replay, and idempotence requirements have a validated equivalent.
---
type: concept
title: Kafka to Solace Semantic Migration
tags: [kafka, solace, migration, messaging, ordering, replay]
related: [kafka, solace, cash-settlement-platform, non-blocking-message-retry, does-fm-solace-meet-indonesia-cash-settlement-rto-rpo]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Kafka to Solace Semantic Migration

Migrating the Cash Settlement Platform from Kafka to Solace is not an endpoint-only replacement. The source identifies material differences in delivery, ordering, replay, retry, scaling, provisioning, and transaction semantics.

## Compatibility areas

- **Ordering:** Kafka orders records within a partition. Solace ordering depends on queue, consumer-flow, competing-consumer, and partition-key configuration.
- **Key routing:** Kafka maps keys to partitions. Solace requires an explicit topic, queue-binding, selector, or key-group mapping.
- **Replay:** Kafka uses retained logs and consumer offsets; Solace replay is broker-managed and platform-configuration dependent.
- **Consumer state:** Kafka consumers pull and manage offsets. Solace clients receive push delivery and manage acknowledgements and redelivery behavior.
- **Delivery semantics:** Kafka idempotent producers and transactions do not directly map to Solace; applications require idempotence controls.
- **Scaling:** Kafka uses partitions and consumer-group members. Solace uses queue consumers, subscriptions, and flow control.
- **Retries:** Spring Kafka non-blocking retry depends on topics, offsets, and seek. Solace requires an application or platform equivalent.

## Platform and application constraints

The source reports customized `KafkaListenerContainerFactory` use, Spring Kafka retry topologies, auto topic creation, self-managed partitioning, and a Kafka-dependent `ratanone-cqrs-spring-boot-starter`. It also reports that Solace topic and queue provisioning is controlled by another team.

Solace can be viable if the enterprise mandates it and the platform team provides DR operations, automation, operational visibility, provisioning flexibility, and validated functional equivalents. The source does not establish that FM Solace meets the Indonesia RTO/RPO requirements. See [[does-fm-solace-meet-indonesia-cash-settlement-rto-rpo]].
---
type: concept
title: Solace-to-Kafka Fan-In
created: 2026-08-24
updated: 2026-08-24
tags: [solace, kafka, fan-in, concurrency, message-bridge]
related: [message-bridge, lazy-kafka-endpoint-initialization-race, message-bridge-deduplication-key-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# Solace-to-Kafka Fan-In

Solace-to-Kafka fan-in is a topology in which multiple Solace consumer routes publish to one shared Kafka destination.

In the Message Bridge incident, Uber message intake changed from one Solace queue feeding one Kafka target to eight queues, partitioned by primary asset class, feeding a shared target. This increases the likelihood that several routes perform their first downstream send simultaneously.

Fan-in does not by itself prove a failure. In this incident, it is a contributing condition for the hypothesized Apache Camel lazy-startup race in which concurrent threads use a shared `KafkaEndpoint` before its `KafkaProducer` is completely initialized.

The source provides no performance measurement or controlled test establishing a specific consumer-count threshold. Claims concerning failure certainty above ten consumers remain unverified.

See [[lazy-kafka-endpoint-initialization-race]].
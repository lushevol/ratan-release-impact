---
type: source
title: Message Middleware DR Solution
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [cash-settlement, indonesia, disaster-recovery, kafka, solace, active-passive]
related: [cash-settlement-platform, kafka, solace, cash-settlement-dc-failover-strategy, kafka-dual-cluster-disaster-recovery, application-level-dual-write, kafka-to-solace-semantic-migration, non-blocking-message-retry, can-dual-write-prove-zero-rpo-for-cash-settlement, does-fm-solace-meet-indonesia-cash-settlement-rto-rpo, what-is-the-kafka-consumer-offset-and-failback-policy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Message Middleware DR Solution

## Summary

This internal technical proposal evaluates message-middleware disaster-recovery options for the Indonesia Cash Settlement Platform as its deployment model changes from Active-Active to Active-Passive across two data centres.

The stated targets are an automated recovery time objective (RTO) of no more than two hours and a recovery point objective (RPO) of zero minutes. The document recommends application-level Kafka dual-write when zero data loss is mandatory and producer changes are allowed. It considers Confluent Cluster Linking / Replicator and Kafka MirrorMaker 2 (MM2) viable alternatives with non-zero RPO due to asynchronous replication lag. It considers a migration to [[solace]] viable only when the enterprise platform team owns DR and can satisfy material compatibility and operating-model requirements.

This is a proposal, not an approved architecture decision. Neither zero RPO nor the automated RTO target is demonstrated through tested failure scenarios or measured recovery evidence.

## Background and target topology

The current deployment runs applications Active-Active across two data centres against one shared Kafka cluster. The proposed model runs the application Active-Passive, with a Kafka cluster in each data centre. This introduces synchronization and operational requirements for topics, partitions, offsets, ACLs, consumer state, failover, and failback.

The proposal relates to [[cash-settlement-dc-failover-strategy]] and extends the middleware implications of the existing Active-Passive platform architecture.

## Objectives

- **RTO:** Within 2 hours (automated).
- **RPO:** 0 minutes for Active-Passive deployments.

The document defines RTO as the maximum acceptable service-restoration time after failure and RPO as the maximum acceptable data loss measured in time.

## Kafka dual-cluster options

| Option | RPO | RTO | Cost | Complexity | Operational Maturity |
| --- | --- | --- | --- | --- | --- |
| MM2 | Low-Medium (non-zero) | Medium | Low | Medium | Medium |
| Confluent Linking/Replicator | Low (non-zero) | Low-Medium | High | Medium | High |
| Dual-Write | Near-Zero to Zero | Low | Medium | High | High |
| Log Shipping | High | High | Low | Low-Medium | Low |
| Solace (Replace Kafka) | Low (platform-dependent) | Low-Medium | High | High | High |

### Kafka MirrorMaker 2

MM2 is described as Kafka Connect-based replication from the active cluster to the passive cluster, with optional offset and ACL synchronization. It is compatible with open-source Kafka stacks and supports flexible topic selection and renaming.

Its limitations are eventual consistency, potentially non-zero replication lag, Kafka Connect operational overhead, and the need for consumer-offset coordination during failback.

### Confluent Cluster Linking / Replicator

Confluent replication is described as an enterprise option with managed replication features, monitoring, and lower operational friction. It may provide lower lag and cleaner offset handling, particularly through Cluster Linking.

The source still classifies its RPO as non-zero, and identifies licensing cost and Confluent platform dependency as constraints.

### Application dual-write

Under this option, producers write every message to both Kafka clusters while consumers read only from the active cluster. The source recommends this option when a zero-minute RPO is required and producer changes are permitted.

The recommendation is conditional. Producers need partial-write handling, retries, idempotence, audit trails, metrics, and extensive failure testing. Dual-write alone does not prove literal zero RPO without a durable protocol for ambiguous acknowledgements, producer failures between writes, reconciliation, and duplicate prevention. See [[application-level-dual-write]] and [[can-dual-write-prove-zero-rpo-for-cash-settlement]].

### Object-store log shipping

The source describes object-store shipping through S3 or MinIO as appropriate for retention, audit, and replay. It is not considered suitable for real-time failover because restoring the passive Kafka cluster increases both RTO and RPO.

## Solace replacement assessment

The source assesses replacing Kafka with [[solace]] PubSub+. In this approach, Kafka is removed from the application path and clients migrate from Spring Kafka to Spring Cloud Stream Solace binder, Solace JMS, or JCSMP. Broker HA/DR, replication, and failover would be operated by the Solace platform team; applications would primarily reroute endpoints or DNS.

The document identifies the following non-equivalences with Kafka:

- Kafka partition ordering differs from Solace queue and flow ordering.
- Kafka key-to-partition routing must be explicitly modeled through Solace topic hierarchy, queue bindings, selectors, or a key-mapping strategy.
- Kafka retained-log and consumer-offset replay differ from Solace broker-managed replay.
- Kafka pull consumers and offset management differ from Solace push delivery, ACKs, and redelivery.
- Kafka idempotent producers and transactions do not map directly to Solace; applications normally provide idempotence.
- Kafka partition-based scaling differs from Solace queue-consumer and flow-control scaling.
- Spring Kafka non-blocking retry based on topics, offsets, and seek has no native Solace equivalent.

The source notes that current applications use customized `KafkaListenerContainerFactory` behavior, Spring Kafka retry patterns, auto topic creation, self-managed partitioning, and `ratanone-cqrs-spring-boot-starter`. Solace queue and topic provisioning is controlled by another team and requires a request process.

The source both assumes that FM Solace could fulfil the RTO/RPO requirement and later states that the team does not know whether FM Solace meets it. Formal platform commitments and DR-test evidence are required. See [[kafka-to-solace-semantic-migration]] and [[does-fm-solace-meet-indonesia-cash-settlement-rto-rpo]].

## Current retry-dependent topics

| # | Topic Name | Retry / DLT Topics | Described usage |
| --- | --- | --- | --- |
| 1 | `Cash_Settlement_Group_Message_Inbound` | `Cash_Settlement_Group_Message_Inbound-retry-0/1/2/3/dlt` | Standardization service consumes cashflow SCBML inbound from TDS3 and [[mxg-adaptor]]. |
| 2 | `TDS3_Trade_Message_Process_In` | `TDS3_Trade_Message_Process_In-retry-0/1/2/3/4/dlt` | Stella trade messages inbound from TDS3. |
| 3 | `TDS3_Trade_Murex_Message_Process_In` | `TDS3_Trade_Murex_Message_Process_In-retry-0/1/2/3/4/dlt` | Murex trade messages inbound from TDS3. |
| 4 | `cash_settlement_cashflow_domain_events` | `cash_settlement_cashflow_domain_events-retry-0/1/2/3/dlt` and `cash_settlement_cashflow_domain_events-retry-5000/10000/20000/dlt` | Lifecycle domain events consumed by standardization, accounting, OpenSearch agent, netting, FX utilization, LMS, and query services. Retry topics are used by query service and OpenSearch agent. |

```java
@RetryableTopic(attempts = "${ratanone.topic.upstream-inbound.attempts:5}", 
				backoff = @Backoff(delay = 15000, multiplier = 2.0), 
				topicSuffixingStrategy = TopicSuffixingStrategy.SUFFIX_WITH_INDEX_VALUE, 
				numPartitions = "${ratanone.topic.upstream-inbound.retry-partition:3}", 
				concurrency = "${ratanone.topic.upstream-inbound.consumer-concurrency:3}")
@KafkaListener(topics = "${ratanone.topic.upstream-inbound.topic}", batch = "false", filter = "cashflowInboundFilter", errorHandler = "consumerErrorHandler", concurrency = "${ratanone.topic.upstream-inbound.consumer-concurrency:3}")
public void handleMessage(ConsumerRecord<String, String> record) {
    //process ConsumerRecord from main topic and retry topics
}

@DltHandler
public void handleDlt(ConsumerRecord<String, String> record) {
	//handle dead letter 
}
```

## CQRS dependency

The document states that `ratanone-cqrs-spring-boot-starter` is a hard Kafka dependency for asynchronous CQRS domain-event publication. It also says that the starter abstracts the underlying middleware for producers and consumers, which creates an unresolved question: whether a Solace transport can be added without changing Kafka-specific APIs, retry behavior, storage, or transactional assumptions.

## Proposed migration sequence

1. Stand up the passive Kafka cluster and validate baseline health.
2. Select and configure a synchronization approach.
3. Run shadow consumers to validate data parity.
4. Run DR drills and measure RPO and RTO.
5. Perform a controlled failover test.

## Open implementation questions

- What failure modes must satisfy RPO = 0, including producer crash, network partition, and full data-centre loss?
- What durable outbox, retry ledger, or reconciliation process closes dual-write partial-failure gaps?
- What is the consumer-offset promotion, reverse-replication, and failback policy?
- Which routing and health mechanisms automate passive-site promotion within two hours?
- Can FM Solace contractually meet the required targets for Indonesia?
- Can `ratanone-cqrs-spring-boot-starter` support a non-Kafka transport while retaining existing guarantees?
- What Solace queue topology preserves partition-key ordering and the seven consumer groups for `cash_settlement_cashflow_domain_events`?
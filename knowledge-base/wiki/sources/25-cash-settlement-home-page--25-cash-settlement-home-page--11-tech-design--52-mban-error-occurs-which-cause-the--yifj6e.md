---
type: source
title: "MB Uber Message Loss: Kafka workerPool Race and Redis Deduplication Failure"
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, solace, kafka, redis, incident-analysis, message-loss]
related: [message-bridge, ratan-bridge-fail-message, solace-to-kafka-fan-in, message-bridge-deduplication-key-lifecycle, lazy-kafka-endpoint-initialization-race, retry-and-failure-persistence-semantics, what-is-the-message-bridge-authoritative-retry-and-terminal-failure-contract, how-should-message-bridge-clean-up-source-and-target-deduplication-keys-on-failure, is-message-bridge-kafka-endpoint-lazy-initialization-safe-under-parallel-solace-consumption, does-group-service-refer-to-group-management-in-message-bridge-incident-analysis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Tech Design"
---
# MB Uber Message Loss: Kafka workerPool Race and Redis Deduplication Failure

This incident analysis describes message loss in `fmrp2` after Uber messages were changed from one Solace queue to eight queues partitioned by primary asset class. Multiple Solace consumer routes then published to a shared Kafka destination.

The document identifies a two-stage causal chain:

1. Concurrent first sends to a lazily initialized Apache Camel Kafka endpoint can fail with `workerPool must be specified`.
2. A failed delivery leaves its source Redis deduplication key active. When Solace redelivers within the 120-second TTL, Message Bridge filters the valid recovery attempt as a duplicate.

The document has an incomplete Solution section and does not establish that a remediation was approved, deployed, or validated.

## Incident evidence

| Environment | Trade ID | Trace ID | Reported outcome |
|---|---|---|---|
| `fmrp2` | `7153422395` | `16a6f26acc4f17d39e9cf45454113ba0` | Reported as lost |
| `fmrp2` | `7153422382` | `7a756a7f83018dda1316ec41bcc9c661` | Reported as lost; used for Redis timeline |
| `fmrp1` | `8009318839` | `b9c77c3e52eecdfa0449b464feadbde1` | Reconsumed after more than two minutes and sent downstream |

The immediate failure occurred in `MessageProducerImpl.sendBody()` while sending to `tdsx_uber_message_json_inbound`:

```text
om.scb.ratan.messagebridge.exception.MessageBridgeSolaceConsumeException:
Solce route sends exchange to endpoint:
kafka:tdsx_uber_message_json_inbound?valueSerializer=com.scb.ratan.messagebridge.serial.TDSXUberToJsonSerializer&brokers=10.198.24.247:9092,10.198.24.249:9092,10.198.24.251:9092&reconnectBackoffMs=10000&retries=10&retryBackoffMs=1000&bufferMemorySize=67108864&compressionCodec=lz4&maxRequestSize=20971520
failed with exception: workerPool must be specified
at com.scb.ratan.messagebridge.route.producer.MessageProducerImpl.sendBody(MessageProducerImpl.java:111)
```

## Topology and concurrency hypothesis

The documented topology changed from one Solace route per Kafka target to multiple Solace routes sharing one target:

```text
Old configuration:

Solace-Consumer-Route-uber-flow-A ──→ kafka:topicX

New configuration:

Solace-Consumer-Route-uber-flow-1 ──┐
Solace-Consumer-Route-uber-flow-2 ──┤
Solace-Consumer-Route-uber-flow-3 ──┤─→ kafka:topicX
...                                 ┤
Solace-Consumer-Route-uber-flow-N ──┘
```

The source attributes the failure to simultaneous use of a shared, lazily created `KafkaEndpoint`: one thread begins `doStart()` and initializes `workerPool`, while other threads invoke `KafkaProducer.process()` before initialization finishes.

`TargetSplittingRoute` further increases concurrent work:

```java
TargetSplittingRoute.selfConfigure()

.split().method(splitter)
.parallelProcessing()
.to(MessageBridgeConstants.DIRECT_SUPPRESSION_ROUTE)
```

This is a technically plausible explanation tied to the observed exception, but the source provides neither an Apache Camel version nor a reproducible concurrency test, thread dump, or lifecycle trace. The suggested threshold that more than ten consumers makes the issue nearly certain is not supported by measured evidence.

See [[solace-to-kafka-fan-in]] and [[lazy-kafka-endpoint-initialization-race]].

## Deduplication failure mechanism

The source provides strong evidence that stale source-side Redis state converts a transient send failure into a suppressed redelivery.

```java
// TargetSplittingRoute.process()
exchange.setProperty(
    DUPLICATION_CHECK_KEY,
    "ratanone:mb:dc:s:Solace-Consumer-Route-uber-flow-10-..."
);

// DispatchProducerRoute.process()
exchange.setProperty(
    DUPLICATION_CHECK_KEY,
    "ratanone:mb:dc:s:kafka:tdsx_uber_message_json_inbound?..."
);

// DispatchProducerRoute try-catch
DuplicationCheckHelper.removeDuplicationKey(exchange);
```

Because `DispatchProducerRoute` overwrites `DUPLICATION_CHECK_KEY`, cleanup reads and removes only the target Kafka key. The original Solace source key is not removable through that path.

| Time | Observed state |
|---|---|
| `09:51:12.922` | A source Redis key is written with `is_duplicated = false` and TTL `120s`. |
| `09:51:13–09:51:18` | `workerPool` failures occur during Kafka sending; target-key cleanup runs. |
| `09:52:34.696` | Solace redelivers the same message after about 82 seconds. The source key remains active, `is_duplicated = true`, and MB filters the message. |

The durable-loss mechanism is therefore not the transient Kafka startup error alone. It is failure to clear the source deduplication identity after an unsuccessful delivery.

See [[message-bridge-deduplication-key-lifecycle]].

## Failure persistence and retries

The expected terminal-failure path is documented as:

```text
sendBody() exception
→ DispatchProducerRoute.onException (6 retries)
→ DIRECT_EXCEPTION_ROUTE
→ ExceptionProducerRoute.process()
→ DIRECT_RAW_MESSAGE_PERSISTENCE_ROUTE
→ RawMessagePersistenceProducerRoute.saveRawMessage()
→ write ratan_bridge_fail_message
```

The source reports no `ExceptionProducerRoute` log such as “Processing occurs exception for target” and infers that retries remained active, so terminal failure persistence did not occur. This inference is plausible but not conclusive: absent logs do not prove that the route was not invoked.

The retry model is ambiguous. The route is said to perform six retries, while the Kafka endpoint configuration contains `retries=10`. It is not established whether these are separate layers, how their backoff interacts, or which failure condition invokes `ExceptionProducerRoute`.

The narrative also alternates between a `raw_message` table and `ratan_bridge_fail_message`; their relationship is not defined.

See [[retry-and-failure-persistence-semantics]] and [[what-is-the-message-bridge-authoritative-retry-and-terminal-failure-contract]].

## Scope and limitations

The source states that affected messages did not reach “the group service.” It does not establish that this service is [[group-management]].

The `fmrp1` example supports the TTL explanation: a redelivery after more than two minutes is said to re-execute normal processing and reach downstream. It does not rule out environmental differences between `fmrp1` and `fmrp2`.

The source does not describe Solace acknowledgement timing, manual recovery, replay status, or an implemented solution.
---
type: entity
title: Message Bridge
created: 2026-08-22
updated: 2026-08-24
tags: ["messaging", "routing", "cashflow", "scbml", "ratan", "service", "integration", "kafka", "solace", "indonesia", "gdc", "message-bridge", "cash-settlement", "apache-camel", "application", "observability", "logging", "redis", "ratanone", "ebbs"]
related: ["ratan-id", "murex", "mxml-to-scbml-conversion", "002-select-scbml-message-bridge-routing-for-indonesia", "does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements", "kafka", "solace", "indonesia-pending-fixing-flag-relay", "what-is-the-approved-gdc-indonesia-kafka-solace-topology-for-fixing-flags", "domain-owned-message-filtering", "message-topic-consolidation", "message-header-propagation", "message-bridge-filtering-vs-domain-service-filtering", "should-message-bridge-own-business-filters", "ratan", "scbml", "generic-message-bridge-configuration", "dynamic-message-bridge-registration", "message-bridge-topictype-centralization", "message-bridge-config-properties", "topic-type", "async-mdc-trace-context-propagation", "message-bridge-trace-id-lifecycle", "ratan-central-business-monitoring", "fxu", "ratan-bridge-fail-message", "solace-to-kafka-fan-in", "message-bridge-deduplication-key-lifecycle", "lazy-kafka-endpoint-initialization-race", "retry-and-failure-persistence-semantics", "ratanone", "ebbs", "accounting-service", "solace-based-ebbs-acknowledgement-integration"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-bridge Analysis of the problem of missing traceId in logs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]An error occurs which cause the message to be lost.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# Message Bridge

Message Bridge (MB), referenced as `ratan.messagebridge`, is a routing and integration application within the [[ratan|RATAN]] platform. The *Message-Bridge Restructure* design describes it as a RATAN integration subsystem that constructs Apache Camel routes between messaging and file-transfer endpoints.

The incident analysis describes Message Bridge as an integration component that consumes messages from Solace, splits and routes work, publishes target messages to Kafka, applies Redis-backed deduplication, and routes terminal failures for persistence. The trace-ID analysis additionally describes asynchronous message-processing flows involving message splitting, suppression, dispatch, and asynchronous event production.

## Restructure and integration scope

According to *Message-Bridge Restructure*, the restructuring design covers these endpoint and integration types:

- Solace
- Kafka
- Enterprise Korea
- SFTP
- IBM MQ
- `kr_mq`
- Folder routes

The intended migration scope additionally lists:

- `enterprise_atlas`
- `enterprise_solace`
- `enterprise_ebbs`
- `enterprise_fileit`

The subsystem is being redesigned around [[generic-message-bridge-configuration]] and [[dynamic-message-bridge-registration]] to reduce bridge-specific classes and manually registered beans. Protocol-specific connection setup and endpoint construction remain necessary, particularly for Solace, Kafka, SFTP, IBM MQ, and folder endpoints.

An IBM MQ acknowledgement route connects Message Bridge to [[murex]] through:

- **Route:** `Ratan-Mxg-Cashflow-Adaptor-Murex-Ack`
- **Queue:** `CF.RATAN.MXG.RESP.uat2`

## Processing and incident-relevant components

The incident documentation identifies the following processing components:

- `TargetSplittingRoute`, which uses `.split().method(splitter).parallelProcessing()`.
- `DispatchProducerRoute`, which publishes to a target endpoint and handles cleanup on errors.
- `MessageProducerImpl`, whose `sendBody()` invokes `template.send(endpoint, sentExchange)`.
- `ExceptionProducerRoute`, which is intended to handle terminal errors.
- `RawMessagePersistenceProducerRoute`, which is intended to persist terminal failures to [[ratan-bridge-fail-message]].

In the reported incident, multiple Solace routes simultaneously sent Uber messages to the shared Kafka topic `tdsx_uber_message_json_inbound`. A `workerPool must be specified` failure occurred in the Kafka send path. The subsequent loss condition was caused by stale source-side deduplication state suppressing Solace redelivery.

## Indonesia SCBML cashflow routing

According to *Indonesia Technical Design*, Message Bridge identifies and directs Indonesia-specific SCBML cashflows.

Under selected Diagram 3:

1. The GDC adaptor publishes SCBML to a Message Bridge Kafka topic.
2. GDC Message Bridge routes Indonesia cashflows to FM Solace for [[ratan-id|Ratan ID]].
3. GDC Message Bridge routes non-Indonesia cashflows to the existing standardization-service topic.
4. Ratan ID Message Bridge consumes the Indonesia SCBML flow.

The same source notes that Message Bridge can persist payment-failure messages. Whether this capability, and associated logs, queues, or error records, are acceptable under Indonesia data-residency controls requires explicit confirmation.

## Indonesia pending-fixing-flag relay

According to *Fixing Flag Process in Indonesia*, `message-bridge` is the proposed integration component for relaying Indonesia pending-fixing-flag messages between GDC and Indonesia messaging domains.

| Domain | Source | Target |
|---|---|---|
| GDC | Kafka topic | FM Solace topic |
| Indonesia | FM Solace queue | Kafka |

The fixing-flag source document spells the Indonesia target as “Kakfa”; this page treats that reference as Kafka.

That source does not identify topic or queue names, clusters, subscriptions, delivery guarantees, security controls, or monitoring responsibilities.

## Filtering role at the RATAN platform entrance

### Current role

According to *Message Bridge Filters*, MB currently applies first-level business filters after consuming messages, then routes only selected messages downstream. The source states that this centralizes filter management and limits processing, logging, and Kafka storage demand in downstream services.

### Proposed role

*Message Bridge Filters* proposes making MB a technical routing layer rather than an owner of business filtering. Under that proposal, MB would:

- Remove business-filter logic.
- Pass messages through after consumption.
- Preserve and carry message headers.

The same proposal assigns applicable business filters to consuming and publishing domain services. It is not an accepted decision: the source contains no conclusion, approval, or implementation evidence.

### Dependencies and risks

According to *Message Bridge Filters*, the proposed role change relies on:

- A defined [[message-header-propagation|header-propagation contract]].
- Compatible [[message-topic-consolidation|topic consolidation]].
- An unresolved SDK/configuration approach for SCBML, UBER/JSON, and header filters.

Moving filtering downstream may affect consumer capacity and timing covered by [[kafka-consumer-poll-timeout]] and [[kafka-listener-consumption-time-tracking]]. The source identifies a potentially high discard rate for the BCS settlement flow, but does not provide supporting measurements.

## Ratan technical-live and EBBS accounting-feed scope

According to *Tech Live of Ratan - Accounting Service with EBBS*, Message Bridge is an integration component included in both proposed Ratan technical-live scopes.

- **Option 1** includes Message Bridge as part of complete Ratan-to-EBBS accounting-feed validation.
- **Option 2** includes only Message Bridge and Service Properties while directly testing a mocked EBBS JSON feed over [[solace]].

This technical-live source does not identify Message Bridge's exact publishing and consuming responsibilities, message-transformation behavior, or acknowledgement-correlation mechanism. These omissions limit the conclusions that can be drawn from the technical-live plan. These scope statements concern the Ratan-to-EBBS technical-live plan and do not define or replace the endpoint responsibilities described in the other Message Bridge designs.

## Deduplication and failure semantics

The incident analysis states that Message Bridge must distinguish between:

- A source delivery identity.
- A downstream publishing identity.
- A retrying failure.
- A terminal failure persisted for recovery.
- A successfully completed downstream publication.

A single mutable `DUPLICATION_CHECK_KEY` was insufficient for cleanup in the documented incident because the target key overwrote the source key before error cleanup.

Further design considerations are documented in:

- [[message-bridge-deduplication-key-lifecycle]]
- [[retry-and-failure-persistence-semantics]]
- [[solace-to-kafka-fan-in]]

## Trace correlation and asynchronous processing

According to *Message-bridge Analysis of the problem of missing traceId in logs*, missing `traceId` values impair end-to-end diagnostic tracing across Message Bridge message chains, including in production. The issue affects both initial logging at route ingress and trace-context propagation across thread boundaries.

### Relevant components

The trace-ID analysis identifies the following components as central to trace correlation:

- `MessageBridgeApplication` configures Camel and Spring asynchronous execution.
- `AbstractConsumerClientRouteBuilder` is the proposed ingress point for early trace-context initialization.
- `TrackingIdProcessor` writes a message-derived identifier to MDC.
- `TargetSplittingRoute` uses `parallelProcessing()`.
- `SuppressionRouteBuilder` is proposed as a split-thread restoration point.
- `EventProducerRoute` uses Spring `@Async`.
- `DispatchProducerRoute` uses `CompletableFuture.runAsync()`.

### Observability dependency

The trace-ID analysis states that Message Bridge requires an explicit [[message-bridge-trace-id-lifecycle|trace ID lifecycle]] and [[async-mdc-trace-context-propagation|MDC propagation]] policy. Camel-managed transitions, Spring-managed asynchronous work, unmanaged futures, and scheduled jobs have distinct context-handling requirements.

Reported validation contexts include [[scbml|SCBML]] in `fmrp1` and [[fxu|FXU]] in `uat4`. This is validation evidence for log visibility only; it does not establish changes to SCBML or FXU functional processing.
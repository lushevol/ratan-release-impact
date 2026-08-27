---
type: concept
title: Message Bridge Trace ID Lifecycle
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, traceid, correlation, apache-camel, logging]
related: [message-bridge, async-mdc-trace-context-propagation, ratan-central-business-monitoring, how-is-mdc-propagated-for-message-bridge-completablefuture-and-scheduled-tasks, is-manual-traceid-restoration-required-after-enabling-camel-mdc-logging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-bridge Analysis of the problem of missing traceId in logs.md"]
---
# Message Bridge Trace ID Lifecycle

The intended Message Bridge trace lifecycle is not yet formally specified. The source proposes initializing a temporary `traceId` at consumer ingress, later replacing it with a business `trackingId`, carrying the value through split messages, restoring it in downstream processing, and clearing thread-local context after asynchronous work.

## Proposed lifecycle stages

1. At consumer ingress, derive `earlyTraceId` from `JMSMessageID`, otherwise `KafkaConstants.OFFSET`, otherwise the Camel Exchange ID.
2. Set `traceId` as an Exchange property and in MDC.
3. Allow `TrackingIdProcessor` to set the actual message `trackingId` in MDC later in the route.
4. For split messages, copy `traceId` into each child message header.
5. At the suppression route, restore the child-message header to MDC and the Exchange property.
6. Propagate captured MDC to Spring `@Async` tasks.
7. Clear MDC after asynchronous task completion.

## Contract ambiguity

The source uses several identifiers as possible `traceId` values:

- `JMSMessageID`
- Kafka offset
- Camel Exchange ID
- business `trackingId`

They have different scopes and semantics. A Kafka offset without topic and partition is not generally a globally unique identity. Replacing an earlier correlation value with a later one also means logs in one flow can use different identifiers.

A durable contract should define:

- whether `traceId` is immutable from ingress to completion;
- whether early transport identity belongs in a separate field such as `transportMessageId`;
- precedence when a business `trackingId` is absent, malformed, or delayed;
- propagation behavior during retry, redelivery, split processing, and failure handling;
- required cleanup boundaries for route-managed and application-managed MDC writes.

## Empty-body branch

The identified empty-body branch records `trackingId` in an Exchange property but does not write it to MDC. This is an initialization failure, not merely a cross-thread propagation failure. Early initialization addresses logs emitted before `TrackingIdProcessor` and logs in that branch.

## Related open questions

The route-specific restoration approach may be redundant with Camel MDC logging, depending on actual runtime behavior; see [[is-manual-traceid-restoration-required-after-enabling-camel-mdc-logging]].

`CompletableFuture.runAsync()` and scheduled-task behavior remain outside the proposed implementation; see [[how-is-mdc-propagated-for-message-bridge-completablefuture-and-scheduled-tasks]].
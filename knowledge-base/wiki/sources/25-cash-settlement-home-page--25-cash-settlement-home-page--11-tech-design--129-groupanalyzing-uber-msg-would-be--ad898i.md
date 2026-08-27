---
type: source
title: Uber Inbound Message Loss and DLT Recovery Design
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, uber, message-processing, retry, dead-letter-topic, incident]
related: [tdsx-uber-message-listener, kafka-persistent-retry-and-dlt-recovery, uber-inbound-message-idempotency-and-error-state, does-tdsx-uber-retryabletopic-work-correctly-with-consumererrorhandler, what-is-the-operational-recovery-process-for-uber-dlt-records, which-group-processing-dependency-failures-may-safely-degrade, what-causes-duplicate-cashflow-ids-and-major-versions-in-uber-trades, orchestration, database-to-kafka-exception-event-reliability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# Uber Inbound Message Loss and DLT Recovery Design

## Summary

This technical design analyzes an Uber-message loss incident in group processing. A downstream exception in `TdsxUberMessageListener` caused deletion of the newly created `ratan_inbound_message` record. The exception then reached Spring Kafka error handling, after which consumption progressed beyond the failed offset. The combination of destructive cleanup and non-durable retry made the business message unrecoverable.

The proposed repair adds persistent Kafka retry topics and a DLT fallback, while retaining failure evidence in inbound and group persistence. Terminal DLT handling is explicitly not successful processing: it leaves recoverable `ERROR` and `PENDING` states and prevents downstream cashflow publication.

## Incident Evidence

The source records a missing split-queue message for:

- Trade ID: `7153008753`
- Trace ID: `20884002ba5214319625367b862437ca`
- Source system: TDSX
- Comparison outcome: UAT4 retained inbound data, while FMRP2 did not.

A Dev reproduction reportedly processed the failed trade ten times under the pre-enhancement implementation. This supports an observed in-memory retry pattern, but does not by itself prove a specific Spring Kafka error-handler configuration or framework default.

A separate incident for trade `7151397157` involved a duplicate-key exception. Three cashflows reportedly shared `cashflowId` `007390420129` and the same major version. This is evidence that data defects can prevent processing, but it is not established as the same root cause as the destructive-cleanup failure.

## Pre-Repair Failure Path

```text
handleMessage()
  -> save(VALIDATED) in ratan_inbound_message
  -> resourceLockManager.run(...)
  -> publishEvent(UberValidatedEvent)
  -> downstream exception
  -> deleteById(inboundRecordId)
  -> rethrow exception through consumerErrorHandler
  -> container error handling and offset progression
  -> no inbound record and no automatically retried Kafka record
```

The critical failure condition is the combination of:

1. deleting the durable inbound processing record on exception; and
2. exhausting a retry path that does not retain a recoverable record for later processing.

The source describes the container behavior as usually consistent with `FixedBackOff(0, 9)`—one initial delivery and nine in-memory retries. That configuration is not verified by provided runtime configuration, Spring Kafka version, consumer logs, or committed-offset evidence.

## Listener Comparison

| Listener | Retry mechanism | Retry method | Terminal behavior |
|---|---|---|---|
| `CashflowInboundListener` | `@RetryableTopic(attempts=5, backOff=15s*2)` | Dedicated Kafka retry topics | DLT fallback |
| `TdsxUberMessageListener` before enhancement | No `@RetryableTopic` | Container-level in-memory retry | No DLT; failure can be discarded after retries |

## Proposed Listener Configuration

```java
@RetryableTopic(
attempts = "${ratanone.topic.tdsx-uber-json-inbound.attempts:5}",
backOff = @BackOff(delay = 15000, multiplier = 2.0),
topicSuffixingStrategy = TopicSuffixingStrategy.SUFFIX_WITH_INDEX_VALUE,
numPartitions = "${ratanone.topic.tdsx-uber-json-inbound.retry-partition:3}",
concurrency = "${ratanone.topic.tdsx-uber-json-inbound.concurrency:1}"
)
@KafkaListener(topics = "${ratanone.topic.tdsx-uber-json-inbound.name}", batch = "false", errorHandler = "consumerErrorHandler", concurrency = "${ratanone.topic.tdsx-uber-json-inbound.concurrency:1}")
public void handleMessage(ConsumerRecord<String, String> record) {
}
```

The source states that the intended retry policy is five attempts. Its Dev test reports four retries before DLT, which is compatible if the configured attempt count includes the initial delivery. This interpretation must be confirmed against the deployed Spring Kafka version and generated retry-topic topology.

## DLT Recovery Contract

The proposed `@DltHandler` follows the SCBML model:

1. Persist the Uber inbound record in `ratan_inbound_message`.
2. Persist the group record in `ratan_cashflow_group`.
3. Persist the group-message record in `ratan_cashflow_group_message`.
4. Reconcile by `major_version` and cashflow event (`New` or `Withdrawal`).
5. Skip data already processed.
6. Mark required but unprocessed data as `ERROR`.

For the tested terminal case, the intended database state is:

| Record | Terminal DLT state |
|---|---|
| `ratan_cashflow_group` | `PENDING` |
| `ratan_cashflow_group_message` | `ERROR` |
| `ratan_inbound_message` | `ERROR` |
| Downstream cashflow | Not emitted |

This provides an auditable incomplete-work state rather than silent loss. It does not define the owner, replay authority, alerting, retention, or remediation SLA for DLT records.

## Dependency Failure Handling

The design adds retry and fallback behavior to two external calls in `CashflowGraphQLService`, following the reference pattern in `CashflowService.queryCashflow()`:

```java
} catch (Exception e) {
if (queryTimes < QUERY_MAX_TIME) {
log.warn("Query cashflow history one more time as exception occurred, cashflowId: {}, retryCount: {}",
cashflowId, queryTimes + 1, e);
return queryCashflowHistoriesByCashflowId(cashflowId, ++queryTimes);
} else {
log.error("Exception occurred when querying cashflow history, reached max retry {}, cashflowId: {}, degraded to empty list.",
QUERY_MAX_TIME, cashflowId, e);
return Lists.newArrayList();
}
}
```

The dependency inventory also reports inconsistent degradation decisions:

| Service or component | Location | Reported failure behavior |
|---|---|---|
| `ratanone-static-data-service` | `AmendmentGroupEventProcessor#isDedicatedChange` | Caught failure returns `true` |
| `CashflowCutoffCommand#getMaterializeCutoff` | Command processing | Caught failure; fields may be absent |
| `FXUSettlementMethodCommand#execute` | Command processing | Caught failure; degradation is not marked `UTIL` |
| `CashflowBicNettingFlagCommand#execute` | Command processing | Caught failure returns an empty string |
| `RATANONE-DATA-AMBASSADOR` | `LegalEntityCommand#execute` | Empty field plus exception flag |
| `DataAmbassadorClient#queryTrade` | `DATradeRepository` | Built-in retry and empty-result fallback |
| `RATAN-CASH-SETTLEMENT-BATCH-SERVICE` | `CashflowPendingFixingFlagCommand#execute` | Caught failure returns a default value |
| `ATAN-CASH-SETTLEMENT-NETTING-SERVICE` | `LienFlagCommand#fetchOriginalTradeIds` | May propagate if not caught by an outer layer |
| `RATAN-CASH-SETTLEMENT-QUERY-SERVICE` | `AmendmentGroupEventProcessor.processReadyEvent` | No retries or fallback reported |

Returning default or empty values must not be assumed safe. The source does not identify which enrichment fields are optional, how degraded data is propagated, or which failures require DLT rather than fallback.

## Dev Test Results

For trade `7153008753` and correlation ID `e059cfa144bb9bc3222f50fb1b4f5c22_7153008753`:

- Before enhancement, the message was reportedly lost after ten in-memory executions, with no group, group-message, or inbound record.
- In terminal-failure Case 1, the message was retried four times through Kafka before DLT; group state was `PENDING`, group-message and inbound states were `ERROR`, and no cashflow was sent downstream.
- In Case 2, a retry succeeded before the terminal threshold and the relevant tables were reported as successfully processed.

These are Dev-environment observations, not a production guarantee of duplicate-free processing.

## Open Questions

- Does `consumerErrorHandler` correctly propagate failures into `@RetryableTopic` routing without committing or seeking past records?
- Was `deleteById` removed from the active listener implementation, despite the replacement code being struck through in the source?
- What unique key and transactional boundary enforce inbound and downstream idempotency?
- What retry-topic and DLT names, ACLs, retention periods, monitoring, and runbooks are deployed?
- Who owns DLT replay, and how is duplicate downstream cashflow publication prevented?
- Which dependency failures are approved for graceful degradation?
- Is `ATAN-CASH-SETTLEMENT-NETTING-SERVICE` a typo for `RATAN-CASH-SETTLEMENT-NETTING-SERVICE`?
- What prevents duplicate `cashflowId` and `major_version` values upstream?
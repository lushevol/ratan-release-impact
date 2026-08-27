---
type: entity
title: Kafka
created: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md", "RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
tags: ["Kafka", "messaging", "event processing", "testing", "api-gateway", "auditing", "cash-settlement", "stp", "asynchronous-processing", "ratan", "offsets", "monitoring"]
related: ["akhq", "cdu", "tds3", "kafka-settlement-test-topics", "mock-settlement-test-data-generation", "api-gateway", "gateway-closed-loop-observability", "lifecycle-batch-status-update-api", "cashflow-batch-transaction-atomicity", "cash-settlement-asynchronous-batch-processing", "non-blocking-message-retry", "ratanone-message-bridge", "ratan-cash-settlement-orchestration", "ebbs", "ratan-transient-failure-recovery"]
updated: 2026-08-25
---

# Kafka

Kafka is used as a messaging platform by the mock settlement-data procedures. Separately, the API Gateway Feature Upgrade source describes Kafka as receiving audit events emitted by the [[api-gateway|API Gateway]] through `KafkaOpenApiAuditService`.

The RATAN ITRS Log source describes Kafka as carrying RATAN settlement-processing messages, including `Cash_Settlement_EBBS_Process_Out_GB` and `Cash_Settlement_Orchestration_Process_In`.

The Batch Status Update API Tuning source identifies Kafka as a possible mechanism for triggering STP processing during post-processing of the [[lifecycle-batch-status-update-api|Lifecycle Batch Status Update API]].

## Mock settlement-data topics

The mock testing data user guide documents the following topics:

```text
Cash_Settlement_Group_Message_Inbound
TDS3_Trade_Message_Process_In
CDU_Trade_Confirmation_Process_In
Trade_Service_Trade_Events
```

The guide uses [[akhq|AKHQ]] to inspect and produce messages. It identifies the latter three topics as:

| Topic | Role described by the mock testing data user guide |
|---|---|
| `TDS3_Trade_Message_Process_In` | Receives trade messages |
| `CDU_Trade_Confirmation_Process_In` | Receives confirmation status |
| `Trade_Service_Trade_Events` | Publishes events |

The mock testing data user guide does not define topic ownership, schemas, headers, partitioning, ordering, retry behavior, or the relationship between confirmation input and event publication.

## API Gateway audit-event integration

According to the API Gateway Feature Upgrade source, the [[api-gateway|API Gateway]] emits audit events to Kafka through `KafkaOpenApiAuditService`.

This integration provides audit-event transport but does not, by itself, establish complete operational observability. That source additionally recommends gateway-specific metrics, dashboards, and alerting.

## Lifecycle Batch Status Update API post-processing

According to the Batch Status Update API Tuning source, Kafka may trigger STP processing after post-processing associated with the [[lifecycle-batch-status-update-api|Lifecycle Batch Status Update API]].

That source does not specify whether Kafka publication participates in the same transaction as [[cashflow-batch-transaction-atomicity|cashflow persistence]]. The implementation therefore needs an explicit consistency, retry, duplicate-handling, and reconciliation model. Kafka-triggered processing should not be assumed to be covered by the database transaction solely because it occurs after batch persistence.

## RATAN settlement-processing topics and offsets

According to the RATAN ITRS Log source, Kafka carries RATAN settlement-processing messages on the following topics:

| Topic | RATAN ITRS Log description |
|---|---|
| `Cash_Settlement_EBBS_Process_Out_GB` | Carries RATAN settlement-processing messages. |
| `Cash_Settlement_Orchestration_Process_In` | Carries RATAN settlement-processing messages. |

The RATAN ITRS Log source records one five-second offset-commit timeout in [[ratanone-message-bridge|`ratanone-message-bridge`]] without a documented outcome.

The same source separately records [[ratan-cash-settlement-orchestration|orchestration]] behavior in which an offset is intentionally not committed when transaction setup fails, allowing processing to retry. These are distinct failure and recovery patterns and are not proven to be causally related.
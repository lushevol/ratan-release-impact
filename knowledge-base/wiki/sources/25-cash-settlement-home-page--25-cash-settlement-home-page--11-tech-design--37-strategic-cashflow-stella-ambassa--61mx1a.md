---
type: source
title: Strategic Cashflow Stella Ambassador
authors: []
year: 2023
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, stella, strategic-cashflow, integration, kafka]
related: [stella, ratanone-stella-ambassador, ratan-cashflow-lifecycle-service, sabre-booking-api, trade-lake, strategic-cashflow, stella-cashflow-status-synchronization, stella-transaction-workflow-consistency, stella-trade-lake-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Strategic Cashflow Stella Ambassador

This technical design records the integration between the Ratan CN cashflow lifecycle service and Stella for strategic-cashflow status updates. It documents an SDK upgrade, separate batch and single message routes, development-environment tests, and observed Stella/Trade Lake failures. It does not establish an approved production contract.

## SDK dependency and channel

```java
<dependency>
    <groupId>com.scb.sabre.fmrep</groupId>
    <artifactId>sabre-booking-api</artifactId>
    <version>1.2.0</version>
</dependency>
```

```java
package com.scb.sabre.booking.api.common;

public enum StellaChannel {
    ...

	RATANCASH_V2("ratancash-v2"),    
    ...

}
```

The dedicated `RATANCASH_V2` channel identifies strategic cashflows as a channel-level Stella integration scope.

## Documented lifecycle tests

| Cashflow ID | Status before | Action | Status after | Transaction version | Notes |
|---|---|---|---|---|---|
| `003486517198` | `PROJECTED` | `Net` | `NETTED` | `0->1` | Trade Lake delay was identified as a potential issue. |
| `003486517198` | `NETTED` | `Unnet` | `PROJECTED` | `1->2` | |
| `003486517198` | `PROJECTED` | `Release` | `RELEASED` | `2->3` | |
| `003486517198` | `RELEASED` | `Settle` | `SETTLED` | `3->4` | |
| `003486517199` | `PROJECTED` | `Settle` | `SETTLED` | `0->1` | Stella does not allow cross-status updates. |
| `003486517199` | `PROJECTED` | `Net` | `NETTED` | `0->1` | |
| `003486517199` | `NETTED` | `Release` | `RELEASED` | `1->2` | |
| `003486517199` | `RELEASED` | `Settle` | `SETTLED` | `2->3` | |

These are development-environment observations. They are evidence for [[stella-cashflow-status-synchronization]], not a complete authoritative Ratan lifecycle state machine.

## Message routes

| Configuration | Topic | Producer | Consumer | Consumer group | Trigger or routing condition |
|---|---|---|---|---|---|
| `message-batch` | `Cashflow_Status_Batch_Command_In` | `ratan-cashflow-lifecycle-service` | `ratanone-stella-ambassador` | `Stella-Ambassador-Message-Batch-Group` | Cashflow scheduled job |
| `message` | `Cashflow_Status_Command_In` | `ratan-cashflow-lifecycle-service` | `ratanone-stella-ambassador` | `Stella-Ambassador-Message-Group` | Status-update trigger |
| `batch-result` | `Cashflow_Status_Batch_Response_In` | `ratanone-stella-ambassador` | `ratan-cashflow-lifecycle-service` | `cashflow-service-stella-batch-response` | `StellaResultEvent` with event type `ALL` or `BROADCAST` and API type `BATCH` |
| `result` | `Cashflow_Status_Response_In` | `ratanone-stella-ambassador` | `ratan-cashflow-lifecycle-service` | `cashflow-service-stella-response` | `StellaResultEvent` with event type `ALL` or `BROADCAST` and API type `SIGNLE` |

The source proposes `Cash_Settlement_Cashflow_Status_Batch_Response_In` and `Cash_Settlement_Cashflow_Status_Response_In` as alternative response topics, but explicitly states that nothing has changed. The existing names remain the only documented names; their production authority is unresolved in [[what-is-the-authoritative-stella-strategic-cashflow-topic-contract]].

## Command examples

Headers:

```text
Key: cashflowId: 003486517198
stellaMessageType: STRATEGIC_CASHFLOW
responseTopic: XXXXXX
```

Batch payload:

```json
[
  {
    "action": "Release",
    "businessVersion": "0",
    "cashflowId": "003486517198",
    "cashflowVersion": "1",
    "commandId": "c32f416e-df0c-415f-b23c-84af91975076",
    "correlationId": "1032892",
    "operation": "STATUS_UPDATE",
    "trackingId": "aae38b50-e495-4f85-8a3e-28ea55fbbe64"
  },
  {
    "action": "Net",
    "businessVersion": "0",
    "cashflowId": "003486517199",
    "cashflowVersion": "0",
    "commandId": "c32f416e-df0c-415f-b23c-84af91975076",
    "correlationId": "1015376",
    "operation": "STATUS_UPDATE",
    "trackingId": "0bbdc024-68af-4974-a6bd-f8bf4fb62c6e"
  }
]
```

Single-command payload:

```json
{
  "action": "Release",
  "businessVersion": "0",
  "cashflowId": "003486517198",
  "cashflowVersion": "2",
  "commandId": "12031",
  "correlationId": "3832245079",
  "operation": "STATUS_UPDATE",
  "trackingId": "MX_FXCASH_330840406_289337760_1679548904267"
}
```

## Result examples

Successful result:

```json
{
  "id": "b165c2ba-1bbc-4e76-b344-7a9e3c7b7029",
  "commandId": "12031",
  "trackingId": "MX_FXCASH_330840406_289337760_1679548904267",
  "cashflowId": "003486517198",
  "correlationId": "3832245079",
  "businessVersion": "0",
  "cashflowVersion": "1",
  "razorStatus": null,
  "stellaCashflowVersion": "2",
  "processStatus": "SUCCESS",
  "errorCode": null,
  "errorMessage": null,
  "stellaStatus": "PROJECTED"
}
```

Failure result:

```json
{
  "id": "5d74cb40-ebff-4bbe-a752-e75ed1e18108",
  "commandId": "12031",
  "trackingId": "MX_FXCASH_330840406_289337760_1679548904267",
  "cashflowId": null,
  "correlationId": null,
  "businessVersion": null,
  "cashflowVersion": null,
  "razorStatus": null,
  "stellaCashflowVersion": "2",
  "processStatus": "FAILED",
  "errorCode": "TL_RETRY_ERROR",
  "errorMessage": "Errors:ProcessingError - Errors:TL_RETRY_ERROR - RETRY MAX TIMES in Elastic Search for transactionId=003486517198, transactionVersion=2\n\n",
  "stellaStatus": ""
}
```

Failure results can omit identifiers supplied on the command and returned on success. This is a recovery and observability risk.

## Failure evidence

- `TimeoutException`: attributed to a non-running Stella environment; documented action is retry until success, but the case could not be reproduced and no retry parameters are specified.
- `TRANSACTION_WORKFLOW_MISMATCH`: a `Release` for transaction `003486517198` on workflow `Cash Settlement` conflicted with an existing `Standard Cash Settlement` workflow. The source states that a preceding `Unnet` had returned success to the Ambassador without synchronizing to Trade Lake.
- `TL_RETRY_ERROR`: Trade Lake was down and Elastic Search retries were exhausted. No recovery procedure is documented.

The source demonstrates that an Ambassador/Stella acknowledgement is not necessarily proof of durable downstream synchronization. See [[stella-trade-lake-reconciliation]].
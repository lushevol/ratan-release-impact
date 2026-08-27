---
type: source
title: NSTP Exception Auto Close Design: Confirmation Status Handling
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [nstp, exception-handling, trade-confirmation, camunda, cash-settlement]
related: [confirmation-driven-nstp-exception-auto-closure, trade-cashflow-exception-version-correlation, ratan-stella-message-event-source, what-are-the-idempotency-retry-and-ordering-rules-for-nstp-auto-close, what-are-the-resulting-cashflow-and-exception-statuses-after-nstp-auto-close, what-is-the-authoritative-camunda-mutiexcption-syncsummary-api-contract, cash-settlement-exception-handling, ratan-cash-settlement-orchestration, trade-service-trade-events]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# NSTP Exception Auto Close Design: Confirmation Status Handling

This internal design specifies an automatic close flow for NSTP exceptions associated with eligible CN Settlement cashflows. The flow is triggered by qualifying events from [[trade-service-trade-events]] and invokes a Camunda interface hosted by [[ratan-cash-settlement-orchestration]].

## Specified Processing Flow

1. Consume Life Cycle monitor events from `Trade_Service__Trade_Events`.
2. Require the event to be `MATCHED`.
3. Require the event EG Confirmation Status to be `Confirm` or `Affirm`.
4. Query `ratan_stella_message_event_source` using `tradeId` and `tradeVersion` to identify CN Settlement cashflow data.
5. Require cashflow status `WAITING` and action `isNstp`.
6. Call the Camunda interface to close exceptions, synchronize exception summaries, and update cashflow status.

The stated trigger rule is:

```text
event.status == MATCHED
AND event.egConfirmationStatus IN (Confirm, Affirm)
```

The exact incoming event field names are not defined by this source.

## Camunda Interface

The source records the endpoint path as `mutiException`, not `multiException`.

```text
POST http://RATAN-CASH-SETTLEMENT-ORCHESTRATION/v1/camunda/task/mutiException/syncSummary
```

The linked normalized host form is:

```text
http://ratan-cash-settlement-orchestration/v1/camunda/task/mutiException/syncSummary
```

### Request Body

```json
{
  "cashflowId": "009371505034",
  "cashflowVersion": 0,
  "businessVersion": 0,
  "minorVersion": "2",
  "action": "Submit",
  "comment": "comment",
  "exceptions": [
    {
      "id": "1631214046280052736",
      "originalExceptionId": "1631214046187761664",
      "exceptionCode": "GSAM Client",
      "businessFlow": "SETTLEMENT",
      "businessType": "NSTPSSI",
      "roleType": "Maker",
      "sourceSystem": "RATAN-RULE-SERVICE",
      "exceptionType": "BUSINESS",
      "exceptionCategory": "NSTP",
      "description": "FMID = 400120692 is GSAM client.",
      "actions": [
        {
          "actionName": "submit",
          "actionType": null,
          "apiUrl": "http://RATAN-RULE-SERVICE/v1/nstpException/submit",
          "requestBody": "{\"affirmedBy\":\"123\",\"phone_email\":\"123\",\"affirmedAt\":\"2023-03-02T08:45:09.759\"}",
          "apiMethod": "POST",
          "componentName": null,
          "componentUrl": null
        }
      ],
      "metaData": null,
      "entityId": "009371505034",
      "entityVersion": 0,
      "entityType": "CASHFLOW",
      "trackingId": "1631214046208733184",
      "exceptionTime": "2023-03-02T08:45:09.759676",
      "status": "PENDING_OPERATOR"
    }
  ]
}
```

### Documented Responses

Success:

```json
{"status": 200, "errorCode": "", "errorMessage": "SUCCESS"}
```

Failure when the Cashflow fixing task cannot be found:

```json
{"status": 404, "errorCode": "RATAN-201050003", "errorMessage": "Cashflow fixing task can not be found"}
```

## Correlation Rules

The design explicitly records the following mappings:

| Source | Target |
|---|---|
| CDU `tracking_version` | cashflow `trade_version` |
| Rule Service `entityId` | cashflow `cashflow__cashflow_id` |
| Rule Service `entityVersion` | cashflow `cashflow__cashflow_business_version` |

These mappings are documented in [[trade-cashflow-exception-version-correlation]].

## Boundaries and Unresolved Details

This design applies only to the stated `MATCHED` plus `Confirm`/`Affirm` condition and eligible CN Settlement cashflows with `WAITING` and `isNstp`. It does not establish a general auto-close rule for all exception categories or confirmation-driven payment-STP flows.

The source does not define the CN Settlement marker, the meaning or storage of `isNstp`, resulting cashflow or exception statuses, idempotency, ordering, retry behavior, atomicity for multiple exceptions, or the authorization implications of the example `roleType: "Maker"` value.
---
type: source
title: Draft Design for Phase 2
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, utilization, settlement-method, draft-design, cashflow]
related: [fxu, utilization-service, fxu-utilization-response-contract, utilization-dlq-retry-and-failure-semantics, gross-util-settlement-method-transition, past-due-accounting-reversal, cashflow-settlement-method-event-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# Draft Design for Phase 2

This draft technical design specifies intended Phase 2 behavior for FXU utilization responses, technical failure responses, and manual bidirectional settlement-method changes between `GROSS` and `UTIL`. It is a proposed contract and does not provide implementation, production, performance, or compatibility evidence.

## Utilization response enrichment

A utilization response returns processing status alongside an echo of the parsed utilization request.

```json
{
  "Utilization": {
    "Utilization_Id": "71110111971",
    "Response": "ACK",
    "Error_Reason": null
  },
  "Request_Info": {
    "Utilization": {
      "Utilization_Id": "71110111971",
      "Orig_Utilization_Id": null,
      "Util_Type": "EARLY-FULL-UTIL",
      "AACode_Comments": "FX",
      "Util_Payment_Ref": "1",
      "Maker_ID": "1642375",
      "Checker_ID": "1376381",
      "Trade": {
        "Trade_Id": "7111011197",
        "Trade_Lake_Trade_Major_Version": "1",
        "Swap_Leg_ID": "",
        "Exchanged_Currency1_Payment_Amount_Currency": "USD",
        "Exchanged_Currency1_Util_Amount": "200.0",
        "Exchanged_Currency2_Payment_Amount_Currency": "SAR",
        "Exchanged_Currency2_Util_Amount": "749.98"
      }
    }
  }
}
```

See [[fxu-utilization-response-contract]].

## Automatic utilization response

The automatic-utilization response carries utilized and remaining amounts for each exchanged currency.

```json
 {
    "Utilization_Id": "fxu.1711101119712.6721092670",
	"Trade": {
        "Trade_Id": "6721092670",
        "Swap_Leg_ID": "",
        "Exchanged_Currency1_Payment_Amount_Currency": "USD",
	    "Exchanged_Currency1_Util_Amount": 100.0,
        "Exchanged_Currency1_Remaining_Amount": 0,
 	    "Exchanged_Currency2_Payment_Amount_Currency": "EGO",
	    "Exchanged_Currency2_Util_Amount": 10000.0,
        "Exchanged_Currency2_Remaining_Amount": 0
     }
  }
```

The draft does not define negative-amount handling, precision and scale, whether both currencies must be fully utilized together, or whether `EGO` is an intended currency value.

## Technical failure responses

Malformed JSON receives an immediate `NACK`; the response has an empty utilization ID and returns the unparsed request as `Raw_Request`.

```json
{
  "Utilization": {
    "Utilization_Id": "",
    "Response": "NACK",
    "Error_Reason": "Raw message error."
  },
  "Request_Info": {
    "Raw_Request": "{\n  \"Utilization\": {\n    \"Utilization_Id\": \"6721092670\",\n    \"Util_Type\": \"VDATE-FULL-UTIL\",\n    \"AACode_Comments\": \"AACode_Comments\",\n    \"Util_Payment_Ref\": \"Util_Payment_Ref\",\n    \"Maker_ID\": \"8220478\",\n    \"Checker_ID\": \"1633330\",\n    \"Trade\": {\n      \"Trade_Id\": \"6721092670\",\n      \"Trade_Lake_Trade_Major_Version\": \"1\",\n      \"Swap_Leg_ID\": \"\",\n      \"Exchanged_Currency1_Payment_Amount_Currency\": \"USD\",\n      \"Exchanged_Currency1_Util_Amount\": 30.0\n    }\n  }"
  }
}
```

For a Ratan internal error, the utilization service uses a DLQ and retries at most five times before returning `NACK`.

```json
{
  "Utilization": {
    "Utilization_Id": "7721092670",
    "Response": "NACK",
    "Error_Reason": "Ratan internal error."
  },
  "Request_Info": {
    "Utilization": {
      "Utilization_Id": "7721092670",
      "Orig_Utilization_Id": null,
      "Util_Type": "EARLY-PART-UTIL",
      "AACode_Comments": "FX",
      "Util_Payment_Ref": "1",
      "Maker_ID": "1642375",
      "Checker_ID": "1376381",
      "Trade": {
        "Trade_Id": "7721092670",
        "Trade_Lake_Trade_Major_Version": "1",
        "Swap_Leg_ID": "",
        "Exchanged_Currency1_Payment_Amount_Currency": "USD",
        "Exchanged_Currency1_Util_Amount": "50"
      }
    }
  }
}
```

The five-attempt policy applies to the Ratan internal-error path, not to invalid JSON. See [[utilization-dlq-retry-and-failure-semantics]].

## Manual `GROSS` and `UTIL` settlement-method changes

The draft assigns the manual settlement-method entry point to [[utilization-service]]. Changes are intended to take effect immediately at trade level, support batches, and return one result per requested trade.

`UTIL → GROSS` must immediately generate a past-due accounting reversal if past-due accounting exists. A `Withdrawal` event's settlement-method value is to be overwritten by the latest `New` event's settlement-method value.

The design states that Group Service must forbid `UTIL` settlement-method restamping, while Utilization Service must provide the controller and service, validate `SettlementMethod=UTIL`, and handle past-due reversals.

```http
POST /v1/utilization/cashflow/settlementMethod/stamping
```

```json
{
  "trades": [
    {
      "tradeId": "123",
      "cashflowIds": ["007300894620", "007300894621"]
    },
    {
      "tradeId": "456",
      "cashflowIds": ["007300894623", "007300894624"]
    },
    {
      "tradeId": "789",
      "cashflowIds": ["007300894625", "007300894626"]
    },
    {
      "tradeId": "112",
      "cashflowIds": ["007300894627", "007300894628"]
    }
  ],
  "settlementMethod": "GROSS|UTIL",
  "comment": ""
}
```

```json
[
  {
    "tradeId": "123",
    "cashflowIds": ["007300894620", "007300894621"],
    "success": true,
    "errorMessage": ""
  },
  {
    "tradeId": "456",
    "cashflowIds": ["007300894623", "007300894624"],
    "success": true,
    "errorMessage": ""
  },
  {
    "tradeId": "789",
    "cashflowIds": ["007300894625", "007300894626"],
    "success": false,
    "errorMessage": "Action not allowed."
  },
  {
    "tradeId": "112",
    "cashflowIds": ["007300894627", "007300894628"],
    "success": false,
    "errorMessage": "Action not allowed."
  }
]
```

## Listed transition outcomes

| Transition condition | Stated outcome |
|---|---|
| `GROSS → UTIL` with Withdrawal carrying `GROSS`, no utilization | `CANCELLED` |
| `GROSS → UTIL` with Withdrawal carrying `GROSS`, utilized | `ERROR` |
| `UTIL → GROSS` with Withdrawal carrying `UTIL`, cashflow not released | `CANCELLED` |
| `UTIL → GROSS` with Withdrawal carrying `UTIL`, cashflow released | `READY + Utilization` |

The source does not formally define the listed states, the meaning of `READY + Utilization`, event ordering, or batch atomicity. See [[gross-util-settlement-method-transition]] and [[what-are-the-atomicity-idempotency-and-event-ordering-rules-for-fxu-settlement-method-stamping]].
---
type: concept
title: FXU Message-Driven Integration
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, messaging, acknowledgement, nack, cash-settlement, integration]
related: [fxu, fx-utilization, fxu-utilization-validation, cash-settlement-service-landscape]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# FXU Message-Driven Integration

The FXU design uses an inbound request topic and an acknowledgement topic for utilization processing.

## Topics

```text
Cash_Settlement_FXU_Request_In
Cash_Settlement_FXU_Ack
```

## Request shape

A request contains utilization identity and origin fields, utilization type, accounting comments, payment reference, maker and checker identifiers, and a nested trade object.

```json
{
  "Utilization_Id": "12345678",
  "Orig_Utilization_Id": "12345678",
  "Util_Type": "VDATE-FULL-UTIL",
  "AACode_Comments": "",
  "Util_Payment_Ref": "",
  "Maker_ID": "12345678",
  "Checker_ID": "12345678",
  "Trade": {
    "Trade_Id": "12345678",
    "Trade_Lake_Trade_Major_Version": "1",
    "Swap_Leg_ID": "Far/Near",
    "Exchanged_Currency1_Payment_Amount_Currency": "USD",
    "Exchanged_Currency1_Util_Amount": "1000.00"
  }
}
```

## Acknowledgement shape

The response reports:

- `Utilization_Id`
- `Response`, with `ACK` or `NACK`
- `Error_Reason`
- The original request under `Request_Info`

Business NACKs describe domain rejection, such as a cancelled trade. Technical NACKs describe invalid raw request data or internal failure, such as `Ratan internal error.`

The source does not define retry, ordering, duplicate-delivery, or idempotent replay behavior. `DUPLICATE_UTILIZE_ID` confirms that duplicate identifiers are validated, but not how the original outcome is handled.
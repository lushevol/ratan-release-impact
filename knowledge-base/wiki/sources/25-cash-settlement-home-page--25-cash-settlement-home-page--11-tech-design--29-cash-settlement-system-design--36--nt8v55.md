---
type: source
title: Cashflow Notification and Auto-Refresh Design
authors: []
year: 2025
url: ""
venue: "Cash Settlement technical design"
tags: [cash-settlement, cashflow, notifications, auto-refresh, query-service, ui]
related: [cashflow-blotter, cashflow-notification-and-auto-refresh, cashflow-version-tuple-comparison, entitlement-aware-ui-notifications, query-service, cash-settlement-cashflow-read-model, cashflow-blotter-query-performance, stella, ratan]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/cashflow notification.md"]
---

# Cashflow Notification and Auto-Refresh Design

## Summary

This design specifies event-driven notifications for the Cashflow Blotter and real-time handling of a cashflow that is open in a detail dialog. It proposes that new or updated cashflows be published with full cashflow data so the UI does not need to query the backend again.

The design distinguishes between:

- **Level 1 notifications:** updates applied to the blotter after the UI evaluates its active search and sorting conditions.
- **Level 2 notifications:** updates to the cashflow currently open in a detail dialog. The UI compares the incoming version with the displayed version and requires the user to refresh before continuing.

The primary operational objective is to make new cashflows visible without manual refresh, particularly for value-today cashflows and cashflows approaching a payment or operational cutoff.

This document describes design intent and proposed behavior. It does not provide implementation results, performance measurements, or acceptance-test evidence.

## Notice Payload Contract

| Attribute name | Type | Note |
|---|---|---|
| `cashFlowId` | string | Cashflow identity |
| `cashflowBusinessVersion` | int | Business version used for freshness comparison |
| `cashflowVersion` | int | Cashflow version used for freshness comparison |
| `cashflowMinorVersion` | int | Minor version used for freshness comparison |
| `cashFlowStatus` | string | Must use the cashflow status defined by the CN team Status Machine |
| `eventAction` | string | `CASHFLOW_UPDATE` or `CASHFLOW_CREATE` |
| `cashflow` | cashflow | Full cashflow information |

## Example Notification Envelope

```json
{
  "cashFlowId": "008690236384",
  "cashflowBusinessVersion": 0,
  "cashflowVersion": 0,
  "cashflowMinorVersion": 0,
  "eventAction": "CASHFLOW_CREATE",
  "cashFlowStatus": "PROJECTED",
  "cashflow": {
    "entity": {},
    "instrument_Common": {},
    "settlement_Instruction": {},
    "trade_Version": 0,
    "portfolio": {},
    "position_Id": "3690235984",
    "bcs_Trade_Id": "1816352",
    "trade_Id": "1816352",
    "trade_State": "VALIDATED",
    "data_Flow": {},
    "trade": {},
    "cashflow": {},
    "settlement_Method": "Cash",
    "delivery_Method": "",
    "parent_Trade_Id": "1816352",
    "bcs_Parent_Trade_Id": "1816352"
  }
}
```

## Nested Cashflow Field Contract

The example payload contains the following nested objects and field names. Casing and underscore conventions are part of the proposed contract.

### `entity`

```text
person
trader_PSID
event_Execution_Marketer_PSID
event_Coverage_Marketer_PSID
booking_Marketer_PSID
event_Booking_Marketer_PSID
event_Trader_PSID
coverage_Marketer_PSID
execution_Marketer_PSID
booking_Entity_General_Ledger_Business_Unit_Id
counterparty_Source_System_Entity_Id
general_Ledger_Business_Unit_Name
booking_Entity_SCI_FMCODE
booking_Entity_SCI_FMID
counterparty_SCI_FMID
counterparty_SCI_FMCODE
counterparty_CIF_Code
```

### `instrument_Common`

```text
isda_Taxonomy
cfi_Code
source_System_Instrument_Sub_Type
equity_Instrument_Reference
parent_Trade_Instrument
```

### `settlement_Instruction`

```text
charge_Bearer
ssi_Unique_Id
ssi_Source
ssi_Priority
sender_To_Receiver_Information_1
sender_To_Receiver_Information_2
sender_To_Receiver_Information_3
sender_To_Receiver_Information_4
sender_To_Receiver_Information_5
sender_To_Receiver_Information_6
remittance_Information_1
remittance_Information_2
remittance_Information_3
remittance_Information_4
nostro_Swift_Message_Type
swift_Payment_Method
swift_Message_Type
is_Third_Party_Payment
account
```

The nested `account` object includes settlement-account and party fields such as `beneficiary_BIC_code`, `beneficiary_Account_Number`, `beneficiary_Bank_Account_Number`, `booking_Entity_Correspondent_Account_Number`, `counterparty_CMS_Account_Number`, `ebbs_Account_Number`, `ebbs_Bridge_Account_Number`, `intermediary_Account_Number`, `ordering_Customer_Account_Number`, and their related names, addresses, cities, and BIC fields.

### `portfolio`

```text
booking_Entity_Trade_Portfolio_Unique_Name
booking_Entity_Trade_Portfolio_Name
```

### `data_Flow`

```text
data_Type
data_Sender
data_Source_System_Country_Code
data_Source_System_Domain_Name
data_Publication_Date_Time
unique_Identifier_Message_Id
data_Publication_Id
data_Source_System
```

### `trade`

```text
action_Type
trade_Lake_Raw_Event_Date_Time
trade_Lake_Valid_From_Date_Time
trade_Lake_Transaction_From_Date_Time
trade_Lake_Latest_Event_Date_Time
trade_Original_Source_System_Name
trade_Lake_Transaction_To_Date_Time
event_Physical_Status
trade_Lake_Valid_To_Date_Time
resultant_Position_Id
```

### Nested `cashflow`

```text
cashflow_Version
cashflow_Business_Version
cashflow_Event_Type
nstp_Reason
payer_Name
netting_Id
payment_Date
is_STP_RATAN
is_STP
payment_Type
event_Date
cashflow_Sub_State_Updater
cashflow_Id
payment_Date_Business_Day_Convention
payment_Receiver_Party_Reference
cashflow_Sub_State_Type
next_Cashflow_Id
exception_Reason
stp_Cutoff_Date_Time
prev_Cashflow_Id
validation_Status
payment_Payer_Party_Reference
status_Event_Type
payment_Currency
payment_Amount
cashflow_State
is_Private_Banking_Cashflow
is_Amended_Post_Settlement
is_Cashflow_Unnet
transaction_Details
pay_Receive_Indicator
execution_Date_Time
cashflow_Sub_State
cashflow_Affirmation_Status
cashflow_Minor_Version
bypass_Workflow_Indicator
is_Payment_Intent_To_Settle
netting_Cuttoff_Date
booking_Entity_SCI_FMCODE
payment_Cutoff_Time
cashflow_Audit_Version
minor_Version_Description
fmo_Comment
fmo_Comment_Updater
fmo_Comment_Timestamp
```

`transaction_Details` is represented in the source example as a Base64-encoded, compressed value. The design does not define its compression, decompression, size, or schema contract.

## Proposed UI Behavior

### Level 1

New records should appear at the top of the list and be visually highlighted with a color or column. The user should not need to refresh the blotter or acknowledge a pop-up. The UI applies current search and sorting conditions after receiving the notification.

The notification centre was deferred for later consideration because currency cutoff information would need to be overlaid.

### Level 2

When a cashflow open in a detail dialog changes, the UI should notify the user and require refresh. The refreshed cashflow must be reopened in its latest version, and allowable actions must be recalculated using the latest status and exceptions.

The approach diagram proposes an alert covering the dialog and forbidding all actions other than refresh. The requirements instead describe a Yes/No reload prompt, with “No” closing the cashflow. The authoritative interaction contract is unresolved.

## Security and Delivery Requirements

- Entitlements must apply to notifications.
- Full-data notifications must not expose settlement or cashflow information to unauthorized users.
- Client-side filtering is intended for presentation and must not replace authorization.
- The source defines `CASHFLOW_CREATE` and `CASHFLOW_UPDATE`, but does not define deletion, cancellation, replay, duplicate handling, ordering, missed-event recovery, acknowledgement, retry, or observability semantics.
- `unique_Identifier_Message_Id` is shown as `null` in the example, so a deduplication and traceability contract is still required.

## Example Values Relevant to Refresh

| Field | Example value | Relevance |
|---|---|---|
| `cashFlowId` | `"008690236384"` | Stable cashflow identity |
| `eventAction` | `"CASHFLOW_CREATE"` | Creation versus update |
| `cashFlowStatus` | `"PROJECTED"` | Status-dependent UI actions |
| `cashflowVersion` | `0` | Version comparison |
| `cashflowBusinessVersion` | `0` | Version comparison |
| `cashflowMinorVersion` | `0` | Version comparison |
| `cashflow_State` | `"PROJECTED"` | Nested cashflow state |
| `payment_Date` | `"2022-03-11"` | Value-date and cutoff context |
| `payment_Currency` | `"JPY"` | Currency context |
| `payment_Amount` | `"1000"` | Payment display |
| `data_Source_System` | `"Stella"` | Source-system provenance |
| `trade_State` | `"VALIDATED"` | Workflow and action eligibility |

## Open Specification Issues

The design requires clarification of:

1. Whether Level 2 refresh uses a Yes/No prompt or an OK-only mandatory refresh alert.
2. What happens to unsaved user changes.
3. Whether freshness is tuple inequality, monotonic ordering, or another domain-specific rule.
4. Where entitlement checks are enforced.
5. How `cashFlowStatus` maps to nested `cashflow_State`.
6. Whether delete, cancel, or withdrawal events are required.
7. How duplicate, delayed, out-of-order, and missed notifications are recovered.
8. Which transport, retry, replay, and observability guarantees apply.
9. Whether every entitled recipient may receive the full settlement-account payload.
10. What throughput and payload-size limits apply to auto-refresh.

## Related Wiki Pages

- [[entities/query-service]]
- [[entities/cashflow-blotter]]
- [[concepts/cashflow-notification-and-auto-refresh]]
- [[concepts/cashflow-version-tuple-comparison]]
- [[concepts/entitlement-aware-ui-notifications]]
- [[concepts/cash-settlement-cashflow-read-model]]
- [[concepts/cashflow-blotter-query-performance]]
- [[entities/stella]]
- [[entities/ratan]]
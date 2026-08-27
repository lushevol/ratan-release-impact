---
type: source
title: FXU RATAN Technical Design
authors: []
year: 0
url: "https://confluence.global.standardchartered.com/display/DSP/FXU+-+RATAN+analysis"
venue: Confluence
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, ratan, cash-settlement, foreign-exchange, technical-design, integration]
related: [fxu, ratan, razor, tds3, fx-utilization, fxu-message-driven-integration, fxu-utilization-validation, which-system-owns-fxu-transaction-coordination, does-mvp-support-partial-fx-utilization, what-is-the-authoritative-fxu-query-api-contract, cash-settlement-platform, cash-settlement-query-service-graphql-read-model, denormalized-cashflow-query-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# FXU RATAN Technical Design

## Summary

This technical design describes integration between FXU, RATAN, RAZOR, and TDS3 for foreign-exchange utilization within the Cash Settlement domain. It presents three alternative ownership models for accounting, exception management, FXU detail persistence, and synchronization transactions. The source does not record which option was selected.

The design also specifies an FXU Query API and message-driven utilization request and acknowledgement flows. The query API returns a nested cashflow, trade, instrument, entity, portfolio, and settlement-instruction projection. The messaging contract supports utilization identifiers, utilization types, trade versions, swap-leg selection, currency amounts, and ACK/NACK outcomes.

The detailed sections titled “Overall Architecture,” “Manual Utilize/Reverse,” and “Auto Utilize/Pastdue” are empty. Architecture diagrams are referenced as images, so sequencing and failure-handling details cannot be verified from the text.

## Integration options

| Option | Accounting | Swift | Exception management | FXU details persistence | Synchronization responsibility |
| --- | --- | --- | --- | --- | --- |
| 1 | RAZOR | RAZOR | FXU | RATAN, TDS3, FXU | FXU coordinates transactions among TDS3, RATAN, and FXU |
| 2 | RAZOR | RAZOR | RATAN | RATAN, TDS3, FXU | RATAN coordinates transactions among TDS3, RATAN, and FXU |
| 3 | RATAN | RAZOR | NA | RATAN | Existing cashflow-status hard block; TDS3 participates if remaining-amount synchronization requires transactional control |

These options change the system boundary for transaction coordination and exception management. They must not be interpreted as a single settled ownership model.

## FXU Query API

The documented API is a POST endpoint with the following environment-specific details:

```text
HOST
https://fmo-mfe-dev.uk.dev.net（DEV）

PATH
/api/ratan/stmcn/v1/cashflows

METHOD
POST

Headers
FMAA-Token：“string”
FMAA-UserId:"string"
FMAA-AppId:"string"
Bank-Id:"string"
Country：string"
```

The source documents the following GraphQL operation:

```graphql
query SettlementCashflowDataUtilizeQuery($payload: RatanUltraQuery!) {
  cashflowUtilizeQuery(payload: $payload) {
    totalResult
    pageIndex
    itemsPerPage
    lastPage
    results {
      Cashflow {
        Cashflow_Id
        Cashflow_Version
        Cashflow_Business_Version
        Cashflow_State
        Cashflow_Event_Type
        Cashflow_Sub_State
        Cashflow_Sub_State_Type
        Cashflow_Minor_Version
        Cashflow_Major_Version
        Payment_Currency
        Payment_Amount
        Remaining_Amount
        Payment_Type
        Payment_Date
        Pay_Receive_Indicator
      }
      Entity {
        Booking_Entity_SCI_FMCODE
      }
      Settlement_Method
      Trade {
        Settlement_Date
        Is_Client_Leg
        Trade_Date
        Trade_Id
        Trade_Version
        Trade_State
        Physical_Status
        Comments
        Base_Product
        Execution_Date_Time
        Buyer_Party_Reference
        Seller_Party_Reference
        Trade_Lake_External_Message_Id
        Trade_Lake_Trade_Major_Version
        Trade_Lake_Trade_Minor_Version
        Source_System_Trade_Internal_Id
        Transaction_Banking_Comments
        Trade_Event {
          Business_Event_Type
        }
        Cash_Financial_Instrument {
          Exchanged_Currency1_Payment_Amount_Currency
          Exchanged_Currency2_Payment_Amount_Currency
          Price
          Base_Currency
          Target_Currency
        }
        Forward_Future_Instrument {
          Exchanged_Currency1_Payment_Amount_Currency
          Exchanged_Currency2_Payment_Amount_Currency
          Forward_Price
          Quote_Basis
          Base_Currency
          Target_Currency
          FX_Leg {
            Far_Leg {
              Exchanged_Currency1_Payment_Amount_Currency
              Exchanged_Currency2_Payment_Amount_Currency
            }
            Near_Leg {
              Exchanged_Currency1_Payment_Amount_Currency
              Exchanged_Currency2_Payment_Amount_Currency
            }
          }
        }
        Swap_Instrument {
          Forward_Future_Instrument {
            Far_Leg {
              Base_Currency
              Quote_Basis
              Target_Currency
              Buyer_Party_Reference
              Seller_Party_Reference
              Forward_Price
              Exchanged_Currency1_Payer_Party_Reference
              Exchanged_Currency2_Receiver_Party_Reference
            }
            Near_Leg {
              Base_Currency
              Quote_Basis
              Target_Currency
              Seller_Party_Reference
              Buyer_Party_Reference
              Forward_Price
              Exchanged_Currency1_Payer_Party_Reference
              Exchanged_Currency2_Receiver_Party_Reference
            }
          }
        }
        Entity {
          Person {
            Coverage_Marketer_PSID
            Trader_PSID
            Execution_Initiator_PSID
            Booking_Marketer_Source_System_Person_Id
          }
          Booking_Entity_SCI_FMID
          Booking_Entity_Country_ISO_Code
          General_Ledger_Business_Unit_Name
          Counterparty_Name
          Counterparty_SCI_LEID
          Counterparty_SCI_FMID
        }
        Data_Flow {
          Data_Source_System
        }
        Portfolio {
          Booking_Entity_Trade_Portfolio_Name
        }
        Instrument_Common {
          ISDA_Taxonomy
        }
      }
      Settlement_Instruction {
        Account {
          SCB_Nostro_Account_Number
          SCB_Nostro_Account_Type
        }
      }
    }
  }
}
```

The MVP example filters on `Trade.Trade_Id` and requests 500 records. The Phase 2 example combines `Trade.Source_System_Trade_Internal_Id` with `Is_Client_Clearing_Trade`, or alternatively filters on `Trade_Id`, and requests 1,000 records. The source does not establish whether these field paths are aliases or whether the result is deduplicated.

## Message contracts

The inbound and acknowledgement topics are:

```text
Cash_Settlement_FXU_Request_In
Cash_Settlement_FXU_Ack
```

The request example is:

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

The response contains a `Utilization` result and an echoed `Request_Info` object:

```json
{
  "Utilization": {
    "Utilization_Id": "71110111046",
    "Response": "ACK",
    "Error_Reason": null
  },
  "Request_Info": {
    "Utilization": {
      "Utilization_Id": "71110111046",
      "Orig_Utilization_Id": "71110111041",
      "Util_Type": "VDATE-PART-REV",
      "AACode_Comments": "FX",
      "Util_Payment_Ref": "1",
      "Maker_ID": "1642375",
      "Checker_ID": "1376381",
      "Trade": {
        "Trade_Id": "7111011104",
        "Trade_Lake_Trade_Major_Version": "1",
        "Swap_Leg_ID": "",
        "Exchanged_Currency1_Payment_Amount_Currency": "USD",
        "Exchanged_Currency1_Util_Amount": "50.0",
        "Exchanged_Currency2_Payment_Amount_Currency": "SAR",
        "Exchanged_Currency2_Util_Amount": "187.5"
      }
    }
  }
}
```

## Validation and failure handling

The source distinguishes business NACKs, invalid request-data NACKs, and internal technical errors. Validation covers required identifiers and objects, trade and cashflow state, settlement means, value dates, available amounts, duplicate utilization identifiers, reverse operations, and product/cashflow consistency.

Important examples include:

```java
public static final String MVP_NO_REVERSE_UTILIZATION = "Currently reverse is not allowed.";
public static final String MVP_NO_EARLY_UTILIZATION = "Currently early utilization is not allowed.";
public static final String MVP_NO_PASTDUE_UTILIZATION = "Currently pastdue utilization is not allowed.";
public static final String MVP_NO_PARTIAL_UTILIZATION = "Currently partial utilization is not allowed.";
public static final String INVALID_UTILIZATION_REQ_STATUS = "Invalid utilization request status in Util_Type.";
public static final String UTILIZATION_ID_NOT_EMPTY = "Utilization_Id can not be empty.";
public static final String ORIGIN_UTILIZATION_ID_NOT_EMPTY = "Orig_Utilization_Id can not be empty.";
public static final String TRADE_ID_NOT_EMPTY = "Trade.Trade_Id can not be empty.";
public static final String TRADE_VERSION_NOT_EMPTY = "Trade.Trade_Lake_Trade_Major_Version can not be empty.";
public static final String SETTLEMENT_MEANS_OR_ACCOUNT_NOT_RIGHT = "Settlement means or account is not FXBRREC or FXBRREC-M.";
public static final String TRADE_IS_AMENDED = "Trade is amended.";
public static final String TRADE_IS_CANCELLED = "Trade is cancelled.";
public static final String RATAN_INTERNAL_ERROR = "Ratan internal error.";
public static final String REMAINING_AMOUNT_NOT_ENOUGH = "Remaining amount is not enough to util.";
public static final String DUPLICATE_UTILIZE_ID = "Duplicate utilizeId found.";
public static final String CASHFLOW_CNT_NOT_WRIGHT = "Cashflow count is not consistency with product.";
public static final String TRADE_CONTAINS_ERROR_CASHFLOW = "Trade contains error cashflow.";
```

## Evidence limitations and open questions

The source contains an internal tension: MVP validation rejects partial utilization, while an ACK example uses `VDATE-PART-REV` and partial amounts. The auto-utilization response is struck through and its detailed design section is empty. The documented host and linked path differ, the `Country` header example is malformed, and scalar types for amounts, prices, dates, and versions are not specified.

See [[does-mvp-support-partial-fx-utilization]], [[which-system-owns-fxu-transaction-coordination]], and [[what-is-the-authoritative-fxu-query-api-contract]] for tracked questions.
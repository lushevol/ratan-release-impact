---
type: source
title: Cash Settlement Korea Accounting Reconciliation — RATAN to TLM
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement — Payment Accounting"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea, accounting, reconciliation, RATAN, TLM, OLTP, eBBS, functional-requirement]
related: [ratan, tlm, aspire, oltp, ebbs, korea-accounting-reconciliation, ratan-accounting-reconciliation-api, accounting-posting-statuses, ebbs-accounting-message-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# Cash Settlement Korea Accounting Reconciliation — RATAN to TLM

## Summary

This functional requirement proposes an interim integration in which [[tlm]] queries accounting information from [[ratan]] for Korea reconciliation. The route is required because [[aspire]] cannot meet the Korea release timeline. The data is intended to include accounting entries sent to [[oltp]], including successful acknowledgements, rejections, and entries with no response.

The supported booking entity is `SCFB_SEOUL`, with FMID `10036645`. The query interval is limited to a maximum of three days.

## Request contract

The requirement defines the following request parameters:

| Parameter | Type and format | Mandatory | RATAN predicate |
|---|---|---:|---|
| `startReleaseTime` | `DateTime(yyyy-mm-dd HH24:MM:SS)`; convert to GMT | Yes | `ratan_accounting_request_task_history.created_at > startReleaseTime` |
| `fmidList` | `List<String>` | Yes | `ratan_accounting_request_task_history.booking_entity_fmid in fmidList` |
| `endReleaseTime` | `DateTime(yyyy-mm-dd HH24:MM:SS)`; convert to GMT | Yes | `ratan_accounting_request_task_history.created_at <= endReleaseTime` |

The implicit condition is:

```sql
ratan_accounting_request_task_history.task_status = 'SENT'
```

The source gives this intended request example:

```bash
curl -X GET "http://localhost:8080/v1/accounting/queryReconRecords/?fmidList=10036645&startReleaseTime=2026-04-02T00:00:00&endReleaseTime=2026-04-05T00:00:00"
```

The linked URL in the source instead contains FMIDs `10075222` and `10075223`, so that URL should not be treated as the authoritative Korea example.

## Accounting statuses

The API is described as returning `SUCCESS`, `SENT`, and `REJECTED` records. The wider accounting status model also contains `HOLD`, `MISSING_INFO`, and `DISABLED`.

- `HOLD`: an accounting entry is generated before the cashflow reaches value date and remains held.
- `MISSING_INFO`: mandatory information is unavailable; the source specifically mentions `SWIFT_SUPPRESSED` when the Nostro is unavailable.
- `DISABLED`: an accounting entry is generated but is not sent to OLTP, including settlement account `UIDD/UISUS` with settlement method `NOX`.
- `SUCCESS`: the entry is sent to OLTP and receives a `SUCCESS` response.
- `SENT`: the entry is sent to OLTP and has not received a response.
- `REJECTED`: the entry is sent to OLTP and receives a `REJECTED` response.

The relationship between the `SENT` task-history predicate and the three response statuses exposed to TLM is not defined.

## Response structure

The response envelope contains `totalNumberOfRecords`, an `accountingRecords` array, and a `publishTimestamp` for each accounting response. The source provides the following representative structure:

```json
{
  "totalNumberOfRecords": 1,
  "accountingRecords": [
    {
      "publishTimestamp": "2024-06-01 12:00:00",
      "message": {
        "data": {
          "id": "Field_Message_ID",
          "type": "post-transactions",
          "attributes": {
            "request": {
              "source-system": "RATAN",
              "posting-type": "FundsTransfer",
              "transaction-type": "RTN",
              "posting-branch": "Field_Posting_Branch",
              "external-system-key": "Cashflow.Cashflow_Id.Cashflow_Business_Version.Cashflow_Minor_Version",
              "transaction-currency": "Field_Transaction_Currency",
              "transaction-amount": "Field_Transaction_Amount",
              "transaction entry": [
                {
                  "value-date": "Field_Value_Date",
                  "account-number": "Field_eBBS_Nostro_Account",
                  "allow-insufficient-funds": "Y",
                  "casa-currency-code": "USD",
                  "transaction-code": "Field_Transaction_code",
                  "transaction-nature": "Field_eBBS_Nostro_DebitCredit"
                },
                {
                  "value-date": "Field_Value_Date",
                  "account-number": "Field_eBBS_Bridge_Account",
                  "allow-insufficient-funds": "Y",
                  "casa-currency-code": "USD",
                  "transaction-code": "Field_Transaction_code",
                  "transaction-nature": "Field_eBBS_Bridge_DebitCredit"
                }
              ]
            }
          }
        }
      }
    }
  ]
}
```

The two transaction entries are understood to represent Nostro and bridge-account legs, but the requirement does not formally specify leg ordering.

## Field and accounting mappings

- `Field_Message_ID` is a UUID with a maximum length of 50.
- `Field_Posting_Branch` is mapped from the booking entity FMID using RATAN static data.
- `Field_External_System_Key` is `Cashflow_Id.Business_Version.Minor_Version`.
- A new cashflow `C1` uses an external key such as `C1.1.1`; withdrawal creates a reversal key such as `C1.2.1`.
- `Field_Transaction_Currency` comes from `Cashflow.Payment_Currency` and is resolved through ISO currency static data, with special logic for SG CNH.
- `Field_Transaction_Amount` comes from `Cashflow.Payment_Amount`; SWIFT-equivalent rounding is required but marked low priority.
- `Field_Value_Date` comes from `Cashflow.Payment_Date` and must use `YYYY-MM-DD`.
- The Nostro account comes from `Settlement_Instruction.Account.EBBS_Account_Number`.
- The bridge account is looked up using `Entity.Booking_Entity_SCI_FMID` and the eBBS bridge-account mapping.
- The transaction code is selected from static data using posting branch and debit/credit direction.
- Nostro direction is `C` when the payer reference equals Party 1 and the cashflow event is `New`; otherwise it is `D`.
- Bridge direction is the inverse: `D` in that case, otherwise `C`.

## Narratives

| Field | Mapping |
|---|---|
| `narration1` | `"DV" + Branch code + cashflow ID` |
| `narration2` | `Party2.SCI.Entity.FM_CODE` |
| `narration3` | `Payment.Instrument_Common.ISDA_Taxonomy` |
| `narration4` | `Trade_Id + " " + Source_System_Trade_Internal_Id` |
| `narration5` | `Transaction_Banking_Comments`; blank for non-utilization |
| `narration6` | `Cashflow.Cashflow_State + " " + Data_Flow.Data_Source_System` |
| `EXTENDEDNARRATIVE1` | `Instrument_Common.Murex_Product_Strategy#Cashflow.Payment_Type#Cashflow.Netting_Id` |
| `EXTENDEDNARRATIVE2` | `Cashflow.splitParentId#Party1.Entity.Booking_Entity_SCI_FMID + " " + Party1.SCI.Entity.FM_CODE` |
| `EXTENDEDNARRATIVE3` | FXU payment reference, area code, maker ID, checker ID, and utilization status; blank for non-utilization, auto-utilization, and past-due cases |
| `EXTENDEDNARRATIVE4` | `Party2.Entity.Counterparty_SCI_FMID`; blank for non-split |
| `EXTENDEDNARRATIVE5` | `Party2.SCI.Entity.Counterparty_Long_Name` |
| `EXTENDEDNARRATIVE6` | `Portfolio.Booking_Entity_Trade_Portfolio_Name` |

## Korea static data

| Entity name | FMID | Country code | Branch code |
|---|---:|---|---:|
| `SCFB_SEOUL` | `10036645` | `KR` | `70` |

| Entity | FMID | Currency category | Bridge account |
|---|---:|---|---|
| `SCFB_SEOUL` | `10036645` | `KRW` | `000287` |
| `SCFB_SEOUL` | `10036645` | `FCY` | `040446` |

## Limitations and unresolved points

This document is a functional requirement, not evidence that the API has been deployed or production-validated. The status predicate, release-time versus `created_at` semantics, GMT conversion, timestamp format, request FMID example, CASA currency, and transaction-entry ordering require confirmation.

The future-state reference is Feature `11898201`, which describes onboarding reconciliation through `OLTP > ASPIRE > TLM` and decommissioning the RATAN-to-TLM route. The source does not define migration criteria or decommissioning ownership.

## References

- [Cash Settlements Migration - Korea - Scope & Plan](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3588497557#CashSettlementsMigrationKoreaScope&Plan-Objective:)
- [Feature 11898201](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11898201)
- [ADO 5967599](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5967599)
- [Korea Accounting - TLM Recon](https://confluence.global.standardchartered.com/display/DSP/Korea+Accounting+-+TLM+Recon)
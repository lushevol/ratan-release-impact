---
type: concept
title: eBBS Accounting Message Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [eBBS, accounting, message-mapping, cashflow, narratives, reversal, reconciliation]
related: [ratan, tlm, ebbs, korea-accounting-reconciliation, ratan-accounting-reconciliation-api, fxu-ratan-utilization-response-contract, netting-resultant-attribute-inheritance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# eBBS Accounting Message Mapping

This concept describes how RATAN cashflow data is mapped into the eBBS-style posting message consumed for Korea accounting reconciliation.

## Static and core fields

- The message ID is a UUID with maximum length 50.
- Posting branch is mapped from entity FMID through RATAN static data.
- Transaction currency comes from `Cashflow.Payment_Currency` and is resolved through ISO currency static data.
- Transaction amount comes from `Cashflow.Payment_Amount`; SWIFT-equivalent rounding is a low-priority requirement.
- Value date comes from `Cashflow.Payment_Date` in `YYYY-MM-DD` format.
- The Nostro account comes from `Settlement_Instruction.Account.EBBS_Account_Number`.
- The bridge account is looked up by `Entity.Booking_Entity_SCI_FMID` and currency category.
- Transaction code is selected using posting branch and debit/credit direction.

## External-system key versioning

The mandatory external-system key is:

```text
Cashflow.Cashflow_Id + "." +
Cashflow.Cashflow_Business_Version + "." +
Cashflow.Cashflow_Minor_Version
```

For example:

```text
New cashflow C1       -> C1.1.1
Withdrawal of cashflow C1 -> C1.2.1
```

This allows a withdrawal reversal to be distinguished from the original accounting entry.

## Two-leg direction logic

For the Nostro leg:

```text
If Cashflow.Payment_Payer_Party_Reference == party1
and Cashflow.Cashflow_Event_Type == New:
    return C
otherwise:
    return D
```

For the bridge leg:

```text
If Cashflow.Payment_Payer_Party_Reference == party1
and Cashflow.Cashflow_Event_Type == New:
    return D
otherwise:
    return C
```

The directions are inverse, but the requirement does not formally specify the ordering of the two transaction entries.

## Narrative mappings

| Field | Source mapping |
|---|---|
| `narration1` | `"DV" + Branch code + cashflow ID` |
| `narration2` | `Party2.SCI.Entity.FM_CODE` |
| `narration3` | `Payment.Instrument_Common.ISDA_Taxonomy` |
| `narration4` | `Trade_Id + " " + Source_System_Trade_Internal_Id` |
| `narration5` | `Transaction_Banking_Comments`; blank for non-utilization |
| `narration6` | `Cashflow.Cashflow_State + " " + Data_Flow.Data_Source_System` |
| `EXTENDEDNARRATIVE1` | `Instrument_Common.Murex_Product_Strategy#Cashflow.Payment_Type#Cashflow.Netting_Id` |
| `EXTENDEDNARRATIVE2` | `Cashflow.splitParentId#Party1.Entity.Booking_Entity_SCI_FMID + " " + Party1.SCI.Entity.FM_CODE` |
| `EXTENDEDNARRATIVE3` | FXU payment reference, area code, maker ID, checker ID, and utilization status |
| `EXTENDEDNARRATIVE4` | `Party2.Entity.Counterparty_SCI_FMID`; blank for non-split |
| `EXTENDEDNARRATIVE5` | `Party2.SCI.Entity.Counterparty_Long_Name` |
| `EXTENDEDNARRATIVE6` | `Portfolio.Booking_Entity_Trade_Portfolio_Name` |

`EXTENDEDNARRATIVE3` is related to utilization information, but [[fxu-ratan-utilization-response-contract]] does not establish that this API uses the FXU response contract. Similarly, inclusion of `Cashflow.Netting_Id` does not define netting behavior described by [[netting-resultant-attribute-inheritance]].
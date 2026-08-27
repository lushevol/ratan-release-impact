---
type: source
title: "Copy of Trade Confirmation & Cashflow STP - Deprecated"
authors: []
year: 2023
url: ""
venue: "Deprecated functional requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [deprecated, trade-confirmation, cashflow, stp, cdu-lake, ratan]
related: [trade-confirmation-driven-cashflow-stp, confirmation-status-normalization, confirmation-source-routing, trade-event-id-lineage, cashflow-suppression, cdu-lake, cdu-exceptor, cdu-ps, tds3, cfets, what-is-the-current-authoritative-confirmation-status-to-stp-mapping-for-ratan, what-is-the-authoritative-trade-confirmation-correlation-key-by-source-system, does-trade-cancellation-withdrawal-bypass-all-settlement-exception-checks, is-citinet-the-same-system-as-citynet-in-cdu-lake-confirmation-messages, what-is-the-current-fmrp-and-cfets-confirmation-status-source-and-eligibility-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# Copy of Trade Confirmation & Cashflow STP - Deprecated

> **Authority:** Deprecated. This document is historical evidence of intended confirmation-driven cashflow STP behavior and legacy message examples. It is not a current interface or business-rule contract without corroboration from active requirements.

## Historical scope

The document describes confirmation status as a key input to cashflow STP/NSTP processing in [[ratan]]. It distinguishes separate paths for Murex 2.11 and Stella trades, documents a historical CDU Lake status mapping, and identifies FMRP and CFETS as direct-Stella confirmation-source exceptions.

## Historical message flows

- **Murex 2.11 trade flow:** `Murex 2.11 → MQ → MLS → EDMI → CDU Exceptor`
- **Murex 2.11 confirmation reversal:** `CDU Exceptor → EDMI → MLS → MQ → Murex 2.11`
- **Stella trade flow:** `Stella/TDS3 → Solace → CDU PS`
- **Stella confirmation notification:** `CDU PS → Stella → TDS3 → Ratan`

[[cdu-lake]] is described as a confirmation-status consolidation layer. It sources Murex 2.11 paper statuses from [[cdu-exceptor]], Murex 2.11 SWIFT statuses from “CitiNet,” and Stella paper/SWIFT statuses from [[cdu-ps]] for FMRP. The source uses both **CitiNet** and **Citynet** spellings; their identity is unresolved.

## Historical STP status mapping

For Murex 2.11 paper and SWIFT notifications received through CDU Lake, Ratan was said to treat these `Confirmation_Status` values as **Confirmed** and allow cashflow STP:

- `Matched`
- `PairedDiscrepHost`
- `PairedDiscrepCounterparty`
- `PairedAutomatically`
- `PairedManually`
- `PairedPaper`
- `PairedPhone`

This deprecated source does not define the treatment of other statuses, reversals, duplicate messages, out-of-order messages, or status changes after STP.

## Historical correlation rules

| Population | Correlation identifier |
| --- | --- |
| Murex 2.11 paper | `Trade_ID` |
| Murex 2.11 SWIFT | `Trade_ID` |
| Stella | `Trade_Id + Trade Major Version` |

The different keys are relevant to [[trade-event-id-lineage]]. The Murex rule must not be applied to versioned Stella events without validation.

## Stella event and cashflow matrix

| Stella Trade Business Event | Stella Trade Action | Trade ID/Major Version | Cashflow Event/ID | Cashflow Major Version | CDU Confirmation Status | Cashflow STP With CDU Confirmation Status |
| --- | --- | --- | --- | --- | --- | --- |
| Trade | Book | T1 + V1 | New + C1 | V1 | T1 + V1 | Y |
| Trade | Cancel | T1 + V2 | Withdrawal + C1 | V2 | NA | 1. No confirmation status for trade withdrawal 2. Cashflow withdrawal event from trade cancellation is special STP case, wont' go to any settlement exception handling( SSI checking/NSTP checking/Suppression checking etc). |
| Withdrawal | Book | T1 + V2 | Withdrawal + C1 | V2 | NA | Same as above |
| Trade | Update | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| Amendment | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| PartialTermination | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| Termination | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | |
| Fixing | | | New | | NA | |
| Novation | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| CloseOut | Book | T1 + V1 | New + C1 | V1 | T1 + V1 | Y |
| PortfolioReassignment | Book | | Withdrawal(Old trade) | | Y | |
| Trade | Revive | T1 + V3 | Withdrawal + C2 New +C1 | V3 | Y | Y |
| Trade | Expiry | T1 + V1 | New +C1 | V1 | NA | 1. Cashflow would be filtered out from trade expiry |

The matrix is source-specific and incomplete. In particular, the `Fixing`, `PortfolioReassignment`, and `Trade Revive` rows are insufficiently specified for implementation. The cancellation-withdrawal bypass is a narrow historical claim relevant to [[cashflow-suppression]], not a global policy.

## FMRP and CFETS exceptions

The source states that, for [[fmrp]], confirmation status should be sourced directly from Stella rather than CDU Lake, using `AFFIRMED` and `CONFIRMED`.

For [[cfets]], the source similarly states that confirmation status should be sourced from Stella rather than CDU Lake, including `COMP`.

Neither statement defines effective dates, fallback behavior, asset-class scope, deployment state, or full eligibility logic.

## Preserved Murex 2.11 paper CDU Lake sample

```js
{ "Confirmation_Lake_Message_Id": "4e3463b3-c8e9-426c-b0bc-558c4272d251", "Source_System_Contract_Internal_Id": "86850476", "Trade_Id": "86850476", "Parent_Trade_Id": "", "Previous_Trade_Reference_Id": "", "Confirmation_Structure_Link_Id": "0", "Matching_Id": "", "Structure_Id": "0", "Unique_Swap_Identifier": "1030245409", "Unique_Transaction_Identifier": "SCBMUREX000000000000000086850476", "Unique_Swap_Identifier_Of_Counterparty": "", "Unique_Transaction_Identifier_Of_Counterparty": "", "Trade_Date": null, "Source_System_Event_Type": "New", "TP_System_Capture_Timestamp": null, "Booking_Entity_Trade_Portfolio_Name": "OP_GBL_RMB_FT2", "Trade_Source_System": "Murex", "Data_Source_External_System": "Hurricane", "Confirmation_Method": "PAPER", "Confirmation_Message_Outbound_Status": "Outbound Completed - Outbound Not Required", "Confirmation_Message_Outbound_Timestamp": null, "Confirmation_Message_Inbound_Status": "Inbound Completed - Inbound Not Required", "Confirmation_Message_Inbound_Timestamp": null, "Confirmation_Message_Type": "Confirmation", "Source_System_Instrument_Sub_Type": "ForeignExchange:FXO", "Instrument_Description": "Cash Settled Currency Option", "Source_System_Instrument_Type": "", "Counterparty_Country_ISO_Code": "HONG KONG", "Counterparty_Name": "STANDARD CHARTERED BANK (HONG KONG) LIMITED", "Counterparty_SCI_FMID": "2", "Counterparty_SCI_LEID": "11153358", "Booking_Entity_Country_ISO_Code": "CN", "Booking_Entity_Name": "STANDARD CHARTERED BANK (CHINA) LIMITED", "Booking_Entity_SCI_FMID": "400677737", "Booking_Entity_SCI_LEID": "11202982", "ISDA_Taxonomy": "ForeignExchange:VanillaOption", "Data_Publication_Id": "86850476", "Trade_Lake_Trade_Major_Version": "", "Trade_Lake_Trade_Minor_Version": "", "Trade_Version": "", "Position_Id": "", "Confirmation_System_Name": "CDU-Xceptor", "Confirmation_Lake_Trade_Id": "", "Trade_Lake_Correlation_Id": "", "Data_Publication_Date_Time": null, "System_Entry_Date": null, "Last_Updated_Date_Time": null, "Last_Updated_System_Name": "", "Trade_Id_Version": "", "Settlement_Type": "", "Confirmation_Status": "Matched", "Confirmation_Timestamp": "29:57.7", "Affirmation_Status": "", "Affirmation_Timestamp": "", "Adjusted_Termination_Date": null, "Fixed_Rate": "", "Initial_Floating_Rate": "", "Notional_Amount_Currency": "", "Notional_Amount": "", "Effective_Date": null, "Execution_Date_Time": "", "Action_Type": "", "External_Trade_Id": "", "Event_Id": "", "Event_Version": "", "Confirmation_System_Event_Type": "", "Tracking_Version": "", "CFI_Code": "", "Trade_State": "" }
```

## Preserved Murex 2.11 SWIFT CDU Lake sample

```js
{ "External_Trade_Id": "", "Confirmation_Message_Outbound_Timestamp": "", "Trade_Lake_Trade_Major_Version": "", "Fixed_Rate": "", "Trade_Source_System": "Murex", "Trade_Id": "86470586", "Source_System_Event_Type": "StatusChange", "Source_System_Instrument_Sub_Type": "", "Unique_Swap_Identifier_Of_Counterparty": "", "Counterparty_SCI_FMID": "", "Effective_Date": "", "Last_Updated_Date_Time": "", "Previous_Trade_Reference_Id": "", "Trade_Version": "", "Booking_Entity_Name": "", "Confirmation_System_Event_Type": "", "Confirmation_Lake_Message_Id": "919780eb-5f55-459d-b470-c3cd7424e409", "Instrument_Description": "", "Affirmation_Status": "", "Confirmation_Status": "PairedAutomatically", "Data_Source_External_System": "", "Structure_Id": "", "Settlement_Type": "", "Confirmation_Message_Type": "", "Trade_Id_Version": "", "Confirmation_Lake_Trade_Id": "", "Booking_Entity_Country_ISO_Code": "", "Data_Publication_Date_Time": "2023-04-27T02:32:36.871", "TP_System_Capture_Timestamp": "", "CFI_Code": "", "Unique_Transaction_Identifier_Of_Counterparty": "", "Confirmation_Message_Inbound_Status": "Paired", "Confirmation_Method": "Electronic", "Initial_Floating_Rate": "", "Notional_Amount_Currency": "", "Matching_Id": "", "Source_System_Contract_Internal_Id": "", "Affirmation_Timestamp": "", "Booking_Entity_SCI_FMID": "", "Notional_Amount": "", "Event_Version": "", "Position_Id": "", "Confirmation_Message_Outbound_Status": "Paired", "Unique_Transaction_Identifier": "", "Event_Id": "", "Confirmation_Message_Inbound_Timestamp": "", "System_Entry_Date": "2023-04-27T00:00", "Counterparty_Name": "", "Adjusted_Termination_Date": "", "Source_System_Instrument_Type": "", "Counterparty_SCI_LEID": "", "Trade_Lake_Correlation_Id": "", "Unique_Swap_Identifier": "", "Counterparty_Country_ISO_Code": "", "Trade_Lake_Trade_Minor_Version": "", "Trade_Date": "", "Action_Type": "", "Trade_State": "", "Execution_Date_Time": "", "Confirmation_System_Name": "Citynet", "Confirmation_Timestamp": "2023-04-27T02:32:35Z", "Parent_Trade_Id": "", "Booking_Entity_SCI_LEID": "", "Confirmation_Structure_Link_Id": "", "Last_Updated_System_Name": "", "Tracking_Version": "", "Booking_Entity_Trade_Portfolio_Name": "", "Data_Publication_Id": "UK-FM-citynet-5826098", "ISDA_Taxonomy": "Commodity:Metals:Precious:SpotFwd:Physical" }
```

## Preserved Solace topics

| Topic purpose | Solace topic |
| --- | --- |
| Track Solace Topic (Paper FX - status match) | `v1/conf/50505-cdu-cl/cdups/json-1.0/paper-fx/status-match/pub` |
| Track Solace Topic (Paper FX - status other) | `v1/conf/50505-cdu-cl/cdups/json-1.0/paper-fx/status-oth/pub` |
| Ratan Solace Topic (Electronic FX - status match) | `v1/conf/50505-cdu-cl/cdups/json-1.0/elec-fx/status-match/pub` |
| Ratan Solace Topic (Electronic FX - status other) | `v1/conf/50505-cdu-cl/cdups/json-1.0/elec-fx/status-oth/pub` |
| Track Solace Topic (Paper IRS - status match) | `v1/conf/50505-cdu-cl/cdups/json-1.0/paper-irs/status-match/pub` |
| Track Solace Topic (Paper IRS - status other) | `v1/conf/50505-cdu-cl/cdups/json-1.0/paper-irs/status-oth/pub` |
| Ratan Solace Topic (Electronic IRS - status match) | `v1/conf/50505-cdu-cl/cdups/json-1.0/elec-irs/status-match/pub` |
| Ratan Solace Topic (Electronic IRS - status other) | `v1/conf/50505-cdu-cl/cdups/json-1.0/elec-irs/status-oth/pub` |

These topic names are preserved historical data only. Their current availability and ownership require validation.
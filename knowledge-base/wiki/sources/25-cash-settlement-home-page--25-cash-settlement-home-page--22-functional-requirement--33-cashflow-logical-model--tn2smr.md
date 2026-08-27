---
type: source
title: Cashflow Logical Model Fields and Data Store
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, ratan, scbml, data-model, functional-requirements]
related: [scbml, stella, murex-2-11, ratan-settlement, tds3, cashflow-logical-model, scbml-cashflow-ingestion-and-persistence, intent-to-settle-payment-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# Cashflow Logical Model Fields and Data Store

## Scope

This functional-requirement document specifies how [[ratan-settlement|Ratan]] receives, transforms, persists, and displays inbound SCBML 4.0 cashflow data in the Stella/Murex 2.11 → [[tds3|TDS3]] → Ratan interface.

It is design evidence, not confirmation that the requirements have been implemented or production-validated.

## Required processing model

- Ratan converts newly inbound SCBML from Stella/Murex 2.11 and stores it in its local database.
- Ratan domain-service processing and FMO GUI actions create cashflow results, normally as new versions, which Ratan also stores locally.
- Storage and cashflow-blotter display are at the individual `<scb:cashflow>` level, not at the enclosing SCBML-message level.
- A `Withdrawal & New` message contains two cashflow events and must create two records and two blotter rows: one Withdrawal and one New.
- A `<scb:cashflow>` can contain multiple `<scb:payment>` elements, although the settlement platform processes one payment.

## Inbound template references

- New: `https://bitbucket.global.standardchartered.com/projects/FDM/repos/scbml-schema/browse/scbml/4-0/examples/SCBML-4-0/cashFlowPayload/cashFlowPayload-4-0/RATAN/Stella_Sample_SCBML-4-0_CashflowPayload-4-0-Cashflow_New.xml`
- Amendment: `https://bitbucket.global.standardchartered.com/projects/FDM/repos/scbml-schema/browse/scbml/4-0/examples/SCBML-4-0/cashFlowPayload/cashFlowPayload-4-0/RATAN/Stella_Sample_SCBML-4-0_CashflowPayload-4-0-Cashflow_Amendment.xml`
- Withdrawal: `https://bitbucket.global.standardchartered.com/projects/FDM/repos/scbml-schema/browse/scbml/4-0/examples/SCBML-4-0/cashFlowPayload/cashFlowPayload-4-0/RATAN/Stella_Sample_SCBML-4-0_CashflowPayload-4-0-Cashflow_Withdrawal.xml`
- Withdrawal & New: `https://bitbucket.global.standardchartered.com/projects/FDM/repos/scbml-schema/browse/scbml/4-0/examples/SCBML-4-0/cashFlowPayload/cashFlowPayload-4-0/RATAN/Stella_Sample_SCBML-4-0_CashflowPayload-4-0-Cashflow_New_Withdrawal.xml`

## Cashflow-event cardinality

| Message/template type | `<scb:cashflow>` elements per message | Required Ratan handling |
|---|---:|---|
| New | One | Persist and display one record. |
| Amendment | One | Persist and display one record. |
| Withdrawal | One | Persist and display one record. |
| Withdrawal & New | Two | Persist and display each event separately: one Withdrawal and one New. |

## Payment-selection rule

The source distinguishes settlement-bearing payments from informational or XVA payments through `scb:isIntentToSettle`. Its stated business rule is preserved below.

```text
If payment_Count>1

        If payment_Count with intendToSettle = True >1 or =0

        Then pick the 1st Payment

        Else If payment_Count with intendToSettle = True = 1

        Then remove payment with intendToSettle = False
Else Skip this check
```

A seven-payment example identifies FVA, CVA, and marketer-commission payments as `false`, while `TerminationFee` is `true`.

The specification does not state whether “remove” means removal from only the settlement-processing projection or also from raw-message retention, persistence, and GUI display. It also gives no exception or monitoring requirement when zero or multiple payments are marked `true`. See [[what-should-ratan-do-with-ambiguous-intent-to-settle-flags]] and [[are-non-settlement-payments-retained-in-ratan]].

## Key SCBML logical-model mappings

The following mappings preserve the field names, data types, and source paths for core lifecycle, payment, STP, and SSI attributes.

| Indexed Term | Data Type | Physical_Model_Field_Name / Derivation Logic |
|---|---|---|
| `Data_Flow.Data_Publication_Date_Time` | DateTime | `/scb:SCBML/scb:header/scb:originationDetails/scb:initiatedTimestamp` |
| `Data_Flow.Data_Publication_Id` | String | `/scb:SCBML/scb:header/scb:originationDetails/scb:trackingId` |
| `Data_Flow.Data_Source_System` | String | `/scb:SCBML/scb:header/scb:captureSystem` |
| `Data_Flow.Unique_Identifier_Message_Id` | String | `/scb:SCBML/scb:header/scb:originationDetails/ scb:uniqueIdentifierMessageId[@uniqueIdentifierMessageIdScheme="[http://www.sc.com/coding-scheme/uniqueIdentifierMessageId](http://www.sc.com/coding-scheme/uniqueIdentifierMessageId)"]` |
| `Cashflow.Cashflow_Id` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/ scb:header/scb:cashflowIdentifier/scb:cashflowId[@cashflowIdScheme="[http://www.sc.com/coding-scheme/cashflowId](http://www.sc.com/coding-scheme/cashflowId)"]` |
| `Cashflow.Cashflow_Version` | Integer | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowVersion` |
| `Cashflow.Cashflow_Business_Version` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:businessVersion` |
| `Cashflow.Cashflow_Major_Version` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowMajorVersion` |
| `Cashflow.Cashflow_Minor_Version` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowMinorVersion` |
| `Cashflow.Cashflow_Event_Type` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/ scb:header/scb:event[@eventScheme="[http://www.sc.com/coding-scheme/event/scbml-business-event](http://www.sc.com/coding-scheme/event/scbml-business-event)"]` |
| `Cashflow.Status_Event_Type` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/ scb:header/scb:event[@eventScheme="[http://www.sc.com/coding-scheme/event/scbml-business-event/Ratan](http://www.sc.com/coding-scheme/event/scbml-business-event/Ratan)"]` |
| `Cashflow.Payment_Currency` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/ scb:payment/conf:paymentAmount/conf:currency [@currencyScheme="[http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15](http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15)"]` |
| `Cashflow.Payment_Amount` | Decimal | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:amount` |
| `Cashflow.Payment_Date` | Date | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentDate/conf:unadjustedDate` |
| `Cashflow.Payment_Type` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentType` |
| `Cashflow.Netting_Id` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/ scb:header/scb:linkId[@linkIdScheme="[http://www.sc.com/coding-scheme/linkId/cashflow/nettingId](http://www.sc.com/coding-scheme/linkId/cashflow/nettingId)"]` |
| `Cashflow.Pay_Receive_Indicator` | String | `if Cashflow.Payment_Payer_Party_Reference=='Party1' then 'Pay' else 'Receive'` |
| `Cashflow.Is_Payment_Intent_To_Settle` | Boolean | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/scb:isIntentToSettle` |
| `Cashflow.Is_STP_RATAN` | Boolean | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:stpIndicator[@stpScheme="[http://www.sc.com/coding-scheme/STP/Ratan](http://www.sc.com/coding-scheme/STP/Ratan)"]` |
| `Cashflow.Is_STP` | Boolean | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:stpIndicator[@stpScheme="[http://www.sc.com/coding-scheme/STP](http://www.sc.com/coding-scheme/STP)"]` |
| `Cashflow.NSTP_Reason` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:nstpReason` |
| `Cashflow.Transaction_Details` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:transactionDetails` |
| `Cashflow.Cashflow_Event_Reason` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:eventReason[@eventReasonScheme=\"[http://www.sc.com/coding-scheme/eventReason](http://www.sc.com/coding-scheme/eventReason)\"]` |
| `Cashflow.Splitting_Id` | — | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:linkId[@linkIdScheme='[http://www.sc.com/coding-scheme/linkId/cashflow/splittingId']](http://www.sc.com/coding-scheme/linkId/cashflow/splittingId%27])` |
| `Settlement_Instruction.SSI_Unique_Id` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:SSIId` |
| `Settlement_Instruction.SSI_Source` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:sourceType` |
| `Settlement_Instruction.Swift_Message_Type` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/ scb:settlementInstruction[scb:partyReference/@href="party2"]/scb:settlementMessageType` |
| `Settlement_Instruction.Value_Date` | String | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href=\"party1\"]/scb:valueDate/conf:unadjustedDate"` |

## Enrichment and internal data

When Ratan receives a cashflow SCBML, it must query the [[tds3|TDS3]] trade API using **trade ID + trade version**. Attributes populated on the Stella/TDS3 trade ticket are then stored in the Ratan cashflow table for downstream functions.

The document further lists Ratan-owned or derived operational fields, including:

- netting and un-netting indicators;
- pending-fixing indicators and NDS parent-trade attributes;
- Ratan STP state, cutoffs, validation status, audit version, exception reason, and FMO comments;
- Murex structure and product attributes;
- SCI-derived counterparty fields;
- nostro, vostro, beneficiary, intermediary, remittance, and SWIFT-routing attributes;
- cashflow split and auto-splitting attributes; and
- `Cashflow.TargetFlow`, whose default is `STRATEGIC`, with non-strategic exceptions for LOANIQ and specified EG, NP, and SA booking-entity groups.

Several mapping rows are explicitly `TBC`, `NA`, blank, or marked as Ratan-managed. The supplied XPath-like paths also contain apparent formatting defects. The source should therefore be treated as a requirement inventory requiring schema and data-quality validation before use as an executable integration contract.

`Cashflow.Position_Id` is specifically marked “Do Not Use - TP System Specific Field”; downstream consumers must notify TDS3 and the FM Data Modelling teams before consuming it.

## Related topics

- [[scbml-cashflow-ingestion-and-persistence]]
- [[intent-to-settle-payment-selection]]
- [[cashflow-logical-model]]
- [[what-is-the-failure-policy-for-ratan-parent-trade-enrichment]]
- [[cash-settlement]]
- [[nostro-configuration]]
- [[straight-through-processing]]
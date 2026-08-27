---
type: concept
title: CN Payments Reporting Field Contract
created: 2026-08-24
updated: 2026-08-24
tags: [cn-payments, reporting, cashflow, murex-211, data-contract]
related: [murex-payment-mxml-to-scbml-transformation, murex-party-fmid-enrichment, murex-payment-pay-receive-derivation, murex-211, payment-date-versus-value-date]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# CN Payments Reporting Field Contract

## Scope

The CN Payments report inventory defines a reporting-oriented representation of Murex 2.11 cashflow data. It combines direct Murex fields, hard-coded source metadata, database and TDS3 enrichment, and derived business fields.

## Hard-coded fields

The proposal hard-codes:

- `Data_Flow.Data_Sender` as `Murex 2.11`.
- `Data_Flow.Data_Source_System` as `Murex 2.11`.
- `Data_Flow.Data_Source_System_Country_Code` as `All`.
- `Data_Flow.Data_Source_System_Domain_Name` as `FM`.
- `Data_Flow.Data_Type` as `CashflowData`.
- `Cashflow.Cashflow_Event_Type` as `New`.
- `Trade.Settlement_Method` as `CASH`.
- `Trade.Delivery_Method` as `CASH`.

## Direct and enriched fields

The inventory identifies:

- `FlowID` for `Cashflow.Cashflow_Id`.
- `Status` for `Cashflow.Cashflow_State`.
- `SysDate` for `Cashflow.Event_Date`.
- `Cur`, `Amount`, and `Value` for currency, amount, and payment date.
- Trade validation status for `Trade.Trade_State`.
- `TrnID` and `TrnRefID` for trade and parent-trade identifiers.
- Entity FMID and CPT FMID for party identifiers.
- `Portfolio` for the booking portfolio.
- Trader ID for `Entity.Person.Trader_PSID`.
- `Comment` as the proposed source for `Cashflow.Prev_Cashflow_Id`.

## Fields requiring derivation

The source marks the following as requiring derivation logic:

- Payer party reference.
- Receiver party reference.
- CFI code.
- ISDA taxonomy.
- Pay/receive indicator.
- Payer name.

The source also leaves payment type, publication ID, execution timestamp, business-unit name and code, portfolio unique name, entity display name, and action type insufficiently specified.

## Contract risks

The report event type is hard-coded to `New`, although the broader mapping defines New, Withdrawal, and Amendment. The report also maps payment date from `Value`, while the SCBML mapping maps it from Murex `releaseDate`; this distinction requires reconciliation.

The report inventory should be treated as an incomplete requirements baseline rather than a finalized schema.
---
type: source
title: Cashflow Details Page
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, functional-requirement, cashflow-details, field-mapping, ui]
related: [cashflow-blotter, cashflow-record, trade-record, cashflow-detail-field-projection, cashflow-status-lifecycle, what-are-the-authoritative-mappings-for-cashflow-details-page-unmapped-fields, what-are-the-valid-values-for-payment-payer-party-reference, what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Cashflow Details page.md"]
authors: []
year: 0
url: ""
venue: ""
---
# Cashflow Details Page

This functional requirement defines a Cashflow Blotter details view with separate **Trade Details** and **Cashflow Details** sections. It maps most displayed fields to logical-model paths and names three additional operational sections: Sub Status, Action History, and Exceptions.

The document does not identify an author, publication date, service/API source, or interaction behavior.

## Trade Details

| Trade Details | Attributes | Logical Model Path |
|---|---|---|
| Trade ID |  | Trade.Trade_Id |
| Trade Version |  | Trade.Trade_Version |
| Trade Status |  | Trade.Trade_State |
| Confirmation Status |  |  |
| Booking Entity |  | Entity.Booking_Entity_SCI_FMCODE |
| Coiunterpart |  | Entity.Counterparty_SCI_FMCODE |
| Portfolio |  | Portfolio.Booking_Entity_Trade_Portfolio_Name |
| Product Taxnomy |  | Instrument_Common.ISDA_Taxonomy |
| CFI Code |  | Instrument_Common.CFI_Code |

The source labels `Coiunterpart` and `Product Taxnomy` are preserved above as source evidence. In prose, these are referred to as **Counterparty** and **Product Taxonomy**.

## Cashflow Details

| Cashflow Details | Attributes | Logical Model Path |
|---|---|---|
| Cashflow ID |  | Cashflow.Cashflow_Id |
| Netting ID |  | Cashflow.Netting_Id |
| Cashflow Business Version |  | Cashflow.Cashflow_Business_Version |
| Cashflow Event |  | Cashflow.Cashflow_Event_Type |
| Cashflow Affirmation |  | Cashflow.Cashflow_Affirmation_Status |
| Value Date |  | Cashflow.Payment_Date |
| Currency |  | Cashflow.Payment_Currency |
| Amount |  | Cashflow.Payment_Amount |
| Pay/Receive |  | If Cashflow.Payment_Payer_Party_Reference=='party1' then 'Pay' Else 'Receive'. |
| Payment Cutoff |  |  |
| Cashflow Status |  | Cashflow.Cashflow_State |

## Additional UI Sections

```text
- Sub Status
- Action History
- Exceptions
```

## Interpretation Boundaries

The requirement establishes a consumer-facing field projection for [[cashflow-blotter]], drawing trade attributes from [[trade-record]] and cashflow attributes from [[cashflow-record]]. It does not establish whether the logical-model paths are direct persistence fields, service response fields, or frontend transformations.

`Cashflow.Cashflow_State` supplies Cashflow Status and is relevant to [[cashflow-status-lifecycle]]. The separate Sub Status section has no defined source or semantics. Likewise, Confirmation Status, Payment Cutoff, Action History, and Exceptions have no mapping or behavioral definition in this requirement.

The Pay/Receive rule is explicitly binary in the document: literal `party1` is displayed as `Pay`; every other value is displayed as `Receive`. The valid domain and null handling for `Cashflow.Payment_Payer_Party_Reference` remain unresolved.

This source may inform the consumer-side projection considered by [[what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]], but it does not identify an API or payload contract.
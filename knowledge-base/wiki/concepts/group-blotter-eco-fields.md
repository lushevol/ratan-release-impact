---
type: concept
title: Group Blotter Eco Fields
created: 2026-08-23
updated: 2026-08-23
tags: [group-blotter, eco-fields, data-model, cashflow, trade]
related: [group-blotter, cashflow-record, trade-record, scbml, what-is-the-authoritative-group-blotter-eco-field-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md"]
---
# Group Blotter Eco Fields

## Definition

Group Blotter Eco Fields are the trade-level and cashflow-level attributes identified for the 2026 [[entities/group-blotter]] requirements. The source distinguishes fields by record location and labels some trade attributes as either Eco fields or Special fields.

The inventory contains twelve fields:

- Eight fields associated with `Cashflow Record`.
- Four fields associated with `Trade Record`.

## Cashflow Record Fields

The cashflow-level inventory is:

- `Entity.Booking_Entity_SCI_FMID`
- `Entity.Counterparty_SCI_FMID`
- `Cashflow.Pay_Receive_Indicator`
- `Cashflow.Payment_Amount`
- `Cashflow.Payment_Currency`
- `Cashflow.Payment_Date`
- `Settlement_Method`
- `Portfolio.Booking_Entity_Trade_Portfolio_Name`

The source does not specify the physical source, join key, type, nullability, or whether any field is stored or derived.

## Trade Record Fields

The trade-level inventory is:

- `LIEN_Monitoring`, explicitly labelled an Eco field.
- `Contract_Typology`, labelled a Special field.
- `Linked_Package_Id`, labelled a Special field.
- `Swap_Agent_Id`, labelled a Special field.

The source does not define the distinction between Eco field and Special field in terms of visibility, governance, processing, or data ownership.

## Release and Version Provenance

`Settlement_Method` has a specific release-dependent sourcing note:

- In the SCBML version, the value is taken from the production `Cashflow Record`.
- In the Uber version, the value is taken from the `Cashflow Record` in the TB release.

This note applies only to `Settlement_Method`; it should not be generalized to the other fields.

`Portfolio.Booking_Entity_Trade_Portfolio_Name` is marked as to be released with RFI. Its availability should therefore be confirmed before it is treated as generally available.

## Relationship to Existing Processing Concepts

`LIEN_Monitoring` is related to [[concepts/lien-aware-netting-and-auto-unnetting]], [[concepts/lien-driven-cashflow-nstp]], and [[concepts/trade-lien-notification-reconciliation]]. The field inventory does not establish that it drives lien processing, netting, or NSTP.

`Swap_Agent_Id` provides an identifier-level connection to [[entities/swap-agent-clear-service]], [[entities/swap-agent-strategy]], and [[concepts/swap-agent-payment-hybrid-settlement]]. Its presence does not establish a settlement strategy or workflow rule.

The listed payment and trade attributes may support [[concepts/group-blotter-cashflow-state-lifecycle]] or [[concepts/bulk-manual-stp-group-blotter]], but this source does not define lifecycle transitions or STP eligibility.
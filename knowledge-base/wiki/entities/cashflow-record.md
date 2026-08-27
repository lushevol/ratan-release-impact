---
type: entity
title: Cashflow Record
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, record, group-blotter, cash-settlement]
related: [group-blotter, group-blotter-eco-fields, cashflow-group]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md"]
---
# Cashflow Record

## Group Blotter Fields

The 2026 Group Blotter requirements associate the following logical-model fields with `Cashflow Record`:

- `Entity.Booking_Entity_SCI_FMID`
- `Entity.Counterparty_SCI_FMID`
- `Cashflow.Pay_Receive_Indicator`
- `Cashflow.Payment_Amount`
- `Cashflow.Payment_Currency`
- `Cashflow.Payment_Date`
- `Settlement_Method`
- `Portfolio.Booking_Entity_Trade_Portfolio_Name`

The source does not define the physical record schema, field types, nullability, join keys, or ownership.

## Release Notes

`Settlement_Method` is sourced from the production `Cashflow Record` for the SCBML version and from the TB-release `Cashflow Record` for the Uber version.

`Portfolio.Booking_Entity_Trade_Portfolio_Name` is marked for release with RFI, and its availability is not confirmed by the source.
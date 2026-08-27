---
type: source
title: 2026 Group Blotter Eco Fields
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, group-blotter, eco-fields, functional-requirement]
related: [group-blotter-eco-fields, group-blotter, scbml, what-is-the-authoritative-group-blotter-eco-field-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md"]
---
# 2026 Group Blotter Eco Fields

## Summary

This functional-requirement document lists twelve fields intended for the 2026 Group Blotter. Eight fields are associated with `Cashflow Record` and four with `Trade Record`.

The document identifies field scope and limited release notes, but does not establish data types, nullability, valid values, join keys, UI behavior, processing rules, ownership, or implementation validation.

## Eco Fields List

| | Trade/Cashflow Record | Logical Model | Comment |
| --- | --- | --- | --- |
| 1 | Cashflow Record | Entity.Booking_Entity_SCI_FMID | |
| 2 | Cashflow Record | Entity.Counterparty_SCI_FMID | |
| 3 | Cashflow Record | Cashflow.Pay_Receive_Indicator | |
| 4 | Cashflow Record | Cashflow.Payment_Amount | |
| 5 | Cashflow Record | Cashflow.Payment_Currency | |
| 6 | Cashflow Record | Cashflow.Payment_Date | |
| 7 | Cashflow Record | Settlement_Method | SCBML Version value taken from Cashflow Record (in Production) Uber Version value taken from Cashflow Record (TB Released with Uber) |
| 8 | Cashflow Record | Portfolio.Booking_Entity_Trade_Portfolio_Name | (To be Released with RFI) |
| 9 | Trade Record | LIEN_Monitoring | Eco field |
| 10 | Trade Record | Contract_Typology | Special field |
| 11 | Trade Record | Linked_Package_Id | Special field |
| 12 | Trade Record | Swap_Agent_Id | Special field |

## Release Notes

`Settlement_Method` has release-specific sourcing notes. In the SCBML version, its value is taken from the production `Cashflow Record`. In the Uber version, its value is taken from the `Cashflow Record` in the TB release.

`Portfolio.Booking_Entity_Trade_Portfolio_Name` is marked as to be released with RFI. The source does not identify the RFI, release date, or validation status.

## Scope and Limitations

The field list should be treated as scope evidence for [[entities/group-blotter]], not as a complete data or processing contract. In particular, the source does not establish whether fields are displayed, searchable, sortable, filterable, mandatory, derived, or used as eligibility criteria for [[concepts/bulk-manual-stp-group-blotter]].

`LIEN_Monitoring` connects the field inventory to lien-related processing, but the source does not define its calculation or workflow effect. Similarly, `Swap_Agent_Id` identifies a Group Blotter field without proving that the Group Blotter applies any specific swap-agent settlement strategy.
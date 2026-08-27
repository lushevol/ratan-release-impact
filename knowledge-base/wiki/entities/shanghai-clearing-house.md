---
type: entity
title: Shanghai Clearing House
created: 2026-08-22
updated: 2026-08-22
tags: [clearing-house, SCH, cash-settlement, auto-netting]
related: [cash-settlement-home-page, ratan, cashflow-auto-netting, auto-netting-static-go-live-sequencing, net-over-net]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Shanghai Clearing House

Shanghai Clearing House, abbreviated as SCH in the source, is a counterparty scope for several bilateral auto-netting rules.

## Rule coverage

The source retains product-specific rules for:

- SCH IRS flows using `Instrument_Common__ISDA_Taxonomy` values or patterns for interest-rate swaps.
- SCH OPT flows using `CURR|OPT|SMP`.
- Eclipse Client Auto Netting for booking entity `10075222`, counterparty `400617196`, and `CURR|OPT|SMP`.

A generic Shanghai Clearing House rule is struck through in the source, while the product-specific IRS and OPT rules remain. The source does not conclusively state whether the generic production rule was disabled.

## Operational significance

The SCH rules illustrate the move from broad counterparty scope to product-specific auto-netting eligibility. An eOPS reference, `SCH202G210A1020925068966`, is associated with the Eclipse and commodity-related work.
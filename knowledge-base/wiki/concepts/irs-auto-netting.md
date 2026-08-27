---
type: concept
title: IRS Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [irs, automatic-processing, cashflow-netting, settlement]
related: [fmrp-china-cash-settlement, client-level-cashflow-netting, resultant-cashflow, component-cashflow, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# IRS Auto Netting

## Definition

IRS auto netting automatically nets the fixed and floating legs of an IRS trade when the value date is before `T+2`, according to the demonstrated scenario.

## Stated result

The fixed-leg and floating-leg cashflows become `Netted`, each with `Sub State Type` `NA`. A resultant cashflow is created with state `Queued`–`Waiting` and `Sub State Type` `Pending Exception`.

The source identifies IRS cashflows using trade and cashflow identifiers such as `N00000000201`, `N00000000202`, and `819255053125`–`819255053128`.

## Subsequent netting

The source also demonstrates manually netting two IRS-generated resultant cashflows. The four underlying component cashflows become `Netted`, the two auto-netting resultants become `Dead`, and a new resultant cashflow becomes `Waiting`.

These outcomes are scenario-specific and should not be generalized to other instrument types or netting paths.

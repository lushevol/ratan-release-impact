---
type: concept
title: Resultant Cashflow
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-netting, settlement, lifecycle]
related: [component-cashflow, client-level-cashflow-netting, irs-auto-netting, cashflow-status-and-substate-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Resultant Cashflow

## Definition

A resultant cashflow is a new cashflow created from one or more component cashflows during netting.

## Demonstrated lifecycle

For client-level netting, the source states that resultant cashflows initially appear as `Queued`–`Waiting`. For IRS auto netting, the resultant is `Queued`–`Waiting` with `Sub State Type` `Pending Exception`.

When two IRS-generated resultant cashflows are netted again, the two prior resultant cashflows become `Dead` and a new resultant cashflow becomes `Waiting`. This behavior is specific to the documented post-IRS scenario.

## Boundary

The source does not specify whether a resultant retains links to all components, how amounts are calculated, or how the lifecycle is represented in downstream systems.

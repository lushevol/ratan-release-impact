---
type: concept
title: Component Cashflow
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-netting, settlement, lifecycle]
related: [resultant-cashflow, client-level-cashflow-netting, irs-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Component Cashflow

## Definition

A component cashflow is an original cashflow included in a netting operation. It contributes to a resultant cashflow and is transformed by the operation.

## Demonstrated outcomes

In client-level netting, the source states that selected component cashflows become `Netted`. In IRS auto netting, both fixed and floating component legs become `Netted` with `Sub State Type` `NA`.

In the post-IRS netting scenario, four underlying component cashflows become `Netted`, while the two prior IRS resultant cashflows become `Dead`.

## Boundary

The source does not define whether `Netted` is terminal, whether component records remain queryable, or how reversals are handled.

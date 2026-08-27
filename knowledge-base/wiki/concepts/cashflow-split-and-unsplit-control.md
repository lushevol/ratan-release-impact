---
type: concept
title: Cashflow Split and Unsplit Control
tags: [cashflow, split, unsplit, reversal, nstp, settlement-control]
related: [ratan, cashflow-netting-and-auto-un-netting, released-settled-amendment-control, stella-trade-event-to-settlement-control]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# Cashflow Split and Unsplit Control

Split and unsplit control governs the treatment of a gross cashflow whose settlement has been divided into child cashflows.

## Unsettled split children

When split children are not released or settled, a cancellation or amendment of the parent gross cashflow triggers automatic un-splitting. The child cashflows move to cancelled end states, and the gross withdrawal is cancelled or superseded according to the event outcome. Only the latest replacement cashflow remains live after an amendment.

## Released or settled split children

When split children are released or settled, Ratan must not automatically undo their settlement. A withdrawal of the gross cashflow is created in `WAITING` and routed to NSTP for user action. For amendments, a replacement gross cashflow is also held for controlled processing.

This distinction prevents automated lifecycle actions from reversing already executed child payments without operational oversight.
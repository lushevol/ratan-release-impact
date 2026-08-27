---
type: concept
title: Rebook Exception
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, exception-management, rebook, cashflow, trade-amendment]
related: [ratan, murex, amendment-driven-cashflow-correlation, payment-date-proximity-matching, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# Rebook Exception

A rebook exception is a Ratan operational control raised for a prospective new cashflow that may have been created by a trade amendment after the original cashflow was released.

The intended amendment flow contains two controlled events:

1. The original cashflow is withdrawn and receives a reversal exception.
2. The replacement cashflow receives a rebook exception.

Operations users validate the withdrawal and replacement cashflows before release.

## Current Ratan detection

Ratan does not have a direct linkage between original and replacement cashflows. It identifies possible rebooks through [[payment-date-proximity-matching]]: a comparator cashflow must share the applicable Trade ID, have the same currency, already be released or settled, and fall within the configured payment-date window.

For Murex cashflows, the relevant identity is Murex Original Trade ID. This is an input to Ratan's heuristic; it is not evidence that [[murex]] provides authoritative amendment lineage.

As of the 2026-05-30 production deployment, the documented payment-date window is five days. This rule should be understood as a candidate-selection control, not confirmed proof of a rebook relationship.
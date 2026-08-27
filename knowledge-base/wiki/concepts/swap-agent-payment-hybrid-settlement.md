---
type: concept
title: Swap Agent Payment Hybrid Settlement
created: 2026-08-23
updated: 2026-08-23
tags: [swap-agent, hybrid-settlement, accounting-only, bilateral-settlement, cashflow-processing]
related: [swap-agent-clear-service, swap-agent-strategy, murex-three-trade-swap-agent-booking-model, swap-agent-cashflow-swift-suppression, ratan-netting-rule-check, nostro-static-data-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# Swap Agent Payment Hybrid Settlement

Swap Agent Payment Hybrid Settlement is the proposed processing model in which settlement eligibility and accounting generation are deliberately separated for cashflows within one economic arrangement.

## Required treatment

Only the initial and final principal payments from Trade 2 are intended to settle bilaterally with the client.

The following flows must bypass bilateral settlement but still generate accounting:

- Trade 1 interim coupons and dummy initial/final principal payments.
- Trade 2 interim principal payments.
- Trade 3 dummy principal payments.

All scoped flows are intended to generate accounting on the Main Nostro account. The source explicitly requires no netting.

## Control boundary

Settlement suppression must not mean dropping a cashflow. The required outcome is an accounting-only cashflow with no bilateral settlement or SWIFT settlement output. This creates a dependency on reliable classification, exception handling, and reconciliation in [[ratan]].

The source is a functional proposal. It does not provide implementation or test evidence, Main Nostro mapping details, or the enforcement mechanism for the no-netting exception.
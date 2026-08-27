---
type: entity
title: Swap Agent Clear Service
created: 2026-08-23
updated: 2026-08-23
tags: [swap-agent, payment-clearing, cash-settlement]
related: [swap-agent-payment-hybrid-settlement, swap-agent-cashflow-swift-suppression, ratan, murex-211]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# Swap Agent Clear Service

The Swap Agent clear service is the external or business payment-clearing service referenced by the Swap Agent Payment functional requirement.

Interim coupons and interim principal payments are intended to be cleared through this service rather than settled bilaterally with the client. In RATAN, those cashflows are intended to bypass settlement processing while retaining accounting generation.

The source does not identify the service provider, interface, confirmation process, payment-status model, or reconciliation controls.
---
type: query
title: How Does Trade 3 Offset Trade 1 Dummy Principal Payments?
created: 2026-08-23
updated: 2026-08-23
tags: [murex-2-11, swap-agent, dummy-principal, trade-booking, accounting-reconciliation]
related: [murex-three-trade-swap-agent-booking-model, swap-agent-payment-hybrid-settlement, murex-211, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# How Does Trade 3 Offset Trade 1 Dummy Principal Payments?

The source says that Trade 3 books “opiate payments” to knock off Trade 1 dummy principal payments. However, the displayed Trade 3 dummy payment amounts and signs match the displayed Trade 1 dummy payments, so the tabulated data does not demonstrate an offset.

## Evidence needed

- Payment currencies and direction for both trades.
- Leg and payer/receiver attributes.
- Accounting debit/credit sign conventions.
- Whether “opiate” is the intended term or a typo for “opposite.”
- Lifecycle timing and cancellation or offset semantics.
- Payment-level and accounting-level reconciliation evidence.

This clarification is required to assess whether Trade 3 creates an economic, settlement, accounting, or merely booking-structural offset.
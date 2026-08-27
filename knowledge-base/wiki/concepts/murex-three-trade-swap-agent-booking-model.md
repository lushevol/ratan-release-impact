---
type: concept
title: Murex Three-Trade Swap Agent Booking Model
created: 2026-08-23
updated: 2026-08-23
tags: [murex-2-11, trade-booking, swap-agent, cross-currency-swap, workaround]
related: [murex-211, swap-agent-strategy, swap-agent-payment-hybrid-settlement, how-does-trade-3-offset-trade-1-dummy-principal-payments]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# Murex Three-Trade Swap Agent Booking Model

The Murex Three-Trade Swap Agent Booking Model is a proposed package-booking workaround for a claimed [[murex-211]] limitation. The source states that one trade cannot generate the required combination of bilateral initial/final principal flows and Swap Agent-cleared interim flows.

## Trade responsibilities

- **Trade 1:** Generates interim coupons under a Vanilla X-ccy swap typology, but also generates unwanted dummy principal flows.
- **Trade 2:** Generates bilateral initial and final principal flows under RFR CCS MTM Fixing, plus accounting-only interim principal flows.
- **Trade 3:** Is stated to create “opiate payments” to knock off Trade 1 dummy principal flows.

All illustrated trades carry the `SWAP_AGENT` strategy and are presented as one package.

## Qualification

The documented limitation is a functional requirement claim, not vendor-confirmed evidence of a universal Murex product limitation. The source also does not demonstrate Trade 3 offset mechanics: its displayed dummy-flow amounts and signs match those of Trade 1. Currency, direction, leg, and accounting-sign semantics are needed to validate the claimed offset.
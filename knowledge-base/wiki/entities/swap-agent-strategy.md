---
type: entity
title: SWAP_AGENT Strategy
created: 2026-08-23
updated: 2026-08-23
tags: [strategy, swap-agent, cashflow-classification, murex]
related: [swap-agent-payment-hybrid-settlement, murex-three-trade-swap-agent-booking-model, swap-agent-cashflow-swift-suppression, murex-211, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# SWAP_AGENT Strategy

`SWAP_AGENT` is the strategy identifier used on all illustrated trades in the proposed three-trade Swap Agent Payment package.

The source implies that this classification is relevant to settlement treatment, accounting-only processing, SWIFT suppression, and no-netting treatment. It does not establish whether `SWAP_AGENT` itself is the enforcement key in Murex or RATAN, nor whether more granular cashflow-level classifications are required.
---
type: concept
title: Swap Agent Cashflow SWIFT Suppression
created: 2026-08-23
updated: 2026-08-23
tags: [swift, suppression, swap-agent, ratan, accounting-only, settlement-control]
related: [ratan, murex-211, swap-agent-payment-hybrid-settlement, fmswg-swift-message-validation, swift-message-reconciliation, ssi-driven-swift-field-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# Swap Agent Cashflow SWIFT Suppression

Swap Agent Cashflow SWIFT Suppression is the proposed RATAN behavior for cashflows classified upstream as “Swap Agent non settle.”

RATAN is intended to:

1. Consume “Swap Agent settle” and “Swap Agent non settle” classifications from [[murex-211]].
2. Generate bilateral settlement output only for Trade 2 initial and final principal payments.
3. Suppress SWIFT settlement output for all other scoped cashflows.
4. Retain accounting generation for suppressed cashflows.

## Required distinction

The control must distinguish Trade 2 bilateral principal payments from Trade 2 interim principal payments. A trade-level suppression rule would be insufficient if it suppresses the required initial or final bilateral payment.

`SUPPRESSXXX` is named in the source but its level of application, relationship to Vostro configuration, and precedence against settlement classifications are unresolved. This source must not be treated as evidence that the separate `SUPPRESSXXX` MT604 control issue was remediated.

## Reconciliation requirement

Deliberate non-generation must be distinguishable from failed, missing, duplicated, or manually deleted SWIFT messages. The source identifies no operational monitoring, reconciliation, replay, idempotency, or exception workflow.
---
type: query
title: Does SUPPRESSXXX Apply to All of Trade 2 or Only Swap Agent Non-Settle Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [suppressxxx, swap-agent, murex-2-11, ratan, settlement-suppression, vostro]
related: [swap-agent-cashflow-swift-suppression, swap-agent-payment-hybrid-settlement, murex-211, ratan, was-the-suppressxxx-mt604-control-defect-remediated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# Does SUPPRESSXXX Apply to All of Trade 2 or Only Swap Agent Non-Settle Cashflows?

The proposed solution says that Murex needs to assign `SUPPRESSXXX` on Trade 1 and Trade 2, while assigning a normal Vostro on Trade 2. This appears to conflict with the requirement that Trade 2 initial and final principal payments settle bilaterally.

## Questions to resolve

- Is `SUPPRESSXXX` applied at trade, leg, cashflow, SSI, Vostro, or downstream instruction level?
- Does its effect vary by payment type or settlement classification?
- How can Trade 2 interim principal be suppressed without suppressing Trade 2 initial and final bilateral principal?
- What does “assign normal Vostro on trade 2” mean when the source also states that distinct Vostro assignments are not supported for the same entity, counterparty, and currency?
- Is this `SUPPRESSXXX` configuration the same control as the one referenced by [[was-the-suppressxxx-mt604-control-defect-remediated]]?

No equivalence with the MT604 control issue should be assumed without configuration evidence.
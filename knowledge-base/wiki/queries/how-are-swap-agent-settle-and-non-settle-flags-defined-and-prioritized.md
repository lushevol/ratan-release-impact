---
type: query
title: How Are Swap Agent Settle and Non-Settle Flags Defined and Prioritized?
created: 2026-08-23
updated: 2026-08-23
tags: [swap-agent, murex-2-11, ratan, settlement-classification, interface-contract]
related: [swap-agent-cashflow-swift-suppression, swap-agent-payment-hybrid-settlement, murex-211, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# How Are Swap Agent Settle and Non-Settle Flags Defined and Prioritized?

The functional requirement proposes that RATAN consume “Swap Agent settle” and “Swap Agent non settle” flags from Murex 2.11, but it does not define them.

## Questions to resolve

- What are the exact Murex fields, values, and permitted combinations?
- Are classifications assigned at package, trade, leg, cashflow, account, or payment-instruction level?
- How are the classifications transported to RATAN and at what lifecycle events?
- What data lineage proves that a RATAN decision used the intended upstream classification?
- What precedence applies when these flags conflict with `SUPPRESSXXX`, Vostro, SSI, product, or standard settlement rules?
- How are Trade 2 initial and final principal flows protected from accidental suppression?

The answer is required before the proposed suppression model can be safely designed or tested.
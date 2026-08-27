---
type: query
title: How Does RATAN Prevent Netting and SWIFT Generation for Swap Agent Non-Settle Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, swap-agent, netting, swift-suppression, accounting-only, controls]
related: [swap-agent-payment-hybrid-settlement, swap-agent-cashflow-swift-suppression, ratan-netting-rule-check, nds-netting, swift-message-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# How Does RATAN Prevent Netting and SWIFT Generation for Swap Agent Non-Settle Cashflows?

The source requires that Swap Agent non-settle cashflows remain accounting-only, produce no SWIFT settlement output, and are not netted. It does not specify the RATAN controls that enforce those requirements.

## Questions to resolve

- Which RATAN rule or classification prevents netting for `SWAP_AGENT` cashflows?
- How does the no-netting treatment interact with standard [[ratan-netting-rule-check]] and [[nds-netting]] precedence?
- Which component suppresses SWIFT generation while allowing accounting generation?
- What tests prove that Trade 2 interim principal is suppressed while Trade 2 initial/final principal remains eligible for bilateral settlement?
- What monitoring and reconciliation identify intentional suppression separately from operational failure?
- How do replay, duplicate delivery, cancellation, and manual-repair events preserve the intended treatment?

Implementation and production-control evidence is required.
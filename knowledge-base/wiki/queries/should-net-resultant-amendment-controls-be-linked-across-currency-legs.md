---
type: query
title: Should Net Resultant Amendment Controls Be Linked Across Currency Legs?
tags: [netting, amendment, cross-currency, resultant-cashflow, settlement-control]
related: [cashflow-netting-and-auto-un-netting, stella-trade-event-to-settlement-control, ratan]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# Should Net Resultant Amendment Controls Be Linked Across Currency Legs?

The source asks whether amendment or cancellation controls for net resultant cashflows can be evaluated independently, or whether linked currency legs of a cross-currency swap must be controlled together.

## Decision needed

For a USD/CNO cross-currency swap, define whether release or settlement status is assessed:

1. Per individual net resultant cashflow;
2. Across all linked currency legs; or
3. By another trade-level grouping.

The decision determines when automatic un-netting is allowed, when manual netting is mandatory, and whether a partial reversal can create economic or operational risk.
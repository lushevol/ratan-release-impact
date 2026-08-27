---
type: concept
title: "Resultant Hard-Blocker Stamping"
created: 2026-08-22
updated: 2026-08-22
tags: [netting, resultant-cashflow, hard-blocker, data-propagation, swap-agent]
related: [swap-agent-coupon-interim-mtm-hard-blocker, netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, ratan-cash-settlement-netting-service, ratanone-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md"]
---
# Resultant Hard-Blocker Stamping

Resultant hard-blocker stamping preserves a component-level release restriction when cashflows are aggregated through netting.

For the `SWAP_AGENT` hard-blocker design, a resultant is marked when any component cashflow has product strategy `SWAP_AGENT` and payment type `Coupon` or `Interim MTM`. The marker is transported through the cashflow payload and exposed to the rule engine:

```text
scb:isHardBlocker
→ Cashflow__Is_Hard_Blocker
→ EnhancedFact.Cashflow__Is_Hard_Blocker
```

The NSTP rule can then identify either a qualifying gross cashflow or any marked resultant:

```text
(Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT"
 && Cashflow__Payment_Type in ("Coupon", "Interim MTM"))
|| Cashflow__Is_Hard_Blocker == true
```

This pattern ensures that release prevention survives aggregation without requiring rule users to parse component strategy and payment-type strings. It is specific to the design described in [[swap-agent-coupon-interim-mtm-hard-blocker]] and should not be assumed to apply to other resultant-cashflow controls.
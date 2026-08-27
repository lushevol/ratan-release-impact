---
type: query
title: What Is the Clearing Swift Suppress Resultant Semantics?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-auto-netting, clearing, swift-suppression, resultant-cashflow]
related: ["clearing-resultant-swift-suppression", "clearing-swift-suppression", "cashflow-auto-netting", "netting-resultant-cashflow", "auto-netting-resultant-nstp"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting.md"]
---
# What Is the Clearing Swift Suppress Resultant Semantics?

The `Clearing_Swift_Suppress` netting type has conflicting descriptions in the functional requirement.

The main mapping assigns the resultant field:

```text
{"Cashflow__Payment_Type":"Bilateral Netting"}
```

However, the later review requests SWIFT suppression for clearing netting resultants, including a `SWAP_AGENT` single-cashflow case. The same review also says a single cashflow with no partner is reinstated to the main flow, without conclusively defining whether it remains SWIFT-suppressed.

Clarify:

1. The canonical resultant payment type for `Clearing_Swift_Suppress`.
2. Whether every resultant is automatically SWIFT-suppressed.
3. Whether a single unmatched cashflow is released, reinstated, SWIFT-suppressed, or subject to a distinct lifecycle.
4. Whether LCH requires a separate netting type rather than reuse of this behavior.
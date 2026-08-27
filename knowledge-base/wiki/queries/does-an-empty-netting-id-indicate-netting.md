---
type: query
title: Does an Empty Netting ID Indicate Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [netting, cashflow, swap-agent, business-rule]
related: [swap-agent, auto-netting, rfr-payment-type-classification, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# Does an Empty Netting ID Indicate Netting?

The technical design classifies a payment as `Netting` when its type is `Interim MTM` or `Coupon`, strategy is `SWAP_AGENT`, and `Cashflow.Netting_Id` is empty or null.

```text
Cashflow.Payment_Type in ("Interim MTM", "Coupon") AND
Instrument_Common.Murex_Product_Strategy == "SWAP_AGENT" AND
(Cashflow.Netting_Id == "" OR Cashflow.Netting_Id == null)
```

This appears semantically inverted because a populated netting ID normally indicates membership in a netting group.

## Questions

- Is this an intentionally named eligibility or processing classification rather than netting-group membership?
- Should the empty/null condition instead test for a populated `Cashflow.Netting_Id`?
- Which behavior should apply to SWIFT-suppressed coupon and interim MTM cashflows?
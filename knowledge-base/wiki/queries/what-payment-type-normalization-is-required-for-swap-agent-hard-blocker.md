---
type: query
title: "What Payment-Type Normalization Is Required for the SWAP_AGENT Hard Blocker?"
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, hard-blocker, payment-type, data-quality, netting]
related: [swap-agent-coupon-interim-mtm-hard-blocker, ratan-cash-settlement-netting-service, auto-netting-rule-check]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md"]
---
# What Payment-Type Normalization Is Required for the SWAP_AGENT Hard Blocker?

The hard-blocker rule and acceptance cases use the canonical values `Coupon` and `Interim MTM`. A representative BIC netting request in the same source uses `paymentType: "Coup11on"` and omits the newly required `murexProductStrategy`.

Confirm whether payment types are canonicalized before hard-blocker validation, whether `Coup11on` is a source typo or recognized upstream value, and whether strategy is enriched server-side when absent from the request.
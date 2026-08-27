---
type: query
title: What Is the Authoritative H1-H2 Historical Group Identity and Cutover Rule?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, h1, h2, cutover, group-identity]
related: [h1-booking-model, h2-booking-model, h1-h2-historical-cashflow-group-continuity, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
---
# What Is the Authoritative H1-H2 Historical Group Identity and Cutover Rule?

The scenario source requires H2 events to find groups established under H1, but it does not identify the field or fields that constitute durable group identity across the booking-model transition.

## Questions to Resolve

- What exactly changed between H1 and H2 booking models?
- Which fields form the cross-model group key?
- Is `C2` an intentional lookup anchor, or are repeated “Find C2” statements copy/paste errors?
- What are the go-live timestamp, timezone, and business-date rules?
- Is `MxSystemDate <= VD <= MxSystemDate+9` the complete H1 eligibility rule?
- Are the Case 3 and Case 4 date mismatches intentional replay or backdating behavior?

The source supports the continuity intent recorded in [[h1-h2-historical-cashflow-group-continuity]], but does not supply an authoritative contract.
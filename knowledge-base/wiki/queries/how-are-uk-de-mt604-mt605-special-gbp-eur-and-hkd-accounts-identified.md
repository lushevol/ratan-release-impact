---
type: query
title: How Are UK/DE MT604 and MT605 Special GBP, EUR, and HKD Accounts Identified?
tags: [query, mt604, mt605, uk, germany, static-data, swift]
related: [ratan, murex, swift-block-2-receiver-derivation, nostro-static-data]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# How Are UK/DE MT604 and MT605 Special GBP, EUR, and HKD Accounts Identified?

The UK/DE review requests confirmation of the special field 56/57 account-identification rules:

- GBP: `//SC[Account number]`
- EUR: `//TR[Account number`
- HKD: to be confirmed by Pradeesh.

The Murex team and static-data owner need to confirm the canonical patterns, validation rules, and their application in RATAN.
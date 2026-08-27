---
type: concept
title: Clearing/SWIFT Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [SWIFT, suppression, clearing, auto-netting, netting-resultant]
related: [cashflow-auto-netting, swift-versus-cashflow-suppression, net-over-net, auto-netting-static-go-live-sequencing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Clearing/SWIFT Suppression

Clearing/SWIFT suppression combines clearing-specific auto-netting with suppression of duplicate or unnecessary SWIFT messages.

## Matching model

The source uses two principal branches:

- A cashflow has a populated `Cashflow__Netting_Id`.
- A cashflow has no netting ID but is marked `Cashflow__Is_Auto_Netting == true`.

This allows suppression to cover both multi-cashflow netting resultants and single cashflows processed by an auto-netting rule.

## Clearing scopes

The process includes LCH, CME, EUREX, JSCC, ICE, TAIFEX, and CITIC. The TAIFEX update explicitly excludes non-auto-netted IRS netting cashflows from one existing branch and adds them when they are auto-netted.

The CITIC update has a pre-update condition but no post-update condition in the source, so its final suppression semantics remain unconfirmed.
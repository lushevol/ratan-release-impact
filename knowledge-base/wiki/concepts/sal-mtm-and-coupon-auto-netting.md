---
type: concept
title: SAL MTM and Coupon Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [sal, swap-agent, auto-netting, swift-suppression]
related: [cashflow-auto-netting, swift-versus-cashflow-suppression, netting-resultant-cashflow, clearing-resultant-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md"]
---
# SAL MTM and Coupon Auto Netting

SAL auto netting is the documented UAT configuration for Swap Agent cashflows. It distinguishes `Interim MTM` and `Coupon` inputs, producing SAL-specific payment types rather than general bilateral-netting resultants.

## Eligibility and configured timing

The documented static rules both run at `01:00 GMT on VD` and assign `NSTP for Maker+Checker`.

- Rule `7351573889412694016` selects `SWAP_AGENT` `Interim MTM` cashflows with no `Netting_Id`; its netting type is `SAL MTM NETTING`.
- Rule `7351574062254944256` selects `SWAP_AGENT` `Coupon` cashflows with no `Netting_Id`; its netting type is `SAL COUPON NETTING`.

The UAT expects a resultant payment type of `SAL MTM Netting` or `SAL Coupon Netting` respectively.

## Suppression scope

The documented suppression rule `7351885393248022528` is intended to automatically SWIFT-suppress:

- SAL MTM or SAL Coupon net resultants with a populated `Cashflow__Netting_Id`; and
- eligible single `Interim MTM` or `Coupon` cashflows where `Cashflow__Is_Auto_Netting == true`.

This is a SAL-specific configuration expectation, not a rule that should be generalized to other [[cashflow-auto-netting]] scenarios.

## Evidence limitation

The UAT source says the Swap Agent test set did not meet expectations and needed more complete cases. Rule-status fields are blank. Accordingly, this page records intended configuration and test scope, not proof of a completed SAL UAT or deployed rule.
---
type: concept
title: Precious-Metal Cashflow Vostro Requirement
tags: [cash-settlement, precious-metals, vostro, swift, scb, validation]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1ki16y7, scb-receive-vostro-validation, concepts/nostro-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping.md"]
---
# Precious-Metal Cashflow Vostro Requirement

## Definition

For SCB receive cashflows, vostro settlement information is mandatory when the currency is one of the four precious-metal codes specified by the requirement:

- `XAU`
- `XAG`
- `XPD`
- `XPT`

This rule addresses a downstream SWIFT-generation prerequisite that is not reliably enforced by the previous receive-cashflow stamping behavior.

## Operational purpose

The current behavior allows SCB receive cashflows to proceed without vostro information. For the specified currencies, SWIFT generation requires that information, so an incomplete cashflow can become stuck in a SWIFT-generation error.

Making vostro mandatory during auto stamping and manual SSI updates shifts the check earlier in the settlement workflow. It is a targeted control for SCB receive cashflows, not a general rule for every receive cashflow or every precious-metal flow in the platform.

## Required consistency

For manual SSI updates subject to the rule:

- Required vostro and nostro fields must be populated.
- Vostro settlement means must equal nostro settlement means.
- Vostro settlement account must equal nostro settlement account.

The source does not define whether all precious-metal currencies share identical SWIFT requirements outside this SSI validation context.
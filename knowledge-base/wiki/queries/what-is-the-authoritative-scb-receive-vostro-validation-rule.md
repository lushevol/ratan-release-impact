---
type: query
title: What Is the Authoritative SCB Receive Vostro Validation Rule?
tags: [cash-settlement, scb, ssi-stamping, vostro, open-question]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1ki16y7, scb-receive-vostro-validation, precious-metal-cashflow-vostro-requirement, concepts/nostro-stamping, entities/scb-london, entities/scb-korea]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping.md"]
---
# What Is the Authoritative SCB Receive Vostro Validation Rule?

## Question

What is the final implemented and approved validation contract for SCB receive cashflows during auto stamping and manual SSI updates?

## Known requirement

The source states that vostro is mandatory for:

- all SCB pay cashflows;
- SCB receive cashflows in `XAU`, `XAG`, `XPD`, or `XPT`;
- SCB receive cashflows using settlement means `"Over-Account"`.

Other SCB receive cashflows bypass the existing vostro-mandatory validation. If `vostro SSI Type` is null, the system copies the nostro settlement means and settlement account into the corresponding vostro fields.

## Unresolved points

1. Does `"Over-Account"` apply as a mandatory condition for every SCB receive currency?
2. At which stage does conditional auto-population occur: auto stamping, manual SSI submission, or both?
3. What does a null `vostro SSI Type` signify operationally?
4. Are auto-populated values persisted, and can users override them?
5. What complete set of fields is covered by “mandatory field in vostro/nostro”?
6. Which SCB legal entities or branches are in scope?
7. Does the rule apply only to newly processed cashflows, or are existing cashflows reprocessed?
8. What acceptance tests and monitoring demonstrate prevention of SWIFT-generation errors?

## Evidence status

The source is a functional requirement and provides requirement-level evidence only. It does not prove that the rule has been implemented, deployed, tested, or adopted as the authoritative production contract.
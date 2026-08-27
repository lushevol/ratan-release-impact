---
type: query
title: What Does adleToSendPerSSIAdhocException Control in Auto Stamping?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, ssi, auto-stamping, configuration, exception-lifecycle]
related: [pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--17g3zt]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping/Cashflow Auto Stamping.md"]
---
# What Does adleToSendPerSSIAdhocException Control in Auto Stamping?

The source names `adleToSendPerSSIAdhocException` as a condition for generating `PRE_ADHOC_ERROR` when auto SSI stamping has a Vostro/Nostro Exception.

## Questions

- Is `adleToSendPerSSIAdhocException` the canonical identifier and spelling?
- Which service, configuration store, or business rule owns the property?
- What is its default value and configuration scope?
- Does it control only `PRE_ADHOC_ERROR` generation or also `ADHOC_SSI_EXCEPTION` behavior?
- Is the property evaluated per cashflow, portfolio, settlement account, or another scope?

The identifier is preserved exactly as written in the source pending confirmation.
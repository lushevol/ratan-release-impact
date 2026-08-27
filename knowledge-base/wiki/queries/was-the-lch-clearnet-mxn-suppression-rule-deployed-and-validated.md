---
type: query
title: Was the LCH Clearnet MXN Suppression Rule Deployed and Validated?
created: 2026-08-23
updated: 2026-08-23
tags: [suppression, static-data, mt103, mxn, swift, production-incident]
related: [fmswg, ssi-plus, fmswg-swift-message-validation, cashflow-suppression-vs-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md"]
---
# Was the LCH Clearnet MXN Suppression Rule Deployed and Validated?

## Question

Was the suppression rule requested for LCH Clearnet Limited deployed and demonstrated to prevent outbound MXN MT103 generation?

## Evidence

The 2025-01-19 incident is marked Closed after a request was sent to the static data team. The source states that the client was meant to be suppressed, yet an MT103 was generated without the mandatory beneficiary account in field `59`.

The source does not contain rule approval, deployment, test, or production-effectiveness evidence.

## Information needed

- the suppression-rule configuration and its effective scope;
- deployment and approval records;
- test evidence showing suppression occurs before SWIFT field validation and message generation;
- monitoring evidence that the rule prevented recurrence.
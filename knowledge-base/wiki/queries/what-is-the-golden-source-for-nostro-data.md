---
type: query
title: What Is the Golden Source for Nostro Data?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, nostro, static-data, settlement-instructions]
related: [standard-settlement-instructions, ssi-stamping, currency-transformation-for-settlement-instructions, fmrp, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# What Is the Golden Source for Nostro Data?

## Question

Which system owns the authoritative Nostro settlement means and account data used by FXO settlement processing?

## Evidence

The static-data section of the FXO checklist labels the Nostro golden source as `TBC`. It separately requires default Nostro stamping, new settlement means and accounts, and transformed-currency lookup such as `SGO` to `SGD`.

## Why It Matters

Without an authoritative source, the design cannot reliably define:

- Account ownership and maintenance.
- Distribution to [[fmrp]] and [[ratan]].
- Effective dating and synchronization.
- Reconciliation and exception handling.
- Approval and authorization controls.
- Behavior when the transformed lookup currency differs from the received currency.

The system owner, data contract, refresh mechanism, and operational support model remain unresolved.
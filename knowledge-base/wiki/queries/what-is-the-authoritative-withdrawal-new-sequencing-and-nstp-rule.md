---
type: query
title: What Is the Authoritative Withdrawal/New Sequencing and NSTP Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, withdrawal, amendment, sequencing, nstp, stp, duplicate-payment-risk]
related: [cashflow-events-control-draft2, reversal-and-correction-cashflow-processing, cashflow-amendment-supersession, how-does-cashflow-blotter-handle-out-of-order-duplicate-and-withdrawal-events, stella, ratan, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft2.md"]
---
# What Is the Authoritative Withdrawal/New Sequencing and NSTP Rule?

The deprecated draft proposes applying “full NSTP” to packed Stella withdrawal-and-new events so that a correction cannot proceed before its withdrawal. It also identifies a duplicate-payment risk when withdrawal and new cashflows arrive independently after an original has been released or settled.

## Questions to resolve

- What event-pair correlation key identifies a withdrawal and its replacement?
- Which packed and separate-message cases are NSTP-eligible?
- Does Murex payment workflow status `SNTR` require a different rule?
- What sequencing guarantee prevents a new payment from reaching STP or release before its withdrawal completes?
- What happens on partial failure, timeout, retry, duplicate delivery, or missing counterpart events?
- Which controls, alerts, and operator overrides are required?

The draft is historical evidence only. It does not confirm that the proposed NSTP rule was implemented or approved.
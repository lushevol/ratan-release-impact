---
type: concept
title: Pending-Fixing STP/NSTP Control
created: 2026-08-22
updated: 2026-08-22
tags: [fixing, stp, nstp, cashflow-routing, settlement]
related: [stella, cashflow-status-handling, netting-key-selection, fxo]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Pending-Fixing STP/NSTP Control

Pending-fixing STP/NSTP control determines whether a cashflow can proceed through straight-through processing while a required fixing event remains outstanding.

## Checklist Scope

The FXO onboarding checklist calls for this control when a new product has fixing events. It cites new [[stella]] products and uses Loan Deposit as an example, including the netting of principal and interest together.

## Required Clarifications

The source does not define:

- What constitutes a pending fixing.
- When the control is evaluated.
- Whether affected cashflows are suspended, rejected, or routed to an NSTP queue.
- How principal and interest netting interacts with fixing status.
- Which event releases a cashflow to STP.
- Which products and branches require the control.

The Loan Deposit example should not be generalized to FXO, IRS, or other products without product-specific confirmation.
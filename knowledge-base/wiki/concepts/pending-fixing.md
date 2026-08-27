---
type: concept
title: Pending Fixing
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-processing, fixing, loan-depo, stp, nstp]
related: [fmrp-prime-uk-uat-drop-2, loan-depo, cashflow-status-and-substate-model, straight-through-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---
# Pending Fixing

Pending Fixing is a processing state in which a cashflow waits for a fixing event before settlement processing continues.

In the Prime UK onboarding checklist, Loan Depo must be configured for Pending Fixing STP/NSTP control when the new product has fixing events. This requirement is product-specific and should not be assumed for IRS or CCS without supporting evidence.

Validation should demonstrate entry into the pending state, release after the fixing event, correct NSTP behavior, and recovery handling when the fixing is delayed or invalid.
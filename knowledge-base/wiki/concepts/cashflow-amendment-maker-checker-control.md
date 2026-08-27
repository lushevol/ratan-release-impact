---
type: concept
title: Cashflow Amendment Maker/Checker Control
created: 2026-08-23
updated: 2026-08-23
tags: [maker-checker, authorization, cashflow, segregation-of-duties]
related: [manual-cashflow-rounding, usd-equivalent-cashflow-adjustment-limit]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# Cashflow Amendment Maker/Checker Control

Cashflow Amendment Maker/Checker Control is the required separation-of-duties workflow for Manual Rounding. One user initiates the payment cashflow amount change and another user authorizes it.

The requirement establishes maker/checker as mandatory but does not specify the approval states, role permissions, rejection or rework behavior, audit fields, notification rules, or the point at which the amended amount becomes available to SWIFT and Settlement Accounting.

## Control questions

The implementation should establish whether the USD-equivalent limit is checked both when the maker enters the adjustment and when the checker approves it. It should also define how duplicate submissions, self-approval, cancellation, expiry, and changes after approval are handled.

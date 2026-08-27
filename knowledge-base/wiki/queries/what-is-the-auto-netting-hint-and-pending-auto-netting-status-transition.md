---
type: query
title: What Is the Auto-Netting Hint and PendingAutoNetting Status Transition?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, hint, pendingautonetting, lifecycle, status-transition]
related: [auto-netting-rule-configuration, auto-netting-job-time, lifecycle-service, ratanone-rule-service, ratan-rule-service, 26-auto-netting-page-md-files--112-cash-settlement-home-page-cash-settlement-home-page-tech-design-cash-settlem--1o5gc6g]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# What Is the Auto-Netting Hint and PendingAutoNetting Status Transition?

The design says that a rule check returns `VD+Shifter` “if hint,” after which [[ratan-rule-service]] calls [[lifecycle-service]] using `IsAutoNettingEligible`.

However, it does not define the hint’s schema, producer, semantics, or precedence. It also requires the scheduled job to query both `Waiting` and `PendingAutoNetting` but does not explicitly state which action transitions a cashflow to `PendingAutoNetting`, nor why both statuses participate in the same grouping logic.

## Decision needed

Define the hint contract and the complete lifecycle transition model, including the actor that sets `PendingAutoNetting`, status eligibility, transition guards, and recovery behavior.
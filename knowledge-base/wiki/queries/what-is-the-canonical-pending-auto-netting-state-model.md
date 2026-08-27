---
type: query
title: What Is the Canonical Pending Auto Netting State Model?
created: 2026-08-22
updated: 2026-08-22
tags: [query, cashflow-state, Pending-Auto-Netting, Pending-Exception, RATAN]
related: [cashflow-auto-netting, cashflow-exception-handling, pending-fixing-stp-nstp-control, what-are-the-canonical-cashflow-state-and-sub-state-values]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md"]
---
# What Is the Canonical Pending Auto Netting State Model?

## Question

What are the authoritative RATAN status, sub-status type, and sub-status values for cashflows held before and after auto netting?

## Evidence to Confirm

The functional requirement uses the following candidate values:

- `WAITING` with sub-status type `Pending Auto Netting`.
- `Pending Operator?` as an uncertain sub-status for cashflows waiting for the auto-netting job.
- `NETTED` after execution.
- `Pending Exception` with `Pending Operator` for the resultant.
- `DEAD` for a manually un-netted resultant.
- `CANCEL` for an upstream-cancelled component.
- `NA` where no sub-status applies.

The question remains open because the source marks `Pending Operator?` with a question mark and does not define the canonical state machine or its relationship to Pending Netting, Pending Exception, and NSTP.

## Required Resolution

Confirm the authoritative enumerations, transition rules, versioning behavior, and UI labels against RATAN implementation or approved operational documentation. Compare the result with [[queries/what-are-the-canonical-cashflow-state-and-sub-state-values]].

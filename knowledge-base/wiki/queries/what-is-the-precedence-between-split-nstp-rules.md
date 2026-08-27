---
type: query
title: What Is the Precedence Between Split NSTP Rules?
created: 2026-08-22
updated: 2026-08-22
tags: [query, nstp, cashflow-splitting, rule-precedence]
related: [cashflow-splitting, split-cashflow-netting-exclusion, ratan-cashflow-lifecycle-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Split Static.md"]
---
# What Is the Precedence Between Split NSTP Rules?

The source proposes four split-related NSTP rules but does not define their precedence or overlap behavior.

A cashflow could potentially satisfy multiple conditions, such as having a split identifier and also being a split amendment or withdrawal. It is unknown whether the system should create all matching exceptions, select one according to priority, or suppress some exceptions.

## Evidence needed

Confirm the rule-engine evaluation order, exception aggregation behavior, suppression rules, and the interaction between split NSTP exceptions and pending NDS netting eligibility.
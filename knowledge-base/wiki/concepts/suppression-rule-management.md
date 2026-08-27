---
type: concept
title: Suppression Rule Management
created: 2026-08-23
updated: 2026-08-23
tags: [static-data, rules, suppression, maker-checker, nstp]
related: [cashflow-suppression, swift-suppression, suppression-maker-checker-workflow, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# Suppression Rule Management

Ratan uses static-data rules to apply automatic Cashflow Suppression and Swift Suppression within the STP/NSTP workflow. Runtime application is single-level and does not require Maker/Checker approval for each matching cashflow.

The Cashflow Suppress Rules Table supports rule definitions using pre-defined fields. An example purpose is suppressing cashflows booked with unsupported entities. Payment Suppression requires a dedicated tile and backend rule type, with the same rule-creation and deletion process as Cashflow Suppression.

Rule creation and deletion require Maker/Checker approval.

The requirement does not define supported fields, operators, precedence, conflicts, effective dates, versioning, or audit retention. See [[what-is-the-authoritative-suppression-rule-schema-and-precedence-model]].
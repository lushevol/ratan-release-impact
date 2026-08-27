---
type: query
title: What Static Data Is Skipped When a Cashflow Is Suppressed?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, settlement, static-data, cashflow-suppression, uat]
related: [cashflow-suppression-rule, manual-entity-settlement-enablement, qatar-slate-one-llc-doh-gbs, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/003 QATAR SLATE ONE LLC DOH(GBS).md"]
---
# What Static Data Is Skipped When a Cashflow Is Suppressed?

## Question

What specific settlement static-data fields, records, or configurations are excluded when the `SLATE` cashflow is handled by the Cashflow Suppression rule?

## Evidence

The 2026-03-23 UAT confirmation states that the `SLATE` cashflow will be cashflow suppressed, that the “rest of static” is not required, and that only the Cashflow Suppression rule is required.

The source does not define “rest of static” or identify the formal rule configuration.

## Required clarification

Confirm:

- The precise static-data scope that can be omitted.
- The Cashflow Suppression rule identifier and trigger conditions.
- The resulting cashflow status and downstream behavior.
- Whether the behavior applies only to this UAT cashflow or to a wider entity or product scope.
- The evidence showing that the rule was configured and executed successfully.
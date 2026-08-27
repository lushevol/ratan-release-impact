---
type: query
title: What Is the Hefei RAZOR-RATAN Routing Rule?
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, routing, razor, ratan, cashflow-suppression]
related: [hefei-branch, 2025-hefei-branch-onboarding, hefei-strategic-settlement-routing, razor, ratan, cashflow-suppression, settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Hefei Branch Onboarding.md"]
---
# What Is the Hefei RAZOR-RATAN Routing Rule?

The checklist places `CN` in the strategic-flow whitelist and says that a cashflow-suppression rule will send activity to [[razor]] or handle it in [[ratan]]. It also states that RATAN generates SWIFT and accounting in the described arrangement.

The source does not define the exact routing predicate, the transaction and product scope, rule precedence, or the system that is authoritative for the decision.

## Evidence needed

- The implemented rule definition and its source system.
- Entity, product, currency, and transaction attributes used for route selection.
- Rule precedence relative to suppression, netting, and manual exceptions.
- Confirmation of which route generates SWIFT and accounting for each in-scope scenario.
- Test evidence for Hefei transactions in both expected and exception paths.
---
type: query
title: Should LIEN Generation on Trade Exceptions Produce NSTP?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lien, nstp, trade-exceptions, rule-service]
related: [lien, rule-service, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# Should LIEN Generation on Trade Exceptions Produce NSTP?

## Question

Should generating a LIEN amount on a trade exception change the cashflow's NSTP classification, or should it only add or update an attribute?

## Evidence

The source proposes a new `ratan-rule-service` rule for NSTP cashflows with LIEN amounts and for generating LIEN on trade exceptions. It does not define the rule expression, precedence, database changes, user coverage, or interaction with existing exception categories.

## Required resolution

The decision should clarify:

- The exact eligibility rule.
- Whether LIEN is a condition, an output, or both.
- Rule precedence against `TechFail`, `Pending Exception`, and other categories.
- Whether the change affects exception classification or only LIEN generation.
- Required database, configuration, and user-coverage changes.
- Acceptance tests for trade exceptions with and without LIEN amounts.
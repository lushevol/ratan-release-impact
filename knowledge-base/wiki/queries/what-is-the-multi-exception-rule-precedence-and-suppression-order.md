---
type: query
title: What Is the Multi-Exception Rule Precedence and Suppression Order?
tags: [cash-settlement, exceptions, rule-engine, ratan]
related: [cashflow-multi-exception-generation, pending-confirmation-affirmation, back-value-exception-management]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# What Is the Multi-Exception Rule Precedence and Suppression Order?

The requirement permits multiple exception tags but specifies only selected dependencies and suppressions:

- SSI processing precedes Back Value.
- Pending Netting and Auto Netting checks precede Previously Netted.
- Reversal suppresses Pending Affirmation.
- A confirmed component cashflow suppresses Pending Affirmation.
- `Over Account` may short-circuit processing.

Define the complete ordered evaluation model, deduplication behavior, dependency graph, and resolution behavior when several rules apply simultaneously.
---
type: concept
title: NSTP and NDIRS Rule Routing
tags: [cashflow, nstp, ndirs, rule-engine, parent-trade, nid]
related: [nds-cashflow-processing, nd-parent-trade-metadata, rule-service, cash-settlement-exception-handling, what-are-the-nid-and-nd-parent-typology-validation-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# NSTP and NDIRS Rule Routing

NSTP and NDIRS rule routing is the parent-typology-dependent rule behavior specified for `ratan-rule-service`.

## Recorded Conditions

- A new rule applies to NSTP cashflows where the parent typology is non-`NDIRS` and NID exists.
- An existing on-demand rule is updated to bypass cashflows whose parent typology is `NDIRS`.

The source establishes these intended conditions but does not define rule priority, whether conditions are evaluated in one rule set or independently, the meaning of “NID exists”, or the resulting cashflow status after a rule match.

This rule routing is specific to `ratan-rule-service`; it does not establish a universal NSTP state machine across [[cash-settlement-exception-handling]].
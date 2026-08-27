---
type: query
title: What Is the Authoritative RATAN Settlement Suppression Rule Contract?
tags: [ratan, settlement, suppression, open-question]
related: [ratan-settlement-suppression-rule-check, ratan-settlement, ratan-rule-service, ratan-suspended-cashflow-rule-filtering]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Core Function copy/RATAN-Settlement  2_Suppression Rule Check.md"]
---
# What Is the Authoritative RATAN Settlement Suppression Rule Contract?

## Question

What are the authoritative criteria, ownership, execution behavior, and downstream handling for the RATAN Settlement suppression rule check?

## Current evidence

Only the source filename was available. It indicates a RATAN Settlement suppression rule check but does not establish the rule contract or confirm whether the check is implemented by [[entities/ratan-rule-service]], the settlement component, or another service.

## Questions to resolve

- What constitutes a suppressible settlement item?
- Is suppression distinct from suspension?
- What are the inputs, outputs, and rule-evaluation order?
- What happens when the rule service or a dependency is unavailable?
- Are suppressed records persisted, audited, retried, reconciled, or discarded?
- Which document or implementation is authoritative?

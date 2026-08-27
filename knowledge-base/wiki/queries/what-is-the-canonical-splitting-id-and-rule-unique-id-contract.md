---
type: query
title: What Is the Canonical Splitting ID and Rule Unique ID Contract?
tags: [cashflow-splitting, identifiers, api-contract, static-data, lineage]
related: [split-cashflow-persistence-and-lineage, split-cashflow-api-contract, split-rule-maker-checker-lifecycle, splitting-cashflow]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# What Is the Canonical Splitting ID and Rule Unique ID Contract?

## Question

Which identifiers are canonical for split groups and split-rule history, and how should clients distinguish them from row and cashflow IDs?

## Evidence

The persistence table holds both `cashflow_id` and `splitting_id`. The unsplit example uses a UUID-like `splittingId`, while the amend-amount example sets `splittingId` to `M00000039085`, which resembles a cashflow ID.

Static-rule query data uses `ruleUniqued`, whereas the audit query parameter and audit outer object use `ruleUniqueId`.

## Needed Resolution

Publish a canonical identifier model for split groups, parent and child cashflows, rule rows, logical rules, versions, and audit records. Confirm whether the naming differences are compatibility fields, typographical errors, or separate identifiers.
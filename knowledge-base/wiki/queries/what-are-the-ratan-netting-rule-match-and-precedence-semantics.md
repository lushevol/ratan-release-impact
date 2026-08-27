---
type: query
title: What Are the Ratan Netting Rule Match and Precedence Semantics?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, netting, static-data, rule-engine, matching, precedence]
related: [ratan, netting-eligibility-rules, cashflow-logical-model, configuration-driven-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Rules Static Data.md"]
---
# What Are the Ratan Netting Rule Match and Precedence Semantics?

The documented CN Day 1 eligibility rule uses `IS` and `IS/IN` operators against booking-entity FM Code, client FM Code, and ISDA Taxonomy. The source does not define how rule evaluation works.

## Questions

- What are the exact semantics of `IS` and `IN`, including list, wildcard, hierarchy, and null behavior?
- Are all populated rule attributes conjunctive?
- How does Ratan select between multiple matching rules?
- Are priority, specificity, effective date, version, status, or maker/checker controls supported?
- What happens when a required logical-model field is absent or invalid?
- How are duplicate rules detected, audited, and resolved?

## Evidence Needed

Obtain the Ratan static-data schema, GUI specification, rule-engine implementation, and test cases for [[netting-eligibility-rules]].
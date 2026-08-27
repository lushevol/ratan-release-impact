---
type: query
title: What Rule Auditability and Approval Controls Does Cash Settlement Require?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, auditability, governance, business-rules, controls]
related: [rule-governance-and-auditability, business-rule-engines, drools, decision-model-and-notation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# What Rule Auditability and Approval Controls Does Cash Settlement Require?

The source proposes separating business logic from code but does not specify the controls necessary to govern mission-critical rule changes.

## Questions to resolve

- Who may author, review, approve, and publish rule changes?
- What testing, simulation, segregation-of-duties, and release evidence is required?
- Which input facts, rule versions, fired rules, and decision outputs must be retained?
- How long must decision evidence be retained and how can outcomes be explained?
- What rollback and incident procedures apply when a rule produces incorrect outcomes?
- How are expression languages and external rule stores secured?
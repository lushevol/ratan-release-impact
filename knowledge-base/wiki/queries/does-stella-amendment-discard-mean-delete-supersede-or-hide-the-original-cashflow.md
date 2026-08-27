---
type: query
title: Does Stella Amendment Discard Mean Delete, Supersede, or Hide the Original Cashflow?
created: 2026-08-23
updated: 2026-08-23
tags: [stella, ratan, cashflow, amendment, auditability]
related: [stella-cashflow-amendment-supersession, stella, ratan, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md"]
---
# Does Stella Amendment Discard Mean Delete, Supersede, or Hide the Original Cashflow?

Sprint 13 specifies that, after a Stella New and Amendment message for the same VD-4 cashflow, RATAN should display the amendment only and “discard the new.”

## Questions to Resolve

- Is the original New record physically deleted, logically superseded, or merely hidden in Cashflow Blotter?
- What message or business key identifies the New and Amendment as the same cashflow?
- Is the original event retained for audit, replay, reconciliation, or investigation?
- What occurs when amendments arrive out of order, are duplicated, or fail processing?

The source establishes only the intended display outcome and not the underlying persistence or audit model.
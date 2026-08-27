---
type: query
title: Which SSI Hierarchy Applies to FXO?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, fxo, ssi, settlement-instructions]
related: [fxo, ssi-stamping, ssi-selection-hierarchy, currency-transformation-for-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Which SSI Hierarchy Applies to FXO?

## Question

Is FXO approved to follow the UK SSI hierarchy, and does that hierarchy replace the old selection model?

## Evidence

The checklist first identifies `SSI Auto Stamping Hierarchy (Old vs New)` as a consideration. A later configuration entry says to follow the UK model, giving `Country Specific + Global Product` SSI priority over `Global Entity + Product Specific` SSI.

This may represent a resolution, a proposal, or a reusable onboarding default. The document does not record an approval, effective date, scope, or decision owner.

## Information Needed

- The approved precedence order.
- Applicable products, branches, and legal entities.
- Tie-breaking and fallback behavior.
- Interaction with CFI code, settlement method, and transformed currency.
- Migration treatment for previously stamped trades.
- Test evidence for competing SSI records.

An authorized decision should be recorded before the hierarchy is treated as final.
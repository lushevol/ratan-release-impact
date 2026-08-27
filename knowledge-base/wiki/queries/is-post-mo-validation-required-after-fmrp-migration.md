---
type: query
title: Is Post-MO Validation Required After FMRP Migration?
created: 2026-08-22
updated: 2026-08-22
tags: [FMRP, post-MO-validation, validation, Indonesia, Jakarta, scope]
related: [indonesia-entity-onboarding-checklist, indonesia-jakarta, fmrp, entity-branch-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2026 Indonesia Instance.md"]
---

# Is Post-MO Validation Required After FMRP Migration?

## Question

After post-MO validation moved to [[fmrp]], is validation still required for the Indonesia/Jakarta onboarding scope?

## Evidence

The first checklist item states:

> Bypass EG/NP/SAUDI/LOANIQ/CN(FX), rest need validation Post MO Validation moved to FMRP, then not required?

The wording indicates uncertainty rather than a completed decision. It distinguishes entities or flows that bypass validation from those that still require validation, but does not define the final rule after migration to FMRP.

## Required resolution

Confirm:

- Whether post-MO validation remains required after the move to FMRP.
- Which products, entities, and currency or trade categories are subject to validation.
- Whether `CN(FX)` is the only currency-related exception.
- Whether the Indonesia/Jakarta entity should bypass validation or follow the validation path.
- Which system owns the authoritative validation rule after migration.

The decision should be recorded before onboarding sign-off because it affects implementation scope and production controls.

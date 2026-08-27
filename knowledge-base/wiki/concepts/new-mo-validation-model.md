---
type: concept
title: "New MO Validation Model"
created: 2026-08-22
updated: 2026-08-22
tags: [validation, cash-settlement, RATAN, Murex, FMRP]
related: [bypass-validation-rule, configuration-driven-onboarding, pending-fixing, 2026-korea-cash-settlement-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/New Entity onboarding checking list - Korea 2026.md"]
---
# New MO Validation Model

## Definition

The New MO Validation Model is the validation approach referenced by the Korea 2026 onboarding checklist as the replacement for the [[concepts/bypass-validation-rule]].

The source states that the Bypass Validation Rule is no longer required because the New MO Validation Model solved the relevant issue. It also contains historical notes that post-MO validation moved to FMRP.

## Operational implication

If the model is deployed and applicable to the relevant products and source flows, new-entity onboarding should not require a bypass rule for LOANIQ/FX or other previously exempted flows. Validation coverage should instead be confirmed as part of onboarding and testing.

## Evidence limitation

The checklist does not identify:

- The implementation release.
- The exact validation behavior.
- The affected product and source-system scope.
- Whether all LOANIQ/FX cases are covered.
- Evidence that the model is live for Korea.

The replacement should therefore be treated as a documented claim pending confirmation, not as proof that the former rule has been removed in production.
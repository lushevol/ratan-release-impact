---
type: query
title: Does Hefei SSI Propagate as a Global Murex SSI?
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, ssi, murex-211, static-data, risk]
related: [scb-hefei, murex-211, ssi-dual-blind-input, static-data-readiness, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--38-04-onboardingentity-pr--27yb0b]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/China Hefei Branch Setup.md"]
---
# Does Hefei SSI Propagate as a Global Murex SSI?

## Question

Will an SSI created for SCB Hefei flow into [[murex-211]] as a Global SSI, and if so, what control prevents unintended visibility or assignment outside Hefei?

## Evidence

The Hefei onboarding checklist states that existing Global SSIs will be selected automatically and that Hefei-specific SSIs should be required only for `SUPPRESSXX` Nostro auto-debit flows or Over-Account clients. It explicitly identifies as an open issue that an SSI created for Hefei branch may flow into Murex 2.11 as a Global SSI.

## Why It Matters

Global propagation would conflict with the intended limited scope of branch-specific SSI data. It may affect settlement-instruction selection for other entities and requires validation of creation, propagation, retrieval, and assignment behavior.

## Information Needed

- The Murex 2.11 SSI scope model and propagation path.
- Whether entity-level restrictions are preserved after interface processing.
- Test evidence for Hefei-specific `SUPPRESSXX` and Over-Account scenarios.
- Mitigation or approval if the SSI must be global.
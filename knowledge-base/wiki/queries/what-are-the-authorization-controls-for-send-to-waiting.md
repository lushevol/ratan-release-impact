---
type: query
title: What Are the Authorization Controls for Send to WAITING?
tags: [authorization, cashflow, reinstate, hold, amount-limits]
related: [held-cashflow-reinstatement, profile-based-usd-authorization-limits, maker-checker-ssi-control, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Actions on Hold.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Are the Authorization Controls for Send to WAITING?

The source gives **Send to WAITING** the same base profile access as `HOLD`, permits the user who performed the hold to select it, and exempts it from the cashflow amount-limit check required by `Unhold`.

## Questions to resolve

- Is the amount-limit exemption intentional for every profile, currency, amount, entity, and settlement product?
- What control compensates for allowing the holding user to reinstate the cashflow?
- Is a mandatory comment the only audit control, or are approval, monitoring, or post-action review requirements also applied?
- Is the exemption enforced server-side as well as in the UI?
- Does the action remain available only when the user is entitled to place the cashflow on hold?

This is an action-specific requirement and must not be generalized to all [[profile-based-usd-authorization-limits]] or [[maker-checker-ssi-control]] behavior without further evidence.
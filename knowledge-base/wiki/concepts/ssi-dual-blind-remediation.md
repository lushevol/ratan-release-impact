---
type: concept
title: SSI Dual-Blind Remediation
tags: [cash-settlement, ssi, maker-checker, validation, dual-blind]
related: [ratan, settlement-ops, maker-checker-settlement-control, cashflow-multi-exception-generation, back-value-exception-management]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# SSI Dual-Blind Remediation

SSI dual-blind remediation requires maker and checker to enter SSI values independently for SSI-related cashflow exceptions in [[ratan]]. The checker must not simply accept the maker's editable entry.

## Applicable SSI outcomes

The requirement covers Missing Vostro, Multi Vostro, Nostro vs Vostro Mismatch, Adhoc SSI, Missing Nostro, and Secondary Vostro. Vostro and Nostro information remain visible in fixed UI locations, with form editability determined by workflow status and user role.

## Required validation

Both GUI and backend must validate:

- Vostro-form data.
- Equality of settlement means between Vostro and Nostro.
- Equality of settlement account between Vostro and Nostro.
- Maker-versus-checker SSI values.

Vostro/Nostro settlement-account or settlement-means mismatch is a hard blocker on checker submission.

## Rejection and rework

If checker SSI differs from maker SSI, Ratan highlights the mismatch. Other exceptions can close, but SSI exceptions remain open. The checker records a rejection comment and returns the cashflow to the maker; the maker then sees only SSI exceptions and receives the prior SSI entry as preloaded data.

For Adhoc SSI, [[settlement-ops]] overrides system-assigned SSI and the maker may update Adhoc SSI plus non-`70/72` fields. Maker submission generates `SSI Modified by Maker`. After rejection, prior input may be preloaded only for the same maker user. It must not be presented as default data to another maker.

The source does not state comparison-normalization rules for fields such as BIC casing, account formatting, optional blanks, or equivalent date representations.
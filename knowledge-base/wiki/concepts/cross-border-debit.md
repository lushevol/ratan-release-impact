---
type: concept
title: Cross-Border Debit
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cross-border-debit, regulatory-processing, SWIFT]
related: [mt202-crossdebit, cross-border-debit-settlement-account-routing, what-takes-precedence-between-crossdebit-and-202-flip-routing, what-is-the-cross-border-debit-lms-feed-contract, fmrp, lms, ssi-plus-es-api, vostro-nostro-ssi-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit.md"]
---
# Cross-Border Debit

## Definition

A cross-border debit is a debit scenario in which a client's account is held with an SCB entity different from the booking entity. The existing `MT202Flip` instruction cannot be used for some of these cases because the instruction is not allowed by the regulator.

The requirement introduces a separate receive-flow processing path using `MT202 CROSSDEBIT`.

## Processing Rule

A Vostro settlement instruction is created in SSI+ with a settlement account formatted as `CCY CROSSDEBIT`, for example `USD CROSSDEBIT`.

For a receive cashflow whose settlement account matches this format:

1. Generate an `MT202 CROSSDEBIT` message.
2. Apply the specialized [[mt202-crossdebit]] field mapping.
3. Generate accounting through the existing accounting process.
4. Send the cross-border debit cashflow feed to [[lms]].

The specialized receive-flow rule does not extend to `MT103 CROSSDEBIT`, which is excluded from the requirement.

## Pay-Flow Boundary

Pay cross-debit cashflows follow the normal `MT103`/`MT202` mapping. The source therefore distinguishes receive and pay flows rather than defining one generalized cross-border mapping.

## Confirmed Clarifications

- `MT202` is the only specialized message in scope for the receive flow.
- Field 57 uses the Nostro BIC.
- GMO BIC is not required.
- No additional field-72 logic is required; the flow relies on SSI setup.
- Accounting is unchanged.

## Unresolved Behavior

The source does not establish the final precedence rule when settlement means indicate `Over account` and the settlement account also matches the `CROSSDEBIT` convention. This is tracked in [[what-takes-precedence-between-crossdebit-and-202-flip-routing]].

The source also does not define the LMS feed contract. See [[what-is-the-cross-border-debit-lms-feed-contract]].
---
type: concept
title: Cross-Border Debit Settlement-Account Routing
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, routing, settlement-account, CROSSDEBIT, SSI]
related: [cross-border-debit, mt202-crossdebit, what-takes-precedence-between-crossdebit-and-202-flip-routing, ssi-plus-es-api, vostro-ssi-best-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit.md"]
---
# Cross-Border Debit Settlement-Account Routing

## Definition

Cross-border debit routing uses the settlement account as a processing discriminator. SSI+ creates a Vostro settlement instruction with an account value in the format `CCY CROSSDEBIT`, such as `USD CROSSDEBIT`.

For receive flows, this convention routes the cashflow to [[mt202-crossdebit]] generation instead of the standard `MT202Flip` path.

## Routing Inputs

The source proposes:

- Settlement account: a currency code followed by `CROSSDEBIT`, for example `USD CROSSDEBIT`.
- Settlement instruction: a Vostro SI configured in SSI+.
- Flow direction: receive flows use the specialized `MT202 CROSSDEBIT` mapping; pay flows retain normal `MT103`/`MT202` mapping.
- Settlement means: a clarification proposed using `Nostro` as settlement means while retaining the settlement account as the cross-debit control.

## Processing Boundaries

This routing convention changes SWIFT message generation only. It does not change the accounting process. The generated cross-border debit cashflow must still be delivered to [[lms]].

No additional field-72 logic is required; the source states that the implementation should rely on SSI setup.

## Unresolved Precedence

The requirement records an unresolved question about a cashflow where settlement means equal `Over account` and the settlement account matches `%CROSSDEBIT`. A later clarification says to check cross debit first, but the authoritative ordering relative to the existing `202 Flip` rule is not fully specified.

This ambiguity is tracked in [[what-takes-precedence-between-crossdebit-and-202-flip-routing]].
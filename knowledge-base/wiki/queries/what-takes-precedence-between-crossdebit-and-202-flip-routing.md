---
type: query
title: What Takes Precedence Between CROSSDEBIT and 202 Flip Routing?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, cash-settlement, routing, CROSSDEBIT, MT202Flip]
related: [cross-border-debit, cross-border-debit-settlement-account-routing, mt202-crossdebit]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit.md"]
---
# What Takes Precedence Between CROSSDEBIT and 202 Flip Routing?

## Question

When a cashflow has settlement means equal to `Over account` and a settlement account matching the `CROSSDEBIT` convention, should the system route it as a cross-border debit or as a `202 Flip` case?

## Evidence

The requirement initially proposes using `CCY CROSSDEBIT` in the settlement account to control cross-debit routing. A clarification proposes `Nostro` as the settlement means while retaining the settlement account as the discriminator.

A later note asks whether the combination of settlement means `Over account` and a settlement account matching `%CROSSDEBIT` should be treated as `202 Flip`. The 2026-01-12 clarification says to check cross debit first, but does not provide a complete precedence matrix or implementation rule.

## Why It Matters

The outcome determines whether the receive flow generates [[mt202-crossdebit]] or follows the existing `MT202Flip` behavior. It also affects the applicability of the specialized Vostro/Nostro field mapping and regulatory controls.

## Required Resolution

Confirm:

- The exact precedence order between `CROSSDEBIT`, `Over account`, and `202 Flip`.
- Whether the rule applies only to receive flows.
- Whether settlement-account matching is exact, pattern-based, or normalized by currency.
- The expected behavior for missing or malformed settlement-account values.
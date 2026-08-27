---
type: concept
title: High Value Exception Dependency
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, exceptions, high-value, checker, stp]
related: [multi-exception-resolution-handling, does-a-maker-only-exception-trigger-or-only-retain-high-value-exception, what-is-the-authoritative-auto-versus-manual-exception-resolution-attribute]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/High Value Exception Scenario Analysis.md"]
---
# High Value Exception Dependency

High Value is a conditional cashflow exception rather than an independently actionable blocking exception. It must not be triggered when it is the sole exception; the cashflow should instead be STPed.

The requirement states that High Value is triggered and retained while another exception requires Checker action. When the relevant companion exception is automatically resolved and no other relevant Checker exception remains, the system must automatically remove High Value so that the cashflow can proceed through STP.

## Resolution Effects

- A manual Maker resolution of a companion exception leaves High Value visible to Checker.
- Automatic resolution may remove High Value if no other qualifying exception remains.
- Automatic resolution does not remove High Value when another Checker-facing exception remains.
- A Checker resolution is described as closing all exceptions under multi-exception handling, but the closure scope is not defined.

Pending Affirmation is the primary example: manual affirmation retains High Value for Checker, while automatic affirmation can remove it and enable STP.

## Implementation Limitation

The documented `operationLevel` predicate identifies Checker exceptions as `CHECKER_ONLY` or `MAKER_CHECKER`, but the same source states that High Value is triggered alongside a `MAKER_ONLY` exception. Therefore, `operationLevel` alone cannot be treated as a complete implementation rule until the generation-versus-retention ambiguity is resolved in [[does-a-maker-only-exception-trigger-or-only-retain-high-value-exception]].

The source also leaves the automatic-versus-manual resolution attribute as TBD; see [[what-is-the-authoritative-auto-versus-manual-exception-resolution-attribute]].
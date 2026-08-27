---
type: concept
title: MO Trade Validation
tags: [middle-office, trade-validation, lifecycle-events, production-control]
related: [fo-hard-block-mo-soft-block, cashflow-lifecycle-state-model, why-does-mo-validation-fail-for-compression-and-termination-trades-on-termination-and-expiry]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/Production Issue & Problem.md"]
---
# MO Trade Validation

MO trade validation is the operational ability of Middle Office (MO) users to validate a trade or its lifecycle-event outcome once the trade is eligible for that control.

The source reports two failures of this capability under `Termination + Expiry`:

- MO could not perform validation on a compression trade.
- MO could not perform validation on a termination trade.

The evidence does not state the validation rule, lifecycle state, system component, error message, or intended outcome. The reports must therefore not be classified as an FO hard block or MO soft block without further evidence. See [[fo-hard-block-mo-soft-block]].

## Required Control Definition

A complete MO validation contract should identify:

- eligible trade types and lifecycle states;
- prerequisites for validation;
- the validation action and permitted outcomes;
- error, rejection, and escalation behavior;
- treatment of termination, expiry, and compression scenarios; and
- whether any associated cashflow state affects validation eligibility.

The reported cases are tracked in [[why-does-mo-validation-fail-for-compression-and-termination-trades-on-termination-and-expiry]].
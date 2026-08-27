---
type: concept
title: Cashflow Withdrawal and New
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, withdrawal, amendment, replacement, nstp, duplicate-payment-risk]
related: [cashflow-status-lifecycle, cashflow-amendment-supersession, cashflow-event-versioning, stella, ratan, murex-2-11, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md"]
---
# Cashflow Withdrawal and New

Cashflow Withdrawal and New is a replacement pattern in which an existing cashflow is withdrawn and a new cashflow is created for the amended trade or market event.

## Decision boundary

The deprecated draft proposes:

- Use `Amendment` before the cashflow reaches `NETTED`, `RELEASED`, or `SETTLED`.
- Use `Withdrawal & New` when the cashflow has reached `NETTED`, `RELEASED`, or `SETTLED`.

The distinction extends [[concepts/cashflow-amendment-supersession]] by separating an in-place versioned update from a withdrawal followed by a new payment instruction.

## Ordering control

The principal control is to complete withdrawal processing before the replacement cashflow can be released. This is especially important when the original cashflow is `RELEASED` or `SETTLED`, because releasing the replacement first may create a duplicate payment.

For Stella messages that package both events, the draft proposes full NSTP treatment for the combined flow. For separate Stella messages, the draft indicates that the new cashflow may be STP in some cases, but does not define the complete eligibility rule.

## Source-specific behavior

For Murex amendments after the original payment reaches workflow status `SNTR`, the draft describes separate reversal and new cashflows. Murex supplies reversal and amendment flags, and the draft proposes using the amendment flag to apply full NSTP treatment.

This Murex behavior is source-specific. It must not be generalized to Stella or Korea `COMP` processing without separate evidence.

## Relationship-level consequences

Withdrawal and New can trigger related lifecycle operations:

- Withdrawal of a netting component can cause automatic un-netting and termination of the resultant.
- Withdrawal of a split parent can cause automatic un-splitting and termination of split children.
- A resultant or child that is outside Ratan may require a generated withdrawal event and operational handling.

The exact financial reversal behavior for released or settled records remains unresolved.

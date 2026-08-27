---
type: concept
title: Held Cashflow Reinstatement
tags: [cashflow, hold, reinstatement, waiting, exception-management]
related: [cash-settlement-home-page, ssi-exception-state-model, adhoc-ssi-workflow, release-cutoff-risk-for-unhold, what-is-the-reinstate-exception-lifecycle-for-held-cashflows, what-are-the-authorization-controls-for-send-to-waiting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Actions on Hold.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Held Cashflow Reinstatement

Held cashflow reinstatement is the controlled return of a cashflow from `HOLD` to `WAITING` through **Send to WAITING**, rather than restoring the cashflow's preceding state through `Unhold`.

## Required behavior

`Send to WAITING` must:

1. Resend the cashflow to the main flow.
2. Set its state to `WAITING`.
3. Attach a `Reinstate` exception.
4. Record `Reinstate` in action history.
5. Require an operator comment in the confirmation popup.

This workflow gives operations an intervention point before release. The documented follow-on outcomes are SSI amendment and release (`RELEASED/SETTLED`), cashflow suppression (`CASHFLOW_SUPPRESSED`), SWIFT suppression (`SWIFT_SUPPRESSED`), and netting (`NETTED`).

## Distinction from Unhold

`Unhold` returns the cashflow to its prior status, which can be `QUEUED`, `WAITING`, or `READY`. In contrast, reinstatement deliberately routes the cashflow to `WAITING`, even where its prior status was `READY`.

The distinction is intended to mitigate [[release-cutoff-risk-for-unhold]] and support remediation such as [[adhoc-ssi-workflow]]. It is not evidence that `Reinstate` has the same lifecycle or semantics as other SSI exceptions described in [[ssi-exception-state-model]].

## Outstanding lifecycle definition

The requirement specifies exception creation but not ownership, clearance, release blocking, retention in history, or behavior when a cashflow is held and reinstated more than once. These gaps are tracked in [[what-is-the-reinstate-exception-lifecycle-for-held-cashflows]].
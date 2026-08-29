---
type: source
title: CCIL Netting Business User Cases
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, ccil, acceptance-cases, functional-requirements]
related: [ccil, ccil-manual-netting, ccil-netting-eligibility-key, manual-un-netting, does-ccil-netting-permit-withdrawal-after-resultant-release-or-settlement, what-is-the-authoritative-ccil-netting-rule-precedence-and-refresh-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
authors: []
year: 0
url: ""
venue: ""
---
# CCIL Netting Business User Cases

This source specifies business-user acceptance cases for manual CCIL netting in the Cash Settlement Home Page. It covers eligibility, creation and release of CCIL resultant cashflows, explicit un-netting, withdrawal behavior, and restoration of `Pending Netting` after selected operational actions.

## Active Requirements

A live manual netting rule in the [[netting-static-blotter]] makes qualifying cashflows `WAITING` with sub-state `Pending Netting`. The active cases consistently state that the counterparty FMID must not be `400021949`.

Users select eligible cashflows in the cashflow blotter, invoke **CCIL Net Selected Cashflow**, choose **Net All Cashflows With Affirmation**, enter affirmation information, and submit. The expected result is:

- Component cashflows become `NETTED`.
- A resultant cashflow is generated.
- The resultant has affirmation status `Affirmed`.
- The resultant amount is correct.
- The payment type is `CCIL Netting`.
- NSTP processing completes through `MAKER_CHECKER`.
- [[ops]] releases the resultant from [[ratan]].

See [[ccil-manual-netting]].

## Eligibility and Validation

The explicit negative case rejects a selected cohort when booking entity, currency, or value date differs between cashflows. The source's literal popup text is grammatically inconsistent, but the scenario establishes that these dimensions must be common across the selected cohort.

See [[ccil-netting-eligibility-key]].

## Un-Netting and Withdrawal

Manual un-netting changes the original resultant to `DEAD` and restores component cashflows to `WAITING` / `Pending Netting`, allowing a new resultant to be generated.

When a component is withdrawn after CCIL netting but before the resultant is `SETTLED` or `RELEASED`, the expected outcome is automatic un-netting:

- The original resultant becomes `DEAD`.
- The withdrawn component becomes `CANCELLED`.
- Unaffected components return to `WAITING` / `Pending Netting`.
- The unaffected components can be netted again into a new CCIL resultant.

This extends [[automatic-un-netting-on-trade-market-events]] with a CCIL acceptance case.

## Reversible Interruptions

The source expects these actions to restore an otherwise qualifying cashflow to `WAITING` / `Pending Netting`:

- Manual Fail followed by Reinstate.
- HOLD followed by UNHOLD.
- Rejection of Swift Suppression.
- Rejection of Cashflow Suppression.

`Settle As Gross` instead changes the selected component to `WAITING` / `Pending Exception` with Settlement Method `Gross`; remaining eligible cashflows may still be netted.

## Scope Limitation

One active row, `AC-Settlement-Manual Netting-006`, is positioned in this CCIL document but uses **Net Selected Cashflow** and expects payment type `Bilateral Netting`. It does not establish CCIL behavior after a resultant becomes `RELEASED` or `SETTLED`. The stated final state also omits one component's expected outcome.

## Deprecated Material

Two struck-through cases are historical only and are not active requirements:

- Disabling or updating a manual netting rule and its effect on existing `Pending Netting` cashflows.
- Whether a CCIL rule takes precedence over a Bilateral Rule.

These unresolved historical topics are tracked in what is the authoritative ccil netting rule precedence and refresh behavior.
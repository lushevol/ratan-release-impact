---
type: concept
title: CCIL Manual Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ccil, manual-netting, affirmation, nstp]
related: [ccil, ccil-netting-eligibility-key, manual-un-netting, netting-static-blotter, ratan, nstp, automatic-un-netting-on-trade-market-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
---
# CCIL Manual Netting

CCIL manual netting is a user-triggered workflow for creating a CCIL resultant cashflow from a selected cohort of eligible component cashflows.

## Preconditions

A manual rule must be live in the [[netting-static-blotter]]. Qualifying components are expected to be `WAITING` with sub-state `Pending Netting`. The source repeatedly requires counterparty FMID not equal to `400021949`.

## Execution

In the cashflow blotter, the user selects components and invokes **CCIL Net Selected Cashflow**. The user then selects **Net All Cashflows With Affirmation**, provides updated affirmation information, and submits.

## Expected Result

The selected components transition to `NETTED`. The generated resultant is expected to have:

- Affirmation status `Affirmed`.
- The correct net amount.
- Payment type `CCIL Netting`.
- Completed NSTP processing with `MAKER_CHECKER`.

[[ops]] then releases the resultant from [[ratan]].

## Related Lifecycle Paths

Explicit [[manual-un-netting]] invalidates the resultant and returns its components to `Pending Netting`. Withdrawal of a component before the resultant is released or settled triggers the corresponding automatic path described in [[automatic-un-netting-on-trade-market-events]].

The source does not define affirmation approval, audit, retry, or concurrency behavior.
---
type: source
title: "Cash Settlement Home Page — Settlement Day 2 Hard Blocker UAT Testing"
authors: []
year: 2025
url: ""
venue: "UAT1"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, UAT, NSTP, hard-blocker, SWAP_AGENT, Settlement-Day-2]
related: [cash-settlement-home-page, swap-agent-mtm-coupon-netting-separation, clearing-resultant-swift-suppression, netting-resultant-cashflow, pending-auto-netting-state, ratan-cashflow-lifecycle-state-machine, ratan-rule-lifecycle-management, netting-validation-and-preview, was-cashflow-auto-netting-uat-formally-passed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Block UAT testing.md"]
---
# Cash Settlement Home Page — Settlement Day 2 Hard Blocker UAT Testing

## Summary

This document records new-solution and previously struck-through old-solution UAT testing for the Settlement Day 2 hard-blocker NSTP rule in UAT1. The document states that the NSTP rule was live on UAT1. The evidence includes expected results, observed results, cashflow identifiers, team-specific evidence, and screenshots, but does not constitute formal UAT sign-off, production deployment approval, or go-live approval.

The new solution was tested on 2025-10-31. The old-solution cases are dated 2025-09-22 and are retained as historical comparison evidence rather than current behavior.

## New-Solution UAT Results

### Scenario 1 — Different payment types

Two cashflows with the same booking entity, counterparty, currency, and payment date were tested:

- C1: `SWAP_AGENT` / `Coupon`
- C2: `SWAP_AGENT` / `Interim MTM`

Selecting both cashflows and choosing `Net Selected Cashflow` resulted in a pre-netting rejection. The recorded message was:

> “SWAP AGENT Coupon or Interim MTM can't net with the other payment type cashflow to avoid clearing eligible cashflows settling Bilaterally”.

Evidence identifiers:

- UK settlement Team: `M00121811010` and `M00121811012`
- Clearing Ops Team: `M00121811011` and `M00121811013`

This supports [[concepts/swap-agent-mtm-coupon-netting-separation]] and [[concepts/netting-validation-and-preview]].

### Scenario 2 — Tested different-strategy combination

Two otherwise matching cashflows were tested:

- C1: `SWAP_AGENT` / `Coupon`
- C2: `RECALC` / `Coupon`

The netting request was rejected with the same message used in Scenario 1. The test demonstrates that this specific `SWAP_AGENT` versus `RECALC` combination was rejected. It does not establish that every different product strategy is incompatible with every other strategy.

Evidence identifiers:

- UK settlement Team: `M00121811014` and `M00121811016`
- Clearing Ops Team: `M00121811015` and `M00121811017`

The message is potentially imprecise for this scenario because both cashflows have the same payment type, `Coupon`, while their Murex product strategies differ.

### Scenario 3 — Same-payment-type Coupon netting

A Hard Blocker NSTP rule was created with Maker Checker. Two matching `SWAP_AGENT` Coupon cashflows were netted:

- C1: `Coupon`
- C2: `Coupon`

The observed sequence was:

1. The rule was visible in the Settlement NSTP Rules Blotter.
2. Resultant `N1` was generated.
3. `N1` hit the NSTP rule and displayed the `Hard block Swap Agent` exception in red.
4. Maker submission was rejected with:

   > “This is a Swap Agent Coupon or Interim MTM cashflow ,can't be released from Ratan”

5. The document records C1 as reaching `Swift Suppressed`.

Evidence identifiers:

- UK settlement Team: `M00121811018` and `M00121811020`
- Clearing Ops Team: `M00121811019` and `M00121811021`

The document does not clarify whether the exception or `Swift Suppressed` status belongs to `N1`, C1/C2, or both. See [[queries/how-are-hard-blocked-netting-resultants-propagated-to-source-cashflows]].

### Scenario 4 — Single pending Interim MTM cashflow

A single `SWAP_AGENT` / `Interim MTM` cashflow was booked in `Pending Auto Netting`:

- C1: `M00121811022` for the UK settlement Team
- C1: `M00121811023` for the Clearing Ops Team

After `Settle as Gross`, the cashflow hit the `Hard Block Swap Agent` exception, displayed in red. Maker submission was rejected with:

> “This is a Swap Agent Coupon or Interim MTM cashflow ,can't be released from Ratan”

The document records C1 as reaching `Swift Suppressed`. This test connects [[concepts/pending-auto-netting-state]], [[concepts/ratan-cashflow-lifecycle-state-machine]], and [[concepts/clearing-resultant-swift-suppression]].

### Scenario 5 — Bulk submission with Bulk Eligible disabled

A Hard Blocker NSTP rule was created with Maker Checker and with `Bulk Eligible` disabled. Two cashflows were selected for Bulk Submit:

- C1: `SWAP_AGENT` / `Interim MTM`, with multiple exceptions including the NSTP hard blocker after `Settle as Gross`
- C2: `SWAP_AGENT` / `Initial Notional`, with multiple exceptions but no NSTP hard blocker

The observed result was:

> C1 is not eligible to submit

Evidence identifiers:

- UK settlement Team: C1 `M00121811024`; C2 `M00121811025`
- Clearing Ops Team: C1 `M00121811026`; C2 `M00121811027`

The final outcome for C2 is not documented. The test supports the rule that a disabled `Bulk Eligible` setting is enforced for the hard-blocked cashflow.

## Historical Old-Solution Testing

The struck-through 2025-09-22 cases recorded the following behavior:

- A single `SWAP_AGENT` / `Coupon` cashflow hit the hard blocker after `Settle as Gross`, could not be released from RATAN, and was recorded as `Swift Suppressed`.
- A single `SWAP_AGENT` / `Interim MTM` cashflow followed the same hard-block path.
- A single `SWAP_AGENT` / `Final Notional` cashflow did not hit the NSTP hard blocker and could be released from RATAN.
- Netting `SWAP_AGENT` / `Coupon` with `SWAP_AGENT` / `Initial Notional` generated a resultant that hit the hard blocker; un-netting made the resultant `DEAD`.
- Netting `SWAP_AGENT` / `Interim MTM` with `SWAP_AGENT` / `Final Notional` generated a resultant that hit the hard blocker; un-netting made the resultant `DEAD`.
- Netting two `SWAP_AGENT` / `Interim MTM` cashflows generated a resultant that did not hit the hard blocker and instead reached the SWIFT-suppressed rule.
- Bulk submission prevented the hard-blocked `SWAP_AGENT` / `Coupon` item from being submitted.

Historical evidence identifiers include `M00202509220`, `M00202509221`, `M02025092230`, `M00202509225`, `M02025092240`, `N00000039388`, `M00202509226`, `M02025092250`, `M00202509227`, `M00202509228`, `M01758535563`, and `M01758536185`.

The old-solution Interim MTM-plus-Interim MTM result was not retested in the new-solution cases. Its current status therefore remains unresolved.

## Evidence Assessment

The source provides strong evidence that:

- The NSTP rule was available in UAT1.
- The tested `SWAP_AGENT` Coupon and Interim MTM combination was rejected before netting.
- The tested same-type Coupon resultant was hard-blocked.
- A single Interim MTM flow was hard-blocked after `Settle as Gross`.
- Maker submission and bulk eligibility controls were enforced.

Evidence is moderate for general `SWAP_AGENT` netting policy and resultant lifecycle behavior. Evidence is incomplete for formal UAT approval, production readiness, exact status propagation between source and resultant cashflows, same-type Interim MTM behavior in the new solution, and the final handling of C2 in Scenario 5.

## Open Questions

- Does the new solution intentionally change same-type `SWAP_AGENT` Interim MTM netting behavior?
- Why does Scenario 2 use a payment-type error message for two Coupon cashflows with different strategies?
- Does the hard-block exception attach to `N1`, the source cashflows, or both?
- Is `Swift Suppressed` an approved terminal outcome after a hard-blocked release attempt?
- What is the final outcome for C2 in the bulk-submission scenario?
- Has formal UAT sign-off or production deployment approval been granted?

## Source Evidence

The source references screenshots stored under `attachments/`, including:

- `image-2025-11-12_14-8-27.png`
- Scenario-specific UK settlement Team and Clearing Ops Team screenshots dated 2025-11-04 and 2025-11-12
- Historical screenshots dated 2025-09-22

The complete source filename is:

`auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Settlement Day2 Requirement -- Hard Blocker -- Hard Block UAT testing.md`
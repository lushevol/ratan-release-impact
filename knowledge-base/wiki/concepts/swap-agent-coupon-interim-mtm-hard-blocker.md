---
type: concept
title: "SWAP_AGENT Coupon and Interim MTM Hard Blocker"
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, hard-blocker, settlement-day-2, nstp, release-control]
related: [swap-agent, settlement-day-2, cashflow-auto-netting, auto-netting-rule-check, resultant-hard-blocker-stamping, clearing-swift-suppression, ratan-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md"]
---
# SWAP_AGENT Coupon and Interim MTM Hard Blocker

The SWAP_AGENT Coupon and Interim MTM hard blocker is a Settlement Day 2 control for cashflows whose Murex product strategy is `SWAP_AGENT` and whose payment type is `Coupon` or `Interim MTM`.

It has two distinct effects:

- Before netting, a qualifying cashflow cannot be netted with a different payment type. `Coupon + Coupon` and `Interim MTM + Interim MTM` are permitted, but `Coupon + Interim MTM`, and either qualifying type combined with `Initial Notional` or `Final Notional`, are prohibited.
- After gross creation or netting, a qualifying cashflow or a marked resultant receives a `HARD_BLOCKER` NSTP exception. The exception blocks maker submit and checker approve actions that would release the cashflow from Ratan.

This is not a universal operational lock. The source expects containment and lifecycle actions such as `Swift Suppressed`, `Manual Failed`, `Reinstate`, `Hold`, `Unhold`, and `Suppress Cashflow` to remain available.

## Scope

The control applies only to [[swap-agent]] cashflows with the two named payment types. It must not be generalized to all `SWAP_AGENT` flows, all products, or all payment types. The source specifically tests `Initial Notional` and `Final Notional` as outside the hard-blocker rule.

## Netting and release behavior

The control is enforced by [[ratan-cash-settlement-netting-service]] before Lifecycle cashflow retrieval and by [[ratan-rule-service]] during NSTP release workflow. Resultant coverage relies on [[resultant-hard-blocker-stamping]].

A hard-blocked item in a bulk selection is isolated: it remains ineligible for submission while non-hard-blocked selected items proceed through the normal bulk workflow.

When configured, [[clearing-swift-suppression]] is an intended containment route for same-type auto-netted resultants. The required default outcome where suppression is not configured remains operationally incomplete.
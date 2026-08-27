---
type: concept
title: Hard Block Swap Agent NSTP Rule
created: 2026-08-22
updated: 2026-08-22
tags: [NSTP, hard-blocker, SWAP_AGENT, RATAN, maker-checker, settlement]
related: [swap-agent-mtm-coupon-netting-separation, ratan-cashflow-lifecycle-state-machine, ratan-rule-lifecycle-management, business-rule-maintenance, pending-auto-netting-state, clearing-resultant-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Block UAT testing.md"]
---
# Hard Block Swap Agent NSTP Rule

## Definition

The `Hard Block Swap Agent` NSTP rule is a non-STP settlement control that prevents qualifying `SWAP_AGENT` Coupon or Interim MTM cashflows from being released from RATAN.

The source states that the rule was live in UAT1 and visible in the Settlement NSTP Rules Blotter.

## Observed Behavior

For same-type `SWAP_AGENT` Coupon netting, the resultant `N1` was generated and then hit the hard-blocker rule. The exception code `Hard block Swap Agent` appeared in red on the GUI. Maker submission was rejected with:

> “This is a Swap Agent Coupon or Interim MTM cashflow ,can't be released from Ratan”

For a single `SWAP_AGENT` Interim MTM cashflow in `Pending Auto Netting`, selecting `Settle as Gross` led to the same hard-block exception and maker-submission rejection.

The tests also recorded the affected cashflows as reaching `Swift Suppressed`. This status transition is documented as an observed result, not as evidence that the cashflow was successfully released.

## Operational Controls

The UAT scenarios created the rule with Maker Checker. A separate bulk test created it with `Bulk Eligible` disabled. The hard-blocked cashflow was reported as not eligible for bulk submission, showing that bulk processing does not override the rule-level eligibility setting.

## Limitations

The evidence does not establish:

- Whether the exception is attached to the resultant, its source cashflows, or both.
- Whether the rule applies to every `SWAP_AGENT` payment type.
- Whether `Swift Suppressed` is an approved terminal outcome or only a technical status transition.
- Whether the UAT evidence represents formal sign-off or production deployment.

See [[queries/how-are-hard-blocked-netting-resultants-propagated-to-source-cashflows]].
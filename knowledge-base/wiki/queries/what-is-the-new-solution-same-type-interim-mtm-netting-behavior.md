---
type: query
title: What Is the New-Solution Same-Type Interim MTM Netting Behavior?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, UAT, SWAP_AGENT, Interim-MTM, auto-netting, NSTP]
related: [hard-block-swap-agent-nstp-rule, swap-agent-mtm-coupon-netting-separation, netting-resultant-cashflow-lifecycle, clearing-resultant-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Block UAT testing.md"]
---
# What Is the New-Solution Same-Type Interim MTM Netting Behavior?

## Question

Does the new solution permit, reject, or hard-block netting between two `SWAP_AGENT` / `Interim MTM` cashflows?

## Evidence

The old-solution test dated 2025-09-22 states that two `SWAP_AGENT` / `Interim MTM` cashflows were netted, producing `N1`. The resultant did not hit the NSTP hard blocker and instead reached the SWIFT-suppressed rule.

The new-solution tests dated 2025-10-31 cover:

- `SWAP_AGENT` Coupon plus `SWAP_AGENT` Interim MTM, rejected before netting.
- `SWAP_AGENT` Coupon plus `RECALC` Coupon, rejected in the tested strategy combination.
- `SWAP_AGENT` Coupon plus `SWAP_AGENT` Coupon, resultant generated and hard-blocked.
- A single `SWAP_AGENT` Interim MTM flow, hard-blocked after `Settle as Gross`.

No new-solution test covers Interim MTM plus Interim MTM. The old result should not be assumed to remain authoritative after the new solution.

## Resolution Needed

A new-solution test should record:

1. Whether the two source cashflows can be netted.
2. Whether a resultant is generated.
3. Which cashflow receives the NSTP exception.
4. Whether the resultant or source flows reach `Swift Suppressed`.
5. Whether un-netting or another lifecycle action is available.
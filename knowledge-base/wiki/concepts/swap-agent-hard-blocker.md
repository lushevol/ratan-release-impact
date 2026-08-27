---
type: concept
title: SWAP_AGENT Hard Blocker
created: 2026-08-22
updated: 2026-08-23
tags: [swap-agent, nstp, settlement-control, release-control, exception-management, hard-blocker, ratan, settlement-release]
related: [swap-agent, ratan, swap-agent-payment-type-netting-control, swap-agent-mtm-coupon-netting-separation, cashflow-multi-exception-generation, netting-un-net-lifecycle, clearing-resultant-swift-suppression, is-hard-block-swap-agent-currently-enabled, resultant-cashflow-hard-blocker-propagation, what-is-the-current-swap-agent-hard-blocker-configuration, murex, cashflow-suppression-rule, early-release]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design/Hard Blocker Uat1 Test Resault.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"]
---
# SWAP_AGENT Hard Blocker

The SWAP_AGENT Hard Blocker is an NSTP settlement and release control for [[ratan]]. It is intended to prevent clearing-eligible `SWAP_AGENT` Coupon and Interim MTM cashflows from being released from RATAN and settling bilaterally.

The deprecated technical-analysis source documents the control as applying where the Murex product strategy is `SWAP_AGENT` and the payment type is `Coupon` or `Interim MTM`. The UAT source tests the control for `SWAP_AGENT` Coupon and Interim MTM cashflows.

## Historical Exception Configuration

The deprecated technical-analysis source identifies the historical configuration as:

- Exception code: `Hard block Swap Agent`
- Exception category: `HARD_BLOCKER`
- Bulk eligibility: `false`

## Eligibility

### Single Cashflows

According to the deprecated technical-analysis source, the documented rule for an individual cashflow requires all of the following:

1. `Cashflow__Netting_Id` is null or empty.
2. `Instrument_Common__Murex_Product_Strategy` matches `SWAP_AGENT`, case-insensitively.
3. `Cashflow__Payment_Type` matches `Coupon` or `Interim MTM`, case-insensitively.

### Resultant Cashflows

Same-type Coupon or Interim MTM cashflows can be netted. The UAT source states that a resultant can subsequently hit the hard blocker.

The deprecated technical-analysis source describes resultant eligibility as using netting identity and a derived component marker. See [[resultant-cashflow-hard-blocker-propagation]].

## Release and Workflow Behaviour

When applicable cashflows or same-type netting resultants hit the rule, UAT evidence shows the GUI displaying the `Hard block Swap Agent` exception in red.

The UAT source reports that RATAN prevents both maker submission and checker approval, with the message:

> "This is a Swap Agent Coupon or Interim MTM cashflow ,can't be released from Ratan"

The deprecated technical-analysis source records hard-block validation during Ratan submit and approve processing. It also states that matching cashflows can remain blocked after a submission attempt while other exceptions may close.

However, the deprecated source is not authoritative regarding the operation level of the current control:

- Its initial local rule creation used `MAKER_CHECKER`.
- A later update used `MAKER_ONLY`.

Accordingly, the deprecated source says it is unsafe to infer whether the *current* control blocks maker submission, checker approval, or both. This does not negate the UAT evidence of both maker and checker blocking in the tested scenario. See [[what-is-the-current-swap-agent-hard-blocker-configuration]] and [[is-hard-block-swap-agent-currently-enabled]].

## Multiple Exceptions and Netting

The UAT source states that a hard-blocked resultant can coexist with Missing Vostro, Pending Affirmation, or other exceptions. In that multiple-exception state, the hard blocker remains release-blocking.

When an Auto SWIFT Suppressed rule is active, the UAT-tested auto-netting flow produces a `SWIFT_SUPPRESSED` resultant instead. When that rule is disabled, the resultant is expected to hit the hard blocker.

## Distinction from Suppression and Other Operations

The UAT source distinguishes blocking release from blocking all operations. It reports that a blocked item can still be manually managed through:

- Swift Suppressed
- Failed
- Reinstate
- Hold
- UnHold
- Cashflow Suppressed

A blocked resultant may also be Unnet.

The deprecated technical-analysis source separately tests interactions with `Settle as gloss`, `Swift suppression`, and `Suppress cashflow`. It states that a hard blocker is not equivalent to a cashflow- or SWIFT-suppression action, but does not formally define which actions remain permissible after the hard block. Related suppression configuration is documented in [[cashflow-suppression-rule]].

## Evidence Status

The UAT evidence has blank result fields and is not a formal confirmation that the control was approved or is currently active. The technical-analysis source is explicitly deprecated. For current enablement and configuration, see [[is-hard-block-swap-agent-currently-enabled]] and [[what-is-the-current-swap-agent-hard-blocker-configuration]].
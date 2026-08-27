---
type: query
title: What Is the Authoritative SWAP_AGENT Mixed-Payment Netting Rule?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, swap-agent, manual-netting, payment-type, settlement-day-2]
related: [hard-block-swap-agent-nstp-rule, swap-agent-mtm-coupon-netting-separation, manual-cashflow-netting, netting-eligibility-rules, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker.md"]
---
# What Is the Authoritative SWAP_AGENT Mixed-Payment Netting Rule?

## Question

Should `SWAP_AGENT` Coupon and Interim MTM cashflows be blocked from manual netting with other payment types, or should they be allowed to net?

## Conflicting evidence

The detailed requirement and proposed solution specify a UI block for:

- Coupon with Interim MTM.
- Coupon with Initial Notional or Final Notional.
- Interim MTM with Initial Notional or Final Notional.
- Coupon or Interim MTM with another product or payment type.

The specified message is:

```text
SWAP AGENT Coupon or Interim MTM can't net with the other payment type cashflow to avoid clearing eligible cashflows settling Bilaterally
```

The same requirement allows same-type Coupon + Coupon and Interim MTM + Interim MTM netting, with the resultant subsequently blocked by NSTP.

However, the open-question answer dated 2025-10-14 states that `SWAP_AGENT` Coupon and Interim MTM will net with other payment-type cashflows. That statement conflicts directly with the detailed matrix and the proposed UI behavior.

## Why resolution matters

The choice changes whether clearing-eligible cashflows can be combined with bilateral flows before the NSTP hard blocker is evaluated. It also affects:

- Manual-netting validation.
- Resultant composition and component-marker propagation.
- The scope of [[hard-block-swap-agent-nstp-rule]].
- Regression expectations for bilateral, BIC and CCIL netting.
- Whether the UI message is an acceptance criterion or obsolete design text.

## Current position

The detailed requirement should be treated as the intended behavior until an owner confirms whether the later clarification superseded it. No formal decision or UAT sign-off is included in the source.

The confirmed rule should explicitly distinguish:

1. Same-type netting eligibility.
2. Mixed-payment-type netting eligibility.
3. Release eligibility after a resultant is created.

## Evidence

- Requirement source: 26-auto-netting-page-md-files--127-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-se--pa7cqz
- Related separation concept: [[swap-agent-mtm-coupon-netting-separation]]
- Related release control: [[clearing-swift-suppression]]
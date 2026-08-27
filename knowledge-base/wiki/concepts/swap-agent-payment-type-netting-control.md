---
type: concept
title: SWAP_AGENT Payment-Type Netting Control
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, netting, payment-type, feature-flag, settlement-day-2]
related: [swap-agent, swap-agent-hard-blocker, swap-agent-mtm-coupon-netting-separation, manual-cashflow-netting, what-is-the-complete-swap-agent-payment-type-netting-matrix, what-is-the-production-setting-and-owner-of-swap-agent-hard-blocker-enabled]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design/Hard Blocker Uat1 Test Resault.md"]
---
# SWAP_AGENT Payment-Type Netting Control

The UAT document describes an unspecified `Enabled` configuration that governs netting restrictions among `SWAP_AGENT` payment types.

## Tested Behaviour

With `Enabled = true`, the documented tests reject these mixed-type pairs:

- Final Notional + Coupon
- Final Notional + Interim MTM
- Interim MTM + Coupon

The wider hard-blocker scenario also specifies rejection of Coupon or Interim MTM paired with Initial Notional or Final Notional. The rejection message states that clearing-eligible cashflows must not settle bilaterally.

With `Enabled = true`, same-type Interim MTM and same-type Coupon pairs remain nettable.

With `Enabled = false`, the tested different-type pairs—Interim MTM + Coupon, Final Notional + Coupon, and Final Notional + Interim MTM—can be netted. Tested same-type Coupon, Interim MTM, and Final Notional pairs can also be netted.

## Scope Boundary

The source does not identify the configuration property's technical name, owner, default, deployment location, or production value. It also does not test every Initial Notional pairing in the enabled configuration. Therefore, this page records UAT-tested combinations rather than a complete authoritative eligibility matrix.

See [[what-is-the-complete-swap-agent-payment-type-netting-matrix]].
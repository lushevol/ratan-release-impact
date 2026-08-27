---
type: query
title: What Is the Complete SWAP_AGENT Payment-Type Netting Matrix?
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, netting, payment-type, eligibility, settlement-control]
related: [swap-agent-payment-type-netting-control, swap-agent-hard-blocker, swap-agent-mtm-coupon-netting-separation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design/Hard Blocker Uat1 Test Resault.md"]
---
# What Is the Complete SWAP_AGENT Payment-Type Netting Matrix?

The UAT source establishes several enabled and disabled netting combinations, but it does not provide a formal exhaustive matrix across Coupon, Interim MTM, Initial Notional, and Final Notional.

## Open Points

- Confirm every pairwise payment-type outcome when `Enabled = true`.
- Confirm whether Initial Notional + Coupon and Initial Notional + Interim MTM are explicitly blocked in the implemented rule.
- Confirm whether directionality, product subtype, legal entity, currency, value date, counterparty, or clearing status changes eligibility.
- Identify the authoritative functional requirement or rule implementation that defines precedence when this control overlaps other netting rules.

The current evidence is recorded in [[swap-agent-payment-type-netting-control]].
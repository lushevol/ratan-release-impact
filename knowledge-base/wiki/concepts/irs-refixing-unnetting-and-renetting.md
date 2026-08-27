---
type: concept
title: IRS Re-Fixing Un-Netting and Re-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [IRS, re-fixing, un-netting, re-netting, amendments]
related: [automatic-un-netting-on-trade-market-events, irs-fixed-floating-leg-netting, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# IRS Re-Fixing Un-Netting and Re-Netting

IRS re-fixing un-netting and re-netting addresses a revised floating-leg coupon after an IRS fixed and floating leg have already been netted.

Before payment release or settlement, the source describes automated processing:

1. The existing floating-leg cashflow is withdrawn and cancelled.
2. The existing IRS net resultant becomes `DEAD`.
3. The fixed leg remains a `NETTED` component.
4. A replacement floating leg is received.
5. RATAN creates a revised net resultant.

The source also describes this treatment after an intra-trade resultant has itself been included in cross-trade netting: the affected intra-trade and cross-trade resultants become `DEAD`, and new resultants are constructed from the revised components.

After the original resultant has been `RELEASED` or `SETTLED`, automation stops. The floating-leg withdrawal and replacement receive `Cancel / Amend after payment release`, are NSTP, and require Operations to manually net the two amendment cashflows into a delta resultant.

This IRS-specific behaviour supplements [[automatic-un-netting-on-trade-market-events]] but does not establish generic un-netting rules for other netting mechanisms. User-initiated un-netting of a net cashflow is explicitly outside Day 1 scope.
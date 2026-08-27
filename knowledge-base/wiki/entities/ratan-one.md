---
type: entity
title: RATAN ONE
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-platform, cashflow, netting, nstp, cash-settlement, ratan, swap-agent]
related: [cash-settlement-home-page, ratan-cash-settlement-netting-service, ratanone-rule-service, ratan-rule-service, swap-agent-coupon-interim-mtm-hard-blocker, hard-block-swap-agent-nstp-rule, clearing-swift-suppression, clearing-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker.md"]
---
# RATAN ONE

RATAN ONE is the settlement platform referenced by the sources for cashflow netting, NSTP exception processing, and operational release actions.

## Role in the `SWAP_AGENT` hard-blocker requirement

For the `SWAP_AGENT` Settlement Day 2 hard-blocker requirement, RATAN ONE is the settlement application from which qualifying `Coupon` and `Interim MTM` cashflows must not be released bilaterally.

The requirement adds the `Hard Block Swap Agent` NSTP exception to prevent both maker submission and checker approval from releasing affected cashflows. The control is implemented across [[ratan-cash-settlement-netting-service]], [[ratanone-rule-service]], and [[ratan-rule-service]] and is visible in the Settlement NSTP Rules Blotter.

The intended operational owner for clearing-eligible flows is Clearing Ops. The affected `SWAP_AGENT` Coupon and Interim MTM flows remain Swift-suppressed in RATAN ONE.

## Control behavior

For a qualifying single or resultant cashflow:

- `Hard Block Swap Agent` is displayed in red.
- Maker submission is rejected.
- Checker approval is rejected.
- The user sees:

```text
This is a Swap Agent Coupon or Interim MTM cashflow ,can't be release from Ratan
```

The rule is scoped to `SWAP_AGENT` `Coupon` and `Interim MTM` cashflows. `SWAP_AGENT` `Initial Notional` and `Final Notional` cashflows are outside this specific hard blocker.

## Relationship to lifecycle actions

The blocker prevents bilateral release from RATAN ONE. The requirement nevertheless allows scenario-specific containment actions, including:

- Swift suppression
- Manual failure
- Hold
- Cashflow suppression
- Un-netting

These actions must not create a path for bilateral release from RATAN ONE.

## Implementation status

The technical-design source provides implementation and test traceability. It does not confirm deployed versions, enabled rule configuration, or production activation.

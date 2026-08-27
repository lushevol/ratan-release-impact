---
type: entity
title: Markitwire
created: 2026-08-22
updated: 2026-08-22
tags: [markitwire, trade-allocation, irs, ccs, cash-settlement, allocation, trading-platform, straight-through-processing]
related: [fmrp, ratan, stella, straight-through-processing, auto-netting, f2b-hk-tw-milestone-checklist, fmrp-prime-uk-uat-drop-2, irs, ccs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---

# Markitwire

## Role in onboarding

Markitwire is an external trade and clearing platform and an allocation source for IRS and CCS scenarios.

The two checklist versions describe Markitwire in separate onboarding scopes:

- In the **HK/TW F2B onboarding** scope, Markitwire IRS and CCS allocation is in scope for Drop 2.
- In the **Prime UK UAT Drop 2** scope, Markitwire is identified as the allocation source for IRS and CCS scenarios.

## Straight-through-processing exception

The checklists state that cashflows for the `ALOC` name are not STP'd. This exception applies to the Markitwire allocation flow and must not be generalized to all IRS or CCS cashflows.

Accordingly, allocation capability and straight-through processing are separate requirements: Markitwire allocation is in scope even though the relevant `ALOC`-name cashflows are explicitly excluded from STP.

## Related onboarding behavior

The HK/TW onboarding checklist requires validation of:

- Allocation handling for IRS and CCS.
- Non-STP treatment for `ALOC`-name cashflows.
- SSI stamping using the applicable product and CFI-code rules.
- Interaction with [[ratan]] and downstream settlement processing.

The available source material does not define Markitwire message formats, allocation identifiers, ownership, or reconciliation procedures.
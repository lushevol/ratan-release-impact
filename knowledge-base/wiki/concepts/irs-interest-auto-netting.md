---
type: concept
title: IRS Interest Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, irs, interest, pending-another-leg, refixing]
related: [auto-netting, pending-another-leg, ratan, fmrp, f2b-hk-tw-milestone-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# IRS Interest Auto Netting

IRS Interest Auto Netting is the process of holding a fixed-leg cashflow until the related floating-leg cashflow is received, then automatically netting the eligible legs.

## Required behavior

The HK/TW onboarding checklist requires:

1. The fixed cashflow is held as `pending another leg`.
2. The floating leg is received.
3. The related cashflows are automatically netted.
4. A re-fixing breaks the previous netting.
5. New netting is created using the latest cashflow.

This sequence must be tested as both an initial netting and a re-fixing scenario. The source does not define correlation keys, event ordering, reversal messages, or reconciliation tolerances.

## Scope boundary

This requirement is specific to IRS interest cashflows. It should not be generalized to NDS Auto Netting, Principal + Interest Netting, or unrelated cross-product flows without separate evidence.
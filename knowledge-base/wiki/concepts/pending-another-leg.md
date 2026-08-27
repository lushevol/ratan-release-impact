---
type: concept
title: Pending Another Leg
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-status, netting, irs, nd-irs, nd-ccs]
related: [irs-interest-auto-netting, auto-netting, cashflow-status-handling, ratan, f2b-hk-tw-milestone-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# Pending Another Leg

`Pending another leg` is a temporary cashflow status used when processing must wait for a related leg before settlement or netting can proceed.

## Checklist usage

The HK/TW onboarding uses this status for:

- IRS fixed cashflows awaiting the floating leg.
- ND IRS behavior that follows normal IRS behavior.
- NDIRS and NDCCS initial cashflows in the referenced scenarios.

The expected pattern is:

```text
Initial leg
    |
    v
pending another leg
    |
    | related leg received
    v
Automatic netting
```

The status is distinct from `Pending Fixing`, `Group Pending`, and `Group Pending Validation`. The source does not define timeout, cancellation, retry, or manual-release semantics.

## Scope caution

ND IRS is explicitly in scope. ND CCS is mentioned in scenarios and in Story `8244494`, but its F2B versus drop-2 boundary remains unresolved. See [[is-nd-ccs-in-scope-for-f2b-hk-tw]].
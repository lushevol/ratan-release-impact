---
type: query
title: Is ND CCS in Scope for F2B HK/TW?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, nd-ccs, nd-irs, f2b, hk, tw, scope]
related: [f2b-hk-tw-milestone-checklist, pending-another-leg, auto-netting, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# Is ND CCS in Scope for F2B HK/TW?

## Question

Is ND CCS part of the current F2B HK/TW onboarding milestone, or is it limited to drop 2?

## Evidence

The checklist states that ND IRS is in scope and should behave like normal IRS. It also includes scenarios for NDIRS and NDCCS in which the initial cashflow is held as `pending another leg`, all legs are tagged, and the legs are automatically netted.

At the same time, the checklist references Story `8244494 [Stella] ND CCS Auto Netting` and marks the feature as available for drop 2. This creates an unresolved release-boundary ambiguity.

## Required resolution

Confirm:

- Whether ND CCS has current-milestone acceptance criteria.
- Whether the NDIRS/NDCCS scenarios belong to the drop-2 test pack.
- Whether SSI stamping and CFI-code validation apply to ND CCS in F2B.
- Which release owns Story `8244494`.
- Whether the adjacent NDS Auto Netting note is a dependency, fallback behavior, or future scope.

Until resolved, ND IRS may be treated as explicitly in scope, while ND CCS should not be recorded as a completed F2B commitment.
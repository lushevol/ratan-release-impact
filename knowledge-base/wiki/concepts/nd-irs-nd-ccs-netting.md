---
type: concept
title: ND IRS and ND CCS Netting
created: 2026-08-22
updated: 2026-08-22
tags: [nd-irs, nd-ccs, netting, nid, ratan, korea]
related: [korea, auto-netting, ccs-auto-netting, irs-auto-netting, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# ND IRS and ND CCS Netting

## Netting model

The Korea checklist states that ND CCS and ND IRS should net in [[entities/ratan]]. The booking-model section associates ND currency handling with NID-based netting.

The checklist also states that only IRS is currently allowed for netting over netting and that ND IRS follows the same ISDA taxonomy.

## Boundary

This requirement concerns cashflow netting and settlement behavior. It should not be interpreted as a requirement to migrate new FMRP products or events, because those rows are explicitly marked as not applicable for cashflow migration.
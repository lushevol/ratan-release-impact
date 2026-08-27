---
type: concept
title: Murex-to-RATAN Rule Replication
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, stella, nstp, suppression, migration]
related: [murex, ratan, stella, cashflow-suppression, straight-through-processing, f2b-hk-tw-milestone-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# Murex-to-RATAN Rule Replication

Murex-to-RATAN rule replication is the selective translation of legacy Murex behavior into RATAN processing for STELLA cashflows.

## Required rule areas

The checklist requires Murex behavior to be replicated for:

- NSTP rules.
- SWIFT suppression rules.
- Cashflow suppression rules.

Murex interface filters that exclude particular auto-suppression counterparties are not available in the same form for STELLA. Those filters must instead be configured as RATAN suppression rules.

This is a behavioral mapping rather than an assumption that implementation is identical. Rule inventory, precedence, effective dates, entity scope, and exceptions must be documented separately.

## Acceptance expectations

Testing should demonstrate that:

- NSTP is triggered as expected.
- Expected SWIFT suppression cases are suppressed.
- Client Clearing Portfolios cashflows are automatically suppressed.
- Replicated behavior works on STELLA cashflows.

The checklist excludes several named NSTP rules according to Candice, including `PRC_SCBHK_SGEI`, `PRC_USD_SGEI`, `PRC_SGE_SWP`, `PRC_HOC_SGE_SWP`, and `PRC_HOSGE_N_IMA`.
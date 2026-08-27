---
type: concept
title: Korea Settlement Accounting
created: 2026-08-22
updated: 2026-08-22
tags: [korea, settlement-accounting, ebbs, aspire, lms, payment, accounting]
related: [korea, ebbs, aspire, lms, cashflow-accounting-release, kro-to-krw-currency-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# Korea Settlement Accounting

## Requirements

The checklist requires `KRO` to `KRW` mapping for accounting and states that Korea requires settlement accounting for all settlement accounts because LMS is not yet onboarded.

It identifies the following accounting components:

- EBBS real-time feed.
- EBBS end-of-day feed.
- ASPIRE integration.
- Bridge account number.
- EBBS branch code.
- EBBS transaction type.
- Onshore-currency treatment.
- Historic cashflows and events on past-value cashflows after cutover.

## Target-model uncertainty

The source considers moving from the Aspire model to an EBBS model but does not establish whether this is an approved transition, a parallel-run design, or a future-state option. Balaji is named to confirm settlement-accounting requirements.

New Vostro and Nostro settlement means and accounts also require agreement.
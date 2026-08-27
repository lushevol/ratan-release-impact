---
type: concept
title: Cash-Settlement Accounting Routing
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, accounting, ebbs, aspire, keystone, migration]
related: [ebbs, aspire, keystone-hk, ratan, cashflow-accounting-release, cashflow-migration, f2b-hk-tw-milestone-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# Cash-Settlement Accounting Routing

Cash-settlement accounting routing is the distribution of settlement accounting events to the appropriate downstream accounting systems during HK/TW onboarding and the Aspire-to-EBBS transition.

## Documented routing

The checklist identifies the following routing:

```text
Keystone (HK) Nostro data       -> EBBS
Keystone (HK) Over Account data -> EBBS
Keystone (HK) Suspense data     -> ASPIRE
```

The processing scope includes EBBS real-time feeds, ASPIRE integration, end-of-day feeds, historic cashflows, and events on past-value cashflows after cutover. Special CNH logic must be checked with Balaji.

## Acceptance criterion

```text
No Accounting Errors
```

The source also marks a settlement-accounting configuration row as “No changes.” This may describe branch and account configuration rather than the accounting architecture, because the same checklist describes an Aspire-to-EBBS operating-model transition. The distinction requires confirmation.

## Missing design data

The source does not define bridge accounts, EBBS branch codes, transaction types, accounting event mappings, reconciliation controls, duplicate handling, or failure recovery.
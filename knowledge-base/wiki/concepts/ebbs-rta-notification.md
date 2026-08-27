---
type: concept
title: EBBS RTA Notification
created: 2026-08-23
updated: 2026-08-23
tags: [ebbs, rta, event-filtering, settlement]
related: [ebbs, ratan, auto-dvp, rta-cashflow-validation, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# EBBS RTA Notification

An EBBS RTA is a real-time alert generated for account debit or credit activity. For Auto DVP, RATAN accepts only `CorporateFinancial` messages with `CreditDebitFlag=D`.

`CorporateFinancial` represents client-account debit or credit activity. `InternalAccount` represents Nostro-account debit or credit activity and is excluded from initial Auto DVP scope. A qualifying debit RTA must still be identified as a receive-cashflow event; RATAN must do nothing for a pay-cashflow RTA.

The source notes that EBBS events are not exclusively DVP-related. It also records that duplicate RTAs were not observed in Razor BAU, although Razor has narration-based duplicate filtering. RATAN's idempotency contract remains unspecified.
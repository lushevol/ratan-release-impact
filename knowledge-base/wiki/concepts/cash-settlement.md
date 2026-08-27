---
type: concept
title: Cash Settlement
created: 2026-08-22
updated: 2026-08-22
tags: [settlement, cashflows, financial-operations]
related: [ratan, ratan-settlement-korea, auto-netting, reconciliation, nostro-configuration, settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# Cash Settlement

Cash settlement is the operational process of discharging cash obligations arising from trades or other financial transactions.

## RATAN Context

In [[ratan]], cash settlement involves:

- Cashflow accounting and queries.
- Grouping and [[auto-netting]].
- Nostro and bridge-account configuration.
- Currency cut-offs.
- Rule evaluation.
- SWIFT MT/MX messaging.
- Routing to systems and consumers such as Murex, LOANIQ, TLM, and TIS.
- Frontend blotters, warnings, dashboards, and operational controls.

## Korea Release

The [[ratan-settlement-korea]] release adds or validates Korea-specific static data, Nostro records, bridge accounts, transaction codes, sender BIC configuration, rules, auto-netting configuration, and frontend entities and currencies.
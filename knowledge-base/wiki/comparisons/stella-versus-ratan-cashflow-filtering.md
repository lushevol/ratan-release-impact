---
type: comparison
title: "Stella Versus Ratan Cashflow Filtering"
created: 2026-08-23
updated: 2026-08-23
tags: [stella, ratan, cashflow, filtering, suppression, architecture]
related: [stella-ratan-cashflow-filtering, suspended-versus-projected-cashflow-status, fx-replication-to-razor, stella, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md"]
---
# Stella Versus Ratan Cashflow Filtering

| Dimension | Stella | Ratan |
| --- | --- | --- |
| Primary role | Apply simple, static, high-volume suppression rules upstream | Apply complex or dynamic filtering and settlement-destination logic |
| Typical outcome | Mark straightforward exclusions `SUSPENDED`; publish other suppressed flows as `PROJECTED` | Retain flows expected to settle in Ratan and filter or abort flows routed elsewhere |
| Example rules | Migrated, shell-trade, ETD, PreAllocation, and portfolio-reassignment cashflows | FX replication, entity/counterparty rules, trade state, event filtering, and FXO structure processing |
| User control | Source does not specify front-end rule editing | Rules must be editable through the front end |
| Exception handling | Suspended flows disappear from the group blotter | Suspended flows may be manually STPed through maker-checker control |
| Key risk | Future FX rule changes may conflict with current routing | Incomplete precedence and amendment handling may create duplicate or missing payments |

The division is an architectural proposal rather than a fully governed contract. The source leaves authority, precedence, status transitions, and configuration synchronization unresolved.
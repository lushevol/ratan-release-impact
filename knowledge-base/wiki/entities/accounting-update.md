---
type: entity
title: AccountingUpdate
tags: [AccountingUpdate, cash-settlement, data-field, production-data]
related: [cashflow, accounting-update-production-volume-baseline, ratanone, uber, fxu]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan/Production Existing Data Testing Cases.md"]
---
# AccountingUpdate

## Context

`AccountingUpdate` is the dimension used by the production data inventory in [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1ijfplm]]. The source lists update categories such as `New`, `Materialize`, `Net`, `Settle`, `GenerateSwift`, and `CashflowStamped`, together with observed counts.

The source also contains `AccountingUpdate` as a value in the same dimension, with a count of `3116582`. It does not explain whether this value is a generic event type, a persisted status, or an aggregate label.

## Data semantics requiring confirmation

The source does not define whether an `AccountingUpdate` count represents rows, events, transitions, messages, or distinct [[cashflow]] objects. It also does not state whether categories are mutually exclusive or whether multiple categories can be recorded for one cashflow.

Until these semantics are confirmed, the values should be treated as an observed production inventory rather than a directly comparable set of lifecycle volumes.
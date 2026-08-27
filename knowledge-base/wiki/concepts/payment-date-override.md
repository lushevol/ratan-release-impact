---
type: concept
title: Payment Date Override
tags: [cashflow, payment-date, value-date, operations, deprecated]
related: [cashflow-detail-field-projection, cashflow-status-lifecycle, cash-settlement-platform, fmo-ops, what-is-the-authoritative-payment-date-override-and-source-visibility-contract]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/SFMRP - Cash Settlement Platform Integration（Deprecated）.md"]
---
# Payment Date Override

A payment-date override is an operations-maintained date distinct from the source cashflow `Value Date`.

## Historical behavior

The deprecated integration requirement states that [[fmo-ops]] may identify an invalid value date and set a separate `Payment Date` while retaining the original `Value Date`. The illustrated payment remains `Pending`.

The source says that `Payment Date` is transparent for Blade and [[stella]]. It does not define whether transparency means the field is hidden, omitted from query responses, displayed read-only, or unavailable for amendment processing.

## Limitations

The source duplicates its only payment-date example and does not specify authorization, audit history, downstream message effects, lifecycle progression, or reconciliation behavior. It is therefore not a current field-ownership contract. See [[what-is-the-authoritative-payment-date-override-and-source-visibility-contract]].
---
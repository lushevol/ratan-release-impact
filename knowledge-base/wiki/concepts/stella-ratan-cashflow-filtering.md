---
type: concept
title: "Stella-Ratan Cashflow Filtering"
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, filtering, suppression, stella, ratan, system-boundary]
related: [suspended-versus-projected-cashflow-status, fx-replication-to-razor, murex-2-11-cashflow-suppression, stella, fmrp, tds3, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md"]
---
# Stella-Ratan Cashflow Filtering

## Responsibility model

The source proposes that Stella own simple, static, high-volume suppression rules, while Ratan maintain complex or dynamic routing logic. Stella marks excluded cashflows as `SUSPENDED` and may publish suppressed cashflows as `PROJECTED`. Ratan retains and filters flows according to their expected settlement destination.

Cashflows expected to settle in Razor should generally be suppressed before or outside Ratan. Cashflows expected to settle in Ratan must remain processable there.

## Rules assigned to Stella

The explicitly Stella-owned rules cover:

- Migrated trades with payment types beginning `Migrated_Aggregated`.
- Shell trades where `Is_Shell_Trade = true`.
- ETD trades with `Base_Product` equal to `Listed Option` or `Future`.
- PreAllocation trades.
- Eligible FX `additionalPayment` cashflows under the current rule.
- Portfolio reassignment aggregation where `Effective Date>=Payment_Date`.

The default remaining outcome is `PROJECTED`.

## Governance limitations

The source contains overlapping or incomplete logic across Stella, Ratan, Murex, and Razor. It does not define authoritative precedence, idempotency, effective dating, configuration ownership, or synchronization controls. Dated entity/counterparty additions and the unsynchronized FMRP1 suppression rule demonstrate that rule-version governance is operationally significant.

The amendment scenario also shows that filtering must account for trade versions, withdrawals, replacement cashflows, and settlement destination to prevent duplicate or missing payments.
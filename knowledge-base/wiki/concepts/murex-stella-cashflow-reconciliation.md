---
type: concept
title: Murex-Stella Cashflow Reconciliation
tags: [reconciliation, cashflow, murex-2-11, stella, trade-migration, cn]
related: [cn-trade-migration, murex-2-11, stella, ratan, cashflow-materialization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Murex-Stella Cashflow Reconciliation

Murex-Stella cashflow reconciliation is the proposed comparison of legacy Murex 2.11 cashflows against cashflows created for migrated Stella trades.

## Trade mapping

The reconciliation relies on a Stella trade extraction:

- `Trade_Id` is the Stella trade ID.
- `Migrated_Trade_Id` is the Murex 2.11 trade ID.

## Matching attributes

Within a mapped trade, cashflows are compared by:

- Entity (`FMID`)
- Counterpart (`FMID`)
- Payment Date
- Currency
- Pay/Receive Direction
- Amount

## Scope uncertainty

The same source specifies two different horizons: “next 9 days” in the initial requirement and `T+7` in the final reconciliation section. It does not define duplicate handling, amount tolerance, one-to-many mapping, unmatched-item workflow, or a reconciliation completion threshold.

See [[what-is-the-authoritative-murex-stella-cashflow-reconciliation-horizon]].
---
type: query
title: "What Were the Authoritative Migration Date and Final Scope?"
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, migration-date, trade-scope, reconciliation, runbook]
related: ["fxo-mini-trade-migration-ratan-cash-settlement", "mini-trade-migration", "high-risk-nstp-rule", "trade-cashflow-reconciliation"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md"]
---
# What Were the Authoritative Migration Date and Final Scope?

## Question

Which migration weekend and trade population should be treated as authoritative for the FXO mini trade migration?

## Evidence requiring resolution

The source file name identifies the `2026-08-15` weekend, and most surrounding activities refer to August 2026. However, Step 6 labels the migration weekend as `2026-05-16`.

The source also records:

- More than 100 trades.
- An interim count of 130 trades on 2026-08-03.
- Five paired portfolio groups.
- An initial portfolio-based Murex rule.
- A later Murex rule based on cancelled or original trade IDs.

It is unclear whether the trade-ID list supplements or fully replaces the portfolio list, how unmapped trades are handled, and what the final count was.

## Related operational questions

Resolution should also establish:

- The timezone and business-calendar interpretation of the VD and payment-date references.
- Whether the missing steps 13, 16, and 17 are intentional.
- Whether both Murex and Stella NSTP rules were disabled after migration.
- The acceptance criteria and sign-off for each reconciliation.
- The treatment of incorrectly released, settled, waiting, or reversed cashflows.
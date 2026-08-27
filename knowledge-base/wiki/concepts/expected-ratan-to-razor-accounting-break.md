---
type: concept
title: Expected Ratan-to-Razor Accounting Break
created: 2026-08-22
updated: 2026-08-22
tags: [Ratan, Razor, accounting, reconciliation, failed-process]
related: [cashflow-technical-failure-recovery, murex-ratan-migration-reconciliation, cashflow-migration-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md"]
---
# Expected Ratan-to-Razor Accounting Break

The source records an operating decision that Ratan will not send a failed cashflow to Razor for accounting. As a result, a difference between the trade and cashflow accounting records is expected in the reconciliation process.

## Stated Behavior

The documented sequence is:

1. A cashflow processing failure occurs in Ratan.
2. Ratan omits that failed cashflow from the accounting flow to Razor.
3. Reconciliation observes a trade-versus-cashflow accounting break.
4. The break is treated as expected for the stated scenario.

This claim is attributed in the source to Dinesh.

## Scope and Controls

The source does not identify the exact failure statuses covered by this behavior, the reconciliation classification code, the break-aging rule, or the process for resolving or approving the break. It should therefore not be generalized to all Ratan failures.

This concept complements [[concepts/cashflow-technical-failure-recovery]] and should be considered in [[concepts/murex-ratan-migration-reconciliation]], particularly where Ratan, Razor, EBBS, PSGL, and TLM results are compared.
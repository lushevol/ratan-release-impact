---
type: concept
title: Static-Data Readiness
created: 2026-08-22
updated: 2026-08-22
tags: [static-data, SSI, Vostro, migration, UAT, settlement]
related: [ssi-plus, fmrp, cashflow-migration-readiness, murex-ratan-migration-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md"]
---
# Static-Data Readiness

Static-data readiness is the verification that settlement accounts, settlement instructions, validation rules, currency controls, netting rules, suppression rules, NSTP rules, and limits are configured and tested before cashflow migration.

## Vostro Dependencies

The source identifies Vostro as the most detailed static-data dependency. Required checks include:

- CFI Code.
- SSI+ changes.
- Settlement account and settlement means.
- Beneficiary BIC and name.
- Ordering customer.
- Swift Type.
- Ratan Vostro validation rules.
- Effective date.
- MT202 Cover Payment.

The source states that Vostro migration remained in progress even though the SSI stamping proof of concept was complete.

## Required Preparation

The planned actions were:

1. Dinesh confirms the CFI Code.
2. Dinesh and Sumita provide the CN client list.
3. The SSI+ team updates the data, reviews it with PO/operations, and uploads it to UAT.
4. The Ratan team verifies Vostro data in ES.
5. The Ratan team executes SSI stamping UAT cases.
6. The Razor team executes Swift Generation test cases.
7. Yash follows up on SSI+ open items.

The source leaves Nostro, Currency Cutoff, Netting Rules, Suppression Rules, NSTP Rules, and USD Limit without status or action details. Blank rows are not evidence of readiness.
---
type: concept
title: Payment Accounting Reversal
tags: [payment-accounting, reversal, settlement, cashflow-lifecycle]
related: [ebbs-payment-accounting-integration, accounting-posting-lifecycle, failed-cashflow-accounting, netting-resultant-cashflow, manual-un-netting, bic-netting-un-netting]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# Payment Accounting Reversal

A payment-accounting reversal is a new eBBS posting that reverses the latest accounting entry associated with a cashflow.

## Triggering actions

The requirement associates reversals with:

- Withdrawal after release.
- Reinstatement.
- Unsuppress approval for a sent `SWIFT_SUPPRESSED` posting.
- Un-netting of a sent `SWIFT_SUPPRESSED` or `FAILED` resultant.
- Component-withdrawal scenarios involving a released resultant.

## Reversal rules

A reversal:

1. Queries the latest accounting transaction.
2. Generates a new message ID and external-system key.
3. Flips `C` to `D` and `D` to `C`.
4. Switches the transaction-code legs.
5. Inherits other fields from the relevant new cashflow unless component-withdrawal rules apply.

For a component withdrawal, the account numbers are inherited from the released resultant’s accounting entry while other fields are generated from the component.
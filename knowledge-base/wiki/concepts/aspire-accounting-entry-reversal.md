---
type: concept
title: Aspire Accounting Entry Reversal
created: 2026-08-23
updated: 2026-08-23
tags: [payment-accounting, reversal, cashflow, aspire]
related: [aspire-payment-accounting, aspire-accounting-status-lifecycle, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# Aspire Accounting Entry Reversal

An Aspire accounting reversal is the reverse flow of the latest accounting entry on a cashflow.

The requirement specifies reversals for qualifying withdrawals, immediate reinstatement, checker-approved unsuppression of a sent SWIFT_SUPPRESSED entry, and un-netting of a sent SWIFT_SUPPRESSED or FAILED netting resultant. When the original accounting entry remains holding, unsuppression disables it and qualifying un-netting is ignored rather than creating a reversal.

These rules are accounting consequences only. They do not independently authorize the underlying withdrawal, reinstatement, unsuppression, or un-netting event.
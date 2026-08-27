---
type: concept
title: Aspire Accounting Status Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [payment-accounting, status, aspire, ratan]
related: [aspire-payment-accounting, aspire-accounting-entry-reversal, what-is-the-authoritative-ratan-aspire-accounting-status-transition-matrix]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# Aspire Accounting Status Lifecycle

The Aspire-accounting status lifecycle describes the processing condition of an accounting entry, not the status of its source cashflow.

- `HOLD`: an entry exists but is held because it has not reached value date.
- `DISABLED`: a held entry is disabled after a reversal scenario before posting.
- `SUCCESS`: an entry has been sent to Aspire.
- `MISSING_INFO`: RATAN does not generate an entry because Nostro or another mandatory value is unavailable.

Cashflow states such as Released, Settled, FAILED, and SWIFT_SUPPRESSED drive eligibility but are not accounting statuses. The complete allowed combinations and transitions remain unresolved in [[what-is-the-authoritative-ratan-aspire-accounting-status-transition-matrix]].
---
type: concept
title: Swift Suppressed LMS Feed Contract
created: 2026-08-23
updated: 2026-08-23
tags: [LMS, Swift, suppression, integration-contract, cash-settlement]
related: [lms, scbml-cashflow-data-message, receive-only-swift-suppressed-cashflow, manual-entity-lms-reference-data-feed, cashflow-suppression-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---
# Swift Suppressed LMS Feed Contract

This contract defines the proposed LMS feed extension for receipt-only cashflows in Swift Suppressed status.

## Confirmed rule

Send the cashflow to LMS when its status is:

- `RELEASED`
- `SETTLED`
- `Swift Suppressed (Receive only)`

Other statuses remain excluded unless separately approved.

## Lifecycle messages

The source records that additional messages are required for:

- Undo Swift Suppression after the initial Swift Suppressed receipt.
- Withdrawal after the initial Swift Suppressed receipt, when the cashflow becomes `CANCELLED`.

No authoritative event names or payload mappings have been agreed. Treatment of `Manual Failed`, resulting in `FAILED`, is unanswered.

## Required contract decisions

The LMS integration must define:

1. The business event for each lifecycle transition.
2. Whether cashflow status is carried in a dedicated field.
3. Whether lifecycle messages are inserts, updates, withdrawals, or another event type.
4. The minimum payload when Vostro/Nostro stamping is unavailable.
5. Retry, idempotency, duplicate, ordering, and reconciliation behavior by `cashflowId`.
6. Validation of `receiverPartyReference = Debit` for receive-only cashflows.

The SCBML `CashflowData` template is a starting point, not a finalized contract.

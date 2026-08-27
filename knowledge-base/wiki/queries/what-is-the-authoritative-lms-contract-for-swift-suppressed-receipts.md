---
type: query
title: What Is the Authoritative LMS Contract for Swift Suppressed Receipts?
created: 2026-08-23
updated: 2026-08-23
tags: [LMS, Swift, suppression, open-question, integration-contract]
related: [swift-suppressed-lms-feed-contract, scbml-cashflow-data-message, lms, manual-entity-lms-reference-data-feed, receive-only-swift-suppressed-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---
# What Is the Authoritative LMS Contract for Swift Suppressed Receipts?

## Question

What exact LMS message contract applies to a receipt-only cashflow as it moves through Swift Suppressed, Undo Swift Suppression, withdrawal to `CANCELLED`, and possible Manual Failed transition to `FAILED`?

## Known evidence

The initial `Swift Suppressed (Receive only)` cashflow must be sent to LMS. Dinesh also confirmed that Undo Swift Suppression and withdrawal require another LMS message.

## Unresolved points

- Event values for each transition.
- Whether the message is an insert, update, withdrawal, or another event.
- Whether a dedicated cashflow-status field is needed.
- Whether the same payload is used for every transition.
- Whether `FAILED` requires a message.
- Retry, duplicate, ordering, and reconciliation rules.

The source records both pending LMS confirmation and later confirmation that messages are needed. The latter resolves message necessity for Undo and Withdrawal but does not resolve their payload semantics.

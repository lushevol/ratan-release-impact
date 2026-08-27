---
type: query
title: Does LMS Require Vostro/Nostro Data for Swift Suppressed Receipts?
created: 2026-08-23
updated: 2026-08-23
tags: [LMS, Vostro, Nostro, SSI, Swift, open-question]
related: [swift-suppressed-lms-feed-contract, scbml-cashflow-data-message, receive-only-swift-suppressed-cashflow, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---
# Does LMS Require Vostro/Nostro Data for Swift Suppressed Receipts?

## Question

Can LMS process a receipt-only Swift Suppressed cashflow when Vostro/Nostro stamping information is unavailable, or must the source system perform additional stamping before sending the message?

## Evidence

The requirement states that Vostro/Nostro stamping may not exist at Swift Suppressed status. The proposed `CashflowData` payload includes SSI, routing, beneficiary, correspondent, and settlement-account fields, but most are marked non-mandatory in the mapping.

## Required confirmation

The LMS team should specify:

- Which settlement-instruction fields are mandatory for a Swift Suppressed receipt.
- Whether missing optional values are accepted.
- Whether additional stamping is required.
- Whether a message may be sent before settlement instructions are available.
- How missing SSI data affects downstream processing and reconciliation.

Until confirmed, the payload cannot be treated as complete for all Swift Suppressed receipts.

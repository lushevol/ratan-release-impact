---
type: concept
title: India Payment LEI SWIFT Enrichment
created: 2026-08-23
updated: 2026-08-23
tags: [LEI, India, SWIFT, payment, regulatory-enrichment]
related: [ratan, sci, ssi-swift-field-enrichment, sci-lei-regulatory-data-lookup, ssi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md"]
---
# India Payment LEI SWIFT Enrichment

India Payment LEI SWIFT Enrichment is the conditional insertion of booking-entity and counterparty Legal Entity Identifiers into generated SWIFT messages for qualifying SCB payments.

## Eligibility Rule

All of the following conditions must hold:

1. The cashflow is a payment rather than a receipt.
2. The payment is an SCB payment.
3. The currency is in the stated `(INR, INO, INY)` scope and is represented as INR in SWIFT.
4. The amount is at least INR 500,000,000.
5. The booking entity is the India branch identified by `FMID = 4` and `FMCODE = SCB BOMBAY*MMB`.
6. The settlement means is `NOS`.
7. The message type is MT103 or MT202.

The rule excludes Over-Account and other settlement means, MT202 Flip, MT103+202COV, and MT210.

## Message Formatting

For MT103, the two LEIs are placed in field 70. For MT202, they are placed in field 72. The booking-entity LEI occupies line 1 and the counterparty LEI occupies line 2.

Existing SSI text on line 1 is displaced to line 3 onwards. The requirement states that content beyond line 2 for field 70 or line 4 for field 72 is ignored.

## Processing Boundary

Enrichment occurs during SWIFT generation in [[ratan]]. LEIs are not required on the SSI user interface. MT192 and MT292 require no independent LEI logic; their corresponding messages should reflect the enriched MT103 or MT202.

This is a narrow India regulatory rule, not a universal requirement to add LEIs to every SWIFT message or settlement instruction.
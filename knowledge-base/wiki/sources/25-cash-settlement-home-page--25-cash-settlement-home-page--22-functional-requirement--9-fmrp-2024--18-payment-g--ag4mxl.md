---
type: source
title: "Payment Generation — FMRP 2024 Functional Requirement"
authors: []
year: 2024
url: ""
venue: ""
tags: [cash-settlement, fmrp, payment-generation, functional-requirement]
related: [fmrp, agency-payment-identification, cashflow-accounting-eligibility, what-is-the-authoritative-agency-payment-booking-and-swift-generation-model]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FMRP 2024/Payment Generation.md"]
---
# Payment Generation — FMRP 2024 Functional Requirement

## Source status

The source path identifies a 2024 FMRP functional-requirement document concerning payment generation. The document body was not available during ingest, so no functional requirements, field definitions, workflows, interfaces, statuses, acceptance criteria, or structured data can be summarized reliably.

## Scope indicated by the filename

The filename indicates a relationship between [[fmrp]] and payment generation within the Cash Settlement functional-requirement collection. This is contextual metadata only and does not establish the system's authoritative role or the document's current status.

Potential areas requiring confirmation from the original document include:

- Payment-generation triggers and eligibility criteria
- Inputs, outputs, and payment identifiers
- Booking and settlement-state prerequisites
- Agency-payment handling
- SWIFT message generation
- Exception, rejection, approval, and retry behavior
- Amendments, cancellations, and payment versioning
- Integrations with [[murex-2-11]], [[ratan]], or other settlement components

## Evidence limitations

No source text was provided for verification. In particular, this page does not assert:

- Which system generates or authorizes payments
- Whether payment generation is automatic or manual
- Which cashflow statuses qualify for payment generation
- Whether accounting booking precedes or follows SWIFT generation
- How payment amendments affect payment identity
- Whether the requirement remains authoritative or has been superseded

The original file should be reviewed before using this page as an implementation or control reference.

## Related investigation

The document may inform the open question [[what-is-the-authoritative-fmrp-payment-generation-contract]]. Comparison with [[what-is-the-authoritative-agency-payment-booking-and-swift-generation-model]] and [[cashflow-accounting-eligibility]] is recommended once the source body is available.
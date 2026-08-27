---
type: query
title: What Are the Idempotency and Recovery Rules for Murex Batch Republication?
created: 2026-08-24
updated: 2026-08-24
tags: [murex, ratan, idempotency, recovery, replay, batch-processing]
related: [murex, ratan, murex-batch-cashflow-ingestion, cashflow-reinstatement-and-replay, cash-settlement-exception-handling, what-is-the-canonical-replay-and-reinstate-procedure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Murex batch processing.md"]
---
# What Are the Idempotency and Recovery Rules for Murex Batch Republication?

The source requires Murex republication after both batch-level and record-level errors, but does not specify how [[ratan]] identifies replacements, prevents duplicates, or resumes a blocked feed.

## Questions to Resolve

- Which file identity, cashflow identity, version, and checksum distinguish an original delivery from a republication?
- Does a republished file replace an entire prior file, replay only rejected records, or include previously accepted records?
- Is a rejected payment republished in a standalone file, a delta file, or a reissued base file?
- Can RATAN continue processing later records after `PaymentValidationError`, and how is partial file success recorded?
- What is the exact scope of the halt after `BatchFileFormatError` or `BatchCountReconError`: feed, region, business date, or sequence?
- What durable state records the block, and what validation is required to unblock processing?
- Who owns alerting, correction, republication, and confirmation of recovery?
- How are duplicate and out-of-order replacement messages handled?

The document establishes the need for republication but does not establish replay semantics. It must not be treated as confirming the canonical procedures in [[cashflow-reinstatement-and-replay]] or [[what-is-the-canonical-replay-and-reinstate-procedure]].
---
type: concept
title: Murex Batch Cashflow Ingestion
created: 2026-08-24
updated: 2026-08-24
tags: [murex, ratan, batch-processing, cashflows, file-ingestion]
related: [murex, ratan, cash-settlement-exception-handling, cashflow-reinstatement-and-replay, what-is-the-authoritative-murex-batch-file-contract, what-are-the-idempotency-and-recovery-rules-for-murex-batch-republication]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Murex batch processing.md"]
---
# Murex Batch Cashflow Ingestion

Murex batch cashflow ingestion is the proposed scheduled transfer of cashflow files from [[murex]] to [[ratan]] for the UK cashflow-feeding requirement.

## Proposed Delivery Pattern

The source describes a two-hourly delivery pattern from `00:00:00` through `19:00:00`:

- Murex sends a snapshot file and a base file for each batch interval.
- Murex creates a complete file after upload completion.
- Base files may contain up to 45,000 records.
- Base files contain only `SNTR`-status cashflows.

The document does not specify the meaning of `SNTR`, the content of snapshot files, or whether a complete file must gate RATAN processing. It also does not define the time zone, expected file count, pairing identifier, ordering, or behavior for delayed and duplicate deliveries.

## Error Granularity

The stated policy separates batch-level failures from record-level failures:

- `BatchFileFormatError` and `BatchCountReconError` stop the current file and all further files while Murex republishes the failed file.
- `PaymentValidationError` stops only the invalid record while Murex republishes the payment.

This is a preliminary policy rather than a complete state machine. The scope of “further files,” the persistence of blocked-feed state, and the handling of later records in a partially invalid file remain unspecified. These issues relate to [[cash-settlement-exception-handling]] and [[cashflow-reinstatement-and-replay]].

## Required Contract Decisions

A production implementation requires an authoritative agreement for file identity, filename count validation, completion-file readiness, snapshot/base relationship, payment identity and versioning, duplicate detection, and recovery/unblocking workflow. Those gaps are tracked in [[what-is-the-authoritative-murex-batch-file-contract]] and [[what-are-the-idempotency-and-recovery-rules-for-murex-batch-republication]].
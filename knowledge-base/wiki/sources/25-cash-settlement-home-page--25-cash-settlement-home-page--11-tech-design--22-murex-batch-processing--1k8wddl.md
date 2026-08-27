---
type: source
title: Murex Batch Processing
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [murex, ratan, batch-processing, cashflow-ingestion, uk]
related: [murex, ratan, murex-batch-cashflow-ingestion, cash-settlement-exception-handling, what-is-the-authoritative-murex-batch-file-contract, what-are-the-idempotency-and-recovery-rules-for-murex-batch-republication, what-is-the-scope-of-murex-batch-processing-for-uk-and-de]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Murex batch processing.md"]
---
# Murex Batch Processing

## Summary

This incomplete high-level design records preliminary requirements for a proposed Murex-to-RATAN cashflow batch feed, referenced as *UK - Murex -> RATAN cashflow feeding*.

Murex is expected to send a snapshot file and a base file every two hours between `00:00:00` and `19:00:00`. Once uploading is complete, Murex creates a complete file. A base file may contain up to 45,000 records and is limited to cashflows with `SNTR` status.

The source distinguishes batch-level errors, which stop the current and subsequent files pending Murex republication, from record-level validation errors, which stop only the affected payment record.

## Stated Requirements

1. Murex sends batch files from `00:00:00` to `19:00:00`.
2. Every two hours, Murex sends two files: a snapshot file and a base file.
3. Murex creates a complete file after upload completion.
4. A base file may contain a maximum of 45,000 records.
5. A base file includes only `SNTR`-status cashflows.

## Exception Handling

| Exception | Exception code | Stated action |
| --- | --- | --- |
| Batch file format error | `BatchFileFormatError` | Stop processing the current file and any subsequent files; wait for Murex to republish the current file. |
| Cashflow count differs from the count encoded by the file-name convention | `BatchCountReconError` | Stop processing the current file and any subsequent files; wait for Murex to republish the current file. |
| Cashflow fields are invalid | `PaymentValidationError` | Stop processing the current record; wait for Murex to republish that payment only. |

## Design Status and Limitations

The detailed-design sections for real-time UK and DE processing, batch processing, Design A, and Design B contain no implementation details. This source is therefore not an approved interface or recovery contract.

In particular, it does not define file naming, delivery location, time zone, file format, snapshot/base precedence, completion-file semantics, file sequencing, blocked-feed scope, idempotency, or recovery ownership. It also does not define `SNTR` or establish whether 45,000 records is a producer constraint, a RATAN acceptance limit, or an estimate.

See [[murex-batch-cashflow-ingestion]] for the stated ingestion pattern and [[cash-settlement-exception-handling]] for the broader exception-handling context. The unresolved file contract and recovery semantics are tracked in [[what-is-the-authoritative-murex-batch-file-contract]] and [[what-are-the-idempotency-and-recovery-rules-for-murex-batch-republication]].
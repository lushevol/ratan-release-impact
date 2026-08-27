---
type: concept
title: eBBS Payment Accounting Integration
tags: [payment-accounting, ebbs, ratan, real-time-processing, json]
related: [ebbs, solace, ratan, accounting-posting-lifecycle, accounting-static-data-mappings, swift-generation-versus-ebbs-accounting-eligibility]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# eBBS Payment Accounting Integration

The eBBS payment-accounting integration is the intended capability for [[entities/ratan]] to generate balanced accounting postings and transmit them to [[entities/ebbs]] in real time through [[entities/solace]].

## Core model

Each new posting contains two legs:

- Nostro account.
- eBBS Bridge account.

When SCB pays, the Bridge is debited and Nostro is credited. When SCB receives, Nostro is debited and Bridge is credited. Reversals invert these directions.

## Eligibility

Accounting eligibility is driven by cashflow status and value-date timing rather than by SWIFT generation alone. `RELEASED`, `SETTLED`, `SWIFT_SUPPRESSED`, and `FAILED` can generate accounting under defined conditions. `CASHFLOW_SUPPRESSED`, `CANCELLED`, `DEAD`, and several pre-release or intermediary statuses suppress accounting.

A `SWIFT_SUPPRESSED` cashflow may require accounting even when no SWIFT message exists, provided Nostro data can be retrieved.

## Integration controls

The integration requires:

- A unique message ID.
- An external-system key based on cashflow ID and business versions.
- Currency, branch, account, transaction-code, value-date, and narrative mappings.
- Response handling for ACK, rejection, timeout, and technical errors.
- Retry and manual-resend operations.
- Dashboard visibility for `SENT`, `REJECTED`, and `MISSING_INFO`.

The requirement is incomplete as an API contract: retry semantics, status enumeration, raw-message retention, and authoritative narration mapping remain unresolved.
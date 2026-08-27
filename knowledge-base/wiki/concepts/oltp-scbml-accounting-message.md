---
type: concept
title: OLTP SCBML Accounting Message
tags: [oltp, scbml, accounting, messaging, kafka]
related: [oltp-accounting, ebbs, ebbs-vs-oltp-accounting-flow, what-is-the-authoritative-oltp-accounting-message-schema]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# OLTP SCBML Accounting Message

An OLTP SCBML Accounting Message is the Korea downstream request format generated from a settlement-accounting task and persisted in `extColumn2`.

The documented envelope includes `ns:SCBML`, `ns:header`, `payload`, `scbmlPayload`, `REQUESTMESSAGE`, `SYSTEMHEADER`, `TRANCOMMONHEADER`, and `TRANDATA`. Reversals modify the OLTP transaction data by flipping account and direction in `TRANDATA`.

The design distinguishes this contract from EBBS `request_info` JSON. It provides samples rather than a complete versioned schema: field ownership, canonical correlation key, BIC mapping, mandatory fields, timestamp precision, and normalization of whitespace-suffixed field names remain unspecified.
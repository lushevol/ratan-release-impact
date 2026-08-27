---
type: query
title: What Is the Authoritative OLTP Accounting Message Schema?
tags: [oltp, scbml, schema, accounting, open-question]
related: [oltp-scbml-accounting-message, oltp-accounting, cash-settlement-accounting-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# What Is the Authoritative OLTP Accounting Message Schema?

The design provides representative SCBML request, ACK, NACK, and EOD NACK examples, but it does not define a canonical schema or compatibility policy.

Open items include field mandatory status and types, constants versus environment configuration, BIC and Receiver BIC derivation, `TRAN_CD` and related transaction-code mappings, timestamp format and timezone, whitespace normalization for reference fields, versioning, and the correlation key between request and response.
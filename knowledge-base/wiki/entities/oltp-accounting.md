---
type: entity
title: OLTP Accounting
tags: [accounting, oltp, korea, downstream-system]
related: [korea-cashflow-migration, ebbs-vs-oltp-accounting-flow, oltp-scbml-accounting-message, oltp-ack-nack-processing, cash-settlement-accounting-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# OLTP Accounting

OLTP Accounting is the Korea-specific downstream settlement-accounting target introduced alongside the established [[ebbs]] flow.

The Cash Settlement Accounting Service publishes OLTP requests to `Cash_Settlement_OLTP_Accounting_KR` and receives responses through `Cash_Settlement_OLTP_Response`. Requests use an SCBML-wrapped JSON structure and are stored in `extColumn2` before publication.

OLTP tasks do not use the EBBS resend job. Normal ACK/NACK responses and end-of-day timeout responses have different documented envelope shapes.
---
type: concept
title: OLTP ACK/NACK Processing
tags: [oltp, acknowledgment, nack, response-processing, accounting]
related: [oltp-accounting, cash-settlement-accounting-service, eventual-consistency-for-cashflow-exceptions-and-swift-status, what-is-the-korea-oltp-retry-and-recovery-policy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# OLTP ACK/NACK Processing

OLTP ACK/NACK Processing receives messages from `Cash_Settlement_OLTP_Response`, persists the response, and updates the associated accounting-task status according to the existing EBBS-style lifecycle.

A normal response uses `YOACK`, `YOEERR`, and `YOEMSG` within `TRANDATA`; the documented success code is `TXN00000`. An EOD NACK has a separate exception envelope containing `ns:exceptions` and timeout text. Parsing and status mapping must account for these distinct shapes.
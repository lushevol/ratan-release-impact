---
type: concept
title: Accounting-File Delivery Acknowledgement
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, file-transfer, acknowledgement, retry]
related: [fileit, accounting-aspire-execution, accounting-feed-file-generation-idempotency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# Accounting-File Delivery Acknowledgement

The proposed flow separates file generation from delivery completion. Following FileIT submission, an execution record is intended to be marked `SENT`; a FileIT response then updates response information, with examples of `ACKED` / `SUCCESS` and `NACK` / `Invalid Request`.

The delivery contract remains incomplete. The design does not define whether acknowledgements are synchronous, how they correlate to execution records, timeout behavior, NACK remediation, or whether re-delivery reuses a filename or execution ID.
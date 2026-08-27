---
type: concept
title: Accounting-Feed File-Generation Idempotency
created: 2026-08-24
updated: 2026-08-24
tags: [idempotency, accounting, file-generation, batch-processing]
related: [accounting-aspire-execution, control-m, accounting-file-delivery-acknowledgement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# Accounting-Feed File-Generation Idempotency

The proposed design intends one accounting transaction file per country and workday job. A later scheduled run should skip work when the relevant filename already exists; the `cf1` example uses this behavior at 22:30.

The `cf5` example instead shows a failed generation remaining in `HOLD` and being regenerated on a later run. The source does not define the authoritative idempotency key, locking model, file-existence semantics, concurrency controls, or the distinction between successfully generated and successfully delivered files.
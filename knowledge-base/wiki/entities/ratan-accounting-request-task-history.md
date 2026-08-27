---
type: entity
title: ratan_accounting_request_task_history
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, accounting, history, reconciliation, oltp]
related: [query-recon-records, latest-sent-accounting-task-history-selection, korea-tlm-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# ratan_accounting_request_task_history

`ratan_accounting_request_task_history` is the OLTP history source specified for Korea accounting reconciliation retrieval. [[query-recon-records]] filters it by `created_at`, `booking_entity_fmid`, and `task_status = 'SENT'`.

For each `task_id`, the retrieval SQL selects the row with the highest `id` among eligible rows. Its `created_at` is exposed as the publication timestamp, and `request_info` supplies the EBBS payload.

The source calls for an index over “`booking_entity_id /created_at/country/task_status`,” although the supplied query filters `booking_entity_fmid`. The authoritative index definition is tracked in [[what-is-the-authoritative-index-for-ratan-accounting-request-task-history-recon-queries]].
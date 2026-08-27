---
type: concept
title: Latest SENT Accounting Task-History Selection
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, history, deduplication, sent-status, sql]
related: [ratan-accounting-request-task-history, query-recon-records, accounting-feed-file-generation-idempotency, korea-tlm-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# Latest SENT Accounting Task-History Selection

Latest SENT accounting task-history selection is the retrieval rule used by Korea `queryReconRecords`: within a release-time window and FMID scope, retain the highest-`id` `SENT` history entry for each `task_id`.

```sql
select distinct on (task_id) id , task_id, rarth.created_at , rarth.request_info from ratan_accounting_request_task_history rarth
where rarth.created_at >= '2026-04-04 01:50:00' and rarth.created_at < '2026-04-04 01:55:00' and booking_entity_fmid in ('10036645')
and task_status in ('SENT') order by task_id, id desc;
```

This is retrieval-level deduplication, distinct from [[accounting-feed-file-generation-idempotency]]. It does not prove that `id` is globally time-ordered, that history rows cannot be re-issued, or that a later non-`SENT` row should suppress an earlier `SENT` row. Those semantics require confirmation.
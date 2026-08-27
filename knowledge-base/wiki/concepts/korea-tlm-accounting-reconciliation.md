---
type: concept
title: Korea TLM Accounting Reconciliation
created: 2026-08-24
updated: 2026-08-24
tags: [korea, accounting, reconciliation, tlm, ebbs, release-time]
related: [tlm, query-recon-records, ratan-accounting-request-task-history, fmaa, latest-sent-accounting-task-history-selection, fmaa-authenticated-accounting-retrieval, value-date-accounting-feed-cutoff, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# Korea TLM Accounting Reconciliation

Korea TLM accounting reconciliation is the retrieval of published RATAN accounting messages by [[tlm]] through [[query-recon-records]]. The returned messages use the [[ebbs]] posting structure and are selected from accounting-task history rather than directly by cashflow payment date.

## Retrieval semantics

The reconciliation window is determined by history `created_at`:

- `created_at >= startReleaseTime`
- `created_at < endReleaseTime`
- requested interval no longer than 72 hours
- only `SENT` task-history records
- latest eligible row per `task_id`

Consequently, an accounting record is included according to its publication/release-time representation in task history, not its payload `value-date`. This is a specific implementation of the distinction documented in [[value-date-accounting-feed-cutoff]].

Consumers should use contiguous, non-overlapping intervals and maintain a durable reconciliation watermark. The source does not establish the canonical timezone or define how to recover records arriving late or being re-published.
---
type: query
title: What Is the Authoritative Index for ratan_accounting_request_task_history Recon Queries?
created: 2026-08-24
updated: 2026-08-24
tags: [database, index, performance, accounting, reconciliation]
related: [ratan-accounting-request-task-history, latest-sent-accounting-task-history-selection, query-recon-records]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# What Is the Authoritative Index for ratan_accounting_request_task_history Recon Queries?

The proposed index names `booking_entity_id`, `created_at`, `country`, and `task_status`, while the retrieval SQL filters `booking_entity_fmid`, `created_at`, and `task_status`, then groups by `task_id` and orders by descending `id`.

Confirm the actual column name, index order, inclusion of `task_id` and `id`, use of a partial `SENT` index, expected data volume, and target latency. The documented 20,286-record extraction does not include enough timing evidence to validate an index design.
---
type: entity
title: ratan_static_cashflow_currency_holiday
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, cashflow, holiday-calendar, reference-data]
related: [rdm, rdm-holiday-and-weekend-ingestion, holiday-data-composite-duplicate-key, holiday-calendar-event-model, ratan-static-rdm-holiday-weekend-message]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# ratan_static_cashflow_currency_holiday

`ratan_static_cashflow_currency_holiday` is the documented structured-data table for normalized RDM holiday and weekend records consumed by cashflow-related processing.

The source identifies `rdm_unique_key` as its duplicate-check field, composed of `center_id + event_date + event_name + file_type`. It does not provide DDL, a unique constraint definition, record-update semantics, or a lifecycle model for deactivated records.
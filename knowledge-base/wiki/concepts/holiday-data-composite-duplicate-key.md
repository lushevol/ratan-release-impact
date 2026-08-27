---
type: concept
title: Holiday Data Composite Duplicate Key
created: 2026-08-24
updated: 2026-08-24
tags: [data-integrity, deduplication, rdm, holiday-calendar]
related: [ratan-static-cashflow-currency-holiday, rdm-holiday-and-weekend-ingestion, holiday-calendar-event-model, what-is-the-ratan-holiday-data-update-and-deduplication-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# Holiday Data Composite Duplicate Key

The documented duplicate-check key for RDM holiday data is `rdm_unique_key`, composed as:

```text
center_id + event_date + event_name + file_type
```

This rule identifies records by center, date, event name, and file type. The source does not state whether the key is enforced by a database constraint or application logic.

Because the composition excludes fields such as `entityState`, `modifiedTime`, and `relatedFinancialCenter`, the behavior for an updated version of an existing holiday record is unresolved.
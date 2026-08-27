---
type: query
title: Which Lifecycle Tables Are Owned by ratan-cashflow-lifecycle-service?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, lifecycle, database, table-ownership, data-model]
related: [ratan-cashflow-lifecycle-service, ratan-cqrs-cashflow-read-model, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md"]
---
# Which Lifecycle Tables Are Owned by ratan-cashflow-lifecycle-service?

The persistence table in the technical design lists `lms_message` for `ratan-cashflow-lifecycle-service`, then presents a sequence of `ratan_cashflow_*`, Razor event-source, and CQRS event tables without a repeated service-name column.

## Open questions

- Do all following rows belong to `ratan-cashflow-lifecycle-service`?
- Is `lms_message` intentionally shared with `ratan-cash-settlement-lms-service`?
- Which service owns scheduler, Razor status, STELLA writeback, and CQRS event tables?
- Does the original rendered source resolve the apparent table-formatting error?

No table ownership should be inferred until the original source representation or database ownership records are verified.
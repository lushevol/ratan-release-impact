---
type: query
title: Can SENT CQRS Cashflow Events Be Compacted Without Losing Required History?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-lifecycle, cqrs, event-store, data-retention, compaction]
related: [ratan-cashflow-lifecycle-service, cash-settlement-database-retention-and-housekeeping, caroline-xinmiao-huang]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md"]
---
# Can SENT CQRS Cashflow Events Be Compacted Without Losing Required History?

The source identifies `ratan_cashflow_lifecycle_service.ratanone_cashflow_service__cqrs_cashflow_events` at 38,243 MB. It proposes two cleanup alternatives for records whose settlement date expired more than one year ago:

1. Clean up all qualifying events.
2. Retain only the latest event for each payment.

Both alternatives require `status = 'SENT'`. [[caroline-xinmiao-huang]] is listed as checker.

## Resolution needed

Establish the authoritative payment identity and definition of “latest” event. Assess whether either option preserves event replay, audit trail, reconciliation, operational debugging, and production recovery requirements.

The source does not select an option and does not demonstrate that compaction is safe.
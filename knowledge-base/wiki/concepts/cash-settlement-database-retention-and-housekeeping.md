---
type: concept
title: Cash Settlement Database Retention and Housekeeping
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, database, data-retention, housekeeping, archival, capacity-management]
related: [ratanone, what-is-the-approved-retention-policy-for-ratanone-workflow-history-tables, who-owns-retention-for-event-record-and-event-history, is-an-archive-required-for-expired-cashflow-query-data, can-sent-cqrs-cashflow-events-be-compacted-without-losing-required-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md"]
---
# Cash Settlement Database Retention and Housekeeping

Cash Settlement database retention and housekeeping is the controlled removal, truncation, preservation, or archival of persisted operational data to manage storage while retaining required auditability, recovery capability, troubleshooting evidence, reconciliation support, and historical-query access.

The source records table-specific proposals rather than an approved common policy. A checker listed beside a table is not necessarily the accountable decision-maker or implementation owner.

## Required controls

A retention decision should establish:

- a schema-qualified table identity, rather than relying on table name alone;
- accountable owner and approval authority;
- eligibility criteria, retention window, and exclusions;
- archival and retrieval requirements;
- backup, recovery, audit, and legal/compliance constraints;
- scheduled execution, monitoring, error handling, and rollback procedures.

## Source-specific distinctions

The document proposes monthly truncation for selected `ratanone.act_hi_*` workflow-history tables, one-month troubleshooting retention for group-management message tables, and a 90-day `created_at` cleanup for `cash_settlement_lms_service.lms_raw_message`.

These rules cannot be generalized. In particular, `ratanone.lms_raw_message` is marked BAU-related despite sharing its table name with the LMS-service table. Query-data archival and CQRS event compaction remain open decisions.

Related operational entities include [[ratan-cashflow-message-io]], [[cashflow-group-management-service]], [[ratan-cashflow-lifecycle-service]], [[lms]], and [[ratanone-rule-service]].
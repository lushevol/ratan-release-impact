---
type: query
title: What Are the Authoritative RATAN Holiday Update and Deletion Semantics?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rdm, holiday-calendar, reconciliation, data-integrity]
related: [rdm, 51358-ratanone-static-data-service, rdm-api-pagination-and-reconciliation, rdm-api-based-holiday-compensation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# What Are the Authoritative RATAN Holiday Update and Deletion Semantics?

The source proposes comparing currency holidays by RDM unique key and applying only inserts and deletes. It also states that RDM treats an unchanged primary key as an update. The design does not establish whether non-key changes can affect cash-settlement cutoff calculations.

## Questions to Resolve

- Which RDM fields are material to holiday and cutoff-date behavior?
- Can `entityState`, currency or MIC identifiers, country, day type, weekday, timestamps, or other attributes change without changing `(center_id, event_date, event_name, file_type)`?
- Must RATAN update an existing record when a material non-key field changes?
- What deletion signal is authoritative: missing snapshot record, `entityState: DELETED`, an explicit API filter, or another mechanism?
- How are updates and deletions made idempotent and auditable?

## Evidence

The existing real-time flow saves or updates `ACTIVE` records and deletes `DELETED` records. The API proposal instead states “just insert/delete no need to update ratan holiday.” These models require a single approved reconciliation contract before deployment.
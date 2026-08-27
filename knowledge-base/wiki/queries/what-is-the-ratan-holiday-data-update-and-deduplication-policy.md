---
type: query
title: What Is the RATAN Holiday Data Update and Deduplication Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, deduplication, data-integrity, holiday-calendar]
related: [holiday-data-composite-duplicate-key, ratan-static-cashflow-currency-holiday, rdm-holiday-and-weekend-ingestion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# What Is the RATAN Holiday Data Update and Deduplication Policy?

`rdm_unique_key` is documented as `center_id + event_date + event_name + file_type`, but the source does not define whether this rule is database-enforced or application-enforced.

The required policy is unknown when an existing record changes in fields excluded from the key, including `entityState`, `modifiedTime`, or financial-center attributes.

## Evidence needed

- Database DDL, indexes, and constraints.
- Upsert or rejection behavior for duplicate keys.
- Processing rules for `ACTIVE` and deactivated records.
- Audit and replay requirements.
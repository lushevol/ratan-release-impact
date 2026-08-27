---
type: concept
title: Schema Evolution for Cash Settlement
created: 2026-08-24
updated: 2026-08-24
tags: [database-migration, backward-compatibility, cash-settlement, ddl]
related: [ratan-inbound-message, ratan-cashflow-rounding-config, ratan-fxu-config]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# Schema Evolution for Cash Settlement

The supplied changes use additive and compatibility-oriented DDL patterns: `CREATE TABLE IF NOT EXISTS`, `ADD COLUMN IF NOT EXISTS`, a non-null column with a default value, nullable metadata additions, and relaxation of a historical payload's `NOT NULL` constraint.

The `raw_message_type text NOT NULL DEFAULT 'XML'` addition enables existing group-message rows to receive a default classification. Making historical `raw_message` nullable permits retained history rows without payload content. Nullable `meta_data` additions to accounting task tables avoid requiring immediate values for existing or new records.

These patterns describe physical migration compatibility only. The source does not provide migration sequencing, rollback procedures, backfill expectations, consumer compatibility rules, or operational deployment controls.
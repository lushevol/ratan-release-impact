---
type: concept
title: PostgreSQL TOAST Storage
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, toast, storage, jsonb, database-capacity]
related: [postgresql, cashflow-data-history, postgresql-jsonb-history-payload-slimming]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Query Service - cashflow_data_history purge.md"]
---
# PostgreSQL TOAST Storage

## Definition

TOAST is PostgreSQL's oversized-attribute storage mechanism. Large values such as `jsonb` payloads can be stored in an associated TOAST table instead of entirely in the ordinary heap.

## Evidence in `cashflow_data_history`

The source reports an 8,446 MB TOAST table for `cashflow_data_history`, compared with 234 MB across the separately inspected indexes. The one-million-row original-payload test had 4,530 MB of TOAST storage, while the slim-all-column replacement had only 8,192 bytes.

These measurements support the conclusion that the large historical Cashflow JSON object is the principal storage driver.

## Design implication

Reducing the retained JSON object is more effective than focusing only on secondary indexes. Replacement-table construction is attractive because it writes compact rows directly, avoiding the temporary bloat observed during mass updates.

The measurements are DEV results and do not establish production performance, compression behavior, or migration safety.
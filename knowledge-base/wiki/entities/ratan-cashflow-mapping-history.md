---
type: entity
title: ratan_cashflow_mapping_history
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cash-settlement, database, audit-history, cashflow-lineage, database-table, cashflow, non-economic-amendment]
related: [ratan-cashflow-mapping, original-replacement-cashflow-mapping, ratanone, cashflow-replacement-mapping, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---

# `ratan_cashflow_mapping_history`

`ratan_cashflow_mapping_history` is a proposed logical history table for [[ratan-cashflow-mapping]]. It records the original-to-replacement cashflow mapping, retaining the original and replacement cashflow identifiers and their version dimensions.

The Group Management Service – Non-Eco Amendment Technical Design describes `id` as the primary key of the history record and `mapping_id` as the primary key of the corresponding `ratan_cashflow_mapping` record. The other source describes `mapping_id` and `id` as integer identifiers, with sample values such as `1,2,3`.

The sources do not specify whether this table is an append-only audit log, when records are written, how revisions are identified, how it is synchronized with [[ratan-cashflow-mapping]], or what retention policy applies.

## Columns

| Column name | Data type | Description | Sample value in cashflow-event design | Sample value in Non-Eco Amendment design |
|---|---|---|---|---|
| `id` | `int` | History-record identifier; the Non-Eco Amendment design describes it as the primary key. | `1,2,3` | `1720275971888111616` |
| `mapping_id` | `int` | Identifier of the corresponding mapping record; the Non-Eco Amendment design describes it as the `ratan_cashflow_mapping` primary key. | `1,2,3` | `1720275970604654592` |
| `original_cashflow_id` | `text` | Original cashflow identifier. The Non-Eco Amendment design describes this as the cashflow ID of the New event. | `C01` | `200094700143` |
| `original_business_version` | `text` | Original cashflow business version. | `0` | `0` |
| `original_cashflow_version` | `text` | Original cashflow version. | `0` | `0` |
| `original_major_version` | `text` | Original cashflow major version. | `0` | `1` |
| `replaced_cashflow_id` | `text` | Replacement cashflow identifier. The Non-Eco Amendment design describes this as the cashflow ID of the New event on a non-economic amendment. | `C03` | `200094700145` |
| `replaced_business_version` | `text` | Replacement cashflow business version. | `1` | `1` |
| `replaced_cashflow_version` | `text` | Replacement cashflow version. | `1` | `1` |
| `replaced_major_version` | `text` | Replacement cashflow major version. | `1` | `2` |
| `ratan_status` | `text` | RATAN status. | `PROJECTED,NETTED,RELEASED,SETTLED,NOSTROMATCHED` | — |
| `upstream` | `text` | Upstream system or systems. | `STELLA/MUREX` | — |
| `upstream_status` | `text` | Upstream status. | `PROJECTED,NETTED,RELEASED,SETTLED,NOSTROMATCHED` | — |
| `status` | `text` | Mapping status. | `ACTIVE/OVERDUE` | — |
| `source_system` | — | Cashflow source system. This field is specified by the Non-Eco Amendment design separately from the `upstream` field described in the cashflow-event design. | — | `STELLA` |
| `created_at` | `timestamp` | Record creation timestamp. | — | — |
| `updated_at` | `timestamp` | Record update timestamp. | — | — |
| `version` | `int` | Record version. | `1` | — |

## Source-specific sample differences

The two designs provide different illustrative values for the same identifier and version fields:

- The cashflow-event design uses values such as `C01`, `C03`, and major versions `0` and `1`.
- The Non-Eco Amendment design uses numeric cashflow IDs such as `200094700143` and `200094700145`, and major versions `1` and `2`.
- These values are retained as source-specific examples rather than combined into a single canonical sample.

The cashflow-event design also specifies `ratan_status`, `upstream`, `upstream_status`, and `status`, while the Non-Eco Amendment design specifies `source_system`. The sources do not establish that `source_system` and `upstream` are the same field or should be treated as interchangeable.
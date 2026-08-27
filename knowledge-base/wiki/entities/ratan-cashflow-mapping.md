---
type: entity
title: ratan_cashflow_mapping
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cash-settlement, database, cashflow-lineage, mapping, database-table, cashflow, non-economic-amendment]
related: [ratanone, ratan-cashflow-mapping-history, original-replacement-cashflow-mapping, schema-evolution-for-cash-settlement, cashflow, non-economic-cashflow-amendment, cashflow-replacement-mapping, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---

# `ratan_cashflow_mapping`

`ratan_cashflow_mapping` is a proposed RATANONE logical persistence table for tracking lineage between an original cashflow and its replacement across business, cashflow, and major versions.

In the non-economic amendment scenario described by the Group Management Service design, the table relates an original `New` cashflow to the `New` cashflow introduced by the amendment. It captures each cashflow's ID, business version, cashflow version, major version, and source system. The broader cash-settlement design describes the table as supporting amendment processing, status tracking, and links between withdrawn cashflows and replacement cashflows.

## Columns

The following columns are identified across the source versions:

| Column |
|---|
| `id` |
| `original_cashflow_id` |
| `original_business_version` |
| `original_cashflow_version` |
| `original_major_version` |
| `replaced_cashflow_id` |
| `replaced_business_version` |
| `replaced_cashflow_version` |
| `replaced_major_version` |
| `source_system` |
| `ratan_status` |
| `upstream` |
| `upstream_status` |
| `status` |
| `created_at` |
| `updated_at` |
| `version` |

The broader cash-settlement design identifies the lineage and status-related columns, including `ratan_status`, `upstream`, `upstream_status`, and `status`. The non-economic amendment design additionally identifies `source_system`.

## Non-economic amendment mapping

The Group Management Service design provides the following descriptions and sample values:

| Column name | Column description | Sample value |
|---|---|---:|
| `id` | Primary key | `1720275970604654592` |
| `original_cashflow_id` | Cashflow ID of `New` event | `200094700143` |
| `original_business_version` | Cashflow business version of `New` event | `0` |
| `original_cashflow_version` | Cashflow version of `New` event | `0` |
| `original_major_version` | Cashflow major version of `New` event | `1` |
| `replaced_cashflow_id` | Cashflow ID of `New` event on non-economic amendment | `200094700145` |
| `replaced_business_version` | Cashflow business version of `New` event on non-economic amendment | `1` |
| `replaced_cashflow_version` | Cashflow version of `New` event on non-economic amendment | `1` |
| `replaced_major_version` | Cashflow major version of `New` event on non-economic amendment | `2` |
| `source_system` | Cashflow source system | `STELLA` |
| `created_at` | — | — |
| `updated_at` | — | — |
| `version` | — | — |

The naming of `replaced_cashflow_id` is potentially ambiguous. Its column description indicates the `New` cashflow produced by the non-economic amendment, while the business scenario describes the earlier cashflow as withdrawn and the later `New` cashflow as its replacement.

## Schema and implementation notes

- The Group Management Service design labels `id` as the primary key.
- That design provides no executable DDL, column types, unique constraints, indexes, foreign keys, or rules for chained mappings.
- The broader cash-settlement design does not specify primary keys, foreign keys, indexes, uniqueness constraints, or transaction semantics.
- Accordingly, the source materials establish the proposed logical mapping and its represented versions, but do not fully define the physical database schema or transaction behavior.
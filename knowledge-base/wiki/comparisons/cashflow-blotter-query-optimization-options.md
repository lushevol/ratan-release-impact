---
type: comparison
title: Cashflow Blotter Query Optimization Options
tags: [cash-settlement, cashflow-blotter, query-performance, PostgreSQL, architecture]
related: [cashflow-blotter, postgresql, pg-hint-plan, value-date-query-performance-guardrail, cash-settlement-cashflow-read-model, domain-owned-postgresql-schemas]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Query Performance Optimization.md"]
---
# Cashflow Blotter Query Optimization Options

The source identifies two optimization paths for Cashflow Blotter searches: narrowing application criteria with value date and influencing PostgreSQL query planning with `pg_hint_plan`. Other database and data-model options are relevant for evaluation but are not proposed or assessed in the source.

## Option Comparison

| Option | Mechanism | Benefits | Risks or open issues | Source status |
| --- | --- | --- | --- | --- |
| Value-date predicate defaulting | Add `VD = Today` to non-identifier searches and limit user-selected VD ranges | Reduces the searched date range and can reduce database work | Changes result semantics; may exclude legitimate historical records; exact threshold and timezone are undefined | Primary proposal |
| Database indexes and query rewrites | Align indexes and SQL structure with common combinations such as VD, Taxonomy, and Booking Entity | May improve execution without changing returned results | Requires query-plan and workload analysis; source provides no index inventory or benchmark | Not evaluated |
| `pg_hint_plan` | Apply explicit hints to influence PostgreSQL query planning | May address poor planner choices for known query shapes | Extension compatibility, brittleness, maintenance, and operational support require assessment | Proposal B, exploratory |
| Read model or materialized view | Serve blotter searches from a purpose-built read-optimized representation | Can isolate user-query workloads from transactional tables | Freshness, storage, synchronization, and reconciliation requirements must be defined | Not evaluated |
| Partitioning or archival strategy | Separate current and historical data to reduce scans | May improve current-data query performance and manage historical data growth | Partition-key design and historical-search behavior require analysis | Not evaluated |

## Recommended Evaluation Sequence

1. Measure baseline latency, query plans, row counts, database load, timeout rates, and result distributions.
2. Test the value-date predicate without silently treating the one-month threshold as proven.
3. Analyze indexes and query rewrites before introducing planner hints.
4. Evaluate `pg_hint_plan` for version compatibility and operational maintainability.
5. Consider a dedicated read model or partitioning if the workload and data volume justify it.
6. Validate that performance changes do not violate historical-search, reconciliation, audit, or operational requirements.

The value-date approach and database-level approaches are not mutually exclusive, but combining them should be tested as a distinct configuration.
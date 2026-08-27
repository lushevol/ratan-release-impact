---
type: concept
title: Denormalized Cashflow Query Read Model
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, read-model, denormalization, database-design, query-service]
related: [cash-settlement-cashflow-read-model, domain-owned-postgresql-schemas, cashflow-data, cashflow-data-history, query-service, trade-standing-settlement-instructions, cashflow-standing-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design.md"]
---
# Denormalized Cashflow Query Read Model

A denormalized cashflow query read model flattens attributes from multiple settlement domains into a query-oriented relational record. The Cash Settlement Query Service design applies this pattern through `cashflow_data` and `cashflow_data_history`.

## Structure

The tables group fields by source or business domain:

- `cashflow__`: cashflow identity, state, payment, validation, netting, lifecycle, and workflow data.
- `trade__`: trade identity, state, event, version, lifecycle, and settlement data.
- `entity__`: booking entity, counterparty, general-ledger, and personnel data.
- `portfolio__`: portfolio identifiers and names.
- `instrument_common__`: instrument classifications.
- `ssi__`: settlement instructions, account details, routing, remittance, and SWIFT data.
- `data_flow__`: publication, source-system, sender, domain, type, and message provenance.

This layout favors straightforward filtering and projection without requiring joins across the contributing domains.

## Trade-offs

The design can simplify read queries, but it also creates several operational concerns:

- Repeated values increase storage and update complexity.
- Wide records make schema evolution and migration more expensive.
- The absence of secondary indexes in the supplied DDL does not provide workload-specific query support.
- Multiple identity and version fields require a canonical key contract.
- Nullable text fields with empty-string defaults require explicit missing-value semantics.
- Materialized values can become stale unless ingestion and correction behavior are defined.
- Embedded SSI and payment-routing data requires strict access, masking, audit, and retention controls.

The source does not provide query plans, workload volumes, latency targets, or index benchmarks. Later performance evidence should therefore be kept separate from this design baseline.

## Current and historical variants

`cashflow_data` appears to represent current query state, while `cashflow_data_history` appears to represent prior records. That interpretation is based on naming and table shape only; it is not a confirmed lifecycle contract.

The design must define how records are inserted, updated, superseded, replayed, corrected, and retained. See [[what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]].
---
type: source
title: Split Design - Delete
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [deprecated, cashflow, split, database-migration, incomplete]
related: [cashflow-split-and-unsplit, cashflow-splitting-id-correlation, what-is-the-authoritative-meaning-and-lifecycle-of-cashflow-splitting-id, what-is-the-authoritative-post-split-withdrawal-amendment-and-netting-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Split design -delete.md"]
---
# Split Design - Delete

This deprecated and incomplete functional-requirement document contains a database schema change for split-related cashflow identity, followed by empty headings for split, unsplit, and withdrawal processes.

## Preserved technical artefact

```sql
ALTER TABLE cash_netting_service.t_cashflow ADD COLUMN IF NOT EXISTS cashflow__splitting_id text NOT NULL DEFAULT '';
CREATE UNIQUE INDEX t_cashflow__splitting_id_idx ON cash_netting_service.t_cashflow (cashflow__cashflow_id,cashflow__splitting_id);
```

## Evidenced data constraint

The migration adds mandatory `cashflow__splitting_id` text to `cash_netting_service.t_cashflow`, with `''` as its default. The composite unique index `t_cashflow__splitting_id_idx` permits one row for each `(cashflow__cashflow_id, cashflow__splitting_id)` pair.

Consequently, a cashflow ID can occur in multiple rows only where the splitting IDs differ. If `''` denotes an unsplit representation, no more than one default representation can exist for a given cashflow ID.

The source does not define the business meaning of `cashflow__splitting_id`, how it is populated or cleared, or whether the schema migration was deployed. The column-addition statement is idempotent, but the index-creation statement has no `IF NOT EXISTS` clause and may fail when rerun after the index already exists.

## Missing process definition

The source includes the headings “Split process detail,” “Unsplit process Detail,” and “Withdraw,” but supplies no content beneath them. It establishes no split lifecycle, unsplit behavior, withdrawal semantics, event ordering, API, status transition, or netting rule.

Use this page only as historical evidence of a proposed persistence constraint. It is not authoritative for [[cashflow-split-and-unsplit]] behavior or post-split withdrawal, amendment, and netting processing.
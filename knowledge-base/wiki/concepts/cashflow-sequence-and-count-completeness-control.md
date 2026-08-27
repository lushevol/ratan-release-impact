---
type: concept
title: Cashflow Sequence and Count Completeness Control
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, sequence, count, completeness, exception-control]
related: [uber-message, cashflow-batch-control, cashflow-event-control, cashflow-lineage-and-operational-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Cashflow Sequence and Count Completeness Control

## Definition

`Sequence` and `Count` are proposed control fields for determining whether the expected set of cashflow publications has been received.

In the source examples, `Sequence` identifies a row's position and `Count` identifies the expected number of rows. An exception may be attached to a particular row, including the final row.

## Limitations

The examples do not define whether rows are separate Uber messages, records within one message, or members of a broader event batch. They also do not define ordering guarantees, batch identity, timeout behavior, replay, idempotency, or recovery.

The non-economic amendment example uses an initial `Count` of 2 and a later `Count` of 4 across six displayed rows, which may represent separate publication sets but is not explained.

This proposal extends, but does not replace, [[cashflow-batch-control]] and [[cashflow-event-control]].
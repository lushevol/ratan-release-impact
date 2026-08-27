---
type: query
title: What Is the Canonical NSTP Exception Storage Model?
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, exceptions, data-model, cashflow, read-model]
related: [nstp-exception-filter, cashflow-exception-read-model-enrichment, exception-platform-service, nstp, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# What Is the Canonical NSTP Exception Storage Model?

The proposed schema adds one `nstp_exception` field to `cashflow_data` and `cashflow_data_history`, while the proposed exception lookup returns all exception codes ordered by `exception_time`.

## Questions to resolve

- Does the projection store one active exception, all exceptions, or an ordered historical collection?
- Does it store a stable machine code, a display label, or both?
- If multiple exceptions apply, what selection, serialization, delimiter, and ordering rules apply?
- How are resolved, removed, and repeated exceptions represented?
- Is the field name `nstp_exception` or `cashflow__nstp_reason`?
- What column type, length, nullability, index, and migration rules are required?
- Is the data model shared with the exception domain described in [[hot-nstp-rule-exception-reconciliation]]?

A decision is needed before schema migration, historical backfill, GraphQL filtering, or UI reliance on the field.
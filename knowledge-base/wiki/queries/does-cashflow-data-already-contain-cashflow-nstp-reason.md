---
type: query
title: Does cashflow_data Already Contain cashflow__nstp_reason?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-data, nstp, schema, data-model, migration]
related: [cashflow-exception-read-model-enrichment, nstp-exception-filter, cashflow-data, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Does cashflow_data Already Contain cashflow__nstp_reason?

The source asks whether `cashflow_data` already contains a column named `cashflow__nstp_reason`, while separately proposing a new `nstp_exception` field in `cashflow_data` and `cashflow_data_history`.

## Required verification

Inspect the authoritative schemas and deployed migrations for:

- Existence and type of `cashflow__nstp_reason`.
- Whether it has current production data.
- Its source, update lifecycle, and business meaning.
- Its relationship to NSTP exception codes and labels.
- Whether it is available in `cashflow_data_history`.
- Whether it can meet the proposed Cashflow Blotter filter requirement.

The result determines whether a new field is necessary or whether a compatibility and migration plan is required.
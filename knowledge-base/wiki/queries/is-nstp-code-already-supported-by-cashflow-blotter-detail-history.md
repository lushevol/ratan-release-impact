---
type: query
title: Is NSTP Code Already Supported by Cashflow Blotter Detail History?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-blotter, detail-history, nstp, ui, audit]
related: [nstp-exception-filter, cashflow-exception-read-model-enrichment, cash-settlement-cashflow-read-model, nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Is NSTP Code Already Supported by Cashflow Blotter Detail History?

The source asks whether the Cashflow Blotter Detail History page already contains an `NSTP Code` field.

## Required verification

- Confirm whether an `NSTP Code` field exists in the current Detail History UI and GraphQL response.
- Identify the current data source and field mapping.
- Determine whether its value represents the same exception domain proposed for `nstp_exception`.
- Compare its semantics with exception-platform `exception_code`, `label`, and `value`.
- Confirm whether historical rows can consistently display the field after the proposed read-model enrichment.
- Identify any migration, backfill, or compatibility requirements.

A confirmed answer is necessary before adding a duplicate field or treating existing detail-history data as equivalent to the proposed NSTP exception filter model.
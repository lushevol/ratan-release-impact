---
type: concept
title: Dormant SSI Processing
created: 2026-08-24
updated: 2026-08-24
tags: [ssi, dormancy, lifecycle-management, cash-settlement, data-aggregation]
related: [ssi-plus, ratanone-stamping-service, bcs, cash-settlement-query-cn-cashflow-data, does-created-at-filtering-correctly-implement-the-ssi-last-used-date-window, what-stamping-states-count-as-ssi-use-for-dormancy, what-is-the-authoritative-ssi-plus-inactivation-and-reactivation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md"]
---
# Dormant SSI Processing

Dormant SSI processing is the process of establishing an SSI's latest observed use date across cashflow flows and using that evidence to support inactivation of SSIs unused for 24 months.

## Intended operating model

The design has two distinct components:

1. **Daily incremental collection**: obtain cashflow-ID and SSI-ID pairs for a particular payment date through the BCS SSI endpoint, alongside the existing FMRP path.
2. **Historical aggregation**: calculate the maximum payment date per SSI from current query data, backup snapshots, and BCS stamping data.

The daily feed supports ongoing last-used-date maintenance. The historical report is a point-in-time reconstruction and uses hard-coded dates from `2024-07-18` through `2026-07-18`.

## Evidence rules in the current design

For BCS data, the process:

- Joins `cashflow_stamping` with `stamped_vostro_account`.
- Excludes only empty-string SSI identifiers.
- Uses `payment_date` as the observed use date.
- Counts only `STP_STAMPING_SHIPPED` stamping records.

For query-model data, the report selects the maximum `cashflow__payment_date` but limits included rows by `created_at`. This distinction can materially alter a result intended to represent a payment-date-based 24-month inactivity rule. See [[does-created-at-filtering-correctly-implement-the-ssi-last-used-date-window]].

## Required lifecycle safeguards

A safe implementation requires an authoritative definition of:

- The business-effective date that determines SSI use.
- SSI identifier normalization across BCS and FMRP data.
- The authoritative 24-month cutoff and processing schedule.
- Deactivation idempotency and auditability.
- Reconciliation between source data and SSI+ status.
- Reactivation when a previously inactive SSI is used again.

The current design does not establish these controls. They are tracked in [[what-is-the-authoritative-ssi-plus-inactivation-and-reactivation-contract]].
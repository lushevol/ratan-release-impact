---
type: concept
title: RDM API Pagination and Reconciliation
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, api, pagination, reconciliation, idempotency, static-data]
related: [rdm, 51358-ratanone-static-data-service, rdm-api-based-holiday-compensation, static-data-synchronization, request-id-based-sync-correlation, per-destination-sync-status-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# RDM API Pagination and Reconciliation

RDM API Pagination and Reconciliation is the control pattern needed to safely maintain RATAN static data from scheduled, paginated RDM responses.

The source proposes calculating total pages from `totalRecords` and `pageSize`, but the implementation must treat incomplete pagination, duplicate rows, empty successful responses, and failed pages as incomplete runs rather than valid snapshots.

## Source-Specific Rules

```text
Integer totalPageNo = (totalRecords+ pageSize-1) / pageSize;
Boolean fetchNextPage = dataQuery.getPage()<= totalPageNo;
```

- Currency-holiday API retrieval starts at page `1`.
- Country-code API retrieval starts at page `0`.
- Country-code API default page size is recorded as `100`.
- The documented date window is `>= dateFrom` and `< dateTo`.

## Reconciliation Requirements

A safe run should:

1. Record a run identifier and requested source window before fetching data.
2. Validate HTTP status, response body, schema, pagination metadata, and date conversion.
3. Complete all expected pages before applying destructive changes.
4. Deduplicate source records by an explicit source identity.
5. Compare local and source state using documented keys and material attributes.
6. Apply changes atomically where feasible, or retain checkpoints and compensating recovery data.
7. Record inserts, updates, deletes, rejected rows, and reconciliation counts.
8. Alert and require controlled handling when differences exceed an approved threshold.

The source describes `ratan_static_cashflow_currency_holiday` identity as:

```text
(center_id, event_date, event_name, file_type)
```

That key supports identity comparison but does not alone establish whether fields outside the key are safe to ignore. This remains an open question in [[what-are-the-authoritative-ratan-holiday-update-and-deletion-semantics]].

The existing file-based policies differ: holiday reconciliation is recorded as `recon-result-sync-to-db: false` with a greater-than-20-difference protection, whereas country reconciliation is recorded as `recon-country-result-sync-to-db: true`. The API design needs an explicit replacement policy.
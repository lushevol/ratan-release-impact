---
type: entity
title: 51358-ratanone-static-data-service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-data, holiday-calendar, country-code, api]
related: [rdm, rdm-api-based-holiday-compensation, rdm-api-pagination-and-reconciliation, ratan-cashflow-group-management-service, static-data-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# 51358-ratanone-static-data-service

`51358-ratanone-static-data-service` stores and serves static data used by Cash Settlement, including currency-holiday and country-code mappings.

In the Indonesia compensation design, it is the local target for scheduled RDM API retrieval. It must maintain the static data required by downstream cutoff-date and SSI-stamping flows without relying on mounted NAS storage.

## Documented Data and Endpoints

| Data | Persistence | Consumer interface |
| --- | --- | --- |
| Currency holidays | `ratan_static_cashflow_currency_holiday` | `POST /v1/staticData/cashflow/shifterDate`; `POST /v1/staticData/cashflow/cutoffs` |
| Country mappings | `ratan_static_cashflow_country_mapping` | `GET /v1/cashflow/country/countryName` |
| Legacy RDM file history | `ratan_static_brdm_history` | File-processing support |
| Legacy bank-code records | `ratan_static_brdm_record` | LEI and bank-code support |

The proposed scheduler-facing reconciliation endpoints are:

```text
/v1/static/data/recon/currencyHoliday
/v1/static/data/recon/specialHoliday
/v1/static/data/recon/countryCode
```

They require the internal action:

```text
RATAN_INTERNAL_FUNC:STATIC_SERVICE:FETCHANDUPDATE
```

## Reconciliation Responsibilities

The service is expected to retrieve all pages, normalize RDM date formats, reconcile RDM records with local persistence, retain an auditable run outcome, and prevent partial or unsafe state changes. The current proposal's insert/delete-only treatment of holidays is not yet proven safe for non-key field changes; see [[what-are-the-authoritative-ratan-holiday-update-and-deletion-semantics]].

The source names `51358-ratan-cash-settlement-group-management-service` as the cutoff-date consumer. Its relationship to existing [[ratan-cashflow-group-management-service]] requires confirmation.
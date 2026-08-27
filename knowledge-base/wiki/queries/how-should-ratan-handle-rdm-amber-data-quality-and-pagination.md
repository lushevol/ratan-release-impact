---
type: query
title: How Should Ratan Handle RDM Amber Data Quality and Pagination?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rdm, data-quality, pagination, compensation, reference-data]
related: [rdm, rdm-reference-data-integration-via-kong, what-is-the-production-readiness-plan-for-ratan-rdm-kong-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation/RDM Integration via Kong Gateway.md"]
---
# How Should Ratan Handle RDM Amber Data Quality and Pagination?

## Open question

What processing, control, and reconciliation policy should Ratanone apply when RDM returns Amber data quality and a large paginated holiday-calendar result?

## Known evidence

The documented currency-holiday response contains:

```text
"dataQuality": "Amber",
"dqRemarks": "",
"totalRecords": "541550",
"pageNo": "1",
"pageSize": "2000"
```

The source supplies no definition of Amber, no acceptance threshold, and no required compensation-processing action. It also does not define pagination parameters, maximum request volume, rate limits, timeout behavior, retries, cache duration, completeness validation, or reconciliation requirements.

## Decisions needed

- Define the meaning and permitted usage of `dataQuality: "Amber"` for each compensation use case.
- Determine whether an Amber result blocks processing, permits processing with an alert, or requires manual approval.
- Confirm the authoritative pagination request contract and expected page-completeness controls.
- Define retry, backoff, timeout, and idempotency behavior.
- Define a cache and refresh strategy for holiday and country reference data.
- Identify the compensation functions that consume each RDM endpoint and their fallback behavior when data is unavailable or incomplete.
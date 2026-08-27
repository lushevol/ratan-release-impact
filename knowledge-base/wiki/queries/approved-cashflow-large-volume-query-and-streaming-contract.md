---
type: query
title: What Is the Approved Cashflow Large-Volume Query and Streaming Contract?
tags: [cashflow, query, streaming, API-contract, open-question]
related: [cashflow-data-api-streaming, cashflow-large-volume-transfer-options, cashflow-data-report, query-service, cashflow-data, paginated-cashflow-batch-processing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume.md"]
---
# What Is the Approved Cashflow Large-Volume Query and Streaming Contract?

The source prefers HTTP streaming through Spring WebMvc `StreamingResponseBody`, but does not establish the complete production contract.

## Questions to Resolve

- What are the exact DQSL and SSDR request and response responsibilities?
- What concurrency, maximum result size, and request-duration targets apply?
- Should slices be defined by day, stable key range, or record count?
- What ordering and pagination key guarantees deterministic results?
- Can multiple slices share one database snapshot or report version?
- What freshness requirements apply to `cashflow_data_report`?
- What are the timeout and buffering behaviors of the client, gateway, proxy, servlet container, and database driver?
- How are cancellation, retries, duplicate requests, authorization, and partial results handled?
- Is the API intended for interactive requests, scheduled jobs, or both?

## Current Evidence

Solution D has a strong rationale for reducing peak application memory and avoiding intentional temporary files. Its performance trade-off is additional PostgreSQL calls. The source does not provide sufficient evidence to approve a specific slice size, consistency model, timeout policy, or protocol.
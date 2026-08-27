---
type: query
title: What Is the Validated and Rollback-Safe Country Data Reload Procedure?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, static-data, country-data, rollback, operational-risk]
related: [country-reference-data-reload, static-data-service, ratan-static-cashflow-country-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md"]
---
# What Is the Validated and Rollback-Safe Country Data Reload Procedure?

The source specifies deletion of all `ratan_static_cashflow_country_mapping` records before upload, but does not provide controls needed to operate that process safely.

## Questions to resolve

- What validation must succeed before `cleanDB` can be called?
- Is a backup or export mandatory, and how is it restored?
- Is replacement atomic, or can consumers observe empty or partially loaded data?
- What approval, authentication, authorization, audit, and environment guardrails govern this operation?
- What validation occurs after upload, including row-count, duplicate, malformed-record, and completeness checks?
- What is the rollback procedure if upload fails after deletion?

Until these controls are established, the documented process in [[country-reference-data-reload]] should be treated as an incomplete operational procedure rather than a production-safe runbook.
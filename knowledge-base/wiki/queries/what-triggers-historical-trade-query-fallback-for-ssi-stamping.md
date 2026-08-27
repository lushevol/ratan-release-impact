---
type: query
title: What Triggers Historical Trade Query Fallback for SSI Stamping?
tags: [ssi-stamping, historical-query, fallback, trade-data, graphql]
related: [historical-trade-query-fallback, graphql-trade-snapshot-retrieval, ratan-ssi-stamping, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--25-ssi-stamping-notifica--1um4ze4]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade Strategic SSI Stamping Tech Design.md"]
---
# What Triggers Historical Trade Query Fallback for SSI Stamping?

What condition causes SSI stamping to use the historical trade query rather than the field-projected GraphQL query, and what are the resulting data and versioning semantics?

## Known evidence

The design states only that the historical fallback queries all trade fields, whereas the normal GraphQL path populates only requested fields.

## Questions to resolve

- What specific GraphQL result, error, data-quality condition, or user action triggers fallback?
- Which system and interface execute the historical query?
- Does the fallback select the same trade major and minor version as the normal path?
- Is the historical schema equivalent to GraphQL for fields consumed by SSI stamping?
- How are no-result, multiple-result, timeout, and retry cases handled?
- Are non-IRS products or absent nested fields a fallback condition?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--25-ssi-stamping-notifica--1um4ze4]] defines the broader all-field fallback payload but leaves its operation unspecified.
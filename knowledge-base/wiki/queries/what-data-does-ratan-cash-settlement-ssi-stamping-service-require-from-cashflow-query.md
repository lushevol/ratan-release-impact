---
type: query
title: What Data Does RATAN Cash Settlement SSI Stamping Service Require from Cashflow Query?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, ssi, api-contract, dependency]
related: [ratan-cashflow-lifecycle-service, cashflow-query-api-performance-optimization, ssi-driven-swift-field-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Cashflow query api optimization.md"]
---
# What Data Does RATAN Cash Settlement SSI Stamping Service Require from Cashflow Query?

## Question

What request pattern and response fields does `ratan-cash-settlement-ssi-stamping-service` require from `/v1/ratan/cashflow/query`?

## Known evidence

The SSI-stamping service is listed as a caller of the cashflow query API. The source provides neither its request pattern nor the fields, tables, lifecycle states, or error-handling behavior it consumes.

## Why it matters

Category-based fetching cannot safely optimize this caller until its dependency is documented. Missing SSI-related fields could affect downstream settlement instruction processing and related [[ssi-driven-swift-field-generation]] behavior.

## Evidence needed

- Client implementation and request payloads.
- Response DTO fields accessed by the service.
- Required data categories and table sources.
- Volume profile, including single versus batch requests.
- Nullability, retry, timeout, and fallback behavior.
- Regression tests demonstrating compatibility with the optimized endpoint.
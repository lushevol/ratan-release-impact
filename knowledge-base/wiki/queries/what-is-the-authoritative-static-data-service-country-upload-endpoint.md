---
type: query
title: What Is the Authoritative Static Data Service Country Upload Endpoint?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, static-data, api, endpoint, documentation]
related: [static-data-service, country-reference-data-reload, ratan-static-cashflow-country-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md"]
---
# What Is the Authoritative Static Data Service Country Upload Endpoint?

The source contains conflicting upload endpoint documentation.

- The upload API table labels the intended endpoint as `http://{static service domain name}/v1/cashflow/country/upload`, but its Markdown hyperlink targets `http://localhost:8989/v1/cashflow/country/cleanDB`.
- The provided cURL command posts to `http://localhost:8989/v1/cashflow/country/upload`.

The cURL command suggests that `POST /v1/cashflow/country/upload` is correct, but this must be verified against the deployed Static Data Service API contract. Verification should also establish the request content type, response structure, authentication requirements, size limit, validation behavior, and supported environments.
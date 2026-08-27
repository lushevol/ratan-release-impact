---
type: query
title: What Is the Approved RDM API Contract for Indonesia Holiday Compensation?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, api-contract, indonesia, holiday-calendar, kong]
related: [rdm, 51358-ratanone-static-data-service, rdm-api-based-holiday-compensation, rdm-api-pagination-and-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# What Is the Approved RDM API Contract for Indonesia Holiday Compensation?

The recorded development, staging, and production URLs are not implementation-ready. Staging links mix visible v2 routes with v1 targets, the special-holiday staging link targets the currency-holiday route, and the country-code staging row mixes gateway and development addresses. A recorded staging wrapper route returned HTTP `200` with a null body.

## Questions to Resolve

- What are the authoritative base URLs, routes, API versions, request parameters, and TLS requirements for each environment?
- What response schemas and pagination fields apply to currency holidays, special holidays, and countries?
- Can the APIs return both active and deleted records sufficiently to maintain RATAN state?
- What must the client do for HTTP success with an empty body, malformed payloads, timeouts, and partial pages?
- Which team owns contract testing and production route validation?

## Evidence

The selected approach is direct scheduled RDM API retrieval through development access or [[kong]] gateway endpoints. The source contains inconsistent endpoint representations and no validated response contract.
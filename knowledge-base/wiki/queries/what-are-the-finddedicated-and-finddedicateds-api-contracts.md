---
type: query
title: What Are the findDedicated and findDedicateds API Contracts?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, api, static-data, ssi, group-management, open-question]
related: [rfi-nostro-stamping-based-on-portfolio, ratanone-static-data-service, dedicated-nostro-selection, ssi-plus]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# What Are the findDedicated and findDedicateds API Contracts?

The requirement names two static-data APIs without supplying their endpoint or message contracts:

- `findDedicated` is provided to `ssi-serivce` to change Nostro query logic.
- `findDedicateds` is provided to `group-serivce` to identify whether `nostroId` changed.

## Information required

- Service ownership and whether `ssi-serivce` is [[ssi-plus]] or a different service.
- Protocol, URI, HTTP method, authentication, and authorization.
- Request fields, especially portfolio and trade-compatibility data.
- Response schema, including candidate ordering and identifiers.
- Error, zero-result, and multiple-result behavior.
- Pagination and effective-date semantics.
- The precise distinction between singular `findDedicated` and plural `findDedicateds`.

Until specified, these names are requirements, not implementable interface contracts.
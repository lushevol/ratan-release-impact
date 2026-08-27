---
type: query
title: What Is the Authoritative RATAN-TIS API Contract?
tags: [ratan, tis, ratanone, rest-api, interface-contract, ola]
related: [tis, ratanone, tis-cashflow-eligibility-rules, withdrawal-cashflow-query-exclusion, 5-ratan--17-ratan-interfaces--13-ratan-and-tis--1t8tke0]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# What Is the Authoritative RATAN-TIS API Contract?

The available source is unreviewed and gives only the high-level flow `TIS <> RESTFUL API <> RATANONE`. It references `OLA_RATAN_API_TIS_v1.0.docx`, but the attachment contents are not available.

## Information required

Confirm the authoritative contract for the TIS interface, including:

- the RATANONE component that exposes or intermediates the API, and its relationship to RATAN;
- API version, environments, base URLs, resources, and request/response schemas;
- authentication, authorization, data-entitlement, and audit requirements;
- query parameters and the exact selection implementation for status, `STTL_MEANS`, reversal events, and FMID;
- the authoritative data sources and field definitions;
- polling, eventing, refresh frequency, pagination, and rate limits;
- error codes, retry behavior, reconciliation, and recovery procedures;
- service ownership, support contacts, SLAs, and approval status.

The documented TIS business scope is preserved in [[tis-cashflow-eligibility-rules]], but it is insufficient to implement or validate an API integration.
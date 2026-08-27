---
type: query
title: What Is the Authoritative Versioned Logical-Field-to-XPath Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, rule-service, xpath, versioning, api-contract]
related: [rule-service, ratanone-foundation, centralized-cashflow-field-mapping-governance, dynamic-cashflow-query-field-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md"]
---
# What Is the Authoritative Versioned Logical-Field-to-XPath Contract?

The technical design proposes [[rule-service]] as the central provider of logical-model-to-XPath mappings by version and context, but it does not define the contract needed by UI, SDK, and Query Service consumers.

## Questions to resolve

- What API endpoint, request structure, response schema, and error semantics apply?
- What do `RATAN_DATA` and `CASHFLOW_DATA` mean operationally?
- Who owns and approves mapping versions?
- Are consumers pinned to a version, automatically upgraded to the latest version, or request-version controlled?
- What compatibility and deprecation guarantees apply?
- During disagreement, cache staleness, or Rule service outage, does the local mapping file or Rule service response take precedence?
- How are version-upgrade events ordered, retried, authenticated, and reconciled?

This must be resolved before centralized governance can be considered an operational contract.
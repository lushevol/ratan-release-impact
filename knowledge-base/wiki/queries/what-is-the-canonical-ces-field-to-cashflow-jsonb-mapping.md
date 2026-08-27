---
type: query
title: What Is the Canonical CES Field-to-cashflow JSONB Mapping?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, data-entitlement, jsonb, field-mapping, data-governance]
related: [ces, query-service, ssdr, cash-settlement-data-entitlement, ces-data-entitlement-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
---
# What Is the Canonical CES Field-to-cashflow JSONB Mapping?

The CES design uses `Entity.Counterparty_Country_ISO_Code` in entitlement examples but generates an SQL predicate for `Entity.Counterparty_SCI_DOMICILE_COUNTRY`. Its assumptions list only `Entity.Booking_Entity_SCI_FMID` and `Entity.Counterparty_SCI_DOMICILE_COUNTRY` as supported fields.

The source does not establish whether the two counterparty-country fields are equivalent, how CES field names map to `cashflow_data.cashflow`, or how all supported fields are validated before policy configuration.

## Questions

- Which CES field names are contractually supported by RATANONE Cash Settlement?
- Is `Entity.Counterparty_Country_ISO_Code` mapped to `Entity.Counterparty_SCI_DOMICILE_COUNTRY`, and under what data-quality conditions?
- Which component validates a CES rule before it affects GraphQL, SSDR SQL, or WebSocket filtering?
- Should an unsupported field cause a visible configuration or runtime error rather than silently return no records?

## Why it matters

JSONB extraction on an absent path does not necessarily fail. An incorrectly configured CES field can therefore deny expected access without an explicit technical error.
---
type: query
title: What Is the Static Data Entitlement Rule Language and Failure Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [data-entitlement, rule-language, static-data-service, query-service, security]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--yw24rt, static-data-service, query-service, cash-settlement-data-entitlement, data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Option2  RATAN existing data entitlement implementation.md"]
---
# What Is the Static Data Entitlement Rule Language and Failure Contract?

## Question

What is the complete contract for entitlement rules returned by [[static-data-service|static-data-service]] and applied by [[query-service|Query Service]]?

## Evidence

The source documents this lookup:

```bash
GET <static-data-service>/v2/rule/entitlement?role=Onshore&country=Nepal
```

It gives the following example predicate:

```text
Entity.Booking_Entity_SCI_FMID IN ('400007847')
```

It also describes `permitted_rule`, `forbidden_country`, and `forbidden_rule` as configuration mechanisms.

## Unknowns

The source does not specify:

- The response schema and expression grammar.
- Allowed fields, operators, literals, and nested expressions.
- How permitted and forbidden rules compose when both apply.
- Validation and query-injection protections.
- Handling of missing, invalid, or conflicting rules.
- Fail-open versus fail-closed behavior when rule retrieval fails.
- Cache lifetime, refresh, audit, and rollback behavior.
- Whether role identifiers are case-sensitive; the source uses both `Onshore` and `OnShore`.

## Required Resolution

Define a versioned API and rule-validation contract before extending entitlement filtering to Cashflow History, SSDR, or Group Blotter.
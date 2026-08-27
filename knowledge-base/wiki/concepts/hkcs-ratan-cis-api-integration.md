---
type: concept
title: HKCS RATAN-CIS API Integration
created: 2026-08-23
updated: 2026-08-23
tags: [HKCS, HAU, RATAN, CIS, API, accounting, integration]
related: [hkcs, hau, ratan, cis, ebbs, ebbs-accounting-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# HKCS RATAN-CIS API Integration

## Integration Model

For the documented HKCS HAU flow, RATAN will not send accounting. CIS is expected to query the relevant data from the RATAN API.

The open-question record also states that accounting for HAU is not required in RATAN. The source does not define whether the data queried by CIS is settlement, cashflow, status, position, or another non-accounting payload.

## Required Contract Definition

Before implementation approval, the integration contract should define:

- API endpoint and version.
- Data scope and object definitions.
- Query timing and freshness requirements.
- Authentication and authorization.
- Error, retry, and idempotency behavior.
- Reconciliation and operational monitoring.
- Ownership boundaries between RATAN and CIS.

## Scope Boundary

The non-accounting conclusion applies only to the documented HKCS HAU flow. It does not establish a general rule for other currencies, metals, entities, or future accounting integrations.
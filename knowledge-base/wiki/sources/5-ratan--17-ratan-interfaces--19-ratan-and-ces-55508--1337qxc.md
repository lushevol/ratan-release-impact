---
type: source
title: Ratan and CES 55508
authors: [Yunzhe Ta, Terris Li]
year: 2026
url: ""
venue: Confluence
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, ces, fm-ces, data-entitlement, interface, cashflow]
related: [ces, ems2, ratan-data-entitlement, data-policy-and-data-profile-precedence, functional-versus-data-entitlement, what-is-the-authoritative-ratan-ces-entitlement-api-contract, what-is-the-authoritative-ces-data-policy-and-data-profile-precedence-model, what-is-the-ratan-ces-outage-and-cached-entitlement-behavior]
sources: ["RATAN/RATAN -Interfaces/Ratan and CES 55508.md"]
---
# Ratan and CES 55508

This document is a high-level overview of the RATAN–CES integration. It describes CES, formerly EMS3, as Financial Markets' strategic data-entitlement solution and states that RATAN calls CES to decide which cashflows OPS users may view.

## Status and provenance

The article records updates and review activity on 2026-03-25, but its Status field is blank. The article says reviewed content should be marked `Published`; therefore, its publication and implementation status should be confirmed.

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Terris Li | 2026-03-25 | @Quill Li @Terris Li | 2026-03-25 | |

## Stated integration purpose

CES is described as a centralized FM solution for managing data-entitlement rules and providing a consolidated view of data access. RATAN integrates with CES to satisfy need-to-know requirements: users should see cashflows only for entities allowed by their profile and location.

The described flow is:

```text
RATAN --(API)--> FM CES
```

The document states that the integration will use CES APIs, FMAA tokens, service-resilience measures, selective enablement, and caching. It does not provide an endpoint, API version, request or response schema, token flow, caching policy, error handling, or audit design.

## Entitlement model

- A **Data Policy** is linked to a user's HR profile, inherited automatically by a new user, and managed by a Policy Owner / COO.
- A **Data Profile** is linked to a user's Role profile and assigned by an EMS3 operator.
- A **Role** represents activities a user may perform within business functions accessible in an application.
- As a general rule, role-based Data Profile rules take precedence over HR-profile-based Data Policy rules.

The example states that a Data Policy can constrain Korea trading for non-Korean users, while a Data Profile can allow GB users to trade Korea trades outside Korea trading hours.

See [[data-policy-and-data-profile-precedence]].

## Scope boundary

The source distinguishes data and functional entitlements:

- CES governs data entitlement for the RATAN Cashflow blotter and BCS Cashflow blotter, qualified by “so far.”
- EMS2 continues to govern menu and button/function entitlement.

This is a scoped authorization boundary, not evidence that CES replaces EMS2 or governs general RATAN functional authorization. See [[functional-versus-data-entitlement]] and [[ratan-data-entitlement]].

## Documentation gaps

The sections for connection details, interface specification, team contacts, known issues, and troubleshooting contain no substantive content. The linked RATAN OLA is not enough to establish an operating contract for this interface.

The source leaves unresolved whether CES is live or target-state, how RATAN behaves during CES or FMAA outages, and how cached decisions avoid stale authorization. These gaps are tracked in [[what-is-the-authoritative-ratan-ces-entitlement-api-contract]], [[what-is-the-authoritative-ces-data-policy-and-data-profile-precedence-model]], and [[what-is-the-ratan-ces-outage-and-cached-entitlement-behavior]].
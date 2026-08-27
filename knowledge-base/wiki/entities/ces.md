---
type: entity
title: CES
created: 2026-08-22
updated: 2026-08-24
tags: [entitlements, authorization, access-control, indonesia, entitlement, fm, cash-settlement, ces, fm-ces, ems3, data-entitlement, financial-markets]
related: [entitlement-based-regional-routing, ratan-id, what-jwt-claims-and-ces-controls-authorize-indonesia-ratan-access, cash-settlement-data-entitlement, ces-data-entitlement-integration, query-service, ssdr, ratan-data-entitlement, data-policy-and-data-profile-precedence, functional-versus-data-entitlement, ems2, what-is-the-authoritative-ratan-ces-entitlement-api-contract, what-is-the-ratan-ces-outage-and-cached-entitlement-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md", "RATAN/RATAN -Interfaces/Ratan and CES 55508.md"]
---

# CES

CES, formerly known as EMS3, is described as Financial Markets' strategic solution for data entitlement. Its stated purpose is to centralize management of data-access rules and provide a consolidated view of those rules.

For the Cash Settlement initiative, CES is identified as FM's strategic data-entitlement solution. In the Indonesia Ratan onshoring design, CES is identified as the authority for Indonesia-versus-global data access.

## RATAN Data Entitlement

The *Ratan and CES 55508* source describes CES as the provider of data-entitlement decisions for RATAN. These decisions are used to limit cashflow visibility to entities that an OPS user is authorized to see.

The documented CES scope is currently:

- RATAN Cashflow blotter
- BCS Cashflow blotter

CES is distinct from [[ems2]]. According to the *Ratan and CES 55508* source:

- CES is responsible for scoped data entitlement.
- EMS2 remains responsible for RATAN menu and button/function entitlement.

RATAN uses CES APIs with FMAA-token authentication and intends to provide resilience, selective enablement, and caching. The source does not define the associated technical or operational contract. See [[what-is-the-authoritative-ratan-ces-entitlement-api-contract]] and [[what-is-the-ratan-ces-outage-and-cached-entitlement-behavior]].

## Indonesia Ratan Onshoring Context

The Indonesia technical-design source states that:

- Indonesia onshore users receive Indonesia data only.
- Other onshore users require approval to access Indonesia data.
- Designated group users may access Indonesia data.
- A user may hold Indonesia and global entitlements concurrently.

That source proposes selecting a Ratan region from an entitlement role and eligible legal-entity FMID, potentially using regional data extracted from or added to JWTs.

The Indonesia technical-design source does not specify:

- The authoritative JWT claims.
- Entitlement mappings.
- The validation algorithm.
- Audit events.
- Denial behavior.

## Cash Settlement Integration Direction

The Cash Settlement data-entitlement source states that [[query-service]] is intended to switch the SSDR cashflow-query integration to CES and that entitlement control is to be added to identified Cash Settlement interfaces.

The source targets a March 2026 go-live but provides no exact go-live date and does not demonstrate that implementation has been completed.

The previous RATAN-owned entitlement implementation is described as no longer being a fallback option for the target integration. Separately, the Cash Settlement data-entitlement source reports that [[ssdr]] was using RATAN-owned entitlement as of 10 December 2025.

## Known Constraints

The Cash Settlement data-entitlement source does not define:

- CES policy capabilities.
- Identity attributes.
- Decision API contracts.
- Availability behavior.
- Caching.
- Audit records.
- Support for allow/deny exception precedence.

It also does not establish formal architectural approval.
---
type: entity
title: FMO Post Trade Portal
created: 2026-08-22
updated: 2026-08-23
tags: [application, post-trade, cash-settlement, cashflow-blotter, FMO, operations-portal, business-rules, RATAN, portal, micro-frontend, settlement-operations, cashflow, testing, login-api]
related: [fmrp-china-cash-settlement, cashflow-status-and-substate-model, client-level-cashflow-netting, hold-and-un-hold, manual-failure-and-reinstatement, settle-as-gross, adhoc-settlement-instructions, ratan, rule-service, business-rule-maintenance, data-ops, ratan-cashflow-blotter, grouping-blotter-delivery-control, data-entitlement-for-settlement-operations, mock-settlement-test-data-generation, bcs, cash-settlement-cashflow, application-tile, region-entitled-drawer-filtering, ems3, ratan-entitlement-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---

# FMO Post Trade Portal

## Role and portal architecture

The RATAN One Processing Guide (DOI) describes FMO Post Trade Portal as a unified micro-frontend portal for post-trade users. It exposes functions from multiple systems as tiles in a common user interface, while access remains controlled by the respective systems.

According to that guide, the portal is an access surface for [[ratan]] operations rather than the authoritative source of cashflow state or settlement processing. User visibility is additionally constrained by [[data-entitlement-for-settlement-operations]].

The same guide identifies settlement-related tiles including:

- Cashflow Blotter
- Grouping Blotter
- Cashflow Dashboard
- Settlement and validation exceptions
- Business rules
- Netting and Nostro static data
- Auto Netting Rules
- SSDR

## Login and regional tile visibility

The Indonesia Cash Settlement design describes FMO Post Trade Portal as a user interface that, after login, calls a login API and displays blotters or drawers according to the API response.

According to that design, visible application tiles are filtered using regional data entitlement from [[ems3]], especially `Entity.Booking_Entity_SCI_FMID`.

This design establishes a UI visibility control rather than complete backend authorization. The underlying blotter APIs may require separate entitlement enforcement.

## Cashflow blotter and settlement operations

In the FMRP China Cash Settlement demonstration source, FMO Post Trade Portal is the user-facing application in which operators log in and open the `cashflow blotter` to find, inspect, select, and operate on cashflows.

That source shows the following portal operations:

- **Net Selected Cashflow**
- **Netting All Cashflow**
- **Hold**
- **Un-Hold**
- **Failed**
- **Reinstate**
- **Settle as Gross**
- **Adhoc SI**

The demonstration source also shows a cashflow details page with `Vostro SI Information` and `Nostro SI Information` areas.

## Testing and mock-data verification

The Mock Testing Data Userguide describes FMO Post Trade Portal as a verification interface used to locate cashflows created during mock testing.

For a mocked cashflow, testers search using the newly generated `cashflowId`.

For a replayed [[bcs]] trade, testers use the Cashflow Blotter `[FX&Equity]` and search for the trade. The guide specifies adding the `BCS_` prefix to the trade search value.

According to the Mock Testing Data Userguide, portal search is a verification step after message production or trade replay. That source does not define the portal's complete search contract or establish that finding a record means the settlement process has completed.

## RATAN One business-rule configuration

The RATAN One Processing Guide for Business Rules Maintenance describes FMO Post Trade Portal as the operations portal used to configure approved RATAN One business rules. The guide places the portal within [[business-rule-maintenance]] and states that it supports rule blotters for:

- Authorization limits
- NSTP
- Cashflow suppression
- SWIFT suppression
- Auto netting

According to the Business Rules Maintenance guide, the documented governance process requires the MT to first review and approve a proposed rule. An eOPS request is then raised for Data Ops to configure the approved rule in the portal.

The guide states that configuration is expected to be tested in UAT before production release. It does not specify the exact division of configuration responsibilities between UAT and production.

## Evidence boundaries

The FMRP China Cash Settlement demonstration source demonstrates portal actions and stated result states. It does not define the portal's internal architecture, service ownership, authorization model, or authoritative relationship to [[blade]], [[stella]], and [[ratan]].

The Mock Testing Data Userguide documents use of the portal to verify mocked cashflows and replayed BCS trades. It does not define the portal's complete search behavior or indicate that a successful search confirms settlement completion.

The RATAN One Processing Guide for Business Rules Maintenance does not provide substantive detail on the portal's architecture, login process, entitlement model, or the technical enforcement of approval controls.

The separate RATAN One Processing Guide (DOI) provides the portal-level characterization of FMO Post Trade Portal as a unified micro-frontend, identifies its tile-based functions, and states that access remains controlled by the respective underlying systems.

The Indonesia Cash Settlement design specifically documents login-API-driven drawer or blotter display and regional tile filtering. It identifies UI visibility control, but does not establish complete authorization enforcement by the underlying blotter APIs.

## Related pages

- [[ratan]]
- [[data-ops]]
- [[ratan-rule-lifecycle-management]]
- [[mock-settlement-test-data-generation]]
- [[bcs]]
- [[cash-settlement-cashflow]]
- [[application-tile]]
- [[region-entitled-drawer-filtering]]
- [[ems3]]
- [[ratan-entitlement-rule]]
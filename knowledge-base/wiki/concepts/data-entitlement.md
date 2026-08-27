---
type: concept
title: Data Entitlement
created: 2026-08-24
updated: 2026-08-25
tags: [authorization, data-entitlement, RATAN, EMS2, onboarding]
related: [ratan-data-entitlement, ems2, function-entitlement, api-gateway, ratan, fmces, integration-onboarding, release-management, 5-ratan--19-ratan-release-copy--23-ratan-release-plan-2026--35-ratan-new-onboarding-checklist-2026--67-20260523--1tga3mm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md", "RATAN/RATAN -Release copy/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_23_CHG0989771_Enable data entitlement by integration with FMCES.md"]
---
# Data Entitlement

**Data entitlement** is the authorization or provisioning of access to specified data for an identified consumer, user, tenant, account, role, or service.

## RATAN and EMS2 design

According to the RATANONE Cash Settlement technical-design authentication-flow source, data entitlement defines the scope of data a user may access after the user has been authorized for a function.

In that design, data entitlement is represented by `dataEntitlementRoles` in the `auth-service` response and by the `Global` role returned for the EMS2 entity [[ratan-data-entitlement]]. The source does not specify the downstream filtering mechanism or whether `Global` means unrestricted access.

## FMCES integration objective

According to the RATAN onboarding checklist source for `CHG0989771`, the stated objective is to enable data entitlement through integration with [[fmces]].

That source does not define the entitlement subject, data scope, decision owner, lifecycle, approval process, or enforcement point.

## Questions requiring confirmation

- What data is being entitled?
- Which consumers or principals receive access?
- Is entitlement requested, approved, provisioned, and revoked through RATAN, FMCES, or both?
- Is the integration synchronous, asynchronous, batch-based, or part of an onboarding workflow?
- What evidence demonstrates successful entitlement and safe rollback?

The concept should remain at this evidence-bounded definition until the source body or an authoritative interface document provides these details.
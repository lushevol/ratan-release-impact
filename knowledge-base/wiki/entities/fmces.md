---
type: entity
title: FMCES
created: 2026-08-24
updated: 2026-08-25
tags: [entitlements, rbac, authorization, ems3, fmces, ratan, integration, data-entitlement]
related: [ems2, ratan, fmces-based-ratan-entitlement-authorization, ratan-jwt-entitlement-claim-design, data-entitlement, is-fmces-the-same-as-fm-ces, 5-ratan--19-ratan-release-copy--23-ratan-release-plan-2026--35-ratan-new-onboarding-checklist-2026--67-20260523--1tga3mm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md", "RATAN/RATAN -Release copy/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_23_CHG0989771_Enable data entitlement by integration with FMCES.md"]
---
# FMCES

## Overview

`FMCES` is a named system or integration endpoint in the RATAN change document [[5-ratan--19-ratan-release-copy--23-ratan-release-plan-2026--35-ratan-new-onboarding-checklist-2026--67-20260523--1tga3mm]]. The filename identifies integration with FMCES as the apparent mechanism for enabling data entitlement.

In the architecture source, FMCES is also referred to as `EMS3` and is described as the proposed replacement entitlement source for Ratan functional RBAC. Its documented response includes:

- `entitlement_name`
- Data-policy rules
- Data-profile rules
- Data-entitlement values

## Authorization relationship to EMS2

No approved mapping establishes authorization parity with [[ems2]], including access involving both `RATAN_ENTITLEMENT_ID` and `RATAN_ENTITLEMENT_GLOBAL`.

## Unresolved identity and ownership

The available evidence does not define what FMCES stands for, establish its ownership, or confirm whether it is distinct from the `FM CES` terminology used in [[are-ratan-one-loaniq-il-and-fm-ces-distinct-deployments]].

Accordingly, no API, message schema, deployment boundary, or operational responsibility should be inferred until an authoritative definition is available.
---
type: concept
title: FMCES-Based Ratan Entitlement Authorization
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, fmces, ems2, entitlement, rbac, authorization]
related: [fmces, ems2, ratan-jwt-entitlement-claim-design, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# FMCES-Based Ratan Entitlement Authorization

The proposed target replaces EMS2 role/action entitlement lookups with FMCES entitlement names, data policies, data profiles, and data-entitlement values.

FMCES may provide the functional access inputs needed by Ratan, but the source does not define an EMS2 parity mapping, decision rules, failure handling, caching model, or treatment of conflicting and mixed entitlements.
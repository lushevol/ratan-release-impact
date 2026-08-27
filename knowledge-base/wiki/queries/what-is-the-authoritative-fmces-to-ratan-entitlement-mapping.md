---
type: query
title: What Is the Authoritative FMCES-to-Ratan Entitlement Mapping?
created: 2026-08-24
updated: 2026-08-24
tags: [fmces, ems2, ratan, entitlement, rbac, authorization]
related: [fmces, ems2, fmces-based-ratan-entitlement-authorization, ratan-jwt-entitlement-claim-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# What Is the Authoritative FMCES-to-Ratan Entitlement Mapping?

Define the approved mapping from EMS2 subject/role/action decisions to FMCES entitlement names, policies, profiles, and data entitlements. Include authorization parity, `RATAN_ENTITLEMENT_ID` and `RATAN_ENTITLEMENT_GLOBAL` semantics, mixed-entitlement users, negative cases, and failure behavior.
---
type: query
title: How Do Entra Token Claims Map to Cash Settlement Function and Data Entitlements?
created: 2026-08-24
updated: 2026-08-24
tags: [microsoft-entra, authorization, entitlements, ces, ems2, claims]
related: [microsoft-entra, entra-based-single-sign-on-and-mfa, function-entitlement, data-entitlement, api-gateway-entitlement-enforcement, cash-settlement-data-entitlement, ems2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/ENTRA integration (draft).md"]
---
# How Do Entra Token Claims Map to Cash Settlement Function and Data Entitlements?

## Question

If Microsoft Entra authenticates Cash Settlement users, which Entra token claims, if any, participate in function and data-entitlement decisions?

## Evidence

The draft discusses Microsoft Entra SSO, MFA, and MSAL-based token acquisition but does not define authorization claims or entitlement behavior. It contains no mapping for Entra groups, application roles, scopes, or custom claims.

## Required Boundary

The integration must distinguish identity authentication from Cash Settlement authorization. Entra-issued claims must not be assumed to replace the existing [[ems2]], CES, or API-gateway entitlement controls.

The authoritative design should specify:

- which component validates the Entra token;
- which claims establish user identity and coarse-grained application access;
- how function entitlements are resolved;
- how data entitlements are resolved and enforced;
- whether CES remains authoritative for data filtering;
- how entitlement changes are reflected during an active session; and
- how missing, stale, or conflicting claims are handled.

This question remains open until the relationship between Entra claims and [[cash-settlement-data-entitlement]] is explicitly documented.
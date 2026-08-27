---
type: concept
title: Single-UI Authentication Flow
created: 2026-08-24
updated: 2026-08-24
tags: [authentication, Single-UI, SSO, bearer-token]
related: [single-ui-authorization, ems2, auth-service, function-entitlement, data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# Single-UI Authentication Flow

The Single-UI authentication flow begins with username-and-password login through the SSO endpoint and produces a `Single-UI-Authorization` bearer token.

Single-UI then uses its BFF to retrieve account-level function entitlements from [[ems2]]. Those entitlements are returned to the frontend, while protected API requests are subsequently checked by the [[api-gateway]] through [[auth-service]].

The source contains incomplete password and token examples and does not define the complete login response schema.
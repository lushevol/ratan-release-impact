---
type: concept
title: Function Entitlement
created: 2026-08-24
updated: 2026-08-24
tags: [authorization, function-entitlement, EMS2, API gateway]
related: [ems2, api-gateway, auth-service, data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# Function Entitlement

A function entitlement determines whether a user may access or invoke a particular application function.

The source gives `RATAN_TRADE_BLOTTER:ACCESS_FMO_POST_TRADE_PORTAL` as an example action and identifies the API gateway as the component that checks the corresponding entitlement through [[auth-service]].

Function entitlement is distinct from [[data-entitlement]]: it authorizes the operation, not necessarily the full data scope exposed by that operation.
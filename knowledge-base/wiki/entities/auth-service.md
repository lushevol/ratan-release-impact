---
type: entity
title: auth-service
created: 2026-08-24
updated: 2026-08-24
tags: [authentication, authorization, auth-service, EMS2]
related: [api-gateway, single-ui-authorization, function-entitlement, data-entitlement, ems2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# auth-service

`auth-service` is the authentication and entitlement dependency called by the API gateway for each incoming API request.

## Interface

The source documents:

```ruby
POST https://uklvadapp1345.uk.dev.net:3833/v3/authenticate
Single-UI-Authorization Bearer eyJ...
```

The example response contains a serialized `entitlement` value with a function role, function actions, and `dataEntitlementRoles`, together with `userInfo`.

## Responsibilities

The documented responsibilities are to verify the `Single-UI-Authorization` bearer token and provide authorization context to the [[api-gateway]]. The source does not specify token expiry, caching, failure handling, or whether `auth-service` directly queries [[ems2]] for every request.
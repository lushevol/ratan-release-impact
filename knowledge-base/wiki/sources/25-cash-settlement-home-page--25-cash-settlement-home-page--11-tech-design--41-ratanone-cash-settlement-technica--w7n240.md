---
type: source
title: RATANONE Cash Settlement Authentication Flow
authors: []
year: 2025
url: ""
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [authentication, authorization, cash-settlement, EMS2, RATANONE, Single-UI]
related: [single-ui-authorization, cash-settlement-home-page, ems2, auth-service, api-gateway, ratan-data-entitlement, function-entitlement, data-entitlement, single-ui-authentication-flow, api-gateway-entitlement-enforcement, ems2-entitlement-lookup]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# RATANONE Cash Settlement Authentication Flow

This technical design describes authentication and entitlement retrieval for the RATANONE Cash Settlement Home Page. It covers Single-UI login, account-level function-entitlement retrieval from [[ems2]], API-gateway authorization through [[auth-service]], and RATAN-specific data-entitlement retrieval.

## Authentication flow

Single-UI authenticates a user through the SSO endpoint and receives a `Single-UI-Authorization` bearer token.

```ruby
POST https://fmo-mfe.uk.dev.net:8453/api/auth/v2/sso/login
{
    "username": "1481696",
    "passwor"...
}

Single-UI-Authorization Bearer eyJ...
```

The password field and bearer-token value are incomplete in the source. They should not be treated as an implementation-ready request or as reusable credentials.

## Function-entitlement retrieval

The Single-UI BFF retrieves account and function entitlements from EMS2.

```ruby
GET https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/account/1481696

{
    "accountStatus": "A",
    "accountName": "1481696",
    "accountType": "User",
    "fullName": "IIQ1481696,User",
    "accountOwner": "1481696",
    "entitlementTypes": [
        {
            "uniqueName": "1511446402|MXMLS_FILEUPLOAD_BSM|1511446459|DPS_MLS",
            "roleName": "DPS_MLS",
            "roleDescription": "",
            "applicationName": "MUREX G2000",
            "isPrivilege": "N"
        }
		...
    ],
    "status": ""
}
```

The source states that the resulting entitlements are returned to the frontend in `"entitlementsToke"` and inside `"entitlements"`. The referenced images are not available in the text extraction, so the exact frontend payload schema remains unverified.

## API-gateway authorization

For each incoming API request, the API gateway calls [[auth-service]] to verify the bearer token and obtain authorization context.

```ruby
POST https://uklvadapp1345.uk.dev.net:3833/v3/authenticate
Single-UI-Authorization Bearer eyJ...

{
    "entitlement": "{\"role\":\"FMO_OPS_BOM\",\"actions\":[\"RATAN_TRADE_BLOTTER:ACCESS_FMO_POST_TRADE_PORTAL\"...],\"dataEntitlementRoles\":\"Global\"}",
    "userInfo": {
        "userId": "1481696",
        "fullName": "1481696",
        "country": "Global",
        "entitlementCountry": "China"
    }
}
```

The response separates function authorization from data authorization:

- `role` identifies a function-entitlement role.
- `actions` identifies permitted application functions.
- `dataEntitlementRoles` identifies a data-access role.
- `userInfo` provides identity and geographic context.

The source does not define token expiry, error handling, caching, retry behavior, or the exact enforcement point for data filtering.

## RATAN data-entitlement lookup

The design uses the following EMS2 endpoint to retrieve RATAN-specific data entitlement.

```ruby
GET https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/entitlements/entity/name/RATAN_DATA_ENTITLEMENT/user/1481696

{
    "entitlements": [
        {
            "id": 11514754,
            "subject": {
                "id": 11164752,
                "name": "RATAN_DATA_ENTITLEMENT",
                "longName": "/RATAN_DATA_ENTITLEMENT",
                "entity": {
                    "id": 11164654,
                    "name": "RATAN_DATA_ENTITLEMENT",
                    "systemName": "RATAN",
                    "locked": true
                }
            },
            "role": {
                "id": 11515751,
                "name": "Global",
                "entity": {
                    "id": 11164654,
                    "name": "RATAN_DATA_ENTITLEMENT",
                    "systemName": "RATAN",
                    "locked": true
                },
                "roleDescription": "Global",
                "isPrivilege": "No"
            },
            "action": {
                "id": 11164807,
                "name": "VIEW_ENTITLEMENT",
                "entity": {
                    "id": 11164654,
                    "name": "RATAN_DATA_ENTITLEMENT",
                    "systemName": "RATAN",
                    "locked": true
                }
            }
        }
    ],
    "count": 1
}
```

The example returns one entitlement for the locked `RATAN_DATA_ENTITLEMENT` entity. Its system is `RATAN`, its role is `Global`, and its action is `VIEW_ENTITLEMENT`.

## Authorization dimensions

The design distinguishes two authorization dimensions:

1. **Function entitlement** controls whether a user may access or invoke a function, such as `RATAN_TRADE_BLOTTER:ACCESS_FMO_POST_TRADE_PORTAL`.
2. **Data entitlement** controls the data scope available to an otherwise authorized user, represented by `dataEntitlementRoles` and the `RATAN_DATA_ENTITLEMENT` role.

The document does not establish whether data-entitlement filtering is enforced by the API gateway, Single-UI BFF, GraphQL layer, or downstream RATAN services.

## Flow summary

```text
Single-UI
  └─ POST /api/auth/v2/sso/login
       └─ receives Single-UI-Authorization bearer token

Single-UI BFF
  └─ GET EMS2 /rest/account/{account}
       └─ receives account/function entitlements
       └─ returns entitlements to frontend

API Gateway
  └─ POST auth-service /v3/authenticate
       └─ verifies bearer token
       └─ retrieves or validates function entitlement
       └─ obtains userInfo and data-entitlement role

auth-service / EMS2
  └─ GET /rest/entitlements/entity/name/RATAN_DATA_ENTITLEMENT/user/{user}
       └─ receives RATAN data entitlement
```

## Open implementation questions

- Is `auth-service` independently retrieving EMS2 entitlements, validating cached claims, or both?
- Are EMS2 entitlements cached during request authorization?
- Where is `RATAN_DATA_ENTITLEMENT` applied to API or database queries?
- How are multiple roles combined?
- How are `country`, `entitlementCountry`, and the `Global` role interpreted?
- What is the authoritative schema for the frontend entitlement token?
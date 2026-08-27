---
type: source
title: "Deprecated API Gateway & Auth Server Combination"
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13473901"
venue: "Cash Settlement Platform Architecture - Indonesia"
created: 2026-08-24
updated: 2026-08-24
tags: [deprecated, ratan, indonesia, iam, api-gateway, entitlement]
related: [ratan, ratan-indonesia-isolated-deployment, ratan-api-gateway-auth-server-consolidation, indonesia-ratan-data-residency-isolation, fmces-based-ratan-entitlement-authorization, ratan-jwt-entitlement-claim-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# Deprecated API Gateway & Auth Server Combination

> [!warning]
> This is a deprecated proposal, not an accepted target architecture. Its stated objectives, dependencies, and routing rules require confirmation from a successor design or approved decision.

The source proposes consolidating [[ratanone-api-gateway]] and [[ratanone-auth-server]] for an Indonesia-isolated [[ratan]] deployment. It also describes a planned migration from [[forgerock-openam]] and EMS2 to [[microsoft-entra-id]] and [[fmces]].

## Stated objectives

| # | Objective | Description |
|---|---|---|
| 1 | Merge API Gateway & Auth Server | Consolidate `ratanone-api-gateway` and `ratanone-auth-server` to reduce integration overhead and simplify Indonesia deployment topology. |
| 2 | Data Entitlement Token Optimisation | Reduce `Single-UI-Entitlement` JWT payload and improve performance through claim, cache, and TTL design. |
| 3 | Functional Entitlement via FMCES | Replace EMS2 with FMCES for functional RBAC. |
| 4 | Entra Onboarding Interface Design | Select a service-to-service authentication flow for Microsoft Entra ID. |
| 5 | Fallback: Entra vs FMAA | Provide an FMAA fallback when Entra ID is unavailable. |

## Component contract

| Component | Tech stack | Role |
|---|---|---|
| SPA (Frontend) | React / MFE | Browser client |
| `ratanone-api-gateway` | Spring Cloud Gateway (WebFlux, Java 17) | Edge routing, authentication enforcement, audit |
| `single-ui-bff` | Spring Boot MVC (Java 17) | Login, JWT issuance, session management |
| `ratanone-auth-server` | Spring Boot MVC (Java 17) | Token validation, Redis session store |
| ForgeRock OpenAM | External IdP | Current OIDC provider |
| OUD (LDAP) | Oracle Unified Directory | Username/password directory |
| EMS2 | External REST service | Current entitlement and RBAC source |
| Redis | In-memory store | Session cache and token store |
| PostgreSQL | Relational database | Session blacklist and application configuration |

## Indonesia isolation constraint

The source states that Indonesian customer and transaction data must remain in-country. It proposes country-scoped PostgreSQL, Redis, and session-management infrastructure, separate from the global deployment. It does not define the corresponding backup, disaster-recovery, telemetry, encryption-key, replication, or support-access boundaries.

See [[indonesia-ratan-data-residency-isolation]].

## Current login evidence

The documented endpoint accepts either credentials or an OIDC authorization code:

```bash
POST /api/auth/v2/sso/login
Content-Type: application/json

{ "username": "1196411", "password": "*********" }

{ "code": "DsFdQ0hLlWzS6ijvQYTGXAzDimo", "clientId": "51358ratan",
  "iss": "https://mfaig.global.standardchartered.com:443/openam/oauth2/realms/root/realms/sso" }
```

The documented controller signature is:

```java
@PostMapping(value = "v2/sso/login")
public ResponseEntity<ResponseOfAuthenticate> authenticate(@RequestBody RequestOfAuthenticate request,
       HttpServletRequest httpServletRequest, HttpServletResponse response) throws JsonProcessingException {
	...
}
```

The supplied NGINX configuration routes the `/api/auth/` path to the gateway rather than directly to `single_ui_bff`:

```nginx
location /api/auth/ {
    rewrite ^/api/auth/(.*)$ /$1 break;
    proxy_redirect    off;
    proxy_set_header  Host $host;
    proxy_set_header  X-Real-IP $remote_addr;
    proxy_set_header  X-Forwarded-Proto http;
    proxy_set_header  X-Forwarded-For $remote_addr;
    proxy_set_header  X-Forwarded-Host $remote_addr;
    proxy_pass http://ratan_backend_api_gateway;
    # proxy_pass http://single_ui_bff;
}
```

This routing evidence does not resolve runtime ownership of login, token issuance, token validation, or Redis sessions. See [[what-is-the-authoritative-ratan-login-jwt-and-session-ownership-model]].

## Entitlement transition

The documented EMS2 lookup is role/action-oriented:

```bash
GET https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/entitlements/entity/name/RATAN_DATA_ENTITLEMENT/user/1481696
```

```json
{
  "entitlements": [
    {
      "subject": { "name": "RATAN_DATA_ENTITLEMENT" },
      "role": { "name": "Global" },
      "action": { "name": "VIEW_ENTITLEMENT" }
    }
  ],
  "count": 1
}
```

The proposed FMCES lookup returns entitlement names, data policies, data profiles, and data-entitlement values:

```json
[
  {
    "user_data": {
      "app_name": "RATAN_ENTITLEMENT_RULE",
      "itam_id": "51358",
      "user_id": "1481696"
    },
    "entitlements": {
      "entitlement_name": [
        "RATAN_ENTITLEMENT_COMMON",
        "RATAN_ENTITLEMENT_GLOBAL"
      ],
      "data_policies": {
        "policy_rules": [
          {
            "data_policy_name": "RATAN - GBS CN PSS",
            "policy_owner": "2021102"
          }
        ]
      },
      "data_profiles": {
        "data_profile_rules": [
          {
            "data_profile_name": "RATAN - back2back FMID",
            "data_profile_owner": "2021102"
          }
        ]
      },
      "data_entitlements": [
        {
          "key": "Entity.Booking_Entity_SCI_FMID",
          "values": ["..."]
        }
      ]
    }
  }
]
```

The source proposes embedding either limited `entitlement_name` values or all `data_entitlements.values` in a JWT. The second option acknowledges excessive token size risk. The stated `values`-based rule involving `"8"` has no documented business meaning or authorization policy.

## Risks and unresolved matters

- ForgeRock/OneMFA is stated to be decommissioned by the end of Q3 2026, while FMAA is proposed as an Entra fallback.
- The gateway/auth-server merger has no documented availability, scaling, migration, or security-boundary assessment.
- No authoritative EMS2-to-FMCES entitlement mapping or mixed-entitlement rule is provided.
- JWT-based country routing lacks a claim contract, revocation strategy, freshness rule, and behavior for users with both or neither country entitlement.
- Source examples contain sensitive personal and entitlement data; this summary retains only the minimum structural evidence.
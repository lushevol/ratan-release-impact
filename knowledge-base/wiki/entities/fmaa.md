---
type: entity
title: FMAA
created: 2026-08-24
updated: 2026-08-24
tags: [fmaa, authentication, service-account, api, ratan, indonesia, token, ces, cash-settlement, authorization, api-access, application-registration, application-access]
related: [cash-settlement-platform, microsoft-entra-id, fmces, ems2, ratan-indonesia-onshoring-2026, ces, auth-service, cash-settlement-data-entitlement, tlm, query-recon-records, fmaa-authenticated-accounting-retrieval, ratan, fmaa-token-based-application-authentication, ratan-interface-architecture]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md", "RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# FMAA (FM Authentication Adapter)

## Role and authentication pattern

FMAA, or FM Authentication Adapter, is described in the RATAN and EMS2-34010 source as the authentication API used by applications connecting to RATAN. After successful authentication, FMAA issues a token that can be used to authorize access to the respective systems.

That source establishes the following high-level pattern:

1. A calling application authenticates through FMAA.
2. FMAA issues a token.
3. The token is used for authorization.

The source does not identify a specific standard or implementation. It should not be assumed from that document that FMAA uses OAuth 2.0, JWT, or any other particular token technology.

## Roles and integrations

The Indonesia upstream/downstream design lists FMAA as the service-account authentication API for the Indonesia RATAN integration perimeter. It associates FMAA with API integration and identifies Balaji, Ts and Biradar, Shivaraj as contacts for the dependency.

The FM CES integration design describes FMAA as the authentication and token dependency used by [[auth-service|auth-service]] when calling [[ces|CES]] for RATANONE Cash Settlement data-entitlement results.

The Korea Accounting – TLM Recon source describes FMAA as the registration and authentication dependency for the Korea accounting-reconciliation API. API clients must register in FMAA to obtain the credentials sent with each request.

## Indonesia endpoint

The Indonesia upstream/downstream design documents the following integration endpoint:

```text
https://fmaaprod.gdc.standardchartered.com/v1/fmaa/oauth2
```

The RATAN and EMS2-34010 FMAA source does not specify an endpoint. Its omission of endpoint details does not override the Indonesia-specific endpoint documented above.

## Authentication headers for Korea accounting reconciliation

The Korea Accounting – TLM Recon source specifies the following request headers for the Korea accounting-reconciliation API:

```text
FMAA-Token: ${token from FMAA}
FMAA-userId: ${userId from FMAA}
FMAA-appId: ${appId from FMAA}
```

## Token handling

According to the FM CES integration design, [[auth-service|auth-service]] already caches FMAA tokens in Redis and renews a token when it is unavailable from the cache. The reviewed configuration confirms `RATAN_PROD` as the account used for the v3 token endpoint.

That design identifies the FMAA token lifecycle as a prerequisite for CES availability from RATAN's perspective. It does not define token-expiry handling, refresh-failure behavior, or a service-level objective.

Separately, the Korea Accounting – TLM Recon source does not document token lifetime, renewal, authorization scopes, error status codes, or credential-rotation procedures.

The RATAN and EMS2-34010 FMAA source leaves the following contract details unspecified:

- Endpoint and protocol
- Client-authentication model
- Token format
- Claims
- Scopes
- Audience
- Expiry
- Refresh
- Revocation
- Transmission method
- Validation path
- Failure handling
- Interface scope

## Open ownership question

The Indonesia upstream/downstream source does not establish whether FMAA is the permanent service-to-service authentication authority, a transitional dependency, or complementary to [[microsoft-entra-id]]. The approved authentication path remains to be confirmed.
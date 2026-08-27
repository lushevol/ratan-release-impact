---
type: query
title: Which JWT Country Field Is Authoritative for Data Entitlement?
created: 2026-08-24
updated: 2026-08-24
tags: [jwt, country, data-entitlement, oud, query-service]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--yw24rt, auth-service, oud, query-service, static-data-service, cash-settlement-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Option2  RATAN existing data entitlement implementation.md"]
---
# Which JWT Country Field Is Authoritative for Data Entitlement?

## Question

Does Cash Settlement entitlement evaluation use `userInfo.country`, `userInfo.entitlementCountry`, another JWT claim, or a derived value?

## Evidence

The documented authentication response includes:

```json
"userInfo": {
    "userId": "1481696",
    "fullName": "1481696",
    "country": "Global",
    "entitlementCountry": "China"
}
```

The documented entitlement-rule lookup instead uses a country parameter:

```bash
GET <static-data-service>/v2/rule/entitlement?role=Onshore&country=Nepal
```

The source states that country data comes from [[oud|OUD]] and is set in the login token, but it does not map an OUD field to the rule lookup parameter.

## Why It Matters

An incorrect country claim could grant overly broad access, deny valid access, or make Taiwan onboarding unreliable. The Taiwan feasibility assessment depends on receiving a distinct and authoritative Taiwan country classification.

## Required Resolution

Confirm the claim-to-parameter mapping in [[auth-service|auth-service]] and [[query-service|Query Service]], including fallback behavior, normalization rules, permitted values, and whether `Global` is a country value or an access classification.
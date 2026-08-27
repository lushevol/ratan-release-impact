---
type: entity
title: OUD
created: 2026-08-24
updated: 2026-08-24
tags: [ldap, user-directory, authentication, oracle-unified-directory, identity, directory, country, entitlement]
related: [single-ui-bff, forgerock-openam, ratan, auth-service, query-service, static-data-service, which-jwt-country-field-is-authoritative-for-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Option2  RATAN existing data entitlement implementation.md"]
---
# OUD

OUD (Oracle Unified Directory) is the documented user directory used for username/password authentication in the Ratan login flow. It is distinct from the OIDC authorization-code flow through [[forgerock-openam]].

## Data entitlement

The data entitlement design identifies OUD as the source of user country information for RATANONE data entitlement evaluation.

The documented entitlement flow places country information into the login token issued through [[auth-service|auth-service]]. [[query-service|Query Service]] then uses the entitlement context to request a filtering condition from [[static-data-service|static-data-service]].

The source assumes that OUD can return a distinct Taiwan country value:

```json
{"lastName":"Song","country":"Taiwan","firstName":"Sybil", ...
```

The authoritative JWT claim for entitlement evaluation is unresolved. An authentication example contains both `country: "Global"` and `entitlementCountry: "China"`, while the entitlement endpoint expects a country value such as `Nepal`. See [[which-jwt-country-field-is-authoritative-for-data-entitlement]].
---
type: concept
title: RDM Reference-Data Integration via Kong
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, kong, oauth2, client-credentials, reference-data, indonesia]
related: [rdm, kong, what-is-the-production-readiness-plan-for-ratan-rdm-kong-integration, how-should-ratan-handle-rdm-amber-data-quality-and-pagination, indonesia-environment-readiness-dependencies]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation/RDM Integration via Kong Gateway.md"]
---
# RDM Reference-Data Integration via Kong

Ratanone's documented RDM integration obtains reference data through [[kong]] using OAuth 2.0 client credentials.

## Required authorization boundary

The documented implementation reuses Kong consumer registration `EDMILDAP_RATAN_EDMI_PROD_Ratanone-PCT2`. The consumer authenticates as `EDMILDAP/RATAN_EDMI_PROD`, and the RDM producer must explicitly grant that consumer access. Authentication is therefore distinct from producer authorization.

The token request requires scope `RDMApiService_GET`. Tokens are documented to expire after 900 seconds.

## Flow

1. Query the dynamic client-registration endpoint using the AD service-account credentials obtained from OneVault.
2. Exchange the returned client ID and client secret for a bearer token using `grant_type=client_credentials`.
3. Invoke the selected RDM endpoint with that bearer token.

The source does not establish whether client-registration lookup belongs in the runtime path or is a provisioning operation. Implementations should avoid logging client secrets or bearer tokens and should define rotation, redaction, and failure behavior.

## Environment and release constraints

SIT configuration is documented as complete, but production onboarding is `TBD`. This is an external readiness dependency for [[indonesia-environment-readiness-dependencies]], not proof of production availability.

The configuration concerns IAG-operated Kong and must not be conflated with internal [[api-gateway]] or [[spring-cloud-gateway]] architecture.

## Operational gaps

The demonstrated holiday response signals `Amber` data quality and a large paginated result set. The source does not specify an acceptance policy for that status, page traversal contract, rate limits, timeout/retry policy, caching interval, or compensation fallback procedure.
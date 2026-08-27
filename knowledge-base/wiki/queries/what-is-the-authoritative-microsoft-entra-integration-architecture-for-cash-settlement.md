---
type: query
title: What Is the Authoritative Microsoft Entra Integration Architecture for Cash Settlement?
created: 2026-08-24
updated: 2026-08-24
tags: [microsoft-entra, architecture, authentication, oauth, oidc, cash-settlement]
related: [microsoft-entra, msal, entra-based-single-sign-on-and-mfa, single-ui-authentication-flow, auth-service, api-gateway]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/ENTRA integration (draft).md"]
---
# What Is the Authoritative Microsoft Entra Integration Architecture for Cash Settlement?

## Question

What production architecture will connect Microsoft Entra to RATANONE Cash Settlement, and how will it coexist with [[auth-service]] and [[api-gateway]]?

## Evidence

The draft presents Microsoft Entra as the bank-approved identity-provider direction and recommends [[msal|MSAL]] for token acquisition by Java Spring and front-end applications. It does not provide an implementation architecture.

## Information Needed

The authoritative design should identify:

- the required application registrations for the front end, gateway, authentication service, APIs, and machine-to-machine clients;
- approved OAuth 2.0 and OpenID Connect flows;
- token issuers, tenants, audiences, scopes, roles, groups, and custom claims;
- the component or components responsible for token validation;
- secret, certificate, and credential rotation controls;
- session, refresh-token, and logout behavior;
- MFA and Conditional Access requirements; and
- the meaning, owner, and release impact of “Onboard ADO.”

Until these details are documented, the source supports a proposed direction but not a finalized implementation contract.
---
type: source
title: ENTRA Integration (Draft)
authors: []
year: 2026
url: "https://learn.microsoft.com/en-us/entra/identity-platform/sample-v2-code?tabs=apptype"
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [microsoft-entra, identity, authentication, cash-settlement, draft]
related: [microsoft-entra, msal, entra-based-single-sign-on-and-mfa, ratanone-microsoft-entra-integration-architecture, entra-token-claims-cash-settlement-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/ENTRA integration (draft).md"]
---
# ENTRA Integration (Draft)

## Scope

This draft describes the proposed Microsoft Entra direction for securing access to RATANONE Cash Settlement. It is a high-level background and prerequisite note rather than a complete integration design. It does not define application registrations, OAuth 2.0 or OpenID Connect flows, token audiences or scopes, JWT validation rules, claim mappings, or deployment configuration.

## Background

The document presents Microsoft Entra as the bank-approved identity-provider solution for securing access. It describes Microsoft Entra application integration as a way to connect applications to Microsoft Entra services, including Azure Active Directory (Azure AD), to support secure single sign-on (SSO) and multi-factor authentication (MFA).

These statements establish the intended platform direction and capabilities. They do not confirm that SSO, MFA, identity governance, access management, or identity protection have been configured for Cash Settlement.

## Prerequisites

| Prerequisite | Status |
|---|---|
| ITAM App Instance ID (`51358`) | Complete |
| Onboard ADO | Incomplete |

The draft does not explain the purpose of the ITAM identifier, define what “Onboard ADO” means, identify an owner, or state whether ADO onboarding is a release blocker.

## Technical Solution

The document cites Microsoft guidance recommending the [[msal|Microsoft Authentication Library (MSAL)]] for token acquisition. It identifies Java Spring and front-end applications as supported implementation targets.

The draft does not select specific MSAL packages or versions and does not define whether the applications will use browser-based authentication, a backend-for-frontend pattern, resource-server validation, confidential-client flows, or machine-to-machine authentication.

## Integration Boundaries

The draft does not specify the relationship between Microsoft Entra and existing Cash Settlement components such as [[auth-service]], [[api-gateway]], [[ems2]], or [[cash-settlement-data-entitlement]]. In particular, it does not establish:

- where Entra-issued tokens will be validated;
- which issuer, tenant, audience, scopes, roles, groups, or custom claims are trusted;
- how authentication claims map to function or data entitlements; or
- whether Entra replaces, fronts, federates with, or supplements existing authentication and entitlement services.

Microsoft Entra integration should therefore be treated as an identified dependency and proposed identity-provider direction, not as evidence that existing CES or EMS2 authorization controls are being replaced.

## Source Assessment

The source provides moderate evidence of the intended identity-provider direction and the recommended use of MSAL. Its evidence is weak for a completed implementation decision because it is marked as a draft and contains no formal approval record, target architecture, implementation scope, or deployment evidence.

See [[ratanone-microsoft-entra-integration-architecture]] for the unresolved architecture questions and [[entra-token-claims-cash-settlement-entitlements]] for the authorization and entitlement mapping questions.
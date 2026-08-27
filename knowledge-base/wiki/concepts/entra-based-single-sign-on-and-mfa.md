---
type: concept
title: Entra-Based Single Sign-On and MFA
created: 2026-08-24
updated: 2026-08-24
tags: [microsoft-entra, sso, mfa, authentication, identity]
related: [microsoft-entra, msal, single-ui-authentication-flow, api-gateway-entitlement-enforcement, cash-settlement-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/ENTRA integration (draft).md"]
---
# Entra-Based Single Sign-On and MFA

## Definition

Entra-based single sign-on (SSO) and multi-factor authentication (MFA) is the proposed use of [[microsoft-entra]] to authenticate Cash Settlement users through a centrally managed enterprise identity platform.

SSO allows users to access the application using an existing enterprise identity session. MFA adds one or more additional verification factors according to the applicable identity and access policies.

## Evidence in the Draft

The source identifies SSO and MFA as outcomes enabled by Microsoft Entra application integration. It does not specify whether MFA will be mandatory for all Cash Settlement users, enforced through tenant-wide Conditional Access, or handled differently for service-to-service clients.

The draft also does not define the selected browser or service authentication flow, redirect URIs, token audiences, scopes, or logout behavior.

## Authentication and Authorization Boundary

SSO and MFA establish or strengthen authentication, but they do not define Cash Settlement function or data authorization. Entra claims may participate in downstream decisions, but the source does not establish a claim-to-entitlement mapping or authorize bypassing [[cash-settlement-data-entitlement]], [[ems2]], or [[api-gateway-entitlement-enforcement]].

The location where tokens are validated—[[api-gateway]], [[auth-service]], individual resource services, or a combination—remains unresolved.
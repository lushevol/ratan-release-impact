---
type: entity
title: Microsoft Entra
created: 2026-08-24
updated: 2026-08-24
tags: [microsoft-entra, identity-provider, iam, authentication, cash-settlement]
related: [msal, entra-based-single-sign-on-and-mfa, single-ui-authentication-flow, auth-service, api-gateway, cash-settlement-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/ENTRA integration (draft).md"]
---
# Microsoft Entra

## Role

Microsoft Entra is presented in the draft as the bank-approved identity-provider direction for RATANONE Cash Settlement. Its intended role is to provide a centrally managed identity and access foundation for application access.

The source describes Microsoft Entra as supporting identity governance, access management, identity protection, secure single sign-on (SSO), and multi-factor authentication (MFA).

## Status in Cash Settlement

The source is a draft and does not confirm a production integration. It establishes documented intent rather than a finalized architecture or implementation decision.

The following details remain unspecified:

- Microsoft Entra tenant and application registrations;
- OAuth 2.0 and OpenID Connect flows;
- token issuers, audiences, scopes, roles, groups, and custom claims;
- token-validation responsibility;
- MFA and Conditional Access policy;
- logout and session-management behavior; and
- integration with [[auth-service]] and [[api-gateway]].

Microsoft Entra must not be assumed to replace [[ems2]], CES, or existing function and data-entitlement enforcement.

## Prerequisites

The draft records ITAM App Instance ID `51358` as complete and “Onboard ADO” as incomplete. It does not define the meaning, ownership, or release impact of ADO onboarding.

## Related Integration Work

The proposed Entra integration is related to [[single-ui-authentication-flow]] and may affect how authenticated identity is propagated to [[api-gateway-entitlement-enforcement]] and [[cash-settlement-data-entitlement]]. The source does not define those integration contracts.
---
type: entity
title: Microsoft Authentication Library (MSAL)
created: 2026-08-24
updated: 2026-08-24
tags: [msal, microsoft-entra, token-acquisition, authentication, java-spring, front-end]
related: [microsoft-entra, entra-based-single-sign-on-and-mfa, ratanone-microsoft-entra-integration-architecture]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/ENTRA integration (draft).md"]
---
# Microsoft Authentication Library (MSAL)

## Role

Microsoft Authentication Library (MSAL) is the recommended client-library family identified by the draft for acquiring tokens from Microsoft identity services. The source states that MSAL is available for Java Spring and front-end applications.

The draft links to Microsoft’s sample guidance: <https://learn.microsoft.com/en-us/entra/identity-platform/sample-v2-code?tabs=apptype>

## Scope of the Recommendation

The source recommends MSAL as a token-acquisition path but does not select:

- a language-specific package;
- a library version;
- an authentication flow;
- application-registration settings;
- credential storage and rotation controls; or
- a token-validation and authorization design.

MSAL should therefore not be treated as the complete security architecture. Token validation, issuer and audience checks, claim mapping, authorization, session management, and integration with [[api-gateway]] or [[auth-service]] require separate decisions.

## Cash Settlement Relevance

MSAL is relevant to the proposed [[microsoft-entra]] integration for RATANONE Cash Settlement. Whether the front end, Java Spring services, or both acquire tokens directly through MSAL remains an open architecture question.
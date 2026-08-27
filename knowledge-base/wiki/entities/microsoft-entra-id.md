---
type: entity
title: Microsoft Entra ID
created: 2026-08-24
updated: 2026-08-24
tags: [iam, identity-provider, sso, mfa, oidc, saml]
related: [forgerock-openam, ratan, ratan-indonesia-isolated-deployment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# Microsoft Entra ID

Microsoft Entra ID is the stated target enterprise IAM platform replacing ForgeRock/OneMFA for Ratan. The source cites SAML/OIDC alignment, centralized Conditional Access, and modern MFA as migration drivers.

The required service-to-service authentication design remains undecided, including the choice between Client Credentials and Managed Identity.
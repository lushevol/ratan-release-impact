---
type: query
title: How Should RATAN Manage Kong Authentication for Scheduled RDM API Calls?
created: 2026-08-24
updated: 2026-08-24
tags: [kong, authentication, rdm, scheduler, credential-management, indonesia]
related: [kong, rdm, 51358-ratanone-static-data-service, rdm-api-based-holiday-compensation, fmces-based-ratan-entitlement-authorization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# How Should RATAN Manage Kong Authentication for Scheduled RDM API Calls?

The selected RDM API design depends on authenticated gateway access in staging and production, but the source does not define the credential lifecycle or ownership model.

## Questions to Resolve

- Which identity, LDAP/client registration, and gateway policy authorize scheduled access from Indonesia?
- Who owns initial provisioning, secret storage, renewal, rotation, revocation, and incident response?
- What token type, expiry, refresh behavior, and retry rules apply?
- Should credentials be cached at service scope, and how are concurrent scheduled executions controlled?
- How is the internal scheduler action `RATAN_INTERNAL_FUNC:STATIC_SERVICE:FETCHANDUPDATE` preserved when Control-M is replaced?

## Evidence

The source asks whether a Kong token should be stored in `localThread` but provides no decision. A thread-local token is not an adequate documented lifecycle strategy for a scheduled service integration.
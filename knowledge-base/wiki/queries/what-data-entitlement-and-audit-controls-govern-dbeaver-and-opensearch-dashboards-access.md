---
type: query
title: What Data Entitlement and Audit Controls Govern DBeaver and OpenSearch Dashboards Access?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, dbeaver, dashboards, entitlement, audit, security]
related: [dbeaver, opensearch-dashboards, opensearch-jdbc-client-connectivity, microsoft-entra, oud]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# What Data Entitlement and Audit Controls Govern DBeaver and OpenSearch Dashboards Access?

## Question

What authentication, authorization, data-entitlement, auditing, and export controls apply when users access Cash Settlement business data through [[dbeaver]] or [[opensearch-dashboards]]?

## Gap

The source provides a direct JDBC-client configuration path but does not specify user identity, role assignment, country-level filtering, data masking, access revocation, query auditing, export controls, or privileged-access approval.

## Related evidence

Existing identity and entitlement material includes [[microsoft-entra]], [[oud]], [[how-do-entra-token-claims-map-to-cash-settlement-function-and-data-entitlements]], and [[which-jwt-country-field-is-authoritative-for-data-entitlement]].

## Evidence needed

- Approved identity-provider and authentication mechanism for both access paths.
- Role and data-scope mappings, including country entitlements.
- Query, export, and administrative audit requirements.
- Access-review and revocation procedures.
- Policy for distributing truststores and connection secrets.
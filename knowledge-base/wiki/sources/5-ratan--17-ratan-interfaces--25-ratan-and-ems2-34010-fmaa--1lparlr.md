---
type: source
title: RATAN and EMS2-34010 FMAA
authors: [Zhenzhen Liu, Junying Jiang, Yunzhe Ta, Daiqi Wang]
year: 2026
url: ""
venue: "RATAN interface documentation"
tags: [ratan, ems2, fmaa, access-control, interface]
related: [ratan, ems2, fmaa, x-ratanone, ratan-ems2-user-entitlement-integration, fmaa-token-based-application-authentication, operational-level-agreement]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# RATAN and EMS2-34010 FMAA

## Summary

This document describes two access-control integrations for [[ratan]]:

- [[ems2]] centrally manages RATAN user entities and the subjects assigned under the `X_RATANONE` entitlement entity.
- [[fmaa]] authenticates applications that connect to RATAN and issues a token for subsequent authorization.

The source is a high-level interface reference. It does not provide a formal API specification, connection configuration, payload schemas, token format, ownership contacts, error catalogue, or recovery procedures.

## EMS2 user and entitlement integration

When a RATAN user logs in, RATAN connects to EMS2 and retrieves the list of subjects under `X_RATANONE`. The document states that this list controls:

- Which blotters are displayed to the user.
- Which right-click or context-menu operations the user may access.

The source characterizes this as dynamic, role-based UI customization. It does not establish whether the same permissions are independently enforced by RATAN backend services.

## FMAA application authentication

Applications connecting to RATAN are described as using FMAA authentication. After successful authentication, FMAA issues a token that can be used to authorize access to the respective systems.

The document does not identify the FMAA protocol, endpoint, client-registration process, token type, claims, scopes, audience, expiry, refresh or revocation behavior, transport headers, or token-validation mechanism.

## High-level flow

1. A RATAN user logs in.
2. RATAN retrieves the user's `X_RATANONE` subjects from EMS2.
3. RATAN uses the returned subjects to determine stated UI visibility and context-menu permissions.
4. An application connecting to RATAN authenticates through FMAA.
5. FMAA issues a token for authorization.

The source does not include request and response sequences, failure paths, or detailed end-to-end message flows.

## Troubleshooting endpoints

The source preserves the following sample EMS2 URLs:

**Sample user-role/account lookup:**

<https://sabre-prod-ems2.gdc.standardchartered.com:16443/ems2/rest/account/1431837>

**Production `X_RATANONE` entitlement lookup:**

<https://sabre-prod-ems2.gdc.standardchartered.com:16443/ems2/rest/entitlements/entity/name/X_RATANONE>

**Non-production `X_RATANONE` entitlement lookup:**

<https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/entitlements/entity/name/X_RATANONE>

These URLs are troubleshooting examples, not a complete contract. The source does not state their HTTP methods, required headers, authentication requirements, response schemas, or operational safeguards.

## OLA reference

The document points to the RATAN FM Settlement OLA:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

It states that the BPMS OLA location is unchanged, but does not define whether the OLA includes EMS2 and FMAA ownership, support targets, or incident responsibilities.

## Documentation status

The document records updates and review activity dated 2026-01-26:

- Updated by: @Zhenzhen Liu, @Junying Jiang, @Yunzhe Ta
- Reviewed by: @Zhenzhen Liu, @Daiqi Wang
- Status: blank

The source text says that status should be updated to `Published` after review, but the status field is empty. Publication or final approval therefore cannot be confirmed from this document.

## Missing information

The following information requires authoritative documentation:

- EMS2 API methods, schemas, authentication, caching, timeout, retry, and outage behavior.
- Mapping from `X_RATANONE` subjects to blotters and context-menu actions.
- Independent backend authorization controls.
- FMAA endpoint, protocol, client onboarding, token format, claims, validation, expiry, renewal, and revocation.
- Scope of applications and RATAN interfaces required to use FMAA.
- Interface ownership, support contacts, and service-level responsibilities.
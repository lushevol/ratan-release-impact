---
type: concept
title: FMAA Token-Based Application Authentication
tags: [fmaa, ratan, application-authentication, token-based-authorization, security]
related: [fmaa, ratan, ratan-ems2-user-entitlement-integration, ratan-interface-architecture, operational-level-agreement]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# FMAA Token-Based Application Authentication

## Overview

FMAA is described as the authentication boundary for applications connecting to RATAN. Following successful authentication, it issues a token for authorizing access to the respective systems.

This mechanism is distinct from the EMS2 user-entitlement flow: EMS2 supplies user subjects, while FMAA authenticates calling applications.

## Supported evidence

The source supports only the following high-level sequence:

1. An application attempts to connect to RATAN.
2. The application authenticates through FMAA.
3. FMAA issues a token.
4. The token is used to authorize access.

No specific token technology should be inferred from this description.

## Missing security contract

The source does not specify the FMAA endpoint, protocol, client registration, credentials, token format, claims, scopes, audience, expiry, refresh, revocation, transport header, validation component, or failure behavior.

It also does not clarify whether FMAA is required for every RATAN interface or only selected application-to-application connections.
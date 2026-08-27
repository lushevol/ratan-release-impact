---
type: query
title: What Is the Authoritative FMAA-to-RATAN Authentication Contract?
tags: [fmaa, ratan, authentication, authorization, api-contract]
related: [fmaa, ratan, fmaa-token-based-application-authentication, ratan-interface-architecture]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# What Is the Authoritative FMAA-to-RATAN Authentication Contract?

## Question

What protocol and operational contract governs application authentication through FMAA when connecting to RATAN?

## Known evidence

The source states that applications connecting to RATAN use FMAA authentication and receive a token for authorization.

## Information required

- FMAA endpoint, protocol, and client-registration model.
- Token format, claims, scopes, audience, expiry, renewal, and revocation.
- Token transmission and RATAN validation behavior.
- Applications and interfaces in scope.
- Authentication failure, outage, and incident-handling procedures.
- Support ownership and relationship to the RATAN FM Settlement OLA.
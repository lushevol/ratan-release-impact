---
type: entity
title: sabre-booking-api
created: 2026-08-24
updated: 2026-08-25
tags: [java, sdk, stella, dependency, api, sabre, ratan]
related: [stella, ratanone-stella-ambassador, stella-channel, fmrp-stella, ratan, ratan-fmrp-stella-interface]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md", "RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# sabre-booking-api

## Role

`sabre-booking-api` is the Java SDK used by the Stella integration. The documented upgrade target is version `1.2.0` of `com.scb.sabre.fmrep:sabre-booking-api`.

The RATAN–FMRP STELLA source presents it as the common technical dependency for both settlement-status write-back and trade-lock status retrieval.

## Components

```text
Cashflow/trade status write back:
  StellaBookingApi

Trade lock status:
  StellaBookingRestApi
```

## Stella integration

The source associates version `1.2.0` with the new `RATANCASH_V2("ratancash-v2")` channel.

It also identifies `StellaBookingApi.sendMessage` and `StellaBookingApi.sendScbml` in a documented `TimeoutException` stack trace.

## Documented endpoint

The validation-related API is represented by the following signature:

```text
/v1/stella/{type}/{operation}/{action}
```

The source does not define the HTTP method, request and response schemas, authentication model, versioning policy, or expansion of the path parameters.

## Boundary

The SDK is an implementation component, not evidence that SABRE, FMRP, STELLA, and the SDK are the same entity. Their architectural relationship remains an open question in [[what-is-the-relationship-between-sabre-fmrp-stella-and-sabre-booking-api]].
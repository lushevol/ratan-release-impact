---
type: query
title: What Is the Relationship Between SABRE, FMRP STELLA, and sabre-booking-api?
tags: [sabre, fmrp-stella, stella, sdk, architecture, open-question]
related: [fmrp-stella, sabre, stella, sabre-booking-api, ratan-fmrp-stella-interface]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# What Is the Relationship Between SABRE, FMRP STELLA, and sabre-booking-api?

## Question

How are SABRE, FMRP STELLA, the STELLA booking engine, `sabre-booking-api`, `StellaBookingApi`, and `StellaBookingRestApi` related architecturally?

## Current evidence

The interface title identifies “SABRE (FMRP STELLA)”. The body refers to Stella APIs, the SABRE/STELLA SDK Booking API, the STELLA booking engine, and the `sabre-booking-api` SDK. The source does not define whether these names represent a product family, platform, service, booking engine, SDK, or support organization.

## Resolution criteria

A definitive architecture description should identify:

- The ownership boundary between SABRE and FMRP STELLA.
- Whether STELLA is a service, platform, or booking engine name.
- Whether `sabre-booking-api` is maintained by SABRE or another team.
- The deployment and dependency relationship between both SDK components.
- The role of SABRE PSS in support and change management.

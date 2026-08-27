---
type: concept
title: Booking Currency to ISO Mapping
created: 2026-08-22
updated: 2026-08-22
tags: [currency, iso, booking, accounting, swift, static-data]
related: [stella, ratan, strategy-golden-source, global-rates-settlement-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Booking Currency to ISO Mapping

Booking currency to ISO mapping converts booking-system currency values into ISO currency codes required by settlement processing, accounting, and SWIFT generation.

The Global Rates requirement calls for a supported booking-currency list and an authoritative mapping agreed with trading-platform and relevant downstream systems. It does not identify the owning system or define the treatment of unsupported, deprecated, or conflicting currency values.
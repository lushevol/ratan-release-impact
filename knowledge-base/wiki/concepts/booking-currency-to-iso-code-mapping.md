---
type: concept
title: Booking-Currency-to-ISO-Code Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [currency, iso-code, swift, accounting, static-data]
related: [new-currency-onboarding-static-data-readiness, ratan, murex-2-11, settlement-accounting, what-is-the-authoritative-change-control-for-pm-and-iso-currency-mappings]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
---
# Booking-Currency-to-ISO-Code Mapping

Booking-currency-to-ISO-code mapping converts an original booking currency into the ISO Code required by both SWIFT and Accounting.

The source describes the RATAN mapping as hardcoded and supplied by Murex 2.11 colleagues. Its reference data is maintained in the Cash Settlement - Accounting Confluence document.

No mapping rows, ISO standard version, validation controls, unknown-currency behavior, or reconciliation process between the reference document and RATAN implementation are defined. Change-control ownership is tracked in [[what-is-the-authoritative-change-control-for-pm-and-iso-currency-mappings]].
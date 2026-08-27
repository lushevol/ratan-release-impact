---
type: concept
title: Agency Payment Identification
created: 2026-08-23
updated: 2026-08-23
tags: [agency-booking, payments, swift, field-72, cn-settlement]
related: [murex-2-11, murex-2-11-cn-derivative-settlement, murex-2-11-field-20-format, what-is-the-authoritative-agency-payment-booking-and-swift-generation-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# Agency Payment Identification

Agency payment identification concerns the recognition of payments arising from agency-profile and agency-portfolio bookings in the Murex 2.11 CN derivative context.

The meeting described a possible gap: current identification uses portfolio information, but agency trades may produce neither a payment in the China agent queue nor a SWIFT message on the agency profile. Field 72 was reported to contain an indicator identifying an agency payment.

## Required Clarifications

- The Front Office agency-booking model.
- Whether Field 72 supplements or replaces portfolio-based identification.
- The expected payment-queue destination and SWIFT-generation behavior.
- Whether Field 20 logic is required for agency bookings.
- Validation through a test or production-like case.

The source does not provide a live production validation, exact Field 72 indicator, or approved target design.
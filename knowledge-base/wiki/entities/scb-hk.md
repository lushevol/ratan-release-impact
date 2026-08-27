---
type: entity
title: SCB HK
created: 2026-08-23
updated: 2026-08-23
tags: [SCB-HK, Gold-Clearing-Agent, HKCS, settlement]
related: [hkcs, hau, ratan, lms, hau-gold-settlement-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# SCB HK

## Role in HKCS

SCB HK is the booking entity for the HKCS initiative and is expected to become a Gold Clearing Agent. HKCS deals will be booked in SCB HK books.

## Booking Convention

Gold for this activity will be booked using `HAU` rather than `XAU`. This distinction drives the related SWIFT, static-data, limits, rounding, and downstream-feed requirements.

## Evidence Boundary

The source states the intended business requirement but does not include approval, implementation, or testing evidence for SCB HK.
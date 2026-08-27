---
type: concept
title: HAU Gold Settlement Configuration
created: 2026-08-23
updated: 2026-08-23
tags: [HAU, gold, settlement, static-data, configuration, HKCS]
related: [hau, xau, hkcs, scb-hk, release-cutoff-configuration, manual-entity-go-live-static-data-controls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# HAU Gold Settlement Configuration

## Definition

HAU gold settlement configuration is the set of booking, static-data, limit, rounding, holiday, and cutoff rules required for the HKCS activity in which SCB HK books gold as `HAU` instead of `XAU`.

## Required or Proposed Rules

- Book HKCS gold deals in SCB HK books using `HAU`.
- Use approval limits matching the existing XAU limits.
- Configure a separate `HAU MAIN` Nostro.
- Configure Vostros as `HAU MAIN`.
- Use three decimal places with rounding off for HAU.
- Assess whether HAU release cutoffs should inherit XAU values.
- Determine whether RDM supplies HAU holiday static data.
- Send HAU cashflows to LMS.

## Unresolved Configuration

The source does not provide the HAU Nostro account record, Vostro records, cutoff values, holiday calendar, effective dates, or deployment evidence. The receiver/Nostro-agent BIC is also contradictory: `BKCHHKHHGSI` appears in the SWIFT requirement, while `BKCHCHKHHGSI` appears in the Nostro requirement.

These unresolved items should be treated as configuration dependencies rather than completed controls.
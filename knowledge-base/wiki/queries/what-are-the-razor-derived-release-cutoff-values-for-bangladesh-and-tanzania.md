---
type: query
title: What Are the Razor-Derived Release Cutoff Values for Bangladesh and Tanzania?
created: 2026-08-23
updated: 2026-08-23
tags: [razor, release-cutoff, bangladesh, tanzania, configuration]
related: [go-live-readiness-for-manual-entity-settlement, tanzania-scb-dar, scb-dhaka-dac-in-country]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md"]
---
# What Are the Razor-Derived Release Cutoff Values for Bangladesh and Tanzania?

For Bangladesh (`FMID 300011470`) and Tanzania (`FMID 10040387`), the checklist leaves `cut_off_time` and `cut_off_shifter` blank and states that Currency/Shifter/Time/Timezone will be sourced from Razor.

## Required resolution

Obtain the actual Razor-derived configuration for each entity, including:

- Currency.
- Cutoff shifter.
- Cutoff time and timezone.
- Effective date and configuration location.
- Configuration owner.
- UAT or production-verification evidence.

Without these values, the cutoff setup is not auditable from the checklist.
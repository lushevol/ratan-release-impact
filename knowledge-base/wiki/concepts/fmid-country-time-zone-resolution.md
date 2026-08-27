---
type: concept
title: FMID-to-Country-to-Time-Zone Resolution
created: 2026-08-23
updated: 2026-08-23
tags: [fmid, timezone, accounting, reference-data]
related: [ratan, manual-entity-go-live-static-data-controls, release-cutoff-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md"]
---
# FMID-to-Country-to-Time-Zone Resolution

For accounting generation, the documented lookup sequence is:

`FMID → country from static data → zoneId from country configuration`

A new country requires an additional country-to-`zoneId` configuration entry. The checklist supplies mappings for the manual-entity countries, including `Asia/Bahrain`, `Africa/Nairobi`, `Africa/Lagos`, `Asia/Colombo`, and `Asia/Dhaka`.

The source does not identify the implementation component, fallback behavior, or validation evidence for this lookup.
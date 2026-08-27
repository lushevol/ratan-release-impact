---
type: query
title: What Are the Authoritative Effective-Date Timezone, Overlap, and Re-Stamping Rules for SSI?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, effective-date, timezone, restamping, dqsl]
related: [ssi-effective-date-selection, ssi-plus, dqsl, ratan-ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# What Are the Authoritative Effective-Date Timezone, Overlap, and Re-Stamping Rules for SSI?

The source defines value-date comparisons to `Start_EffectiveDate` and `End_EffectiveDate` but does not define whether VD is a business date or timestamp, which timezone applies, or whether end dates are inclusive across all systems.

It also does not specify processing where both dates exist, overlapping old and `_ED` records are eligible, DQSL notifications are duplicated or late, or cashflows are already released, settled, or final. These rules are necessary for safe re-stamping and idempotent processing.
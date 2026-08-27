---
type: entity
title: BicNetting Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, configuration, bicnetting, maker-checker]
related: [static-configuration-management, static-configuration-auditability, pending-configuration-change-isolation, nostro-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# BicNetting Configuration

BicNetting Configuration is an existing static-configuration domain whose maker/checker workflow differs from Nostro.

When an existing record is updated, the source describes BicNetting as creating a separate pending record. The original remains confirmed while the pending record receives its own ID. On approval, the pending data is copied back to the original record and the temporary record is discarded.

This approach can make audit history difficult to retrieve because events for one logical configuration span multiple record IDs. The source also reports that the list may not refresh after operations and that the original record may be deleted while an update request is pending.

These behaviors are source-reported implementation findings and should be validated against the deployed system before migration or remediation.
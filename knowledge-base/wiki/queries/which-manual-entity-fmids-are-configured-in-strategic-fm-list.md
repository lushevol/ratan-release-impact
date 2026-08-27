---
type: query
title: Which Manual-Entity FMIDs Are Configured in STRATEGIC_FM_LIST?
created: 2026-08-23
updated: 2026-08-23
tags: [strategic-fm-list, swift, fmid, cashflow-suppression, open-question]
related: [strategic-fm-list-swift-generation-control, ratan, swift, cashflow-suppression-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md"]
---
# Which Manual-Entity FMIDs Are Configured in STRATEGIC_FM_LIST?

The checklist requires all non-suppressed manual-entity FMIDs to be included in `STRATEGIC_FM_LIST` for SWIFT-message generation, while excluding `SLATE_QFC` / FMID `401081696`.

Verify the authoritative production list, confirm the intended exclusion, and obtain message-generation evidence for every included FMID.
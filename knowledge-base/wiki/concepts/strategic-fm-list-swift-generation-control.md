---
type: concept
title: STRATEGIC_FM_LIST SWIFT Generation Control
created: 2026-08-23
updated: 2026-08-23
tags: [swift, business-rules, cashflow-suppression, fmid]
related: [swift, ratan, cashflow-suppression-rule, cashflow-suppression-and-swift-generation, which-manual-entity-fmids-are-configured-in-strategic-fm-list]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md"]
---
# STRATEGIC_FM_LIST SWIFT Generation Control

`STRATEGIC_FM_LIST` is a business-rule list checked during SWIFT-message generation. The checklist states that non-suppressed manual-entity FMIDs must be included for SWIFT messages to be generated.

`SLATE_QFC`, FMID `401081696` for `SLATE ONE LLC*DOH`, is an explicit exception. It must not be added because it is cashflow-suppressed. This is not a general rule for all Qatar entities.

The checklist provides no production list extract or runtime message-generation validation.
---
type: query
title: Is Kenya MX Eligibility Using the Correct Sender BIC Prefix?
created: 2026-08-23
updated: 2026-08-23
tags: [kenya, mx, swift, bic, configuration]
related: [manual-entity-swift-mx-bifurcation, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# Is Kenya MX Eligibility Using the Correct Sender BIC Prefix?

The latest Kenya MX row uses sender prefix `SCBLTZ`, which is also the Tanzania prefix. The superseded Kenya condition used `SCBLKE`.

Confirm the correct Kenya sender BIC condition, the approved implementation version, and whether any deployed configuration copied the Tanzania condition.
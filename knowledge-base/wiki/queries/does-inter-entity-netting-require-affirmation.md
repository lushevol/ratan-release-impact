---
type: query
title: Does Inter-Entity Netting Require Affirmation?
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, affirmation, ratan, settlement]
related: [inter-entity-auto-netting, auto-netting-affirmation-removal, 26-auto-netting-page-md-files--135-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-se--634gz8]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting.md"]
---
# Does Inter-Entity Netting Require Affirmation?

The inter-entity requirement says matched cashflows are netted “with affirmation,” while unmatched flows proceed gross without affirmation. The same source lists removal of auto-affirmation logic as a dependency but says it is not currently a blocker.

Clarify whether affirmation is a transitional legacy behavior, a manual control, or superseded by [[auto-netting-affirmation-removal]]. The answer affects the target lifecycle and rollout controls for [[inter-entity-auto-netting]].
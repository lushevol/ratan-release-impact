---
type: query
title: Does Removal of Auto Affirmation Apply to Manual Net?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, manual-netting, auto-affirmation, approval, operations]
related: [auto-netting-affirmation-removal, cashflow-auto-netting, manual-cashflow-netting, pending-confirmation-affirmation, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Remove Auto Affirmation from Auto Netting.md"]
---
# Does Removal of Auto Affirmation Apply to Manual Net?

## Question

Does the proposed removal of mandatory affirmation extend from the listed auto-netting categories to manual netting?

## Evidence

The requirement comment states that mandatory affirmation should be removed from manual netting and identifies discussion with Dinesh and Deepak. The comment is not incorporated into the behavior matrix as an approved manual-net requirement, and no replacement approval workflow or exception behavior is defined.

## Current position

Manual netting should be treated as out of scope or unresolved until the discussion produces an explicit decision. The auto-netting behavior documented in [[concepts/auto-netting-affirmation-removal]] must not be generalized to [[concepts/manual-cashflow-netting]] without confirmation.

A decision should specify whether manual-net cashflows remain unaffirmed, which exception is generated, who approves the cashflow, and how trade match status interacts with manual approval.
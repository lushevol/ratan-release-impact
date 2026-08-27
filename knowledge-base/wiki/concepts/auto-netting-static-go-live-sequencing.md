---
type: concept
title: Auto-Netting Static Go-Live Sequencing
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, go-live, static-data, rule-sequencing]
related: [cashflow-auto-netting, auto-netting-rule-management, auto-netting-resultant-nstp, clearing-swift-suppression, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Auto-Netting Static Go-Live Sequencing

Auto-netting static changes are sequenced to reduce inconsistent treatment during production activation.

## Required order

1. Create or update NSTP rules.
2. Create or update SWIFT suppression rules.
3. Create or update netting-static rules.

The sequence separates resultant approval handling from downstream message suppression and eligibility configuration. Suppression rules for a specific family are intended to become effective only after the corresponding auto-netting rule has been created or enabled.

## Scope

The process covers bilateral netting, BIC netting, SAL MTM and Coupon netting, CCIL netting, clearing/SWIFT suppression netting, and TAIFEX/CITIC IRS net-over-net rules.

The source records intended dates and reference times, but does not define whether `VD` and `V-1` use business-day calendars, how holidays are handled, or how activation is rolled back.
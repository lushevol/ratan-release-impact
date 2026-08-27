---
type: concept
title: Netting Release Control
tags: [cash-settlement, netting, release, maker-checker]
related: [ratan, s2bng, fmo-users, netting-resultant-cashflow-lifecycle, what-is-the-authoritative-ratan-release-state-for-netting-actions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Netting Release Control

Netting and un-netting are permitted only while a cashflow is unreleased.

For a cashflow Released through `Razor>FMSRE`, the source prohibits net and un-net actions. It characterizes this as a soft block and notes that an incremental posting is pending, so the final enforcement design and deployment state remain unresolved.

In Ratan, manual release of a net cashflow requires maker/checker workflow, subject to FMO user profiles and limits. SI amendment on a net cashflow is allowed only before release.
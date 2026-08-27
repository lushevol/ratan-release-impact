---
type: concept
title: Component Amendment Netting Exception
tags: [cash-settlement, netting, exception-management, amendment]
related: [netting-exception-recovery, netting-release-control, netting-resultant-cashflow-lifecycle, what-are-the-netting-component-amendment-state-transitions-and-accounting-effects]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Component Amendment Netting Exception

When a trade amendment affects a component cashflow of an unreleased net cashflow, the system must create an exception.

Users must manually review and accept the new net cashflow before it can be released. This is a pre-release requirement and does not define treatment after release.

The source does not specify state transitions for the prior resultant, component cashflows, accounting, payment instructions, notifications, or rejection of the proposed new net.
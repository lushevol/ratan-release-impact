---
type: concept
title: FX-Leg Netting Consistency
tags: [cash-settlement, netting, fx, settlement-method]
related: [cashflow-netting, what-is-the-authoritative-fx-leg-netting-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
created: 2026-08-23
updated: 2026-08-23
---
# FX-Leg Netting Consistency

One leg of an FX trade may be netted independently. The other leg must follow settlement method `NET`.

The source does not clarify whether the opposite leg must also be included in a netting set, whether it only receives the `NET` settlement-method value, or how this requirement interacts with release, amendment, and un-netting controls.
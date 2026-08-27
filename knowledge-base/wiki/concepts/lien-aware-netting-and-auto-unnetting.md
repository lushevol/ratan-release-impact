---
type: concept
title: Lien-Aware Netting and Auto-Un-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [lien, netting, auto-un-netting, ratan, cashflow]
related: [ratan, tds3, lien-driven-cashflow-nstp, ratan-netting-rule-check, nds-netting, cashflow-lifecycle-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# Lien-Aware Netting and Auto-Un-Netting

Lien-aware netting requires [[ratan]] to apply **“LIEN on Trade”** to a netting-resultant cashflow when any component cashflow has a parent trade with lien in [[tds3]]. This is an any-component rule; the source does not define aggregation of lien amounts.

A netting-resultant cashflow may auto-un-net only when it:

- is not `READY + Pending Ack`, `RELEASED`, or `SETTLED`;
- does not already carry **“LIEN on Trade”**; and
- has newly detected lien from the latest parent-trade event.

The specification does not define whether auto-un-netting is mandatory, how component cashflows are recreated or transitioned, how concurrent settlement progression is controlled, or how failures are recovered. The `READY + Pending Ack` notation also requires formal state-model confirmation.
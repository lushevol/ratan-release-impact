---
type: concept
title: Cashflow Netting and Un-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, netting, un-netting, settlement, lifecycle]
related: [ratan, cashflow-blotter, cashflow-status-lifecycle, cashflow-record, lien-aware-netting-and-auto-unnetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# Cashflow Netting and Un-Netting

The CN Settlement demo defines GUI-triggered netting and un-netting behaviour for individual cashflows in [[Ratan]].

## Netting

Netting is expected to:

- change each component cashflow status to `Netted`;
- create a resultant cashflow in `Queued` status;
- set the resultant amount to the sum of component-cashflow amounts; and
- assign the same netting ID to component and resultant cashflows.

## Un-netting

Un-netting is expected to restore component cashflows to `Queued` and change the resultant cashflow status to `Dead`.

The source does not define currency or value-date eligibility, aggregation and rounding rules, partial un-netting, audit retention, or netting-ID reuse. Unlike [[Lien-Aware Netting and Auto-Un-Netting]], this source does not mention liens.
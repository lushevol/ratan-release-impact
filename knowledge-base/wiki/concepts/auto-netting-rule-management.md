---
type: concept
title: Auto Netting Rule Management
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, rule-management, Data-Ops, cash-settlement, configuration]
related: [cash-settlement-home-page, cashflow-auto-netting, ratan, cashflow-blotter-action-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md"]
---
# Auto Netting Rule Management

Auto-netting rule management is the proposed Data Ops workflow for creating and maintaining RATAN cashflow auto-netting rules through the Auto Netting Rule Blotter.

## UI and Access

The Auto Netting Rule Blotter shares the UI of the manual netting rule blotter. A field or flag identifies whether a rule is manual or automatic. Access is restricted to the Data Ops profile.

## Rule Configuration

Day 1 rule configuration supports:

- Selection of available cashflow fields.
- A mandatory Booking Entity.
- A netting datetime expressed as `VD`, `VD-1`, or `VD-2` plus time.
- Exclusion criteria.
- Duplicate-condition validation.

Currency-pair criteria, extra netting keys such as `structure id`, and configurable rule priority are not in Day 1 scope.

## Rule Actions and Non-Retroactivity

The allowed rule actions are update and delete. There is no refresh function. Changes affect only newly received cashflows.

Cashflows already held in Pending Auto Netting remain there if their rule is updated or deleted before execution. They require manual Ops review, creating an operational reconciliation and ownership concern tracked by how are pending auto netting cashflows reconciled after rule changes.

---
type: query
title: What Does SETTLED Mean After FMSGW or FMSRE Manual Delete?
created: 2026-08-23
updated: 2026-08-23
tags: [swift, settlement-status, manual-payment, operational-risk]
related: [swift-status-lifecycle-and-reconciliation, fmswiftgateway, fmsre, amh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# What Does SETTLED Mean After FMSGW or FMSRE Manual Delete?

## Question

After `FMSGW Deleted`, `FMSRE Deleted`, or `Manual Delete`, does RATAN `SETTLED` represent confirmed payment completion, closure of the RATAN workflow, or an outstanding manual-payment responsibility?

## Evidence

The requirement maps all three outcomes to `SETTLED`, while stating that users are expected to make payment manually through Oscar or AMH.

## Why it matters

If dashboard users interpret `SETTLED` as financial completion, deleted messages could conceal unpaid or manually processed obligations. A distinct manual-payment-required indicator, ownership field, and completion reconciliation may be required.
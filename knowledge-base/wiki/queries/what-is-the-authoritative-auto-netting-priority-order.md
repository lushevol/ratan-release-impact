---
type: query
title: What Is the Authoritative Auto Netting Priority Order?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, rule-priority, rule-selection, sal]
related: [cashflow-auto-netting, netting-scenario-priority, sal-mtm-and-coupon-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md"]
---
# What Is the Authoritative Auto Netting Priority Order?

## Question

What complete order determines auto-netting rule selection when a cashflow matches multiple rules?

## Available evidence

The UAT source specifies two behaviours:

1. A rule with a higher-priority netting type should win.
2. When matching rules have the same netting type, the latest-created rule should win.

Its example expects `SAL Coupon Netting` to take precedence over `Bilateral Netting`.

## Gap

The source does not provide the full order across Bilateral, CCIL, BIC, SAL, clearing-specific, and other netting types. It also does not define whether priority is global, configurable, or dependent on rule scope.
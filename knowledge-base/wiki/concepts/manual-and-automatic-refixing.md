---
type: concept
title: Manual and Automatic Re-Fixing
created: 2026-08-24
updated: 2026-08-24
tags: [refixing, duplicate-payment-prevention, cashflows, uat]
related: [cashflow-event-control, cashflow-netting-and-auto-un-netting, cashflow-version-concurrency-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# Manual and Automatic Re-Fixing

The CN Drop 2 UAT catalogue includes separate scenarios for manual and automatic re-fixing. Each requires three consecutive fixes and verification that no duplicate payment is created.

The scenarios treat repeated fixing as a cashflow versioning and payment-generation control, not merely as a recalculation test. Correct processing should avoid duplicate payment obligations while preserving the intended current cashflow.

The source provides no execution result or implementation detail for either scenario. Further evidence should be connected to [[concepts/cashflow-netting-and-auto-un-netting]] and [[concepts/cashflow-version-concurrency-control]].
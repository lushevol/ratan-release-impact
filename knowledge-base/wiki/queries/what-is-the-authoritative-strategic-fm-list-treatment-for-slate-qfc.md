---
type: query
title: What Is the Authoritative STRATEGIC_FM_LIST Treatment for SLATE_QFC?
created: 2026-08-23
updated: 2026-08-23
tags: [strategic-fm-list, slate-qfc, cashflow-suppression, swift, configuration]
related: [cashflow-suppression-rule, cashflow-suppression-and-swift-generation, why-is-slate-one-not-configured-for-downstream-settlement-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md"]
---
# What Is the Authoritative STRATEGIC_FM_LIST Treatment for SLATE_QFC?

The source states that SWIFT generation checks `STRATEGIC_FM_LIST`, and that cashflow-suppressed `SLATE_QFC` does not need to be configured in the list. However, the only displayed row under the `STRATEGIC_FM_LIST` heading is:

`SLATE_QFC | 401081696 | SLATE ONE LLC*DOH`

## Required resolution

Confirm whether this row is:

- an active `STRATEGIC_FM_LIST` configuration;
- an exclusion or exception record;
- a stale configuration that should be removed; or
- documentation illustrating an entity that is deliberately not configured.

The resolution should identify the controlling business rule, current production state, responsible owner, and expected SWIFT-generation outcome.
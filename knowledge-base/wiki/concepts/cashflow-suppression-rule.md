---
type: concept
title: Cashflow Suppression Rule
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, suppression, settlement, uat, business-rule]
related: [qatar-slate-one-llc-doh-gbs, manual-entity-settlement-enablement, settlement-day-2, what-static-data-is-skipped-when-cashflow-is-suppressed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/003 QATAR SLATE ONE LLC DOH(GBS).md"]
---
# Cashflow Suppression Rule

A Cashflow Suppression rule is the business or system rule that determines that a cashflow should be suppressed rather than proceed through the normal settlement path.

## Role in the SLATE UAT case

For the `SLATE` cashflow associated with [[qatar-slate-one-llc-doh-gbs]], the 2026-03-23 confirmation states that:

1. The cashflow will be cashflow suppressed.
2. The remaining settlement static data is not required.
3. Only the Cashflow Suppression rule is required.

This is an entity- and cashflow-specific UAT interpretation. It is not evidence of a universal rule that all suppressed cashflows, manual entities, or Settlement Day 2 cases can omit their normal static data.

## Definition gaps

The source does not specify the rule’s identifier, trigger conditions, precedence, resulting status, audit requirements, or downstream notifications. It also does not define which static-data records or fields are included in “the rest of static.”

The distinction between intended UAT behavior and verified execution should be preserved until formal configuration or test evidence is available.
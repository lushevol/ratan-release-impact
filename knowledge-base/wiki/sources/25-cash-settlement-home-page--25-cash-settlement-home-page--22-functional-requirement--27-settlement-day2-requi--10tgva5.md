---
type: source
title: "QATAR SLATE ONE LLC DOH(GBS) UAT Confirmation"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement-day-2, manual-entities, cashflow-suppression, slate]
related: [qatar-slate-one-llc-doh-gbs, cashflow-suppression-rule, manual-entity-settlement-enablement, settlement-day-2, what-static-data-is-skipped-when-cashflow-is-suppressed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/003 QATAR SLATE ONE LLC DOH(GBS).md"]
---
# QATAR SLATE ONE LLC DOH(GBS) UAT Confirmation

## Context

This UAT clarification belongs to the [[concepts/settlement-day-2]] requirement for enabling settlement for manual entities in the [[entities/cash-settlement-home-page]].

The confirmation concerns the cashflow associated with `QATAR SLATE ONE LLC DOH(GBS)`, referred to as `SLATE`.

## Confirmed behavior

On 2026-03-23, the source records the following confirmation with Synthia:

> “Confirmed with Synthia ,SLATE cashflow will be cashflow suppressed ,then rest of static is not required. Only Cashflow Suppression rule is required.”

For this specific UAT case:

- The `SLATE` cashflow is intended to be cashflow suppressed.
- The remaining settlement static data is described as unnecessary.
- The only required configuration or rule is the Cashflow Suppression rule.

## Scope and evidence

This is a stakeholder confirmation in a UAT-testing context. It does not include test steps, expected and actual results, screenshots, logs, a rule identifier, or configuration values. The source therefore records the intended behavior and requirement interpretation, not verified production execution.

The conclusion must remain limited to the cited `SLATE` cashflow. It does not establish that all cashflows for `QATAR SLATE ONE LLC DOH(GBS)`, all manual entities, or all Settlement Day 2 scenarios may omit settlement static data.

## Open details

The source does not define:

- The static-data fields covered by “rest of static”.
- The formal identifier or precedence of the Cashflow Suppression rule.
- The conditions that trigger suppression.
- The resulting cashflow status or downstream handling.
- Whether suppression is permanent, entity-specific, cashflow-specific, or limited to this UAT scenario.
- Synthia’s role or approval authority.

See [[what-static-data-is-skipped-when-cashflow-is-suppressed]] for the unresolved static-data and rule-scope questions.
---
type: query
title: Must QATAR SLATE ONE LLC*DOH Cashflow Suppression Be Verified in UAT?
created: 2026-08-23
updated: 2026-08-23
tags: [uat, cashflow-suppression, qatar, manual-entities, configuration]
related: [qatar-slate-one-llc-doh-gbs, cashflow-suppression-rule, cashflow-suppression-and-swift-generation, why-is-slate-one-not-configured-for-downstream-settlement-processing, tranche-2-manual-entity-settlement-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# Must QATAR SLATE ONE LLC*DOH Cashflow Suppression Be Verified in UAT?

## Question

If the QATAR SLATE ONE LLC*DOH cashflow is intended to be cashflow-suppressed, what minimum UAT evidence is required, and can settlement setup or scenario execution be omitted?

## Evidence

The tracker records cashflow `S00000120444` under QATAR SLATE ONE LLC*DOH and states that Synthia mentioned it should be cashflow suppressed and may not need setup, while asking whether it should be verified during UAT.

This is stakeholder guidance recorded in a tracking sheet, not an approved configuration decision or proof that suppression is active.

## Required Clarification

Confirm the configured suppression rule, the expected downstream behavior, whether setup is intentionally excluded, and the evidence required to demonstrate that the cashflow is suppressed without unintended settlement or message processing.

## Status

Open. Link to [[queries/why-is-slate-one-not-configured-for-downstream-settlement-processing]] for the related configuration question.
---
type: query
title: Should UG Split Cashflows Trigger WHT NSTP Rules?
created: 2026-08-23
updated: 2026-08-23
tags: [uat, uganda, cashflow-splitting, withholding-tax, wht, nstp]
related: [cashflow-splitting, split-cashflow-persistence-and-lineage, tranche-2-manual-entity-settlement-uat, uganda-scb-uganda-kam-gbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# Should UG Split Cashflows Trigger WHT NSTP Rules?

## Question

Under what conditions should the UG split cashflows in the Withholding TAX case trigger a WHT NSTP rule?

## Evidence

The tracker records UG Split cash flow - Withholding TAX, case15, with cashflows `S00000121068/S00000121067`. The 2026-08-13 comment asks whether the split cashflow should hit WHT NSTP and notes that no split cashflow was observed hitting a WHT NSTP rule.

The source does not define the expected rule, eligibility conditions, static data, or whether the absence of a rule hit is a failure.

## Required Clarification

Confirm the WHT NSTP rule contract, applicable split-cashflow attributes, tax and settlement-instruction data, parent-child lineage behavior, and expected status for each cashflow. Attach rule-evaluation and downstream-processing evidence before classifying the result.

## Status

Open. The source raises a specification or configuration question; it does not establish that WHT NSTP should apply.
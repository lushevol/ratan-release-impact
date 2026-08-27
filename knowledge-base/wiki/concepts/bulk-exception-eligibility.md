---
type: concept
title: Bulk Exception Eligibility
created: 2026-08-22
updated: 2026-08-22
tags: [bulk-processing, exception-management, NSTP, maker-checker, auto-netting]
related: [hard-block-swap-agent-nstp-rule, ratan-rule-lifecycle-management, business-rule-maintenance, pending-auto-netting-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Block UAT testing.md"]
---
# Bulk Exception Eligibility

## Definition

Bulk exception eligibility determines whether a cashflow may be included in a bulk submission operation under the attributes configured on its applicable exception or NSTP rule.

## UAT Evidence

In the 2025-10-31 UAT test, a Hard Blocker NSTP rule was created with Maker Checker enabled and `Bulk Eligible` disabled. Two cashflows were selected for Bulk Submit:

- C1: `SWAP_AGENT` / `Interim MTM`, with multiple exceptions including the NSTP hard blocker after `Settle as Gross`
- C2: `SWAP_AGENT` / `Initial Notional`, with multiple exceptions but no NSTP hard blocker

The observed result was that C1 was not eligible to submit. The document does not specify the final disposition of C2.

## Boundary

Bulk submission does not override the disabled `Bulk Eligible` setting for the tested hard-blocked cashflow. The evidence does not establish whether other cashflows in the same selection are independently submitted, rejected with the batch, or left unchanged.
---
type: query
title: Should NDS Fixing Netting Follow the IRS Resultant-Cashflow Rule?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, NDS-fixing, IRS-netting, resultant-cashflow, lifecycle]
related: [nds-product-scope-netting, irs-resultant-cashflow-netting, netting-resultant-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting.md"]
---
# Should NDS Fixing Netting Follow the IRS Resultant-Cashflow Rule?

## Question

Should `NDS Fixing Netting` receive the same resultant-cashflow pre-check and pending-netting withdrawal restriction proposed for `IRS Netting`?

## Evidence

The source explicitly raises this question after describing the `IRS Netting` exception and lifecycle change, but provides no decision or acceptance criteria. `NDS Fixing` is included in the NDS product-scope typology list, but that inclusion does not establish equivalent resultant-cashflow behavior.

## Required Resolution

The decision should compare the lifecycle, booking, settlement, and workflow characteristics of `NDS Fixing Netting` with `IRS Netting`. It should specify whether the rule is shared, adapted, or excluded, and identify the relevant `Murex 2.11` and `Stella` support scope.
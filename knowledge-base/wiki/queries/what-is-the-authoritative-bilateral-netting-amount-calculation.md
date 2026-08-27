---
type: query
title: What Is the Authoritative Bilateral Netting Amount Calculation?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bilateral-netting, amount-calculation, open-question]
related: [bilateral-netting, netting-resultant-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# What Is the Authoritative Bilateral Netting Amount Calculation?

The requirement repeatedly states that the resultant amount must be correct but does not define the calculation.

## Questions

- Is the resultant the signed sum of component amounts?
- How are debit and credit directions represented?
- Are mixed-sign, zero, or partially cancelled components supported?
- Are rounding and currency precision applied before or after aggregation?
- Is the amount validated against an external system?

A confirmed formula is required before the amount assertion can be implemented as a complete acceptance rule.
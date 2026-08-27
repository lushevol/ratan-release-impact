---
type: concept
title: Netting Resultant Settlement Method Selection
created: 2026-08-23
updated: 2026-08-23
tags: [netting, resultant-cashflow, settlement-method, gross, DVP, CCIL]
related: [netting-resultant-cashflow, cashflow-netting, ccil, what-is-the-authoritative-settlement-method-precedence-for-netting-resultants]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# Netting Resultant Settlement Method Selection

The netting requirement describes the resultant settlement method as hard-coded `Gross`, but includes two conditional exceptions:

- Use `DVP` if any component cashflow has `DVP`.
- Use `CCIL` for IRS Netting.

The source does not state precedence when both conditions could apply, nor does it define whether the conditions are evaluated before or after any other resultant-generation rules.

Until resolved, this should not be implemented as an unqualified `Gross` default. See [[what-is-the-authoritative-settlement-method-precedence-for-netting-resultants]].
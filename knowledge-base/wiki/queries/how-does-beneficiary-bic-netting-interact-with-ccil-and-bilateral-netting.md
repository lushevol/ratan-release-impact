---
type: query
title: How Does Beneficiary BIC Netting Interact with CCIL and Bilateral Netting?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, beneficiary-bic, ccil, bilateral-netting, eligibility]
related: [beneficiary-bic-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md"]
---
# How Does Beneficiary BIC Netting Interact with CCIL and Bilateral Netting?

## Question

Are Beneficiary BIC Netting, CCIL Netting, and Bilateral Netting mutually exclusive, and what eligibility and precedence rule applies when a cashflow qualifies for more than one mode?

## Evidence

The source requires segregation between Beneficiary BIC Netting and CCIL Netting/Bilateral Netting. It does not define segregation at an implementation level.

## Required decision outputs

- Whether netting modes are mutually exclusive.
- Priority order where multiple eligibility rules match.
- Whether users may choose a mode.
- Queue, status, and resultant identity boundaries by mode.
- Static-data and authorization boundaries.
- Behavior for already queued or partially selected cashflows when eligibility changes.
---
type: concept
title: NDIRS CNY Leg Mapping
created: 2026-08-24
updated: 2026-08-24
tags: [ndirs, cny, irs, ratan, cashflow-mapping, cortex]
related: [irs, ratan, cortex, cashflow-netting-and-auto-un-netting, murex-ratan-cashflow-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# NDIRS CNY Leg Mapping

The UAT issue register records a pending mapping issue for NDIRS booked as a CNY fixed-floating IRS. For trade `4348263238`, both legs flowed into RATAN as USD Coupon/float rather than being represented with the expected CNY-specific leg or currency mapping.

The issue is described as a possible enhancement in [[entities/cortex]], but the source does not establish whether the correction belongs in Cortex, RATAN, upstream Murex configuration, or another component.

This is a trade-specific finding. It should not be generalized to all IRS or all NDIRS cashflows. Confirmation of the authoritative mapping remains an open question.
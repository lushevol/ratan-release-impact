---
type: entity
title: Cortex
created: 2026-08-22
updated: 2026-08-23
tags: [cortex, delivery-events, nd-rates, cashflows, global-rates, ndirs, cny, cashflow-mapping, enhancement]
related: [ratan, nd-delivery-currency-cashflow-model, fmrp, ndirs-cny-leg-mapping, irs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# Cortex

## Non-deliverable Rates delivery events

According to *Global Rates - Settlement Strategy Process & Dependency*, Cortex is identified as a trade or event source for non-deliverable Rates products. The stated target approach is for delivery events from Cortex to be sent in the delivery currency, after which subsequent cashflows are created.

The source does not decide whether conversion occurs within the same trade or through a separate conversion trade.

## NDIRS CNY fixed-floating IRS mapping

According to *CN Drop 2 UAT - Settlements Scenarios - 2024*, Cortex is named as a possible enhancement area for an NDIRS CNY fixed-floating IRS mapping issue. The issue concerns trade `4348263238`, whose two legs flowed into [[RATAN]] as USD Coupon/float.

That source does not confirm that Cortex owns the mapping or that a Cortex change was implemented. The authoritative correction point remains unresolved.
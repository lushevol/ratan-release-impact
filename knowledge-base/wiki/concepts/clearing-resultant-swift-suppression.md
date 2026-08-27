---
type: concept
title: Clearing Resultant SWIFT Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [clearing, swift, suppression, auto-netting, resultant-cashflow]
related: [swift-versus-cashflow-suppression, cashflow-auto-netting, sal-mtm-and-coupon-auto-netting, are-clearing-resultant-swift-suppression-rules-active]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md"]
---
# Clearing Resultant SWIFT Suppression

Clearing resultant SWIFT suppression is a documented UAT/static-configuration pattern for selected clearing counterparties and auto-netting outputs. It applies only where the named rule conditions match.

## Documented scope

The source records intended suppression configuration for:

- LCH, through an update from rule `7351244948348235776` to `7351891133699129344`;
- CME, EUREX, JSCC, and ICE, through new rule `7355932145617928192` and post-rule ID `7356611640855298048`;
- SAL MTM and Coupon resultants or eligible single cashflows, through rule `7351885393248022528`;
- SCH IRS and option scenarios, through rules `7356241418356981760` and `7356241729352040448`.

The clearing rules use populated `Cashflow__Netting_Id` to identify resultants and additionally include certain auto-netting single-cashflow cases.

## Predicate correction

For CME, EUREX, JSCC, and ICE, the documented correct predicate uses:

```text
Entity__Counterparty_SCI_FMID in ("400902327", "400923856", "400947070", "400971369")
```

The source marks an equality comparison against the comma-delimited string as wrong:

```text
Entity__Counterparty_SCI_FMID == "400902327,400923856,400947070,400971369"
```

The latter cannot match an individual FMID and therefore represents a material configuration defect.

## Status limitation

All cited suppression-rule status fields are blank. The source establishes intended rules and a correction requirement, but does not prove approval, deployment, or effective runtime suppression. See [[are-clearing-resultant-swift-suppression-rules-active]].
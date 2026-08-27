---
type: entity
title: ratan-cash-settlement-netting
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, netting, cash-settlement, fmrp-uber]
related: [ratan, chg1016055, fmrp-uber, auto-netting, rule-engine-trade-attributes, release-rollback-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# ratan-cash-settlement-netting

`ratan-cash-settlement-netting` is the RATAN service responsible for netting-related processing in [[chg1016055]].

## Release Artifact

- Deployment step: `5`
- Active branch: `release/v3.0.14`
- Package: `3.0.14-20260723.3`
- Pipeline run: `20260723.3`
- Owner: Yonghua Li
- Rollback: recorded as existing

## Scope

The package adds ten [[fmrp-uber]] trade fields for rule checks. The source also instructs operators to restart the netting service after auto-netting configuration ID `9` is introduced through the database deployment.

## Release-Train Note

The source strikes through `release/v3.1.2` and identifies `release/v3.0.14` as current. It states that the package was merged with `main` and the 2026-07-25 BAU release, while BAU changes were to be rolled back.

No explicit explanation for the lower-numbered release branch is provided.
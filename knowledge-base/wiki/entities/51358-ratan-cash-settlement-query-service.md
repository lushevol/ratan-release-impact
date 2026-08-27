---
type: entity
title: 51358-ratan-cash-settlement-query-service
created: 2026-08-22
updated: 2026-08-23
tags: [ratan, query-service, tis, fmrp-uber, service, indonesia, cash-settlement, api-migration]
related: [ratan, chg1016055, fmrp-uber, rule-engine-trade-attributes, release-rollback-readiness, 51358-ratanone-query-service, audit-trail, cash-settlement-audit-api-migration, which-service-owns-id-eslogging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Audit API migration plan from GDC to ID.md"]
---
# 51358-ratan-cash-settlement-query-service

`51358-ratan-cash-settlement-query-service` is a RATAN backend query service included in [[chg1016055]].

According to the Indonesia Audit API migration plan, it is the intended Indonesia service location for migrated Custom Search/View APIs.

## Release Artifact

The release-plan source records the following artifact details:

- Deployment step: `5`
- Active branch: `release/v4.3.2`
- Package: `4.3.2-20260723.1`
- Pipeline run: `20260723.1`
- Owner: Chen Yang
- Rollback: recorded as existing

## Release Scope

According to the release-plan source, the service scope includes:

- TIS API integration.
- New [[fmrp-uber]] fields.
- Performance-testing-related changes.

## Indonesia Audit API Migration

According to the Indonesia Audit API migration plan, this service is directed to implement:

- `/v2/customview/filters`
- `/v2/customview/views`

The same migration-plan source names this service in the Indonesia-location column for `/v1/esLogging`, but does not confirm it as that API's final owner. That source separately proposes [[audit-trail]] for Indonesia frontend error logs and leaves the ownership choice open.

See [[cash-settlement-audit-api-migration]] and [[which-service-owns-id-eslogging]].

## Release-Train Note

The release-plan source strikes through `release/v4.3.6` and package `4.3.6-20260721.9`, replacing them with the numerically lower `release/v4.3.2` and `4.3.2-20260723.1`.

That source states that the package was merged with `main` and the 2026-07-25 BAU release associated with `CHG1030738`, with an instruction to roll back BAU changes. It does not explain whether the lower version reflects branch strategy, dependency alignment, or a functional downgrade.
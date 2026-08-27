---
type: comparison
title: Group Enrichment Versus TDS3 Lookup for SSI Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [SSI-stamping, architecture, CCY-Pair, TDS3, group-management]
related: [group-management-service, ssi-stamping-service, tds3, group-ready-ccy-pair-enrichment, ccy-pair-based-nostro-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Group Enrichment Versus TDS3 Lookup for SSI Stamping

The source presents two unapproved alternatives for making `CCY Pair` available to SSI stamping.

| Criterion | Option 1: Group management enrichment | Option 2: TDS3 lookup |
|---|---|---|
| Change scope | Changes Group Management Service and SSI Stamping Service | Changes SSI Stamping Service |
| Data path | Group service enriches the value; SSI stamping extracts it from SCBML | SSI stamping queries TDS3 for `Currency_Pair` |
| Runtime dependency | Depends on group readiness and complete group data | Depends on a runtime TDS3 lookup |
| Performance | Implied to be better because no TDS3 lookup is needed during SSI stamping | Expected to degrade because of the TDS3 lookup |
| Incomplete-group behavior | A manually delivered incomplete group may not be enriched | Avoids waiting for another leg or group enrichment |
| Operational risks | Requires missing-pair and incomplete-group handling | Requires latency, timeout, and lookup-failure handling |
| Database change | None expected | None expected |

The source does not select either option. A decision should be recorded only after the missing-data, fallback, replay, and performance requirements are defined.
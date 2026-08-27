---
type: source
title: RATAN Application Documentation Register
authors: []
year: 2026
url: ""
venue: "Internal RATAN documentation register"
tags: [ratan, application-documentation, service-governance, operational-documentation]
related: [ratan, ratanone, application-documentation-set, ratan-service-governance, ratan-user-guide-segmentation, ratan-operational-resilience-plans, ratan-test-environment-specification, canonical-ratan-ratanone-service-identity]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -App Docs/RATAN -App Docs.md"]
---
# RATAN Application Documentation Register

## Summary

This document is an index of formal documentation associated with the RATAN application and service. It links architecture or service-management material, user guides, service and operational agreements, recovery and restoration plans, a capacity-management plan, and a test-environment specification.

The register provides evidence that RATAN is supported by a multi-layer documentation and governance framework. It does not reproduce the linked documents and therefore does not establish specific service-level targets, operational ownership, recovery objectives, capacity thresholds, test-environment characteristics, or current document status.

## Documentation coverage

The user documentation is divided by functional or regional context:

- **Settlement:** `User manual - RATAN`
- **Korea:** `Ratan One Processing Guide(DOI)-Korea`
- **Trade:** `2-User Guideline`

The operational documentation is separated into service-level, operational-level, disaster-recovery, restoration, capacity-management, and test-environment artifacts.

## Source register

| Document Type | Link |
| --- | --- |
| ASRM | [ASRM - RATAN](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=1592289045) |
| User Guide | Settlement : [User manual - RATAN](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2863770766) Korea: [Ratan One Processing Guide(DOI)-Korea - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Ratan+One+Processing+Guide%28DOI%29-Korea) Trade : [2-User Guideline - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/2-User+Guideline) |
| SLA | [SLA - RATAN](https://teamsites.zone1.scb.net/sites/sm/Lists/SLA%20List/All%20Items.aspx#InplviewHashd674effe-f354-4677-b494-29ad45ddc0f4=SortField%3DDocument_x0020_Review_x0020_Due_-SortDir%3DAsc-FilterField1%3DTechnology%255Fx0020%255FService%255Fx0020%255FM-FilterValue1%3DZou%252C%2520Gevin-FilterField2%3DProduction%255Fx002f%255FDecomm-FilterValue2%3DProduction) |
| OLAs | [08 - OLA - RATAN](https://confluence.global.standardchartered.com/display/PSS/08+-+OLA+-+RATAN+ONE) |
| Service Recovery Plan(DR) | [RATAN (51358) Recovery (DR) Plan [PLAN-16314]](https://onepoint.global.standardchartered.com/ui/form/mid=102767&pid=72795704&iid=528748105) |
| Service Restore Plan | [RATAN (51358) Restore Plan [PLAN-16315]](https://onepoint.global.standardchartered.com/ui/form/mid=102767&pid=75608234&iid=528747392/flag%3D1%26emd%3D1%26obj_id%3DPLAN-16315%26action_type%3DUPDATE%26mode%3Dview) |
| Capacity Plan | [RATAN (51358) Capacity Management Plan [PLAN-16312]](https://onepoint.global.standardchartered.com/ui/form/mid=102767&pid=75441175&iid=526477139/flag%3D1%26emd%3D1%26obj_id%3DPLAN-16312%26action_type%3DUPDATE%26mode%3Dview) |
| Test Environment Spec | [Ratan Application Test Environment Specifications - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Ratan+Application+Test+Environment+Specifications) |

## Relationship to existing RATAN material

This register adds a service-governance view to the existing technical documentation around [[ratanone]], [[ratanone-settlement-orchestration-service]], cash settlement, Korea processing, and trade-information sourcing.

Relevant existing material includes:

- [[trade-information-sourcing-for-cash-settlement]]
- [[korea-cashflow-migration]]
- [[korea-tlm-accounting-reconciliation]]
- [[cash-settlement-database-retention-and-housekeeping]]

The register does not independently confirm or contradict implementation claims in those technical sources.

## Evidence limitations and open points

The source does not state:

- The meaning of `ASRM`
- Whether RATAN, RATAN ONE, and RatanOne are identical services or different scopes
- Document owners, versions, review dates, or effective dates
- SLA targets or OLA responsibilities
- Recovery time objectives, recovery point objectives, or restoration procedures
- Capacity thresholds, monitoring requirements, or planning horizons
- Test-environment names, topology, dependencies, data requirements, or refresh procedures

The service identifier `51358` appears in the recovery, restore, and capacity-management records. Its relationship to the canonical [[ratan]] or [[ratanone]] service identity requires verification.

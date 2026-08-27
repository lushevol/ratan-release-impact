---
type: source
title: Indonesia Development Integration Plan
authors: []
year: 2026
url: ""
venue: Internal implementation plan
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, ratan, onshoring, integration, release-readiness, uat, gdc]
related: [ratan-indonesia-onshoring-2026, indonesia-environment-readiness-dependencies, indonesia-hybrid-gdc-id-message-flow, ratanone-message-bridge, ratan-cash-settlement-batch-service, what-is-the-approved-indonesia-gdc-id-message-processing-topology, what-is-the-approved-indonesia-folder-route-type-policy, what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# Indonesia Development Integration Plan

This is an Indonesia RATAN Cash Settlement implementation and release-readiness tracker. It records planned infrastructure, platform, integration, frontend, QA, CI/CD, and UAT deployment activities. It is not an approved target-state architecture or evidence that production readiness, UAT deployment, or testing has completed.

The plan supports [[ratan-indonesia-onshoring-2026]] and describes a hybrid arrangement: batch and MXG-adaptor processing remain GDC-only, while Netting is described as ID-driven. The stated status snapshot shows API gateway regional validation and gateway/auth-server combination work as in progress in Dev; most integration, frontend, and QA activities are marked `NOT START` or have no recorded completion status.

## Planning interpretation

- VIP is a prerequisite for DNS and firewall work.
- PostgreSQL setup is a prerequisite for the stated HashiCorp database-account integration.
- Foundation setup precedes service properties and service deployment.
- Nginx administration depends on an ADO pipeline.
- NAS, FileIT, GDC Kafka synchronization, and the DR solution remain unresolved.
- The plan records an in-progress “API gateway and auth server combination,” but does not establish that the deprecated combined architecture is approved or reinstated.
- The UAT service list identifies intended release composition for work item `15018293`; blank UAT and ID Staging deployment-status fields do not confirm deployment or testing.
- Some branch and version fields appear malformed or inconsistent and require repository verification before use as authoritative release records.

## Development Plan — Production Readiness

| | Category | Task Description | Owner | Nginx LB server Status | App Server Status | Request CR/Detail Infomation | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DevOps | Infra – VIP | @Zeyu Zhou | | | | discuss with nginx team |
| 2 | Infra – DNS (Depends on VIP) | @Zeyu Zhou | server DNS manifest (in progressing, web team working) | app server DNS not require | | |
| 3 | Infra – Firewall (Depends on VIP) | @Zeyu Zhou | | | | if other server visit us, use our own nginx or the lb nginx |
| 4 | Infra – SSL cert, Keystore & truststore? | @Zeyu Zhou | | app server ssl not start | | |
| 5 | Infra – NAS | @Zeyu Zhou | | | | wait after OAT, is fileIT still depends on NAS? data sync on GDC Kafka needed? pending on DR solution. |
| 6 | foundation setup – PG | @Zeyu Zhou | - | | | waiting for SAT/OAT stop, account setup |
| 7 | Auth – Hashicorp integration | @Zeyu Zhou | - | | | only db account, waiting for PG setup |
| 8 | foundation setup – Redis(manual) | @Zeyu Zhou | - | | | |
| 9 | foundation setup – Kafka(manual) | @Zeyu Zhou | - | | | |
| 10 | foundation setup – ELK(manual) | @Zeyu Zhou | - | | | |
| 11 | foundation setup – Nginx | @Zeyu Zhou | - | | | lb ansible |
| 12 | Service deployment | @Zeyu Zhou | - | | | |
| 13 | Generic service account creation | | - | | | |
| 14 | Entra integration (FMAA) ? not now | @Zeyu Zhou | - | | | |
| 15 | ADO – CICD get ready for both foundation component and microservices | @Zeyu Zhou | - | | | |
| 16 | BE dev | New solace topic + queue for Murex cashflow inbound | @Xinmiao Huang @Junli Gao | | | | |
| 17 | SSI+ engagement for new solace queue creation | @Xinmiao Huang | | | | |
| 18 | RDM FileIT engagement | @Xinmiao Huang | | | | |
| 19 | RDM real time message solace queue creation | @Xinmiao Huang | | | | |
| 20 | Service properties setup (depends on foundation setup ready) | @Xinmiao Huang | | | | |
| 21 | API gateway development – region validation | @Xinmiao Huang | | | | |
| 22 | API gateway and auth server combination | @Xinmiao Huang | | | | |

## Development Plan — Non-Production Readiness

| | Category | Task Description | Owner | Dev Status | UAT Status | Staging Status | Man day | Request CR/Detail Infomation | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DevOps | Infra – VIP | @Zeyu Zhou | | | | 15 | https://scbnow01.service-now.com/onesc?id=ticket&table=sc_req_item&sys_id=b0780dc12b9c4b90c570febbec91bf0e&view=sp | |
| 2 | Infra – DNS (Depends on VIP) | @Zeyu Zhou | | | | 15 | | |
| 3 | Infra – Firewall (Depends on VIP) | @Zeyu Zhou | | | | 15 | | |
| 4 | Infra – SSL cert, Keystore & truststore? | @Zeyu Zhou | | | | 15 | | |
| 5 | Infra – NAS | @Zeyu Zhou | | | | TBC | | |
| 6 | foundation setup – PG | @Zeyu Zhou | | | | | | |
| 7 | Auth – Hashicorp integration | @Zeyu Zhou | | | | | DEV： My Request - RITM4503433 - oneSC; UAT： STG： | |
| 8 | foundation setup – Redis(manual) | @Zeyu Zhou | | | | | | |
| 9 | foundation setup – Kafka(manual) | @Zeyu Zhou | | | | 2 | | |
| 10 | foundation setup – ELK(manual) | @Zeyu Zhou | | | | 2 | | |
| 11 | foundation setup – Nginx | @Zeyu Zhou | | | | TBC | | depends Nginx admin account depends on ado pipeline |
| 12 | foundation setup – prometheus + grafana | @Zeyu Zhou | | | | 2 | | |
| 13 | Service deployment | @Zeyu Zhou | | | | TBC | | Depends on foundation setup |
| 14 | Generic service account creation | | | | | | | reuse GDC account |
| 15 | Entra integration (FMAA) ? not now | @Zeyu Zhou | | | | | | need to check whether need to add our hostname to their truststore |
| 16 | ADO – CICD get ready for both foundation component and microservices | @Zeyu Zhou | | | | | | |
| 17 | BE dev | New solace topic + queue for Murex cashflow inbound | @Xinmiao Huang @Junli Gao | NOT START | NOT START | NOT START | | | |
| 18 | SSI+ engagement for new solace queue creation | @Xinmiao Huang | NOT START | NOT START | NOT START | | | |
| 19 | RDM FileIT engagement | @Xinmiao Huang | NOT START | NOT START | NOT START | | | |
| 20 | RDM real time message solace queue creation | @Xinmiao Huang | NOT START | NOT START | NOT START | | | |
| 21 | Service properties setup (depends on foundation setup ready) | @Xinmiao Huang | NOT START | NOT START | NOT START | | | |
| 22 | API gateway development – region validation | @Xinmiao Huang | IN PROGRESS | NOT REQUIRED | NOT REQUIRED | | | |
| 23 | API gateway and auth server combination | @Xinmiao Huang | IN PROGRESS | NOT REQUIRED | NOT REQUIRED | | | |
| 24 | FE dev | UX design | @Guiling Wang | NOT START | NOT START | NOT START | | | involve Tech and Anbur, Geoffrey will head up first. |
| 25 | Routing logic development | @Guiling Wang | NOT START | NOT START | NOT START | | | |
| 26 | QA | Integration Testing | TBC | NOT START | NOT START | NOT START | | | |
| 27 | Regression Testing | TBC | NOT START | NOT START | NOT START | | | |
| 28 | Performance Testing | TBC | NOT START | NOT START | NOT START | | | |

## UAT service install list — material Indonesia-specific entries

Release work item: `15018293` — RATAN Settlement Onshore dummy release WI.

| # | Services | Has Code Change | GDC deploy dependency | ID Release branch | pom version(defined by caroline) | prod version | ID STG Version | UAT deploy Owner | ID STG deploy status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ratan-service-properties-indonesia | No | | | | | 20260525.8 | | |
| 2 | ratanone-eureka-server | No | | release/v3.1.1 | | | 3.0.1-20240830.3 | | |
| 3 | ratanone-config-server | No | | release/v3.1.1 | | | 3.0.1-20240830.3 | | |
| 4 | ratanone-api-gateway | No | | release/v3.1.2 | | | 3.0.2-20250901.2 | | |
| 5 | ratan-exception-platform | No | | release/v3.7.7 | | | 3.6.7-20260520.4 | | |
| 6 | ratanone-auth-server | No | | release/v3.1.7 | | | 3.0.7-20260326.4 | | |
| 7 | ratanone-message-event | No | | release/v3.2.1 | | | 3.1.1-20251017.12 | | |
| 8 | ratanone-rule-service | No | | release/v2.5.9 | | | 2.4.9-20260610.2 | | |
| 9 | ratanone-static-data-service | No | | release/v4.3.4 (linked target `release/v4.2.4`) | | | 4.2.4-20260522.5 | | |
| 10 | ratanone-audit-trial | Yes, eslog and change es key in yml | Not mandatory | release/v3.2.0 （base on feature/main_260618_es） | 3.2.0 | 3.1.2-20241115.6 | 3.1.2-20260709.2 | | |
| 11 | ratan-cash-settlement-orchestration | No | | release/v4.2.0 （base on feature/upgrade_version_260717） | 4.2.0 | | 4.1.4-20260629.1 | | |
| 12 | ratan-cash-settlement-accounting-service | No | | release/v2.3.0 （base on feature/upgrade_version_260717） | 2.3.0 | | 2.1.0-20260525.1 | | |
| 13 | ratan-cashflow-lifecycle-service | No | | release/v4.2.0 （base on feature/upgrade_version_260717) | 4.2.0 | | 4.1.4-20260630.3 | | |
| 14 | ratan-cash-settlement-fx-utilization-service | No | | release/v2.1.0 （base on feature/upgrade_version_260717） | 2.1.0 | | 2.0.0-20260525.2 | | |
| 15 | ratan-cash-settlement-group-management-service | yes, status write back | Not mandatory | release/v3.3.0 （base on feature/id_ack260609) | 3.3.0 | 3.0.8-20260522.5 | 3.2.3-20260617.1 | | |
| 16 | ratan-cash-settlement-lms-service | yes, decouple adaptor trade | Not mandatory | release/v4.1.0 （base on feature/main_260615_removeTradeQuery | 4.1.0 | 4.0.2-20260408.3 | 4.0.2-20260709.1 | | |
| 17 | ratan-cash-settlement-netting-service | Yes, resultant cf id prefix | Not mandatory | release/v4.1.0 （base on feature/v4.0.0-260601-prefix) | 4.1.0 | 4.0.0-20260519.11 | 3.0.10-20260601.1 | | |
| 18 | ratan-cash-settlement-query-service | yes, filter & view query | Not mandatory | release/v4.4.0.0; feature/ID_pipeline_enabling | | 4.3.0-20260618.2 | 4.3.0-20260710.2 | | |
| 19 | ratan-cash-settlement-ssi-stamping-service | No | | release/v4.4.0.0 （base on feature/upgrade_version_260807） | | 4.2.1-20260624.1 | 4.2.1-20260624.1 | | |
| 20 | ratanone-data-ambassador | No | | release/v4.0.0.0 （base on feature/upgrade_version_260807） | | 3.9.2-20260630.4 | 3.9.2-20260630.4 | | |
| 21 | ratanone-swift-service | No | | release/v4.4.0.0 wi （base on feature/upgrade_version_260807） | | 4.2.1-20260623.3 | 4.2.1-20260623.3 | | |
| 22 | ratan-rule-service | No | | release/v3.3.0.0 feature/upgrade_version_260807 | | 3.1.5-20260522.8 | 3.1.5-20260522.8 | | |
| 23 | ratanone-message-bridge | No | Mandatory | release/v5.1.0.0 feature/upgrade_version_260807 | | 5.0.5-20260604.2 | 5.0.5-20260604.2 | | |
| 24 | ratan-central-monitoring | | | release/v1.0.0 | | | 1.0.0-20250606.3 | | |
| 25 | 51358-ratanone-ansible | NA | | | NA | NA | NA | | NA |
| 26 | 51358-mfe-admin-module | Yes, add ID route & tiles | | release/v1.2.3 | | | | | |
| 27 | 51358-mfe-base | Yes, add ID handle for api | | release/v2.2.1 | | | | | |
| 28 | 51358-mfe-container | Yes, add prefix for url, add route for ID, enhance global style | | release/v1.8.14 | | | | | |
| 29 | 51358-mfe-cashflow-blotter | Yes, add prefix for url, add route for ID, booking entity fmid in drop down list should only include ID | | release/v1.45.1 | | | | | |
| 30 | 51358-mfe-nostro-static | Yes, add prefix for url, add route for ID | | release/v1.2.6 | | | | | |
| 31 | 51358-mfe-rules | Yes, add prefix for url, add route for ID | | release/v1.11.3 | | | | | |
| 32 | 51358-mfe-trades | Yes, support redirect to GDC and ID based on trade booking entity | | release/v1.16.4 | | | | | |
| 33 | 51358-ratan-cash-settlement-batch-service | Yes, Fixing flag changes | Mandatory | release/v2.1.0 | | 2.0.0-20260326.4 | 2.0.1-20260703.1 | @Haolin Song | |
| 34 | 51358-ratanone-stella-ambassador | | | release/v3.4.0 | | 3.2.13-20260408.2 | 3.2.13-20260408.2 | | |
| 35 | 51358-ratan-mxg-cashflow-adaptor | yes | Only GDC, | | | | | @Haolin Song | |

## Message Bridge Flow Definition

```text
GDC Existing

GDC Changes

Code change:

Batch (GDC only)

1. need to publish message to another topic Cash_Settlement_Mxg_Inbound_Batch_All for message bridge to consume.
2. ID doesn't have this service deployed

Netting (ID drive)

1. Netting resultant cashflow id prefix
2. Splitting resultant cashflow id prefix

Indonesia Flow Definition

Question: Whether need to keep folder route type?
```

## Open issues

See [[what-is-the-approved-indonesia-gdc-id-message-processing-topology]] for the missing steady-state topology, data movement, ordering, deduplication, recovery, and ownership rules. See [[what-is-the-approved-indonesia-folder-route-type-policy]] for the unresolved routing question and [[what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia]] for the unspecified cashflow-ID prefix contract.
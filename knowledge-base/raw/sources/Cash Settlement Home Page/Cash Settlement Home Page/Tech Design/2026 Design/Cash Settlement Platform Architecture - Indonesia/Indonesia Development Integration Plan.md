#

# ADO task list

[ID tasks - Boards](https://dev.azure.com/sc-ado/FMQPR/_queries/query/6ed268c6-16e8-4272-af93-3ea129e6029c/)

# Development Plan(Prod Readiness)

<details>
<summary>Expand Details</summary>

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

</details>

# Development Plan(Non-Prod Readiness)

Refer to ADO: [RATAN Settlement Indonesia Onshore (SQUAD) Onshore Sprint 2 Taskboard - Boards](https://dev.azure.com/sc-ado/FMQPR/_sprints/taskboard/RATAN%20Settlement%20Indonesia%20Onshore%20(SQUAD)/FMQPR/RATAN%20Settlement%20Indonesia%20Onshore%20(SQUAD)/Onshore%20Sprint%202)

<details>
<summary>Expand Details</summary>

| | Category | Task Description | Owner | Dev Status | UAT Status | Staging Status | Man day | Request CR/Detail Infomation | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DevOps | Infra – VIP | @Zeyu Zhou | | | | 15 | [https://scbnow01.service-now.com/onesc?id=ticket&table=sc_req_item&sys_id=b0780dc12b9c4b90c570febbec91bf0e&view=sp](https://scbnow01.service-now.com/onesc?id=ticket&table=sc_req_item&sys_id=b0780dc12b9c4b90c570febbec91bf0e&view=sp) | |
| 2 | Infra – DNS (Depends on VIP) | @Zeyu Zhou | | | | 15 | | |
| 3 | Infra – Firewall (Depends on VIP) | @Zeyu Zhou | | | | 15 | | |
| 4 | Infra – SSL cert, Keystore & truststore? | @Zeyu Zhou | | | | 15 | | |
| 5 | Infra – NAS | @Zeyu Zhou | | | | TBC | | |
| 6 | foundation setup – PG | @Zeyu Zhou | | | | | | |
| 7 | Auth – Hashicorp integration | @Zeyu Zhou | | | | | DEV： [My Request - RITM4503433 - oneSC](https://scbnow01.service-now.com/onesc?id=ticket&table=sc_req_item&sys_id=4830245ffbc6b6545054f8225eefdca2&view=sp) UAT： STG： | |
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

</details>

# Surrounding System Integration Plan

[Cash Settlement Platform Architecture - Indonesia - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+Platform+Architecture+-+Indonesia#CashSettlementPlatformArchitectureIndonesia-SurroundingSystemIntegration)

# Services Install List(for UAT)

Release WI: [Release **15018293** RATAN Settlement Onshore dummy release wi](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15018293)

| | Services | Has Code Change | GDC deploy dependency | ID Release branch | Sync main Date | pom version(defined by caroline) | prod version | ID STG Version | Pipeline/PR | UAT deploy Owner | ID STG deploy status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ratan-service-properties-indonesia | No | | | | | | 20260525.8 | | | |
| 2 | ratanone-eureka-server | No | | [release/v3.1.1](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-eureka-server?version=GBrelease/v3.1.1) | | | | 3.0.1-20240830.3 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-eureka-server/pullrequest/3061812](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-eureka-server/pullrequest/3061812) | | |
| 3 | ratanone-config-server | No | | [release/v3.1.1](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-config-server?version=GBrelease/v3.1.1) | | | | 3.0.1-20240830.3 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-config-server/pullrequest/3061929](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-config-server/pullrequest/3061929) | | |
| 4 | ratanone-api-gateway | No | | [release/v3.1.2](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-api-gateway?version=GBrelease/v3.1.2) | | | | 3.0.2-20250901.2 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-api-gateway/pullrequest/3061964](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-api-gateway/pullrequest/3061964) | | |
| 5 | ratan-exception-platform | No | | [release/v3.7.7](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-exception-platform?version=GBrelease/v3.7.7) | | | | 3.6.7-20260520.4 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-exception-platform/pullrequest/3061983](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-exception-platform/pullrequest/3061983) | | |
| 6 | ratanone-auth-server | No | | [release/v3.1.7](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-auth-server?version=GBrelease/v3.1.7) | | | | 3.0.7-20260326.4 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-auth-server/pullrequest/3062008](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-auth-server/pullrequest/3062008) | | |
| 7 | ratanone-message-event | No | | [release/v3.2.1](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-message-event?version=GBrelease/v3.2.1) | | | | 3.1.1-20251017.12 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-message-event/pullrequest/3062142](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-message-event/pullrequest/3062142) | | |
| 8 | ratanone-rule-service | No | | [release/v2.5.9](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-rule-service?version=GBrelease/v2.5.9) | | | | 2.4.9-20260610.2 | [https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-rule-service/pullrequest/3062224](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-rule-service/pullrequest/3062224) | | |
| 9 | ratanone-static-data-service | No | | [release/v4.3.4](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-static-data-service?version=GBrelease/v4.2.4) | | | | 4.2.4-20260522.5 | [Pull request 3196468: ID ADO update - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-static-data-service/pullrequest/3196468) | | |
| 10 | ratanone-audit-trial | Yes, eslog and change es key in yml | Not mandatory | [release/v3.](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-audit-trial?version=GBrelease/v3.3.4_t1)2.0 （base on feature/main_260618_es） | no change ~~[Pipelines - Run 20260806.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14077880&view=results)~~ [Pipelines - Run 20260807.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14093863&view=results) | 3.2.0 | 3.1.2-20241115.6 | 3.1.2-20260709.2 | | | |
| 11 | ratan-cash-settlement-orchestration | No | | release/v4.2.0 （base on feature/upgrade_version_260717） | no change [Pipelines - Run 20260806.5](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14079055&view=results) | 4.2.0 | | 4.1.4-20260629.1 | | | |
| 12 | ratan-cash-settlement-accounting-service | No | | release/v2.3.0 （base on feature/upgrade_version_260717） | changed [Pipelines - Run 20260806.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14080007&view=results) | 2.3.0 | | 2.1.0-20260525.1 | | | |
| 13 | ratan-cashflow-lifecycle-service | No | | release/v4.2.0 （base on feature/upgrade_version_260717) | changed [Pipelines - Run 20260806.2](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14089429&view=results) | 4.2.0 | | 4.1.4-20260630.3 | | | |
| 14 | ratan-cash-settlement-fx-utilization-service | No | | release/v2.1.0 （base on feature/upgrade_version_260717） | no change [Pipelines - Run 20260806.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14079421&view=results) | 2.1.0 | | 2.0.0-20260525.2 | | | |
| 15 | ratan-cash-settlement-group-management-service | yes, status write back | Not mandatory | release/v3.3.0 （base on feature/id_ack260609) | changed [Pipelines - Run 20260806.2](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14089633&view=results) | 3.3.0 | 3.0.8-20260522.5 | 3.2.3-20260617.1 | | | |
| 16 | ratan-cash-settlement-lms-service | yes, decouple adaptor trade | Not mandatory | release/v4.1.0 （base on feature/main_260615_removeTradeQuery | changed [Pipelines - Run 20260806.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14089725&view=results) | 4.1.0 | 4.0.2-20260408.3 | 4.0.2-20260709.1 | | | |
| 17 | ratan-cash-settlement-netting-service | Yes, resultant cf id prefix | Not mandatory | release/v4.1.0 （base on feature/v4.0.0-260601-prefix) | changed [Pipelines - Run 20260806.6](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14089799&view=results) | 4.1.0 | 4.0.0-20260519.11 | 3.0.10-20260601.1 | | | |
| 18 | ratan-cash-settlement-query-service | yes, filter & view query | Not mandatory | release/v4.4.0.0 [feature/ID_pipeline_enabling](https://dev.azure.com/sc-ado/777f0ba6-cfdf-4f44-99dd-ae1dc434f5c5/_git/51358-ratan-cash-settlement-query-service?version=GBfeature/ID_pipeline_enabling) | [Pipelines - Run 20260806.4](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14090102&view=results) | | 4.3.0-20260618.2 | 4.3.0-20260710.2 | [Pipelines - Run 20260717.2](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=13620139&view=results) | | |
| 19 | ratan-cash-settlement-ssi-stamping-service | No | | release/v4.4.0.0 （base on feature/upgrade_version_260807） | [Pipelines - Run 20260807.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14093628&view=results) | | 4.2.1-20260624.1 | 4.2.1-20260624.1 | [Pull request 3067825: #13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-cash-settlement-ssi-stamping-service/pullrequest/3067825) | | |
| 20 | ratanone-data-ambassador | No | | release/v4.0.0.0 （base on feature/upgrade_version_260807） | [Pipelines - Run 20260806.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14090536&view=results) | | 3.9.2-20260630.4 | 3.9.2-20260630.4 | [Pull request 3067992: #13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-data-ambassador/pullrequest/3067992) | | |
| 21 | ratanone-swift-service | No | | release/v4.4.0.0 wi （base on feature/upgrade_version_260807） | [Pipelines - Run 20260807.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14094044&view=results) | | 4.2.1-20260623.3 | 4.2.1-20260623.3 | [Pull request 3068794: #13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-swift-service/pullrequest/3068794) | | |
| 22 | ratan-rule-service | No | | release/v3.3.0.0 feature/upgrade_version_260807 | [Pipelines - Run 20260807.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14094831&view=results) | | 3.1.5-20260522.8 | 3.1.5-20260522.8 | [Pull request 3068944: #13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-rule-service/pullrequest/3068944) | | |
| 23 | ratanone-message-bridge | No | Mandatory | release/v5.1.0.0 feature/upgrade_version_260807 | [Pipelines - Run 20260807.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=14095093&view=results) | | 5.0.5-20260604.2 | 5.0.5-20260604.2 | [Pull request 3069048: #13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-message-bridge/pullrequest/3069048) | | |
| 24 | ratan-central-monitoring | | | release/v1.0.0 | | | | 1.0.0-20250606.3 | | | |
| 25 | 51358-ratanone-ansible | NA | | | | | NA | NA | NA | | NA |
| 26 | 51358-mfe-admin-module | Yes, add ID route & tiles | | [release/v1.2.](https://dev.azure.com/sc-ado/FMQPR/_git/51358-mfe-admin-module?version=GBrelease/v1.2.2)3 | | | | | | | |
| 27 | 51358-mfe-base | Yes, add ID handle for api | | [release/v](https://dev.azure.com/sc-ado/FMQPR/_git/51358-mfe-admin-module?version=GBrelease/v1.2.2)2.2.1 | | | | | | | |
| 28 | 51358-mfe-container | Yes, add prefix for url, add route for ID, enhance global style | | release/v1.8.14 | | | | | [Pipelines - Run 20260716.2](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=13587530&view=results) | | |
| 29 | 51358-mfe-cashflow-blotter | Yes, add prefix for url, add route for ID, booking entity fmid in drop down list should only include ID | | release/v1.45.1 | | | | | | | |
| 30 | 51358-mfe-nostro-static | Yes, add prefix for url, add route for ID | | release/v1.2.6 | | | | | | | |
| 31 | 51358-mfe-rules | Yes, add prefix for url, add route for ID | | release/v1.11.3 | | | | | | | |
| 32 | 51358-mfe-trades | Yes, support redirect to GDC and ID based on trade booking entity | | release/v1.16.4 | | | | | | | |
| 33 | 51358-ratan-cash-settlement-batch-service | Yes, Fixing flag changes | Mandatory | release/v2.1.0 | | | 2.0.0-20260326.4 | 2.0.1-20260703.1 | [Pull request 3069222: '#13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-cash-settlement-batch-service/pullrequest/3069222) | @Haolin Song | |
| 34 | 51358-ratanone-stella-ambassador | | | release/v3.4.0 | | | 3.2.13-20260408.2 | 3.2.13-20260408.2 | [Pull request 3069314: #13996712 ado pipeline for ID CICD enabling - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-stella-ambassador/pullrequest/3069314) | | |
| 35 | 51358-ratan-mxg-cashflow-adaptor | yes | Only GDC, | | | | | | | @Haolin Song | |

# Message Bridge Flow Definition

## GDC Existing

## GDC Changes

## Code change:

**Batch (GDC only)**

1. need to publish message to another topic Cash_Settlement_Mxg_Inbound_Batch_All for message bridge to consume.
2. ID doesn't have this service deployed

**Netting (ID drive)**

1. Netting resultant cashflow id prefix
2. Splitting resultant cashflow id prefix

## Indonesia Flow Definition

Question: Whether need to keep **folder** route type?
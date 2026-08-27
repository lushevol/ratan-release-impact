---
type: source
title: RATAN ONE Access Provisioning Guide
authors: []
year: 2023
url: "https://scbnow01.service-now.com/itsp?id=sp_sc_cat_item&sys_id=c5b6df4887d5a9501e0deb150cbb35b9"
venue: Internal operational guide
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, ratan-one, access-provisioning, servicenow, entitlements, rbac]
related: [ratan, fmo, myit-service-catalogue-servicenow, ratan-one-access-control, ratan-subject-to-tile-authorization, maker-checker-settlement-control, auto-netting-rule-management, what-is-the-canonical-ratan-nostro-and-bic-netting-subject-mapping, what-is-the-current-ratan-one-entitlement-provisioning-and-approval-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/How to apply for RATAN ONE access.md"]
---
# RATAN ONE Access Provisioning Guide

This undated operational guide documents how to request RATAN ONE access through the myIT Service Catalogue. It describes a layered access model consisting of request group and sub-group, functional role, data-entitlement scope, and request subject mapped to an application tile.

The guide is evidence of the documented request design only. It does not confirm current production permissions, action-level authorization, approved access requests, or the current status of the stated E-Form upgrade.

## Documented provisioning limitation

> For entitlement X_RATANONE and RATAN_DATA_ENTITLEMENT, currently can only use bulk request to grant access, corresponding E-Form still in progress of upgrade

This is a time-sensitive operational constraint. Its current validity requires confirmation through [[what-is-the-current-ratan-one-entitlement-provisioning-and-approval-routing]].

## Request channel

The documented channel is [[myit-service-catalogue-servicenow]]:

- Catalog item: `RATAN ID Creation/Amendment`
- URL: <https://scbnow01.service-now.com/itsp?id=sp_sc_cat_item&sys_id=c5b6df4887d5a9501e0deb150cbb35b9>
- Stated workflow: select Group and Sub Group, select the required Role, select the required Subject, then submit the request.

## Functional and data-entitlement roles

| Request Category | Request Group | Request Sub-Group | Role | Request Data Entitlement Role | New/Existing |
| --- | --- | --- | --- | --- | --- |
| RATAN Function Access Role | FMO | Business Rule Approver | FMO_BR_APR | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Business Rule Maker | FMO_BR_MKR | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | MO User | FMO_MO | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | FMO | MO Super User | FMO_MO_SUP | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | FMO | Operations User | FMO_OPS | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | FMO | Operations Back Office Officer | FMO_OPS_BO | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Operations Back Office Clerk | FMO_OPS_BOC | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Operations Back Office Leader | FMO_OPS_BOL | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Operations Back Office Manager | FMO_OPS_BOM | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Operations Investigator | FMO_OPS_INV | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Operations Maker | FMO_OPS_MKR | Global/GBS/Onshore | New |
| RATAN Function Access Role | FMO | Operations Super User | FMO_OPS_SUP | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | FMO | FMO Read Only User | FMO_RO | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | FMO | Static Data Checker | FMO_STA_CKR | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | FMO | Static Data Maker | FMO_STA_MKR | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | NON FMO | NON FMO Read Only User | NON_FMO_RO | Global/GBS/Onshore | Existing |
| RATAN Function Access Role | PSS | PSS | PSS_RO | Global/GBS/Onshore | Existing |
| RATAN Data Entitlement Role | N/A | N/A | GBS | GBS | New |
| RATAN Data Entitlement Role | N/A | N/A | Global | Global | New |
| RATAN Data Entitlement Role | N/A | N/A | Onshore | Onshore | New |
| RATAN Function Access Role | FMO | Operations Back Office Supervisor | FMO_OPS_BOS | Global/GBS/Onshore | New |

The role names indicate separation among operations, business-rule, static-data, management, investigation, and read-only responsibilities. They do not define the precise application actions granted by each role. The documented role model provides access-governance context for [[maker-checker-settlement-control]], but does not demonstrate transaction-level approval enforcement.

## Request subjects and RATAN ONE tiles

| | Subject in request | Tile in RATAN ONE |
| --- | --- | --- |
| 1 | RATAN_TRADE_BLOTTER | Trade Processing - Trade Blotter |
| 2 | RATAN_CASHFLOW_BLOTTER | Settlement - Cashflow Blotter [FX & Equity] |
| 3 | RATAN_STRATEGIC_CASHFLOW_BLOTTER | Settlement - Cashflow Blotter |
| 4 | RATAN_CASHFLOW_GROUP_BLOTTER | Settlement - Grouping Blotter |
| 5 | RATAN_VALIDATION_EXCEPTION | Exception Management - Validation Exceptions |
| 6 | RATAN_SETTLEMENT_EXCEPTION | Exception Management - Settlement Exceptions |
| 7 | RATAN_PROFILE_LIMITS | Business Rule- Authorization Limits |
| 8 | RATAN_SETTLEMENT_STP_RULE | Business Rule - Settlement NSTP Rules Business Rule - Settlement NSTP Rules [FX & Equity] |
| 9 | RATAN_SUPPRESSION_RULE | Business Rule - Suppresion Rules Business Rule - Suppresion Rules [Swift] Business Rule - Suppresion Rules [Cashflow] |
| 10 | RATAN_AUTO_NETTING_RULE | Business Rule - Auto Netting Rules |
| 11 | RATAN_ENTITLEMENT_RULE | Business Rule - Data Entitlement Rules |
| 12 | RATAN_NOSTRO_BLOTTER | Static - Nostro Static |
| 13 | RATAN_NETTING_RULE | Static - Netting Static |
| 14 | RATAN_NOSTRO_BLOTTER | Static - BIC Netting Static |
| 15 | ~~RATAN_MO_EXCEPTION~~ | Unused for now |

`RATAN_AUTO_NETTING_RULE` is documented as the request subject for the Auto Netting Rules tile. This does not establish configuration authority, rule semantics, or approval workflow for [[auto-netting-rule-management]].

The repeated `RATAN_NOSTRO_BLOTTER` identifier maps to both Nostro Static and BIC Netting Static. The source does not establish whether this is intentional or a documentation defect; see [[what-is-the-canonical-ratan-nostro-and-bic-netting-subject-mapping]].

## Request approver routing

The following internal routing information is transcribed from the source for authorized operational use.

| Profile | Approver_Group | Approvers |
| --- | --- | --- |
| FMO_MO | Ratan_FMO_MO_User_Approvers | 1579123;1658668;1551697 |
| FMO_MO_SUP | Ratan_FMO_MO_Sup_User_Approvers | 1579123;1658668;1551697 |
| PSS_RO | Ratan_PSS_RO_User_Approvers | 1612478;1399585 |
| FMO_STA_CKR | Ratan_FMO_Sta_Dat_User_Approvers | 1624508;1629651;1165312 |
| FMO_STA_MKR |  |  |
| NON_FMO_RO | Ratan_NON_FMO_RO_User_Approvers | 1607036;1364100;1166409;1658804 |
| FMO_OPS | Ratan_FMO_Ops_User_Approvers | 1607036;1364100;1166409;1658804 |
| FMO_OPS_SUP | Ratan_FMO_Ops_Sup_User_Approvers | 1598139;1658804;1364100;1166409 |
| FMO_RO | Ratan_FMO_RO_User_Approvers | 1607036;1364100;1166409;1658804 |
| FMO_BR_APR | Ratan_FMO_Ops_BusinessRules_User_Approver | 1364100;1166409;1658804 |
| FMO_BR_MKR |  |  |
| FMO_OPS_BO | Ratan_FMO_Settlement_User_Approvers | 1364100;1166409;1658804 |
| FMO_OPS_BOC |  |  |
| FMO_OPS_BOL |  |  |
| FMO_OPS_BOM |  |  |
| FMO_OPS_MKR |  |  |
| FMO_OPS_BOS |  |  |
| FMO_OPS_INV | Ratan_FMO_Investigation_User_Approvers | 1207323;1658804 |
| GBS | Ratan_Data_Entitlement_Approvers | |
| Global |  |  |
| Onshore |  |  |

Blank fields are a documentation-completeness issue, not proof that ServiceNow lacks routing. The distinction between an access-request approver group and an in-application business-rule approver is also unspecified.
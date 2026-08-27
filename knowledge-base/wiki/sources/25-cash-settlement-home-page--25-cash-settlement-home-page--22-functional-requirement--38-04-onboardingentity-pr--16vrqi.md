---
type: source
title: 2025 Tranche3 Static Data Go Live Checklist
authors: []
year: 2025
url: ""
venue: Internal operational checklist
created: 2026-08-22
updated: 2026-08-22
tags: [tranche-3, entity-onboarding, static-data, go-live, jersey]
related: [jersey, zhengzhou, taeyuan, lms, entity-onboarding-static-data-controls, is-jersey-tranche-3-go-live-a-static-data-onboarding-or-a-full-settlement-activation, are-the-tranche-3-suppression-rule-configurations-deployed-and-validated-in-production, what-is-the-authoritative-lms-routing-policy-for-jersey-zhengzhou-and-taeyuan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md"]
---
# 2025 Tranche3 Static Data Go Live Checklist

This operational checklist records Tranche 3 static-data tasks for [[jersey]], with entity-level SWIFT static-data and LMS-routing requirements also covering [[zhengzhou]] and [[taeyuan]].

The document identifies configuration tasks and UAT rule identifiers, but does not provide production deployment evidence, formal approval, completion status, test results, rollback plans, or go-live attestation. Screenshot-only evidence and the referenced SSI workbook require review in their originating repository.

## Checklist data

| Title | ADO No | Sub Items | Remark | Dev Owner |
| --- | --- | --- | --- | --- |
| [Tranche3] Static Data Setup | [https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9905158/ https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10434193](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9905158/) | nostro | Please refer to Jersey SSI (005)-Reformat-confirmed by Pradeesh_V3.xlsx 📎 [Jersey SSI (005)-Reformat-confirmed by Pradeesh_V3.xlsx](attachments/Jersey SSI (005)-Reformat-confirmed by Pradeesh_V3.xlsx) | Joey |
| release cut off | Currently users are not settling any trades in Jersey entity. Therefore maintain the existing currencies list. Keep as is Jersey,No need to do any change | Eddie |
| branch bridge account (equivalent to EBBS bridge suspense) | **1.Ebbs bridge account** **![image-2025-9-19_14-22-26.png](attachments/image-2025-9-19_14-22-26.png)** **2.Ebbs nostro account ** 123613180028881491098 | Eddie |
| entity level swift static 1.Jersey 2. TAEYUAN, ZHENGZHOU | **1.Jersey** ![image-2025-9-19_14-22-46.png](attachments/image-2025-9-19_14-22-46.png) **2.ZHENGZHOU&TAEYUAN** **![image-2025-9-19_14-23-10.png](attachments/image-2025-9-19_14-23-10.png)** | Eddie |
| nstp , netting , swift suppression | **1**.**Deliverable currencies---Swift suppression** GBP, GHS, JOD, TRY, AUD, CHF, DKK, EUR, HKD, NZD, SEK, SGD, THB, THO, USD, ZAR, HUF,KES, PLN, AED, SAR, BWP, NOK, ZMK, MAD, ILS, PKR, NGN, UGX, TZS Rule created on UAT:7374420229233111040 ![image-2025-9-19_14-25-11.png](attachments/image-2025-9-19_14-25-11.png) **2.Metal currencies---Cashflow suppression** Metal Currencies XAU,XAG,XPD,XPT,XRH,XU5,XG2,XT3,XD3,XRU,XS9,XS5,XSD,XU6,XU7,XG5,XUC,XG3, XGC,XD1,XD2,XG1,XR1,XT1,XT2,XU1,XU2,XU3,XU4,XU8,XTN,XDN,XUD,XG4,XG6,XGF, XS6,XSF,XSI,XS4,XGI,XGA,XG7 Rule created on UAT:7369258354199584768 ![image-2025-9-19_14-26-15.png](attachments/image-2025-9-19_14-26-15.png) **3.Add Jersey FMID(400910415) to existing 'Non FMRP entities' cashflow suppression rule** **,** **SAUDI is keep as is** Rule id on UAT : 7369288575163731968 ![image-2025-9-19_14-25-55.png](attachments/image-2025-9-19_14-25-55.png) | Eddie |
| CPT Control | ![image-2025-9-19_15-20-38.png](attachments/image-2025-9-19_15-20-38.png) | Eddie |
| [Tranche3] Entity setup in blotter | [https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9905654/](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9905654/) | Jersey Manual Entities | ![image-2025-9-19_16-45-34.png](attachments/image-2025-9-19_16-45-34.png) | Guiling Wang |
| [Tranche 3] LMS filter | [Story 9920605 [Tranche 3] LMS filter](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9920605) | | Jersey shouldn’t flow to LMS ZHENGZHOU &TAEYUAN need to flow to LMS | Eddie |

## Recorded configuration requirements

- The Jersey SSI and nostro setup refers to `Jersey SSI (005)-Reformat-confirmed by Pradeesh_V3.xlsx`; the workbook contains details not represented in the text extract.
- The source instructs that Jersey's existing currency list remain unchanged because users are not settling trades in the entity.
- A branch bridge account is described as equivalent to EBBS bridge suspense. The referenced EBBS nostro account number is retained in the source table and should be handled according to applicable data-classification controls.
- The source distinguishes deliverable-currency SWIFT suppression from metal-currency cashflow suppression.
- Jersey FMID `400910415` is to be added to the existing `Non FMRP entities` cashflow-suppression rule. `SAUDI` is to remain unchanged.
- Jersey is to be configured as a manual entity in the blotter under ADO work item `9905654`.
- LMS policy is entity-specific: Jersey must not flow to [[lms]], whereas ZHENGZHOU and TAEYUAN must flow to LMS.

## UAT-only rule references

| Purpose | UAT rule ID |
| --- | --- |
| Deliverable currencies — SWIFT suppression | `7374420229233111040` |
| Metal currencies — cashflow suppression | `7369258354199584768` |
| Non FMRP entities — cashflow suppression | `7369288575163731968` |

These identifiers are explicitly identified as UAT rules. They are not evidence that equivalent rules were deployed or validated in production.

## Evidence limitations

The checklist heading includes NSTP and netting, but its text supplies no specific NSTP setup or netting-rule configuration. Several rows also do not align cleanly with the five-column header, so ownership and field assignment should be checked against the original document.

See [[entity-onboarding-static-data-controls]] for the control model, [[cashflow-suppression-vs-swift-suppression]] for the suppression distinction, and [[release-readiness-attestation]] for the difference between a checklist and formal go-live approval.
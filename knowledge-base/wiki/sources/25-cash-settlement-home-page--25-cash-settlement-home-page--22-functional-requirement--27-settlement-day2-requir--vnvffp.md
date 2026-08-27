---
type: source
title: "HKCS Initiative: Onboarding for HAU Currency"
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/GMSD/HONG+KONG+Physical+Gold+Settlement+initiative"
venue: "Internal functional-requirement checklist"
created: 2026-08-22
updated: 2026-08-22
tags: [hau, hkcs, settlement-day-2, swift, static-data, uat]
related: [hau, xau, hong-kong-physical-gold-settlement, hau-currency-onboarding, settlement-day-2, nostro-static, swift-entity-configuration, ebbs-settlement-accounting, should-hau-inherit-xau-holidays-and-cutoffs, should-lms-convert-hau-to-xau, does-hau-require-swift-message-customization, why-does-hau-accounting-processing-have-a-service-story-if-accounting-publication-is-not-required, which-netting-rules-apply-to-hau]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md"]
---
# HKCS Initiative: Onboarding for HAU Currency

This checklist records implementation scope and UAT1 setup for enabling `HAU` in RATAN ONE Settlement Day 2 processing under the [[hong-kong-physical-gold-settlement]] initiative.

It is evidence of planned configuration and one controlled UAT path, not confirmation of a production release. Checklist statuses, pull requests, and pipeline results are blank.

## Checklist

| # | Check item | Impact scope | Recorded comment |
| --- | --- | --- | --- |
| 1 | Static data: spot-rate conversion for HAU | `ratanone-static-data-service`; `ratanone.ratan_static_spot_rate`; `StaticSpotRateController.getSpotRate` | No completion status recorded. |
| 2 | Static data: holiday configuration for HAU | `ratanone-static-data-service`; `ratanone.ratan_static_cashflow_currency_holiday` | Open: configure HAU directly or inherit the existing XAU holiday configuration. |
| 3 | Static data: currency cut-off configuration for HAU | `ratanone-static-data-service`; `ratanone.ratan_static_cashflow_currency_cut_off` | Open: configure HAU directly or inherit XAU cut-off data. |
| 4 | Static data: PM currency configuration for HAU | `ratanone-swift-service`; `ratanone_swfit_service.swift_static_pm_currency` | No completion status recorded. |
| 5 | Static data: ISO currency mapping for HAU | `ratanone-static-data-service`; `[ratanone.sd](http://ratanone.sd).holiday-currency-list (onshore\|offshore)` | HAU is described as offshore, like XAU; the checklist says no addition is needed. |
| 6 | Static data: rounding configuration for HAU | `ratan-cash-settlement-group-service` | HAU should attach to the existing XAU rounding configuration. |
| 7 | Frontend currency dropdown | RATAN ONE GUI | Open: whether HAU should be added; Judy was consulted. |
| 8 | Vostro setup | SSI+ | No completion status recorded. |
| 9 | Nostro setup | `ratanone-data-ambassador`; `ratanone.ratan_static__cashflow_nostro` | UAT1 setup recorded. |
| 10 | Accounting-message publishing | `ratan-cash-settlement-accounting-service` | The source says no accounting entry needs to be published for HAU. |
| 11 | LMS-message publishing | `ratan-cash-settlement-lms-service`; [[lms]] | Open: whether LMS should convert HAU to XAU. |
| 12 | SWIFT-message publishing | `ratanone-swift-service` | Open: whether HAU requires customization. |
| 13 | Razor-message publishing for LoanIQ | `ratan-cashflow-lifecycle-service`; Razor; LoanIQ | No customization is required, confirmed with Carrie. |
| 14 | Business-rule impact | Manual netting and auto netting | Possible impact on `FMO UK Non X Currency Netting` and `Commodity Auto Netting – PM Currencies`; confirmation is pending. |

## Static-data verification queries

```sql
select * from ratanone.ratan_static_spot_rate where quote_currency = 'HAU';
```

```sql
select * from ratanone.ratan_static_cashflow_currency_holiday where iso_currency_code = 'HAU' and text("version") = (select activated_version from ratanone.ratan_static_activated_version where table_name = 'ratan_static_cashflow_currency_holiday' and active = true);
```

```sql
select * from ratanone.ratan_static_cashflow_currency_cut_off where currency = 'HAU' and text("version") = (select activated_version from ratanone.ratan_static_activated_version where table_name = 'ratan_static_cashflow_currency_cut_off' and active = true);
```

```text
[ratanone.sd](http://ratanone.sd).holiday-currency-list (onshore|offshore)
```

## UAT1 settlement-to-SWIFT path

The documented UAT1 flow generated cashflow `M00127675004`, then proceeded through maker submission, checker approval, and HAU SWIFT-message generation.

| Step | Activity | Recorded result |
| --- | --- | --- |
| 1 | Set up nostro | An HAU nostro static record was inserted. |
| 2 | Set up PM configuration | HAU was inserted into `swift_static_pm_currency`. |
| 3 | Set up SWIFT static data | HAU UDF data was inserted for `GOLD`, `FOZ`, `9950`, and `HONGKONG`. |
| 4 | Generate HAU cashflow | Cashflow ID: `M00127675004`. |
| 5 | Maker submission | Maker entered the vostro, selected the nostro, and submitted. |
| 6 | Checker approval | Checker approved the cashflow. |
| 7 | Generate SWIFT message | An HAU SWIFT message was generated. |

This establishes basic configured-path feasibility only. The source does not retain a SWIFT payload, acceptance result, downstream delivery proof, or assertion criteria.

### UAT1 static-data setup

```sql
INSERT INTO ratanone.ratan_static__cashflow_nostro (id, legal_entity, legal_entity_fmid, settlement_currency, ebbs_nostro_account, settlement_means, settlement_account, senders_correspondent53_swift, senders_correspondent53_fullname, senders_correspondent53_address, senders_correspondent53_city, senders_correspondent53_postcode, senders_correspondent53_account, created_at, updated_at, notice_to_receive, ratan_label, "version", currency_pair, data_status, maker_id, checker_id, tlm_set_id, primary_flag, nostro_static_id, start_date, end_date, data_version, nostro_type) VALUES('id-hk8ebce-00ba-4c1f-aa8f-98f64c651111', 'HONGKONG', '2', 'HAU', '99999191742', 'NOS', 'HAU MAIN', 'SCBLGB2LTSY', '', '', '', '', '', '2026-07-22 15:23:24.370', '2026-07-22 15:23:24.370', 'Y', 'live', 1, '', 'SAVE_CONFIRMED', 'SYSTEM', 'SYSTEMconfirm', '', true, 50300012, '2020-01-01', '9999-12-31', 3, 'DEFAULT');
```

```sql
INSERT INTO ratanone_swift_service.swift_static_pm_currency(currency) VALUES ('HAU') ON CONFLICT (currency) DO NOTHING;
```

```sql
INSERT INTO ratanone_swift_service.swift_static_udf_swf_ls (k_currency, v_allocation, v_available_location, v_quality, v_type, v_unit) VALUES('HAU', 'UNALL', 'HONGKONG', '9950', 'GOLD', 'FOZ');
```

## Service-change branches

| Service | Feature branch | PR | Pipeline |
| --- | --- | --- | --- |
| `ratan-cash-settlement-accounting-service` | `feature/14724643-HKCS-Initiative` | Not recorded | Not recorded |
| `ratanone-swift-service` | `feature/14724643-HKCS-Initiative` | Not recorded | Not recorded |
| `db-repository` | `feature/14724643-HKCS-Initiative` | Not recorded | Not recorded |

## Linked Azure DevOps stories

| Story | Scope |
| --- | --- |
| [15548535](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548535) | Sort the checklist for HAU currency onboarding |
| [14900306](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14900306) | Accounting processing for HAU currency |
| [14900316](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14900316) | SWIFT processing for HAU currency |
| [15548867](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548867) | Vostro setup for HAU currency |
| [14923453](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14923453) | Nostro setup for HAU currency |
| [14969343](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14969343) | FX rate verification |
| [15548232](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548232) | Add a frontend dropdown item for HAU currency |
| [15548335](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548335) | Prepare cut-off data for HAU currency |
| [15548837](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548837) | Prepare rounding configuration data for HAU currency |

## Open delivery questions

The source does not resolve HAU holiday and cut-off treatment, LMS representation, SWIFT customization, frontend availability, accounting-suppression semantics, or netting-rule eligibility. These are tracked in [[should-hau-inherit-xau-holidays-and-cutoffs]], [[should-lms-convert-hau-to-xau]], [[does-hau-require-swift-message-customization]], [[why-does-hau-accounting-processing-have-a-service-story-if-accounting-publication-is-not-required]], and [[which-netting-rules-apply-to-hau]].
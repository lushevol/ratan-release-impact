# check list

| | check item | status | impact scope | comment |
| --- | --- | --- | --- | --- |
| 1 | static data - spot rate conversion for HAU | | service: ratanone-static-data-service table: ratanone.ratan_static_spot_rate interface: StaticSpotRateController.getSpotRate <details> <summary>Expand Details</summary> select * from ratanone.ratan_static_spot_rate where quote_currency = 'HAU'; </details> | |
| 2 | static data - holiday config for HAU | | service: ratanone-static-data-service <details> <summary>Expand Details</summary> select * from ratanone.ratan_static_cashflow_currency_holiday where iso_currency_code = 'HAU' and text("version") = (select activated_version from ratanone.ratan_static_activated_version where table_name = 'ratan_static_cashflow_currency_holiday' and active = true); </details> | should holiday config setup for HAU or inherit from XAU(exist holiday for XAU currently)? <details> <summary>Expand Details</summary> ![image-2026-7-22_11-30-20.png](attachments/image-2026-7-22_11-30-20.png) </details> |
| 3 | static data - currency cutoff config for HAU | | service: ratanone-static-data-service table: ratanone.ratan_static_cashflow_currency_cut_off <details> <summary>Expand Details</summary> select * from ratanone.ratan_static_cashflow_currency_cut_off where currency = 'HAU' and text("version") = (select activated_version from ratanone.ratan_static_activated_version where table_name = 'ratan_static_cashflow_currency_cut_off' and active = true); </details> | should currency cutoff setup for HAU or inherit from XAU? <details> <summary>Expand Details</summary> ![image-2026-7-22_14-5-11.png](attachments/image-2026-7-22_14-5-11.png) </details> |
| 4 | static data - PM currency static data for HAU | | service: ratanone-swift-service table: ratanone_swfit_service.swift_static_pm_currency | |
| 5 | static data - ISO currency mapping for HAU | | service: ratanone-static-data-service config: [ratanone.sd](http://ratanone.sd).holiday-currency-list (onshore|offshore) | is HAU offshore currency which same to XAU? **no need** |
| 6 | static data - rounding config for HAU | | service: ratan-cash-settlement-group-service | whether to add HAU rounding config(exist for XAU)? **attached from exist XAU** |
| 7 | frontend static data - currency dropdown list for HAU in GUI | | | whether to add HAU currency for frontend(checked with judy)? <details> <summary>Expand Details</summary> ![image-2026-7-22_11-13-59.png](attachments/image-2026-7-22_11-13-59.png) </details> |
| 8 | vostro setup | | SSI+ | |
| 9 | nostro setup | | service: ratanone-data-ambassador table: ratanone.ratan_static__cashflow_nostro | |
| 10 | accounting message publishing | | service: ratan-cash-settlement-accounting-service | not need to publish accounting entry for HAU |
| 11 | lms message publishing | | service: ratan-cash-settlement-lms-service | should LMS need to convert HAU to XAU? |
| 12 | swfit message publishing | | service: ratanone-swift-service | should swift have customization for HAU? |
| 13 | razor message publishing for loaniq | | service: ratan-cashflow-lifecycle-service | should publishing to razor have customization for HAU? no customization(confirmed with carrie) |
| 14 | impacted business rule if exist | | | possible impact rule to be confirmed: Manual Netting rule: - FMO UK Non X Currency Netting Auto Netting rule: - Commodity Auto Netting – PM Currencies |

# test in lower environment

## test for HAU in UAT1

| | step | comment |
| --- | --- | --- |
| 1 | setup nostro | <details> <summary>Expand Details</summary> INSERT INTO ratanone.ratan_static__cashflow_nostro (id, legal_entity, legal_entity_fmid, settlement_currency, ebbs_nostro_account, settlement_means, settlement_account, senders_correspondent53_swift, senders_correspondent53_fullname, senders_correspondent53_address, senders_correspondent53_city, senders_correspondent53_postcode, senders_correspondent53_account, created_at, updated_at, notice_to_receive, ratan_label, "version", currency_pair, data_status, maker_id, checker_id, tlm_set_id, primary_flag, nostro_static_id, start_date, end_date, data_version, nostro_type) VALUES('id-hk8ebce-00ba-4c1f-aa8f-98f64c651111', 'HONGKONG', '2', 'HAU', '99999191742', 'NOS', 'HAU MAIN', 'SCBLGB2LTSY', '', '', '', '', '', '2026-07-22 15:23:24.370', '2026-07-22 15:23:24.370', 'Y', 'live', 1, '', 'SAVE_CONFIRMED', 'SYSTEM', 'SYSTEMconfirm', '', true, 50300012, '2020-01-01', '9999-12-31', 3, 'DEFAULT'); </details> |
| 2 | setup PM config for HAU | <details> <summary>Expand Details</summary> INSERT INTO ratanone_swift_service.swift_static_pm_currency(currency) VALUES ('HAU') ON CONFLICT (currency) DO NOTHING; </details> |
| 3 | setup swift static data for HAU | <details> <summary>Expand Details</summary> INSERT INTO ratanone_swift_service.swift_static_udf_swf_ls (k_currency, v_allocation, v_available_location, v_quality, v_type, v_unit) VALUES('HAU', 'UNALL', 'HONGKONG', '9950', 'GOLD', 'FOZ'); </details> |
| 4 | generate cashflow for HAU | cashflow id: M00127675004 ![image-2026-7-22_18-48-9.png](attachments/image-2026-7-22_18-48-9.png) |
| 5 | maker input vostro and select nostro then submit | ![image-2026-7-22_18-50-17.png](attachments/image-2026-7-22_18-50-17.png) |
| 6 | checker approve | ![image-2026-7-22_18-51-15.png](attachments/image-2026-7-22_18-51-15.png) |
| 7 | generate swift message for HAU | ![image-2026-7-22_18-51-55.png](attachments/image-2026-7-22_18-51-55.png) |

# service changes

| | service | feature branch | pr | pipeline |
| --- | --- | --- | --- | --- |
| 1 | ratan-cash-settlement-accounting-service | feature/14724643-HKCS-Initiative | | |
| 2 | ratanone-swift-service | feature/14724643-HKCS-Initiative | | |
| 3 | db-repository | feature/14724643-HKCS-Initiative | | |

# ADO

| | ADO |
| --- | --- |
| 1 | [Story 15548535 [HKCS Initiative] sort the checklist for HAU currency onboarding](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548535) |
| 2 | [Story 14900306 [HKCS Initiative] accounting processing for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14900306) |
| 3 | [Story 14900316 [HKCS Initiative] swift processing for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14900316) |
| 4 | [Story 15548867 [HKCS Initiative] vostro setup for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548867) |
| 5 | [Story 14923453 [HKCS Initiative] nostro setup for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14923453) |
| 6 | [Story 14969343 [HKCS Initiative] FX rate verification](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14969343) |
| 7 | [Story 15548232 [HKCS Initiative] add a dropdown item in frontend for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548232) |
| 8 | [Story 15548335 [HKCS Initiative] prepare cutoff data for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548335) |
| 9 | [Story 15548837 [HKCS Initiative] prepare rounding config data for HAU currency](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15548837) |

# reference document

[HONG KONG Physical Gold Settlement initiative - Financial Markets Solutions Delivery - Confluence](https://confluence.global.standardchartered.com/display/GMSD/HONG+KONG+Physical+Gold+Settlement+initiative)
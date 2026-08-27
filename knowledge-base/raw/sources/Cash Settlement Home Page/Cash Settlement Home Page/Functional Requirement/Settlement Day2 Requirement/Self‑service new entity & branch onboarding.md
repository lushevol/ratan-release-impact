#

# Background

Current new-entity onboarding requires multiple backend configuration changes and static data imports that must be deployed on scheduled release windows. This creates a long lead time and limits the team’s ability to respond quickly to business needs. The goal of this requirement is to introduce a user self‑service solution that streamlines onboarding, improves turnaround time, and reduces dependency on scheduled deployments.

# ADO

[https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11351733](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11351733)

# Requirement Details

- ~~**Option 1**: provide excel template for user to import all the static via file, system will import the data to backend table.~~
- **Option 2: **build new blotter for new entity onboarding, and required static are added as sub tiles

### **User Profile**

Static ops have edit access , other user profile have read only access - same as existing nostro static blotter

### **Static Details**

- **Currency Mapping** (including rounding static and iso ccy mapping ) - | Non-ISO CCY | Precision | Type | ISO CCY | | --- | --- | --- | --- | | | 0 | ROUNDING_OFF | |
- **Onboarding Dashboard (Drilldown from "New Entity Onboarding" from home page)** - | FMID | FMCODE | Status | Missing Static | | --- | --- | --- | --- | | | | | format to be confirmed | - ##### Branch Code - | FMID | FMCODE | Branch Code | | --- | --- | --- | | | | | - ##### Nostro Static - existing Blotter, link to new entity onboarding - need to enable bulk upload function - ##### Swift Generation: - | FMID | Sender BIC | Field 53 BIC | Field 53 CCY | Field 58 BIC | | --- | --- | --- | --- | --- | | | | | | |

- - ##### Release Time - | Booking Entity FMID | Booking Entity FMCODE | Currency | cutoff time (GMT) | cutoff shifter | cutoff shifter unit | | --- | --- | --- | --- | --- | --- | | | | | | -2/-1/0 | BUSINESS DAY | - Accounting Static - | Booking Entity FMID | Booking Entity FMCODE | EBBS Bridge Account | Country Full Name | Country Code | ZoneId () | Posting Branch | Txn Type Code | Dr Txn Code | Cr Txn Code | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | BAHRAIN | BH | Asia/Bahrain | 055 | RTN | 478 | 378 |

- **EXPAND: Below items are not mandatory for new entity onboarding, keep in backend for now** - | ##### ~~PM CCY~~ | ##### ~~PM CCY Receiver BIC~~ | | --- | --- | | | | - ##### ~~UDF_Strategy ~~- | ##### k_strategy | ##### v_allocation | ##### v_available_location | | --- | --- | --- | | ##### COM_BOE_DELIV | ##### ALLOC | ##### BOE | | ##### COM_CHAS_LDN | | ##### LONDON | - ##### ~~UDF_SWF_LS~~ - not mandatory for new entity onboarding, keep in backend for now | ##### k_currency | ##### v_allocation | ##### v_available_location | ##### v_quality | ##### v_type | ##### v_unit | | --- | --- | --- | --- | --- | --- | | ##### XAG | ##### UNALL | ##### LONDON | ##### 9990 | ##### SILV | ##### GOZ | | ##### XAQ | ##### UNALL | ##### LONDON | | ##### GOLD | ##### FOZ | - CFI Code Mapping **EXPAND_END**

# Link

[Self Service new branch/entity onboarding Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3556617786)

# UI Changes

- Separate Static Blotter

| | Blotter | Mock UI |
| --- | --- | --- |
| 1 | Tile | ![image-2026-7-3_17-21-37.png](attachments/image-2026-7-3_17-21-37.png) |
| 2 | Onboarding Dashboard | Option1![image-2026-7-10_17-25-0.png](attachments/image-2026-7-10_17-25-0.png) VS Option2 ![image-2026-7-10_17-25-19.png](attachments/image-2026-7-10_17-25-19.png) |
| 3 | Branch Code | ![image-2026-7-10_17-28-46.png](attachments/image-2026-7-10_17-28-46.png) |
| 4 | Release Time | ![image-2026-7-10_17-25-57.png](attachments/image-2026-7-10_17-25-57.png) |
| 5 | Currency Mapping | ![image-2026-7-10_17-27-23.png](attachments/image-2026-7-10_17-27-23.png) |
| 6 | Settlement Accounting | ![image-2026-7-10_17-27-48.png](attachments/image-2026-7-10_17-27-48.png) |
| 7 | Swift Static | ![image-2026-7-2_17-36-12.png](attachments/image-2026-7-2_17-36-12.png) |
| 8 | Bulk Upload Function | ![image-2026-7-2_17-36-34.png](attachments/image-2026-7-2_17-36-34.png) ![image-2026-7-2_17-36-52.png](attachments/image-2026-7-2_17-36-52.png) ![image-2026-7-2_17-37-6.png](attachments/image-2026-7-2_17-37-6.png) ![image-2026-7-2_17-37-31.png](attachments/image-2026-7-2_17-37-31.png) ![image-2026-7-2_17-37-48.png](attachments/image-2026-7-2_17-37-48.png) |
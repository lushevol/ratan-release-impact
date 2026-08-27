---
type: concept
title: RATAN-Eligible Entity Configuration
tags: [ratan, murex-211, fmrp, entity-eligibility, static-data, change-control]
related: [ratan, fmrp, fmrp-payment-eligibility-and-suppression, cn-settlement-murex-211-integration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document.md"]
---
# RATAN-Eligible Entity Configuration

RATAN eligibility is controlled through entity records in `SCB_ENTITY_DBF`. The source identifies the following fields:

| Field | Meaning |
| --- | --- |
| `M_LABEL` | Entity name |
| `M_CTP_COD` | Counterparty or entity code |
| `M_EBBS` | EBBS indicator |
| `M_ENTITY_TYP` | Entity type, such as `subsidiary` or `branch` |
| `M_FEDS_ENT` | Federation or entity grouping code |
| `M_PAY_HUB` | Payment hub |

The source states that CN entity data must not be changed for this project without a change ticket. It also requires amendments to `FMRP_ENTITY_DBF` to follow change-ticket control and the Murex 2.11 pre-Cab process.

## Eligible entity population

| `M_LABEL` | `M_CTP_COD` | `M_EBBS` | `M_ENTITY_TYP` | `M_FEDS_ENT` | `M_PAY_HUB` |
| --- | --- | --- | --- | --- | --- |
| BEIJING | SCB/BEIJING | Y | subsidiary | CHN | CHINA |
| NANJING | SCB/NANJING | Y | subsidiary | CHN | CHINA |
| TIANJIN | SCB/TIANJIN | Y | subsidiary | CHN | CHINA |
| ZHUHAI | SCB/ZHUHAI | Y | subsidiary | CHN | CHINA |
| SHANGHAI | SCB/SHA | Y | subsidiary | CHN | CHINA |
| XIAMEN | SCB/XIA | Y | subsidiary | CHN | CHINA |
| SHENZHEN | SCB/SHENZHEN | Y | subsidiary | CHN | CHINA |
| GUANGZHOU | SCB/GUANGZHOU | Y | subsidiary | CHN | CHINA |
| SUZHOU | SCB/SUZHOU | Y | subsidiary | CHN | CHINA |
| CHENGDU | SCBCHENGDU/CGD | Y | subsidiary | CHN | CHINA |
| QINGDAO | SCB/QDO | Y | subsidiary | CHN | CHINA |
| CHONGQING | SCBCNCQG/CQG | Y | subsidiary | CHN | CHINA |
| HHANGZHOU | SCBCNHANGZH/HNZ | Y | subsidiary | CHN | CHINA |
| NNCHANG | SCBCHINANAN/NCG | Y | subsidiary | CHN | CHINA |
| DALIAN | SCBCHINADAL/DLN | Y | subsidiary | CHN | CHINA |
| NINGBO | SCBCHNIBR/NGB | Y | subsidiary | CHN | CHINA |
| HOHHOT | SCBCHHOBR/HHH | Y | subsidiary | CHN | CHINA |
| XXIAN | SCBLXIAN/XIN | Y | subsidiary | CHN | CHINA |
| FOSHAN | SCBCNFOSBR/FOS | Y | subsidiary | CHN | CHINA |
| JINAN | SCBCNJNABR/JNA | Y | subsidiary | CHN | CHINA |
| CHANGSHA | SCBCNCHANG/CGS | Y | subsidiary | CHN | CHINA |
| FUZHOU | SCBCNFUZHOU/FZH | Y | subsidiary | CHN | CHINA |
| KUNMING | SCBCNKMG/KMG | Y | subsidiary | CHN | CHINA |
| FT2 SHA | SCBSHAFTU/FT2 | Y | subsidiary | CHN | CHINA |
| SHYANG | SCBCNSHY/SYG | Y | subsidiary | CHN | CHINA |
| CHINA HO | SCBCNCHO/CHO | Y | subsidiary | CHN | CHINA |
| WUHAN | SCBL/WUH | Y | subsidiary | CHN | CHINA |
| ACU SING | SCBACU/SIN | Y | branch | SG | SOUTH EAST ASIA |
| DBU SING | SCB/SIN | Y | branch | SG | SOUTH EAST ASIA |
| SACU SING | SSCBACU/SIN | Y | subsidiary | SG | SOUTH EAST ASIA |
| SDBU SING | SSCB/SIN | Y | subsidiary | SG | SOUTH EAST ASIA |
| MUMBAI | SCB/MMB | Y | branch | MUM | EAST ASIA |
| GIFTCITY | SCBGIFTCITY/MUM | Y | branch | GFT | EAST ASIA |
| KLISLAMIC | ISLAMICKL/KUL | Y |  | KL | SOUTH EAST ASIA |
| KLUMPUR | SCB/KUL | Y | subsidiary | KL | SOUTH EAST ASIA |

Payments with a value date within nine days are in scope, subject to the documented product, currency, RAZOR, and amount exclusions.
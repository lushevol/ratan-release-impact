---
type: concept
title: Murex-RATAN Cashflow Ringfencing
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, china, ringfencing, precious-metals, cashflow-routing]
related: [murex-211, ratan, precious-metal-cashflow-vostro-requirement, precious-metal-currency-classification, cn-settlement-murex-211-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# Murex-RATAN Cashflow Ringfencing

CN Murex-RATAN ringfencing determines whether a trade continues to settle in [[murex-211]] or is sent to [[ratan]].

A trade is a precious-metal deal when:

1. Its entity is in the documented China scope.
2. At least one cashflow under the trade contains a precious-metal currency.

For a precious-metal deal, every cashflow under the trade remains settled in Murex 2.11. For other trades, the documented intended route is RATAN.

## Documented entity scope

```text
BEIJING
CHANGSHA
CHENGDU
CHINA HO
CHONGQING
DALIAN
FOSHAN
FT2 SHA
FUZHOU
GUANGZHOU
HHANGZHOU
HOHHOT
JINAN
KUNMING
NANJING
NINGBO
NNCHANG
QINGDAO
SHANGHAI
SHENZHEN
SHYANG
SUZHOU
TIANJIN
WUHAN
XIAMEN
XXIAN
ZHUHAI
```

The source does not identify the authoritative precious-metal currency catalogue, the relevant static-data owner, or the outcome when an amendment adds or removes a precious-metal cashflow. Those issues are tracked in [[what-is-the-authoritative-precious-metal-currency-definition-for-cn-murex-ratan-ringfencing]].
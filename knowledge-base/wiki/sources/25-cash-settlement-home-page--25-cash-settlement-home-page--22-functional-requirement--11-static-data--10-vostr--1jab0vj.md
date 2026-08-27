---
type: source
title: Murex Vostro Analysis
created: 2026-08-24
updated: 2026-08-24
tags: [vostro-ssi, murex, ratan, cms, swift, mt103, mt202]
related: [cms-dependent-swift-message-generation, mt202-beneficiary-institution-field-58a-resolution, what-are-the-jakarta-cms-field-72-special-rules, what-is-the-literal-mt202-field-72-output-for-non-cms-jakarta-cashflows, how-does-cms-affect-mt210-and-mtx92, cfi-code-mapping-for-murex-vostro-ssi, murex-2-11, ratan, ratanone-swift-service, notice-to-receive-mt210-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex Vostro Analysis.md"]
authors: []
year: 2022
url: ""
venue: ""
---
# Murex Vostro Analysis

This functional/design note compares Murex Vostro and BCS RATAN Vostro screens and documents CMS Account Holder behavior for SWIFT-message construction. It provides explicit conditional rules for MT103 and MT202, including MT202 field 58a, but does not provide implementation evidence or test results.

The source states that the CMS Account Holder tick box indicates a CMS flag affecting MT103, MT202, MT210, and MTX92. Detailed rules are supplied only for MT103 and MT202; MT210 and MTX92 effects remain unspecified.

## CMS Account Holder: MT103 rules

|  | MT103_CMS | MT103 |
| --- | --- | --- |
| Header Block2- Receiver BIC | Account holder BIC (SWIFT_ACHL) | IF (FIN_COPY is blank) THEN Counterparty BIC OTHERWISE IF intermediary Code is NOT blank THEN intermediary Code OTHERWISE Account holder BIC (SWIFT_ACHL) |
| 26T - Transaction Type Code | NA | Applicable. value as :26T:TOF for AED payment |
| 53 - Sender's Correspondent | For China entity IF (CMS Account Number NOT blank) THEN **53a:line1= CMS Account number **line2= our entity BIC OTHERWISE 53a line1=entity swift code | not rely on CMS Account number |
| 56 | NA | Applicable |
| 57 - Account With Institution | CMS Flag don't impact mt103. only affect mt210 | not rely on CMS Flag |
| 72 - Sender to Receiver | IF CMS_FLAG=Y IF (entity=JAKARTA AND product in (NDF,IRS,CS,FXO)) THEN has special logic for different product on F72 OTHERWISE combination of SNDREC1~6 line1:SNDREC1 line2:SNDREC2 line3:SNDREC3 line4:SNDREC4 line5:SNDREC5 line6:SNDREC6 | IF CMS_FLAG <> Y IF (entity=JAKARTA AND CCY= IDR/IRO/IRY AND product in (NDF,IRS,CS,FXO)) THEN has special logic for different product on F72 OTHERWISE combination of SNDREC1~6 line1:SNDREC1 line2:SNDREC2 line3:SNDREC3 line4:SNDREC4 line5:SNDREC5 line6:SNDREC6 |
| 77b | CMS Flag only affect DUBAI entity | not rely on CMS Flag |

## CMS Account Holder: MT202 rules

|  | MT202_CMS | MT202 |
| --- | --- | --- |
| Header Block2- Receiver BIC | Our entity BIC | IF (FIN_COPY is blank) THEN Correspondent's BIC ( ie.Nostr filed 53 Corr.Code) OTHERWISE IF intermediary Code is NOT blank THEN intermediary Code OTHERWISE Account holder BIC (SWIFT_ACHL) |
| 53 - Sender's Correspondent | For China entity IF (CMS Account Number NOT blank) THEN **53a:line1= CMS Account number** line2= our entity BIC OTHERWISE 53a line1=our entity BIC | not rely on CMS Account number |
| 72 - Sender to Receiver | IF CMS_FLAG=Y IF (entity=JAKARTA AND product in (NDF,IRS,CS,FXO)) THEN has special logic for different product on F72 OTHERWISE combination of SNDREC1~6 line1:SNDREC1 line2:SNDREC2 line3:SNDREC3 line4:SNDREC4 line5:SNDREC5 line6:SNDREC6 | IF CMS_FLAG<>Y IF (entity=JAKARTA AND CCY= IDR/IRO/IRY AND product in (NDF,IRS,CS,FXO)) THEN hardcode :[72:/TTC/103](http://72/TTC/103) OTHERWISE combination of SNDREC1~6 line1:SNDREC1 line2:SNDREC2 line3:SNDREC3 line4:SNDREC4 line5:SNDREC5 line6:SNDREC6 |

## MT202 Field 58a: Beneficiary Institution

58 only applicable to mt202

Red highlights mean value come from murex GUI

| IF Beneficiary(58) is NOT populated IF ctp BIC is blank AND Beneficiary A/C is blank THEN 58D:Ctp LongName OTHERWISE line1 58D:Beneficiary A/C line2 Ctp LongName IF ctp BIC is NOT blank AND Beneficiary A/C is blank THEN 58A:Ctp BIC OTHERWISE line1 58A:Beneficiary A/C line2 Ctp BIC |
| --- |

| IF Beneficiary(58) is populated IF Beneficiary(58)'s BIC is blank AND Beneficiary A/C is blank THEN 58D:Beneficiary(58)'s LongName OTHERWISE line1 58D:Beneficiary A/C line2 Beneficiary(58)'s LongName IF Beneficiary(58)'s BIC is NOT blank AND Beneficiary A/C is blank THEN 58A:Beneficiary(58)'s BIC OTHERWISE line1 58A:Beneficiary A/C line2 Beneficiary(58)'s BIC |
| --- |

## Murex Product vs. CFI Code

```text
IRD|IRS

IRD|CCS

IRD|LNBR

CURR|FXD|FXD

etc.
```

## Interpretation boundaries

[[cms-dependent-swift-message-generation]] captures the documented MT103 and MT202 branching rules. The source does not establish whether the CMS Account Holder tick box and `CMS_FLAG` are the same persisted control, nor does it identify the authoritative source for `SWIFT_ACHL`, `FIN_COPY`, CMS Account Number, or `SNDREC1`–`SNDREC6`.

The source supports only product-path context for [[cfi-code-mapping-for-murex-vostro-ssi]]; it contains no CFI-code values and must not be treated as an authoritative mapping.

The Jakarta “special logic” outputs are not included. The non-CMS MT202 value appears as malformed Markdown in the source and requires confirmation through [[what-is-the-literal-mt202-field-72-output-for-non-cms-jakarta-cashflows]].
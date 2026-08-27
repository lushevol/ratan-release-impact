---
type: source
title: Nostro Static Golden Source
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-24
updated: 2026-08-24
tags: [nostro-static-data, golden-source, nams, rdm, sci, fmo, functional-requirement]
related: [nostro-static-golden-source, nostro-account-taxonomy, nostro-account-normalization, nostro-centralization, nostro-static-data-migration, nostro-record-composite-uniqueness, nams, rdm, ratan, sci, razor, gptm, murex-2-11, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md"]
---

# Nostro Static Golden Source

## Source status

This document is a proposed functional and architectural requirement. It describes a target operating model and data mapping, not confirmed implementation behavior or production validation.

## Purpose and background

The requirement addresses the absence of a centralized golden source for Nostro static data. Nostro, over-account, and suspense-account records are currently maintained in multiple FMO and trading-platform systems, including RATAN, RAZOR, GPTM, and MUREX2.11. Centralizing the data is intended to reduce duplicated maintenance and omission risk.

The proposed architecture uses [[nams]] as the golden source for existing Nostro static data. [[rdm]] receives and enriches the data, sources legal-entity and agent-bank information from [[sci]], and distributes the resulting model to FMO systems. [[ratan]] is proposed as the pilot consumer, followed by RAZOR, GPTM, and other FMO systems.

Metal-currency Nostros are not available in NAMS and are proposed to be maintained directly in RDM.

## Account categories

The requirement treats three categories as Nostro static:

- **Nostro Account:** An account held by one legal entity with another legal entity for paying or receiving funds.
- **Over Account:** An account held within the same legal entity for paying or receiving funds from clients of that entity.
- **Suspense Account:** An internal account used for settlement-accounting entries where no payment or receipt of funds is involved.

The proposed `Settlement_means` field distinguishes these categories with values including `NOS`, `Over Account`, and `Suspense`.

## Proposed source and distribution architecture

```text
NAMS
  └── Existing Nostro static
        ↓
      RDM
  ├── Enrichment and normalization
  ├── Legal-entity and agent-bank data from SCI
  └── Distribution to FMO systems
        ↓
RATAN pilot → RAZOR / GPTM and other FMO systems
```

The requirement leaves ownership boundaries unresolved. NAMS is described as the golden source, while RDM owns new attributes, performs transformations, and directly maintains metal-currency Nostros.

## NAMS and SCI field mapping

| Data Source | Field S.No | Unique Key for Nostro Best Matching Logic | Nostro Static Field Name | Sample | Source System | Source System Field | Field is currently Mandatory in NAMS? | Value | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Existing Fields in NAMS** | 1 | Y | Agent Bank SCI Code | 11034125/1 | NAMS | Agent Bank SCI Code | TBC | | |
| 2 | Y | Status | Open/Closed | NAMS | Status | TBC | Open/Closed | |
| 3 | | Ledger Account Number_EBBS | HK7251800192082CNY238 | NAMS | Ledger Code | TBC | HK7251800192082CNY238 | |
| 4 | | Agent Bank_Swift | SCBLCNSXSHA | NAMS | Agent Bank BIC Code | TBC | SCBLCNSXSHA | |
| 5 | | Statement Account Number | 501511239996 | NAMS | Account Number | TBC | 501511239996 | Need data massaging by FMO in RDM |
| 6 | | Recon System Nostro ID | 20USD48 | NAMS | Recon System NostroId | TBC | 20USD48 | Manually input in NAMS, no interface with TLM |
| 7 | Y | Settlement_currency | CNY BDT,etc | NAMS | Currency Code | TBC | CNY | |
| **New Fields to be created in RDM** | 8 | Y | Settlement_means | NOS | NAMS/RDM | Settlement_means | | NOS / Over Account / Suspense etc | Need to add in RDM for Overaccount / Suspense Nostros |
| 9 | Y | Settlement_account | BDT MAIN | NAMS/RDM | | ---- | | New field in RDM |
| 10 | Y | Effective Start Date | 01/Jan/2023 | RDM | ---- | ---- | | New field in RDM |
| 11 | Y | Effective Closure Date | 31/Dec/2022 | RDM | ---- | ---- | | New field in RDM |
| 12 | Y | Nostro Used by FMO | Y (leave Blank if No) | RDM | ---- | ---- | Y / Blank | New field in RDM |
| 13 | Y | FMO System | RATAN | RDM | FMO system | ---- | ALL / RAZOR / GPTM / RATAN | New field in RDM |
| 14 | | Notice_to_receive | Y (leave Blank if No) | RDM | ---- | ---- | Y / Blank | New field in RDM |
| 15 | | PSGL Chart Field | 2387251800122102761950 | RDM | ---- | Various | | New field in RDM |
| **RDM to Source Data from SCI** | 16 | Y | Legal_entity_fmid | 400452428 | SCI | ALTAS_ID | ---- | 400452428 | ALTAS_ID:2 SCI_ID: 11153358 SCI &NAMS link RDM to source from SCI |
| 17 | | Legal_entity_code | SCB HONGKON*HKG | SCI | ATLAS_CODE | ---- | SCB HONGKON*HKG | RDM to source from SCI |
| 18 | | Agent Bank_fullname | SCB CHINA SHANGHAI SHA | SCI | NM_PARTY_SHORT | ---- | SCB CHINA SHANGHAI SHA | RDM to source from SCI |
| 19 | | Agent Bank_address | 25 TH FLOOR STAN CHART TOWER 201 CENTURY AVENUE PUDONG SHANG | SCI | NM_ADDRESS1 NM_ADDRESS2 | ---- | 25 TH FLOOR STAN CHART TOWER 201 CENTURY AVENUE PUDONG | RDM to source from SCI |
| 20 | | Agent Bank City | SHANGHAI CN | SCI | NM_ADDRESS4 | ---- | SHANGHAI | RDM to source from SCI |
| 21 | | Agent Bank Postal Code | 200120 | SCI | NM_POST_CODE | ---- | 200120 | RDM to source from SCI |
| **To be Analyzed if relevant** | 22 | | SSI | | NAMS | SSI | TBC | SSI / Non-SSI / Blank | Need to determine if this field is relevant |
| 23 | | Correspondent Type | | NAMS | Business Type | TBC | "Securities" / "Cash/Correspondent" | Need to determine if this field is relevant |

### Identifier mappings

| Mapping: | NAMS.Agent Bank SCI Code | SCI.SCI_ID+'/'+SUB_PROFILE_SCID |
| --- | --- | --- |
| | 11153358/1 | 11153358/1 |
| | | |
| | NAMS Agent Bank BIC Code | SCI.ATLAS_CODE |

The relationship between `Agent Bank BIC Code`, `SCI.ATLAS_CODE`, and actual SWIFT BIC semantics requires validation.

## Suspense-account data

### RAZOR settlement means

```text
SUS    GBFXSUS    ALOCSUS    FXBRREC    TBSUS    FXSUS    TBFXSUS    FISUS    DVSUS    WMSUS    FATCASUS    HIBSUS    MMSUS    CPN SUSP    PVBSUS    SUSP    WHTSUS    CLS SUSP
```

### Suspense-account key candidates

| Field S.No | Expect NOS column | Sample | Comment |
| --- | --- | --- | --- |
| 1 | settlement account | DVSUS | Searching Key |
| 2 | settlement means | DVSUS | Searching Key |
| 4 | legal entity/ legal entity | | Searching Key ?? Need to add |
| 5 | currency | | Searching Key ?? Need to add |
| 6 | ebbs account number | | Razor save in TABLE#DATA#SITRN_DBF |
| 7 | PSGL Mapping | | Razor don't save it, maintained by downstream |
| 8 | Bridge Account Number | | Razor use a Lookup table to maintain it |

The source does not resolve whether suspense records belong in NAMS, RDM, or RATAN. It also suggests that legal entity and currency may be required to make the search key unique.

## Account-number representation differences

| NAMS | RAZOR | Difference |
| --- | --- | --- |
| 15209909601AED | 15 2099096 01 | Currency +space |
| 5000408097 | DK4920005000408097 | Account info |
| 0100001846001 | HU 39120010080000184600100004 | Account info +suffix |
| 600-392027 | IL510126000000000392027 | Account info + replace '-' to '000000' |

The requirement states that FMO may need to massage `Statement Account Number` in RDM. It does not define whether the original value, a canonical value, and consuming-system representations must all be retained.

## Multiple-account example

| NAMS | RAZOR |
| --- | --- |
| SCB Entity SCI Code | Account Number | Currency Code | LEID/SUB ID | Legal Entity | Closing Entity | Settlement Account | Settlement Account Number |
| 12921313/1 | 690750AUD00001 | AUD | 12921313/1 | SCB SG LTD*SIN | CE SGSUBDB | AUD MAIN | 690750AUD00001 |
| 12921313/1 | 1803004693504 | AUD | 12921313/1 | SCB SG LTD*SIN | CE SGSUBDB | AUD OTH 2 | 1803004693504 |
| 11090155/71 | 949321AUD00001 | AUD | 11090155/71 | SCBLDBU*SIN | CE SGDBU | AUD ACLR | CHT0001974 |
| | | | 11090155/71 | SCBLDBU*SIN | CE SGDBU | AUD OTH 2 | 1803004693500 |
| | | | 11090155/71 | SCBLDBU*SIN | CE SGDBU | AUD MAIN | 949321AUD00001 |

The examples show that a legal entity and currency can have multiple accounts and that not every NAMS account is necessarily relevant to FMO. `Nostro Used by FMO` and `FMO System` therefore require explicit governance.

## Open points

1. Where should suspense data be stored: NAMS, RDM, or RATAN?
2. Should RATAN cache Nostro data or resolve it from RDM at runtime?
3. Can one account number map to many EBBS ledger accounts?
4. What is the authoritative ownership model between NAMS and RDM?
5. What is the canonical account-number normalization and source-value-retention contract?
6. Are `SSI` and `Correspondent Type` required fields?
7. How should metal-currency Nostros be governed and reconciled?

## Evidence boundary

The requirement provides concrete mapping examples and identifies integration risks, but it does not establish approved ownership, implemented interfaces, production completeness, or validated uniqueness rules.
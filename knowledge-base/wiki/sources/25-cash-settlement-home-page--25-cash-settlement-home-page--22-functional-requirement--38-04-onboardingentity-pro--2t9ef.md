---
type: source
title: Korea Cashflow Migration F2B Onboarding Checklist
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page"
created: 2026-08-22
updated: 2026-08-22
tags: [korea, cashflow-migration, onboarding, cash-settlement, functional-requirement]
related: [korea, cashflow-migration, korea-ssi-onboarding, kro-to-krw-currency-mapping, ccs-auto-netting, korea-swift-mx-message-generation, korea-settlement-accounting, korean-character-reporting, ebbs, tds3, krx, lms, cdups]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# Korea Cashflow Migration F2B Onboarding Checklist

## Source scope

This working checklist assesses the onboarding of Korea cashflows into cash-settlement, settlement-instruction, accounting, netting, SWIFT/MX, and related operational workflows. It distinguishes cashflow migration from broader trade migration into [[entities/fmrp]].

The checklist is not a completed design or acceptance specification. Several entries remain marked as to be agreed, TBC, unknown, or dependent on confirmation from named teams or individuals.

## Scope conclusions

The source identifies the following Korea-specific conclusions:

| Area | Conclusion |
| --- | --- |
| Dashboard | Add Korea to the dashboard |
| Nostro stamping | Follow default |
| ND CCS / ND IRS | Net in [[entities/ratan]] |
| Clearing | Add KRX as a netting counterparty |
| FX Replication | Yes |
| FXU | Yes, but no dependency on FXU |
| NDS Auto Netting | Yes |
| IRS Auto Netting | Yes, follow current |
| CCS Auto Netting | Yes, follow current |
| Trade migration | Not applicable for cashflow migration |
| FMRP Events | Not applicable for cashflow migration |
| FMRP Products | Not applicable for cashflow migration |
| Touch Point Data | Not applicable for cashflow migration |
| LMS | LMS entity filter will be removed |
| Pending fixing | Use Murex flag |
| Vostro SSI | No new settlement means |
| Rounding | Truncation, to be agreed |
| TDS3 | Required |
| MT/MX | MX for all except MT210 |
| Korean characters | SSDR report dependency: Yes |
| Go-live | N/A for analysis |

## Structured source data

```text
SSI Auto Stamping:
- SSI Auto Stamping Hierarchy (Old CN/SG/IN/MY/EG/SA/NP/AG/LOANIQ vs New UK & new onboarding)
- CFI code Selection( Only looking up first 2 characters and special logic on IRS/CCS only)
- Settlement Method (FEDWIRE / CASH)
- Single Agent / Two Agent Supported (3 Agent not supported)
- Trade SSI Stamping to CDUPS (XML + Product based)
- Currency code transformation (when receive SGO, lookup SGD)
- Korea requirement: KRO to KRW

Nostro Auto Stamping:
- Default Nostro Stamping
- ~~Currency code transformation (when receive SGO, lookup SGD)~~
- Korea: follow default

SWIFT Generation:
- MT Generation - MT103, 202, MT103+202COV, MT210, FlipMT202, MT192, MT292, MT604, MT605, MT692
- MX Generation - Pacs.008.001.08 (MT103)
- Pacs.009.001.08 (MT202 & 202COV)
- Camt.056.001.08(MT192 & MT292)
- camt.057(MT210)
- Korea: MX for all except MT210
- pacs008, 009, Camt.056 MT210 TBC with ISO when they migration MT210

Currency Configuration:
- Non-ISO to ISO Code mapping
- Precious Currency Mapping
- KRO to KRW required for payment and accounting

LMS / settlement accounting:
- LMS entity filter will be removed
- LMS not onboarded yet need to generate sett accounting for all sett account

Clearing:
- KRX ot be added as netting counterparty

Korea-specific items:
- Integration with Murex Korea by solace? ???
- Korea language issue? Require to support in SSI, SCI, cashflow data?
- no dependency on korean characters SSDR report dependency - Yes
```

## Functional checklist

### SSI and settlement instructions

The checklist records a new-onboarding SSI hierarchy path, CFI selection based on the first two characters with special IRS and CCS logic, FEDWIRE or CASH settlement methods, and support for single-agent and two-agent structures. Three-agent structures are not supported. Trade SSI stamping feeds CDUPS through XML and product-based logic.

Korea requires `KRO` to `KRW` currency transformation. The exact hierarchy position, settlement method, agent structure, and scope of the transformation remain unspecified.

Nostro stamping should follow the default behavior. The previously described currency transformation for SGO/SGD is struck through in the Nostro section.

### Payment messages

The checklist lists MT and MX support for MT103, MT202, MT103 plus MT202COV, MT210, FlipMT202, MT192, MT292, MT604, MT605, and MT692. The listed MX mappings are:

- `Pacs.008.001.08` for MT103
- `Pacs.009.001.08` for MT202 and MT202COV
- `Camt.056.001.08` for MT192 and MT292
- `camt.057` for MT210

The Korea direction is “MX for all except MT210.” The final MT210 treatment and ISO release dependency are TBC.

### Accounting and settlement accounts

The source identifies EBBS real-time and end-of-day feeds, ASPIRE integration, possible movement from the Aspire model to the EBBS model, and treatment of historic and past-value cashflows after cutover. It also requires settlement accounting for all settlement accounts because LMS is not yet onboarded.

Bridge account numbers, EBBS branch codes, transaction types, onshore-currency treatment, and the authoritative accounting model require confirmation. Balaji is identified for settlement-accounting confirmation.

### Netting and clearing

Korea requires NDS auto netting, current IRS auto-netting behavior, and current CCS auto-netting behavior. ND CCS and ND IRS should net in RATAN using NID-based logic. KRX must be added as a netting counterparty.

Only IRS is currently allowed for netting over netting, and ND IRS follows the same ISDA taxonomy. The source does not establish that every netting type or product population applies to Korea.

### Business rules and operational dependencies

The checklist records unresolved requirements for:

- Korea-specific NSTP rules where SCB entities are counterparties or booking entities
- SWIFT suppression for auto-debit-by-agent and shared Nostros
- Replication of Murex-to-RATAN exclusion filters as RATAN suppression rules
- Updates to the onboarded-entity whitelist
- FX-product suppression exclusions
- Firewall access for users in the new location
- TDS3 integration for trade-confirmation status
- DVP NSTP setup
- SSDR support for Korean characters

## Explicit migration boundary

Rows covering Murex-to-FMRP trade migration, FMRP events, FMRP products, and touch-point data are marked as not applicable for cashflow migration. This does not remove the need to assess Murex, RATAN, STELLA, EBBS, TDS3, settlement-account, netting, reporting, or payment-message dependencies.

## Open items

The source leaves the following matters unresolved:

- Exact Korea settlement means and settlement accounts
- Whether `KRO` is an inbound, internal, or legacy code
- Final MT210 message and ISO release
- Korea’s SSI hierarchy position
- One-agent or two-agent settlement requirements
- EBBS branch, bridge-account, and transaction-type values
- ASPIRE and EBBS cutover or parallel-run model
- Korea-specific NSTP and suppression rules
- Rounding or truncation rule
- Solace-based Murex Korea integration
- Korean-character support beyond SSDR
- Formal go-live criteria and UVT verification points
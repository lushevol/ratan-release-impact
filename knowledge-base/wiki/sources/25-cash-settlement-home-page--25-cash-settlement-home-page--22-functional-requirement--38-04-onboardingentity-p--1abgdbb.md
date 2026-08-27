---
type: source
title: 2025 Tranche 3 Onboarding
authors: []
year: 2025
url: ""
venue: Internal functional requirement checklist
created: 2026-08-22
updated: 2026-08-22
tags: [tranche-3, entity-onboarding, uat, cash-settlement, static-data]
related: [jersey, zhengzhou, taeyuan, lms, tranche-3-entity-onboarding, ratan, cash-settlement-home-page, payment-and-cashflow-suppression-governance, cashflow-suppression-vs-swift-suppression, ssi-dual-blind-input]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3 Onboarding.md"]
---
# 2025 Tranche 3 Onboarding

This internal UAT follow-up checklist records Tranche 3 entity-onboarding configuration for [[jersey]], [[zhengzhou]], and [[taeyuan]] in [[ratan]]. It covers static data, SWIFT and cashflow suppression, [[lms]] routing, Cashflow Blotter visibility, CPT Control, and maker-checker UAT cases.

The document does not provide a reliable overall sign-off state: it contains both confirmation statements and a statement that user confirmation has not been received. UAT rule creation and screenshot references do not establish production deployment or formal business acceptance.

## Entity SWIFT static

```text
Verification queries:
select * from ratanone_swift_service.swift_static_data_sender_bic ssdsb;
select * from ratanone_swift_service.swift_static_data_correspondent_bic ssdcb;
```

| Entity | Branch code | FMID | Sender BIC | Field 53 BIC (Rule 1) | Field 53 currency | Field 58 BIC (Rule 2) |
|---|---:|---:|---|---|---|---|
| JERSEY | 05 | 400910415 | SCBLJESHXXX | SCBLJESHXXX |  | SCBLJESHXXX |
| ZHENGZHOU | 73 | 400516442 | SCBLCNSXZZH | SCBLCNSXGMO | CNY | SCBLCNSXGMO |
| TAEYUAN | 73 | 400516443 | SCBLCNSXTAY | SCBLCNSXGMO | CNY | SCBLCNSXGMO |

The source records that Sumita replied with ZHENGZHOU and TAEYUAN static on 2025-09-12. It references UAT1 Field 53 BIC cases `M00119946666` and `M00119949999`, but readable test outputs are not included.

## JERSEY suppression configuration

The source distinguishes entity-specific suppression treatments for JERSEY:

| Treatment | UAT rule ID | Scope |
|---|---:|---|
| SWIFT suppression | `7374420229233111040` | Deliverable currencies |
| Cashflow suppression | `7369258354199584768` | Metal currencies |
| Non FMRP entities cashflow suppression amendment | `7369288575163731968` | Add JERSEY FMID `400910415`; retain SAUDI unchanged |

```text
SWIFT-suppressed deliverable currencies:
GBP,GHS,JOD,TRY,AUD,CHF,DKK,EUR,HKD,NZD,SEK,SGD,THB,THO,USD,ZAR,HUF,KES,PLN,AED,SAR,BWP,NOK,ZMK,MAD,ILS,PKR,NGN,UGX,TZS

Cashflow-suppressed metal currencies:
XAU,XAG,XPD,XPT,XRH,XU5,XG2,XT3,XD3,XRU,XS9,XS5,XSD,XU6,XU7,XG5,XUC,XG3,XGC,XD1,XD2,XG1,XR1,XT1,XT2,XU1,XU2,XU3,XU4,XU8,XTN,XDN,XUD,XG4,XG6,XGF,XS6,XSF,XSI,XS4,XGI,XGA,XG7
```

The checklist attributes the intended approach to Pradeesh: deliverable currencies use SWIFT suppression and metal currencies use cashflow suppression. It also records that JERSEY requires neither NSTP nor netting. Rule expressions, precedence, effective dates, and production rule IDs are not supplied.

## Routing and blotter scope

- Story `9920605` specifies that JERSEY (`400910415`) must be filtered in RATAN and must not flow to LMS.
- ZHENGZHOU and TAEYUAN should flow to LMS.
- Story `9905654` covers Cashflow Blotter quick search, filters, country and entity dropdowns, dashboard visibility, and grouping.
- As of 2025-09-16, ZHENGZHOU and TAEYUAN were recorded as already in production; JERSEY required a country configuration; and SAUDI was to remain configured as `SAUDI`.
- Story `10476997`, initially tracking FCBUSLANKA, HKGCT, GCT, and SCBPLC pending FMID confirmation, was later marked “Combined with above.” The underlying entity disposition remains unrecorded.

## JERSEY go-live items

The source records a JERSEY branch suspense bridge claimed to be equivalent to an [[ebbs]] bridge suspense arrangement:

| Item | Value |
|---|---|
| Bridge account | `123613180028890791098` |
| EBBS nostro account | `123613180028881491098` |
| Branch code | `05` |

A note says Balaji should confirm the bridge and nostro accounts; the final confirmation is not captured.

The crossed-out release cut-off item contains the following query and a note that no go-live change is needed at `version=3`:

```sql
select * from ratanone.ratan_static_cashflow_currency_cut_off
where legal_entity_fmid = '400910415';
```

CPT Control is stated to require an update at go-live for FMID `400910415`, with a 2025-09-17 note listing “previous Oct 12 2025,” `USD 1`, and `XAU 1`. CPT’s meaning, owner, implementation path, and validation evidence are absent.

## Maker-checker UAT evidence

The checklist references screenshot evidence for the following workflows:

- TAEYUAN case 31, message `M00119946456`: maker modifies settlement means and submits; checker approves.
- ZHENGZHOU case 30: maker submits ad hoc SSI; checker rejects; maker resubmits; checker approves; maker modifies and submits; checker approves.
- ZHENGZHOU case 31, message `M00119946000`: maker submits; checker rejects; maker modifies and submits; checker approves.

These examples support execution of maker-checker flows in UAT, but lack explicit expected results, environment and version information, named testers, and final UAT acceptance.

## Open issues

- [[what-is-the-final-uat-and-production-sign-off-status-for-tranche-3-entities]]
- [[what-is-the-authoritative-production-decision-for-the-saudi-murex-manual-entity-suppression-rule]]
- [[what-does-cpt-control-mean-and-how-is-it-validated-for-jersey-go-live]]
- [[what-is-the-final-onboarding-disposition-of-fcbuslanka-hkgct-gct-and-scbplc]]
- [[what-is-the-authoritative-jersey-bridge-and-ebbs-nostro-account-configuration]]
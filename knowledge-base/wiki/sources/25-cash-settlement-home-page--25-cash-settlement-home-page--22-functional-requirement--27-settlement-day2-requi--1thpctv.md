---
type: source
title: Swift Message Analysis for Manual Entities
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [settlement-day-2, manual-entities, swift, iso-20022, ratan]
related: [ratan, fmsgw, nostro-static, manual-entity-swift-mx-bifurcation, ratan-swift-reference-and-correspondent-derivation, ssi-driven-swift-and-mx-field-population, swift-block-3-minimal-output, cashflow-suppression-and-swift-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# Swift Message Analysis for Manual Entities

This functional-requirement record validates RATAN-generated SWIFT MT and ISO 20022 MX messages for manual settlement entities. Its recurring approval outcome is that differences from legacy or production samples require **no SWIFT message change**.

The source is an approval and configuration baseline, rather than a complete end-to-end test specification. Several routing and field-derivation rules are referenced only through screenshots or external Confluence material.

## Approved MT-generation baseline

For the reviewed manual entities, RATAN may retain its canonical reference construction:

```text
:20:DV{Field_Branch_Code}{Field_Cashflow_Id}
:21:DV{Field_Branch_Code}{Field_Cashflow_Id}
```

This is accepted even where legacy samples use an `FX` prefix, a non-cashflow reference, or other identifiers.

RATAN may generate `:53A:` where comparison samples omit Tag 53. The correspondent BIC is derived from static data, with accepted fallback to a Nostro-related BIC where currency-level configuration is absent in the reviewed cases. This approval does not extend to `:53D:`, which RATAN does not support in the reviewed flow.

`MT202 Flip` is the accepted classification for reviewed receive/flip scenarios. RATAN may populate `:52:` and `:53B:` according to its Flip logic.

## SSI-driven optional fields

Optional MT fields are configuration-dependent:

- `MT202`: `:56A:` or `:56D:` and `:72:`
- `MT103`: `:56A:` or `:56D:`, `:70:`, and `:72:`
- `MT202 Flip`: `:52:`, `:53B:`, and `:72:`

RATAN should populate these fields when the relevant SSI or SSI+ data is configured. Their absence from a legacy sample is not, by itself, a reason to suppress a configured field.

## Block 3 and related MT exceptions

RATAN supports UETR output through `{121:...}`. The reviewed Pakistan, Bangladesh, Tanzania, and Qatar cases accept omission of historical or gateway-specific Block 3 values such as `{108:...}` and `{103:TIS}`.

For Qatar, `MT210` may omit Block 3. Tag `25` is relevant only for KRW and is not expected for the reviewed Doha scenario.

## MX field behavior

For MX output, RATAN's configuration-driven behavior was accepted despite differences from comparison messages:

- In `pacs.009`, create `SttlmAcct` only when `53AccNumber` exists and the settlement method is `INDA` or `INGA`.
- Populate `CdtrAcct` when the relevant field-57 account is configured in SSI.
- Populate `CdtrAgtAcct` when the relevant field-54 account is configured in SSI+.
- Populate `InstrForNxtAgt` when RATAN conditions are satisfied.
- `PmtTpInf/InstrPrty` is optional and may be absent.
- `CtgyPurp/CORT` should be available for applicable MX MT103 / `pacs.008` output.

## Operative MX bifurcation configuration

| Tranche | Country / FMID | Operative MX condition | Output model | Manual-entity business go-live | ISO go-live |
|---|---|---|---|---|---|
| Tranche 1 | Kenya / `300011525` | Sender BIC starts `SCBLTZ`; receiver does not start `SCBLTZ`; Nostro static BIC is not `TANZTZTXXXX`; settlement account does not end `DFCC` | Internal and external MX | Last week of Aug-2026 | `13-Jun` |
| Tranche 1 | Tanzania / `10040387` | Sender BIC starts `SCBLTZ`; receiver does not start `SCBLTZ`; Nostro static BIC is not `TANZTZTXXXX`; settlement account does not end `DFCC` | Internal and external MX | Last week of Aug-2026 | `13-Jun` |
| Tranche 1 | Vietnam / `10041530` | Sender BIC starts `SCBLVN`; MT103, MT202, or MT202COV | Internal MT; external MX | Last week of Aug-2026 | `03-Oct` |
| Tranche 1 | Bangladesh / `300011470` | Sender BIC starts `SCBLBD`; MT103, MT202, or MT202COV | Internal MT; external MX | Last week of Aug-2026 | `05-Sep` |
| Tranche 1 | Sri Lanka / `10036647` | Sender BIC starts `SCBLLK`; receiver does not start `SCBLLK`; MT103, MT202, or MT202COV | Internal MT; external MX | Last week of Aug-2026 | `05-Sep` |
| Tranche 1 | Pakistan / `10036655` | Sender BIC starts `SCBLPK`; MT103, MT202, or MT202COV | Internal MT; external MX | Last week of Aug-2026 | `05-Sep` |
| Tranche 1 | Zambia / `10041903` | Sender BIC starts `SCBLZM`; MT103, MT202, or MT202COV | Internal MT; external MX | Last week of Aug-2026 | `17-Oct` |
| Tranche 2 | Nigeria / `300084297` | Sender BIC starts `SCBLNG`; MT103, MT202, or MT202COV | Internal and external MX | Third week of Sept-2026 | `22-Aug` |
| Tranche 2 | Ghana / `10037477` | Sender BIC starts `SCBLGH`; receiver does not start `SCBLGH`; MT103, MT202, or MT202COV | Internal and external MX | Third week of Sept-2026 | `22-Aug` |
| Tranche 2 | Bahrain / `10036430` | Sender BIC starts `SCBLBH`; MT103, MT202, or MT202COV | Internal and external MX | Third week of Sept-2026 | `08-Aug` |
| Tranche 2 | Uganda / `10041902` | Sender BIC starts `SCBLUG`; MT103, MT202, or MT202COV; all-to-MX confirmation remains pending | Internal and external MX | Third week of Sept-2026 | `22-Aug` |
| Tranche 2 | Qatar / `300010782` | Sender BIC starts `SCBLQA`; receiver does not start `SCBLQA`; MT103, MT202, or MT202COV | Internal and external MX | Third week of Sept-2026 | `08-Aug` |
| Excluded | SLATE ONE LLC*DOH / `401081696` | Cashflows are suppressed; only suppression static is required | Not applicable | Not applicable | Not applicable |

For cancellation, `camt.056` is eligible only where the original message is MX. `MT192` is the cancellation type for MT103, while `MT292` applies to MT202 and MT202COV.

## Material exceptions and unresolved items

- The Kenya rule uses `SCBLTZ`, although its superseded text used `SCBLKE`. This appears inconsistent and requires resolution before configuration.
- Uganda retains a pending decision on whether all eligible flows should generate MX.
- ISO go-live values such as `13-Jun` and `05-Sep` omit a year and require normalization.
- Sri Lanka states that RATAN sends an LKR `MT202` to CMS and CMS releases `pacs.009`, while also confirming MX is in scope. Ownership of `pacs.009` generation remains unclear.
- Zambia must use structured addresses before the stated RTGS restriction in Nov-2026.
- Branch code is used in Tags `:20:` and `:21:` and is required in the FMSGW JMS header when RATAN publishes through Solace. Duplicate branch codes therefore require downstream correlation review.

See [[manual-entity-swift-mx-bifurcation]], [[ratan-swift-reference-and-correspondent-derivation]], and [[ssi-driven-swift-and-mx-field-population]].
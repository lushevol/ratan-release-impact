---
type: source
title: Murex Products CFI Code Mapping
authors: []
year: 0
url: ""
venue: Internal functional requirement static-data document
tags: [cfi-code, murex-2-11, ssi-plus, vostro-ssi, static-data, historical-reference]
related: [cfi-code-mapping-for-murex-vostro-ssi, what-is-the-authoritative-cfi-code-mapping-for-murex-211-vostro-ssi-securities, murex-2-11, ssi-plus]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/CFI Code.md"]
---
# Murex Products CFI Code Mapping

This document records a proposed mapping from Murex 2.11 product classifications and SSI+ Security IDs to CFI-code patterns for Vostro SSI static data.

## Status and reliability

Every value in the original mapping table is struck through. The source provides no replacement, approval status, owner, effective date, or implementation evidence. Treat all mappings as historical and unverified; do not use them as a production static-data contract.

The document states that the first two Vostro SSIs are “Alert” SSIs used by all applications, with the remaining securities specific to Murex 2.11. However, the table does not identify the two Alert SSIs.

## Preserved mapping

### Murex Products CFI code mapping

The full list of Murex 2.11 Vostro SSI: The top 2 are 'Alert' SSI which are used for all applications, the remaining are Murex 2.11 specific securities.

MXG IRD LN_BR

| ~~SSI+ Security ID~~ | ~~SSI Security Name~~ | ~~Family~~ | ~~Group~~ | ~~Type~~ | ~~CFI Code~~ | ~~Comment~~ |
| --- | --- | --- | --- | --- | --- | --- |
| ~~SCBCRDCDS~~ | ~~MXG CRD CDS~~ | ~~CRD~~ | ~~CDS~~ | | ~~SC****~~ | |
| | | | | | ~~HC****~~ | ~~Credit Default Swap Single Reference Callable~~ ~~Multi Callable Extinguishing Range Accrual (CERA)~~ |
| ~~SCBCRDRTRS~~ | ~~MXG CRD RTRS~~ | ~~CDS~~ | ~~RTRS~~ | | ~~SC****~~ | ~~Not sure about the product~~ |
| ~~SCBIRDBOND~~ | ~~MXG IRD BOND~~ | ~~IRD~~ | ~~BOND~~ | | ~~JR****~~ | |
| ~~SCBIRDCF~~ | ~~MXG IRD CF~~ | ~~IRD~~ | ~~CF~~ | | ~~HR****~~ | ~~IR Derivatives\Swap or Struct Swap\IRS with Capped MTM Conservative Booking~~ ~~IR Derivatives\Swap or Struct Swap\Bullet KO KI Swap, Leveraged In Arrears Swap with KO Cap, Periodic Knock Out Swap, IR Derivatives\Options\Periodic Knock In Floor and Knock Out Cap~~ ~~SR****~~ |
| ~~SCBIRDIRS~~ | ~~MXG IRD IRS~~ | ~~IRD~~ | ~~IRS~~ | | ~~SR****~~ | |
| ~~SCBIRDCS~~ | ~~MXG IRD CS~~ | ~~IRD~~ | ~~CS~~ | | ~~SR****~~ | |
| ~~SCBIRDLNBR~~ | ~~MXG IRD LN_BR~~ | ~~IRD~~ | ~~LN_BR~~ | | ~~DY****~~ | ~~find a way to separate principle and interest for both loan and deposit~~ |
| ~~SCBIRDOPT~~ | ~~MXG IRD OPT~~ | ~~IRD~~ | ~~OPT~~ | ~~OTC~~ | ~~HR****~~ | ~~No identifier for OTC~~ |
| | | ~~CURR~~ | ~~FUT~~ | ~~FUT~~ | ~~FF****~~ | |
| ~~SCBCUFXFX~~ | ~~MXG CURR FXD FXD~~ | ~~CURR~~ | ~~FXD~~ | ~~FXD~~ | ~~JF****~~ | ~~FX Forward~~ |
| | | ~~CURR~~ | ~~FXD~~ | ~~FXD~~ | ~~JF***N~~ | ~~NDF~~ |
| | | ~~CURR~~ | ~~FXD~~ | ~~FXD~~ | ~~IF****~~ | ~~FX Spot~~ |
| ~~SCBCUFXXSW~~ | ~~MXG CURR FXD XSW~~ | ~~CURR~~ | ~~FXD~~ | ~~XSW~~ | ~~SF****~~ | ~~FX Swap~~ |
| ~~SCBCUOPASN~~ | ~~MXG CURR OPT ASN~~ | ~~CURR~~ | ~~OPT~~ | ~~ASN~~ | ~~HF****~~ | |
| | | ~~CURR~~ | ~~OPT~~ | ~~FLEX~~ | ~~HF****~~ | |
| ~~SCBCUOSMP~~ | ~~MXG CURR OPT SMP~~ | ~~CURR~~ | ~~OPT~~ | ~~SMP~~ | ~~HF****~~ | |
| ~~SCBCUOSMP~~ | ~~MXG CURR OPT SMP~~ | ~~SCF~~ | ~~SCF~~ | ~~SCF~~ | ~~MM****~~ | |

Reference: [BCS Cash Settlements - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/BCS+Cash+Settlements)

## Recorded gaps

- `SCBIRDCF` presents both `HR****` and `SR****` in the same context.
- `SCBCRDRTRS` has an uncertain product classification.
- `SCBCUOSMP` is reused across two distinct taxonomy and CFI-code mappings.
- FX futures, NDF, FX spot, and flexible currency-option rows lack SSI+ Security IDs and SSI Security Names.
- `LN_BR` requires a distinction between principal and interest for loans and deposits.
- The OTC option entry explicitly states that no identifier exists for OTC.

See [[cfi-code-mapping-for-murex-vostro-ssi]] for scope and interpretation limits, and [[what-is-the-authoritative-cfi-code-mapping-for-murex-211-vostro-ssi-securities]] for unresolved ownership and replacement questions.
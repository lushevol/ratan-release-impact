---
type: source
title: Murex 2.11 Vostro SSI
authors: []
year: 2023
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, vostro-ssi, murex-211, static-data, ratan, cfi-code]
related: [ratan, ssi-plus, cfi-code-mapping-for-murex-vostro-ssi, ssi-stamping-behavior-differences, es-static-data-layer, tds3, murex-211-vostro-ssi-data-quality, how-does-ratan-map-mx211-cfi-prefixes-to-vostro-ssis]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md"]
---
# Murex 2.11 Vostro SSI

## Summary

This functional requirement describes how RATAN will reuse existing Murex 2.11 Vostro Standing Settlement Instructions (SSIs). RATAN is expected to select an SSI using the CFI code stamped on a cashflow, while existing Security IDs in SSI+ must be updated with the corresponding CFI code.

The requirement is primarily a mapping and data-quality dependency. It does not define a complete migration procedure, API contract, fallback algorithm, or acceptance checklist.

## Reuse and CFI-code lookup

- Existing Murex 2.11 SSIs will be reused by RATAN.
- RATAN will fetch the applicable SSI using the CFI code stamped on the cashflow.
- Existing SSI+ Security IDs must be updated with CFI codes.
- SSI records are not maintained at a product-equivalent CFI granularity. The requirement gives `XFXXXX` as an example of a broad value used across FX Spot, Forward, and Swap products.
- BLADE, CFETS, and S2BX cashflows receive their CFI code from STELLA.
- RATAN must stamp the CFI code for Murex 2.11 cashflows.
- For Murex 2.11 processing, RATAN retains the first two characters of the CFI code stamped on the Murex 2.11 trade in TDS3.

The source does not establish whether SSI lookup uses the full CFI code, the retained two-character prefix, or separate values at different processing stages.

## Vostro SSI population and attributes

The source identifies the following characteristics:

- The full Murex 2.11 Vostro SSI population includes two top-level “Alert” SSIs used across applications, followed by Murex 2.11-specific securities.
- Some SSIs are assigned to CN payments with year `2022`.
- CN trades use `MXG BLANK`.
- Swift types are relevant for Murex 2.11 SSIs, particularly securities with a Murex name.
- No placeholder is defined for SWIFT fields 58/59 for Murex 2.11 Vostro SSIs.
- Settlement method is associated with Murex securities.
- Some SSI records are missing branch information in ES.
- Settlement Account and Settlement Means are blank for 98.8% of the reviewed Murex 2.11 SSI population.
- The requirement proposes investigating whether `Spare1` can represent a cover-payment flag. This is not an approved data contract.

## Vostro query conditions

The source references an attached image named `SSI_Query.jpg` for Vostro query conditions in FMRP. The textual source does not provide the query fields, operators, joins, precedence, or fallback behavior. The image must therefore be transcribed and validated before it is treated as a testable query contract.

## Data-quality and implementation risks

The 98.8% blank rate for Settlement Account and Settlement Means is the principal readiness risk. Reuse of the existing SSI population depends on whether these fields are mandatory for RATAN processing, populated by another system, or intentionally optional.

Additional unresolved risks include:

1. Coarse CFI values may map several products to one SSI selection.
2. The relationship between full CFI values and TDS3-derived prefixes is unspecified.
3. Missing branch identifiers in ES may prevent complete routing or validation.
4. SWIFT field 58/59 behavior is not defined.
5. CN-specific values may be legacy conventions whose scope is unclear.
6. The proposed `Spare1` cover-payment representation requires design approval.
7. The attached query and branch-identifier images are not represented as structured text.

## Evidence boundaries

This page records the source as a functional requirement, not as evidence that the behavior is implemented or formally approved. The source provides no complete CFI mapping table, SSI identifier list, data extract, denominator for the 98.8% calculation, or production validation results.

See [[murex-211-vostro-ssi-data-quality]] for the data-readiness implications and [[how-does-ratan-map-mx211-cfi-prefixes-to-vostro-ssis]] for the unresolved CFI matching contract.
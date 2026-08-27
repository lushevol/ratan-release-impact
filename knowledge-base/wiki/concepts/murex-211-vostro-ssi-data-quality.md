---
type: concept
title: Murex 2.11 Vostro SSI Data Quality
tags: [vostro-ssi, murex-211, ssi-plus, data-quality, settlement-readiness]
related: [murex-211, ssi-plus, es-static-data-layer, murex-211-vostro-ssi-reuse, cfi-code-mapping-for-murex-vostro-ssi]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md"]
---
# Murex 2.11 Vostro SSI Data Quality

The Murex 2.11 Vostro SSI population contains the static-data attributes required for RATAN reuse, but the source identifies material completeness and definition gaps.

## Attribute findings

| Attribute or rule | Finding |
|---|---|
| Swift Type | Relevant for Murex 2.11 SSIs, particularly securities with a Murex name |
| SWIFT fields 58/59 | No placeholder is defined for Murex 2.11 Vostro SSIs |
| Settlement Method | Associated with Murex securities |
| Branch ID | Missing for some SSI records in [[es-static-data-layer]] |
| Settlement Account | Blank for 98.8% of the reviewed Murex 2.11 SSI population |
| Settlement Means | Blank for 98.8% of the reviewed Murex 2.11 SSI population |
| Cover-payment flag | `Spare1` is proposed for investigation, not approved as a contract |
| CN payment assignment | Some SSIs are assigned with year `2022` |
| CN trade value | CN trades use `MXG BLANK` |

## Primary readiness risk

The 98.8% blank rate for Settlement Account and Settlement Means is the strongest quantitative finding. The source does not state whether the fields are mandatory for RATAN, supplied by another system, or intentionally optional. This must be resolved before the existing population is considered ready for operational reuse.

## Other unresolved requirements

- Define whether branch ID is mandatory, optional, or derivable.
- Specify how SWIFT fields 58/59 are represented when no placeholder exists.
- Confirm the scope and meaning of the CN year `2022` assignment.
- Define `MXG BLANK` and determine whether it is limited to CN trades.
- Decide whether `Spare1` may carry cover-payment semantics without conflicting with other uses.
- Transcribe and validate the branch-identifier evidence and FMRP query conditions from the source images.
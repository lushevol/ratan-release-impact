---
type: query
title: What Is the Authoritative CFI Code Mapping for Murex 2.11 Vostro SSI Securities?
tags: [cfi-code, murex-2-11, vostro-ssi, ssi-plus, static-data, data-governance]
related: [cfi-code-mapping-for-murex-vostro-ssi, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--8-cfi-cod--i6t2qx, murex-2-11, ssi-plus]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/CFI Code.md"]
---
# What Is the Authoritative CFI Code Mapping for Murex 2.11 Vostro SSI Securities?

The only available mapping record is fully struck through, has no approval metadata, and contains incomplete and conflicting entries. An approved owner and source of truth are required before any static-data implementation or remediation.

## Questions to resolve

1. Has the struck-through mapping been superseded, and where is the approved replacement?
2. Are values such as `SR****`, `HR****`, and `JF***N` complete CFI codes, wildcard matching patterns, or partial display values?
3. Which SSI+ Security IDs are the two claimed Alert SSIs used by all applications?
4. Is `SCBIRDCF` classified by `HR****`, `SR****`, or multiple context-dependent values?
5. Why does `SCBCUOSMP` / `MXG CURR OPT SMP` appear under both `CURR / OPT / SMP / HF****` and `SCF / SCF / SCF / MM****`?
6. Which SSI+ Security IDs should be assigned to FX futures, NDF, FX spot, and flexible currency options?
7. How must `IRD / LN_BR` distinguish principal from interest and loan from deposit?
8. What identifier or classification is required for `IRD / OPT / OTC`?

## Decision boundary

This query concerns Vostro SSI static-data classification only. It must not be resolved by assuming applicability to Nostro stamping, dedicated Nostro selection, RFI logic, or SWIFT processing.

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--8-cfi-cod--i6t2qx]] preserves the incomplete historical mapping. [[cfi-code-mapping-for-murex-vostro-ssi]] documents its scope and constraints.
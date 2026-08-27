---
type: query
title: What Is the Authoritative Mapping from MXG Blank to CFI Code?
tags: [cn-settlement, vostro, ssi, cfi, product-mapping, open-question]
related: [cn-vostro-ssi-scope-and-extraction, murex-2-11, fmrp, cn-settlement]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex 2.11 CN Vostro SSI.md"]
---
# What Is the Authoritative Mapping from `MXG Blank` to CFI Code?

## Question

Should an Murex SSI security value of `MXG Blank`, interpreted historically as applicable to all Murex products, be represented in the target SSI+ or CFI model by CFI Code `******`?

## Evidence

The deprecated source reports 3,906 `MXG Blank` records and 1,728 `MXG XXX` records. It describes `MXG Blank` as an all-product scope and product-specific values such as `MXG IRS` as limited to a particular Murex product.

The proposed `******` mapping is presented as a question, not as an approved business rule. No target-schema definition, sample reconciliation, or owner approval is included.

## Required resolution

Confirm:

1. whether `MXG Blank` means all products in every relevant SSI context;
2. whether CFI `******` is a valid wildcard representation;
3. how blank, malformed, and product-specific security values are handled;
4. whether Global and entity-specific records use the same mapping;
5. how the mapping is validated against SSI+ extraction results.

Until resolved, migration logic should preserve the original Murex value and flag the proposed wildcard mapping for review.
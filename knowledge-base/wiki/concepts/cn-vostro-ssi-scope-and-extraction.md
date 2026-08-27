---
type: concept
title: CN Vostro SSI Scope and Extraction
tags: [cn-settlement, vostro, ssi, ssi-plus, murex-2-11, migration, data-quality]
related: [murex-2-11, fmrp, cn-settlement, cn-trade-migration, cn-vostro-ssi-mxg-blank-cfi-mapping, cn-vostro-ssi-count-reproducibility]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex 2.11 CN Vostro SSI.md"]
---
# CN Vostro SSI Scope and Extraction

## Overview

CN Vostro SSI extraction distinguishes between Global instructions and instructions scoped to named China entities. The distinction is operationally significant because the two populations were extracted using different criteria and should not be combined without a defined deduplication and applicability model.

This page summarizes historical evidence from deprecated Murex 2.11 material. It does not define an approved SSI+ contract.

## Scope dimensions

### Global versus entity-specific

A Global SSI uses a blank Murex entity in the extraction query and is associated with China through counterparty country or China desk information. The source reports 2,744 Global Vostros with China desk information and separately reports 2,108 SSI records whose entity value is `Global`.

An entity-specific SSI uses a named China branch or legal entity, such as `BEIJING`, `SHANGHAI`, or `GUANGZHOU`. The source reports 146,988 records in the China-entity extraction and 3,526 records in one entity segmentation.

The source interprets `Global` as applicable across SCB branches and a named branch as applicable only to that entity. This interpretation requires confirmation before migration rules are implemented.

### Security applicability

The source distinguishes `MXG Blank` from product-specific values such as `MXG IRS`:

- `MXG Blank` is interpreted as applying to all Murex products.
- `MXG XXX` values are interpreted as applying to a particular Murex product.
- The proposed target representation is CFI Code `******` for all-product applicability.

The CFI mapping is explicitly unresolved and must not be treated as an approved rule.

### Current-record filtering

Both reported Murex extraction queries use:

```text
M_NOVO=1 AND M_NEXT=0
```

This appears intended to select new/current records and exclude records with successors. Whether this is the approved SSI lifecycle definition remains open.

## Proposed SSI+ segmentation

The historical extraction matrix combines scope, security, product family, and currency dimensions. It includes Global/00 with CURR, CRD, COM, IRD, and SCF variants, as well as China-entity populations and USD-specific conditions.

The notation `Global/00` suggests a possible equivalence between the Murex Global scope and an SSI+ value of `00`, but the source does not confirm that equivalence. The segmentation should therefore be treated as a test matrix rather than a target specification.

## Data-quality and reproducibility risks

The source reports inconsistent data-source capitalization and malformed values, including `manual`, `MANUAL`, and `maual`. The China entity list includes trailing spaces and apparent naming variants. These values require normalization before counts or migration completeness can be assessed.

The China-entity SQL also references `CPM.M_LABEL` without declaring `TRN_CPDF_DBF CPM` in the `FROM` clause. The client query contains an unquoted Atlas legal-entity value and appears to comment out the `DO NOT USE` exclusion. These defects weaken the reproducibility of the reported populations.

Settlement Account/Means is blank for most CN Vostros. A blank must not be converted into a universal default until its business meaning is established.

## Relationship to migration work

The concept is relevant to [[projects/cn-trade-migration]] and broader [[concepts/cn-settlement]] work. It complements, but does not supersede, current settlement-account routing and Murex-to-RATAN requirements. The source should be classified as historical evidence under [[queries/which-cash-settlement-requirement-documents-are-authoritative-after-deprecation]].
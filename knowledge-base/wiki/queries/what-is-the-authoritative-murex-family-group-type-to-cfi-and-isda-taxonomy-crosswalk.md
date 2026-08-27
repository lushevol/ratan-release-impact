---
type: query
title: What Is the Authoritative Murex Family Group Type to CFI and ISDA Taxonomy Crosswalk?
created: 2026-08-24
updated: 2026-08-24
tags: [cfi, isda-taxonomy, product-classification, murex-211, ratan-mls]
related: [murex-payment-mxml-to-scbml-transformation, murex-211, ratan, cfi-code-mapping-for-murex-vostro-ssi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# What Is the Authoritative Murex Family Group Type to CFI and ISDA Taxonomy Crosswalk?

## Question

How should Murex transaction Family, Group, and Type values generate the SCBML CFI code, ISDA taxonomy, and source-system instrument subtype?

## Current evidence

The mapping provides the example:

- Family: `COM`.
- Group: `SWAP`.
- Type: `FXD`.
- Proposed ISDA taxonomy: `Commodity:Swap`.
- Proposed source-system subtype: `{MocksubType}`.

The enhancement evidence instead references:

- `IRD|CS|`.
- `IRD|IRS|`.
- Product dimensions `family`, `group`, and `type`.
- Confirmation statuses `COMP` and `VALD`.

RATAN MLS is identified as the transformation location, and the source says to check the CFI mapping with Dinesh. No complete crosswalk or precedence rule is supplied.

## Required resolution

Confirm the authoritative mapping for:

- CFI code.
- ISDA taxonomy.
- Source-system subtype.
- Payment type.
- Trade action type.

The resulting crosswalk should define valid input domains, output values, versioning, ownership, and behavior for unmapped products.
---
type: query
title: What Is the Canonical SSI Stamping Product Classification Precedence?
created: 2026-08-23
updated: 2026-08-23
tags: [query, ssi-stamping, product-classification, scbml, foreign-exchange]
related: [ssi-stamping-service, scbml, ssi-stamping-product-mapping, scbml-trade-enrichment-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# What Is the Canonical SSI Stamping Product Classification Precedence?

The source contains conflicting product indicators in its concrete confirmation example:

- API request: `productType: "spot"`.
- SCBML product taxonomy: `ForeignExchange:Forward`.
- MX sub-product type: `Spot`.
- Product typology: `Outright`.

The design does not specify which value governs SSI Stamping product routing and CFI mapping.

## Required decision

Define the precedence among API `productType`, SCBML `productId`, SCBML `productType` values, MX sub-product type, and typology.

The rule should cover at least FX Spot, FX Forward, FX Swap, Bullion Spot, Bullion Forward, and other multi-leg products. It should also define behavior when fields are absent or contradictory.

## Why this matters

The classification determines the CFI code, XPath extraction path, single-leg versus multi-leg result model, legacy versus refactored implementation path, and settlement-instruction lookup behavior.
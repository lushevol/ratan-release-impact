---
type: concept
title: SSI Stamping Product Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [ssi-stamping, product-mapping, cfi, foreign-exchange, xpath]
related: [ssi-stamping-service, ssi-stamping, scbml, scbml-trade-enrichment-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# SSI Stamping Product Mapping

The SSI Stamping design defines the following product-to-CFI mappings:

| Product type | CFI Code |
| --- | --- |
| FX Spot | `I-F-X-X-X-X` |
| FX Forward | `J-F-X-X-X-X` |
| FX Swap | `S-F-X-X-X-X` |

The mapping is marked closed in the source design.

## Unresolved extraction

Although the mapping itself is closed, the source paths for CFI Code, Settlement Method, and Settlement Type remain open pending Product Owner confirmation. Payment currency is parsed as a list from SCBML and then identified by SSI Stamping logic.

A sample message creates a classification conflict: the API request uses `productType: "spot"`, while the SCBML contains `ForeignExchange:Forward` as a product taxonomy, `Spot` as an MX sub-product type, and `Outright` as a typology. The precedence among these fields is not defined.

## Implementation impact

New products, including Bullion Spot and Bullion Forward, are intended to use a refactored implementation compatible with XPath 2.0 and product-agnostic SCBML generation. Existing products retain the legacy implementation according to the documented direction.